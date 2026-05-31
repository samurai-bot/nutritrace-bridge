#!/usr/bin/env python3
"""Create NutriTrace MCP webhook workflows in n8n."""

import json, os, requests

API_KEY = os.environ["N8N_KEY"]
BASE = "https://tech-vm.tail3190c5.ts.net/api/v1"
HEADERS = {"X-N8N-API-KEY": API_KEY, "Content-Type": "application/json"}
NT = "http://100.111.123.105:3002"  # host IP, reachable from n8n's Docker network

SETTINGS = {"executionOrder": "v1", "availableInMCP": True, "callerPolicy": "workflowsFromSameOwner"}

def webhook_node(path):
    return {"parameters": {"httpMethod": "GET", "path": path, "responseMode": "lastNode", "options": {}},
            "type": "n8n-nodes-base.webhook", "typeVersion": 2.1, "position": [0, 0], "name": "Webhook"}

def http_node(method, url, query_params=None):
    p = {"method": method, "url": url, "options": {}}
    if query_params:
        p["sendQuery"] = True
        p["queryParameters"] = {"parameters": query_params}
    return {"parameters": p, "type": "n8n-nodes-base.httpRequest", "typeVersion": 4.4,
            "position": [200, 0], "name": "HTTP Request"}

def create(name, path, http):
    wf = {"name": name, "settings": SETTINGS, "nodes": [webhook_node(path), http],
          "connections": {"Webhook": {"main": [[{"node": "HTTP Request", "type": "main", "index": 0}]]}}}
    r = requests.post(f"{BASE}/workflows", headers=HEADERS, json=wf)
    if r.status_code not in (200, 201):
        return print(f"❌ {name}: {r.status_code} {r.json().get('message','')}")
    wid = r.json()["id"]
    ra = requests.post(f"{BASE}/workflows/{wid}/activate", headers=HEADERS)
    if ra.status_code not in (200, 201):
        return print(f"⚠️ {name}: created but activate failed ({ra.status_code})")
    print(f"✅ {name}")

# Delete any stale NutriTrace workflows from previous attempts
r = requests.get(f"{BASE}/workflows?limit=50", headers=HEADERS)
for w in r.json().get("data", []):
    if "NutriTrace" in w.get("name", "") and not w.get("active"):
        requests.delete(f"{BASE}/workflows/{w['id']}", headers=HEADERS)

# --- Create workflows ---

create("NutriTrace Search Foods - MCP", "nutritrace-search-foods",
    http_node("GET", f"{NT}/foods/search", [
        {"name": "q", "value": "={{$json.query.q}}"},
        {"name": "limit", "value": "={{$json.query.limit || \"10\"}}"}]))

create("NutriTrace Weight History - MCP", "nutritrace-weight-history",
    http_node("GET", f"{NT}/weight/history"))

create("NutriTrace Daily Stats - MCP", "nutritrace-daily-stats",
    http_node("GET", f"{NT}/stats/daily", [
        {"name": "date", "value": "={{$json.query.date || $now.format(\"YYYY-MM-DD\")}}"}]))

create("NutriTrace Weekly Stats - MCP", "nutritrace-weekly-stats",
    http_node("GET", f"{NT}/stats/weekly"))

create("NutriTrace Food Categories - MCP", "nutritrace-food-categories",
    http_node("GET", f"{NT}/foods/categories"))

create("NutriTrace Diary Get - MCP", "nutritrace-diary-get",
    http_node("GET", f"={NT}/diary/{{{{$json.query.date}}}}"))

create("NutriTrace Food by ID - MCP", "nutritrace-food-by-id",
    http_node("GET", f"={NT}/foods/{{{{$json.query.id}}}}"))
