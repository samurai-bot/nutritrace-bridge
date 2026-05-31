# NutriBridge

REST API + MCP server + n8n webhooks that let AI agents (OpenClaw, Hermes Agent, Claude) read and write nutrition data from a self-hosted [NutriTrace](https://github.com/TraceApps/nutritrace) instance.

## What It Does

NutriTrace is a single-container nutrition tracker (Svelte + Express + SQLite). It works great for humans but ships with no API layer for agents. NutriBridge wraps it:

```
NutriTrace (:3000) ── SQLite ── NutriBridge (:3002 / :3003)
                                      │
              ┌───────────────────────┼──────────────────────┐
              │                       │                      │
          OpenClaw              Hermes Agent              Claude
        (direct HTTP)          (native MCP)         (n8n MCP webhooks)
```

## Architecture

Single host, shared SQLite, zero pip dependencies:

```
├── nutritrace        (ghcr.io/traceapps/nutritrace)  :3000  UI
├── nutritrace-api    (python:3.11-alpine)             :3002  REST
├── nutritrace-mcp    (python:3.11-alpine)             :3003  MCP
└── nutritrace.db                                      632+ foods
```

8 n8n webhook workflows provide MCP access for Claude via the same pattern used by existing Strava and Scribble Wiki integrations.

## Project Structure

```
├── src/
│   ├── nutritrace-api.py        REST server (stdlib, ~500 lines)
│   └── nutritrace-mcp.py        MCP JSON-RPC server (stdlib)
├── scripts/
│   ├── build-sg-food-db-v2.py   SG food database builder
│   └── create-nutritrace-n8n.py n8n MCP webhook factory
├── n8n-workflows/               8 exportable workflow JSONs
├── config/
│   ├── docker-compose.yml
│   └── .env.example
└── Makefile
```

## Quick Start

```bash
cp config/.env.example .env     # set JWT_SECRET and data paths
docker compose -f config/docker-compose.yml up -d

# build food database
docker exec nutritrace python3 /tmp/build-sg-food-db-v2.py
docker exec nutritrace python3 -c "
import sqlite3; conn = sqlite3.connect('/data/db/nutritrace.db')
conn.execute('UPDATE foods SET user_id=1 WHERE user_id IS NULL')
conn.commit()"

# create n8n MCP webhooks (for Claude access)
python3 scripts/create-nutritrace-n8n.py
```

## REST API

`http://host:3002` — no auth, internal LAN, pure stdlib.

| Method | Path | Purpose |
|---:|---:|---|
| GET | `/health` | Health check |
| GET | `/weight/history` | All weight entries |
| POST | `/weight/log` | Log a weight entry |
| GET | `/diary/:date` | Diary for a date |
| POST | `/diary/add` | Log food by name |
| GET | `/foods/search?q=&limit=` | Fuzzy food search |
| GET | `/foods/:id` | Single food detail |
| GET | `/foods/categories` | All categories with counts |
| GET | `/stats/daily?date=` | Daily totals per meal |
| GET | `/stats/weekly` | 7-day rollup + averages |

## n8n MCP Webhooks

8 workflows exported in `n8n-workflows/`. Import into n8n, enable `availableInMCP`, done.

| Webhook | Method | What |
|---|---|---|
| `nutritrace-search-foods` | GET | Search food database |
| `nutritrace-weight-history` | GET | Weight timeline |
| `nutritrace-daily-stats` | GET | Daily calorie/macro summary |
| `nutritrace-weekly-stats` | GET | 7-day stats with averages |
| `nutritrace-food-categories` | GET | All 37 categories |
| `nutritrace-diary-get` | GET | Full diary entry |
| `nutritrace-food-by-id` | GET | Single food by ID |
| `nutritrace-diary-add` | POST | Add food to diary |

## Food Database

632+ foods across 37 categories — Singapore-centric, continuously expanding:

- Hawker: rice dishes, noodle soups, fried, snacks, hot and cold drinks
- Japanese: ramen, sushi, donburi, katsu, tempura, sides
- Chinese / Zi Char: dim sum, stir-fries, noodles, congee, seafood
- Korean: BBQ, stews, fried chicken, banchan
- Western: pasta variants, burgers, steaks, salads, sandwiches
- Indian: thali, biryani, curries, naan, tandoori
- Thai, Vietnamese, Indonesian, Middle Eastern
- Fast food: McDonald's, KFC, Subway, MOS, Jollibee
- Bakery, breakfast, bubble tea, hot pot, desserts, drinks

## Known Quirks

- **Diary items are inlined full food objects** — no `food_id` field. Read nutrition directly from `item.nutrition`.
- **Nutrition key inconsistency** — most foods use `proteins`/`carbohydrates`, some use `protein`/`carbs`. Stats aggregator normalizes both.
- **Meal slots are numeric** — `0`=breakfast, `1`=lunch, `2`=dinner, `3`=snacks.
- **`diary` table has no `created_at`** — only `updated_at`.
- **Zero pip dependencies** — everything is Python stdlib.

## License

MIT
