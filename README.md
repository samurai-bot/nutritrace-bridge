# 🦞 NutriBridge

**AI agent bridge for NutriTrace** — REST API + MCP server + n8n webhooks that let AI agents (PennyClaw, Hermia, Claude Code CLI) read and write nutrition/weight/food data from a self-hosted NutriTrace instance.

> Built 2026-05-31 by PennyClaw during a Sunday afternoon pairing session. Deployed on a homelab Proxmox cluster running Ubuntu 26.04.

## What It Does

NutriTrace is a self-hosted nutrition tracker (single Docker container, SQLite). It's great for humans but has no API layer for AI agents. NutriBridge fills that gap:

```
NutriTrace UI (:3000) ─── SQLite DB ─── NutriBridge (:3002 REST / :3003 MCP)
                                              │
                    ┌─────────────────────────┼──────────────────┐
                    │                         │                  │
               PennyClaw                  Hermia           Claude Code CLI
            (direct curl)           (native MCP tools)   (n8n MCP webhooks)
```

## Architecture

```
tech-vm (3 containers, shared SQLite)
├── nutritrace          (ghcr.io/traceapps/nutritrace:latest)  → :3000
├── nutritrace-api      (python:3.11-alpine)                   → :3002
├── nutritrace-mcp      (python:3.11-alpine)                   → :3003
└── SQLite DB           ~/nutritrace/data/db/nutritrace.db     632+ foods
```

Plus 8 n8n webhook workflows (`availableInMCP: true`) for Claude Code CLI access.

## Project Structure

```
nutritrace-bridge/
├── src/
│   ├── nutritrace-api.py       # REST API server (stdlib, zero deps)
│   └── nutritrace-mcp.py       # MCP JSON-RPC server (stdlib)
├── scripts/
│   ├── build-sg-food-db-v2.py  # Build SG food database (632+ foods)
│   └── create-nutritrace-n8n.py # Create n8n MCP webhook workflows
├── config/
│   ├── docker-compose.yml      # Deployment compose
│   └── .env.example            # Environment template
└── README.md
```

## Quick Start

```bash
# 1. Clone and configure
cd ~/nutritrace
cp config/.env.example .env
# Edit .env: set JWT_SECRET, DATA_DB_PATH, DATA_UPLOADS_PATH

# 2. Deploy NutriTrace + API + MCP
docker compose -f config/docker-compose.yml up -d

# 3. Build the food database
docker exec nutritrace python3 /tmp/build-sg-food-db-v2.py
docker exec nutritrace python3 -c "
import sqlite3; conn = sqlite3.connect('/data/db/nutritrace.db')
conn.execute(\"UPDATE foods SET user_id=1 WHERE user_id IS NULL AND deleted_at IS NULL\")
conn.commit()"

# 4. Create n8n MCP webhooks (if using Claude Code CLI)
python3 scripts/create-nutritrace-n8n.py
```

## REST API Endpoints

All at `http://{host}:3002`. No auth (internal LAN). See `src/nutritrace-api.py` for full docs.

| Method | Path | What it does |
|---|---|---|
| GET | `/health` | Health check |
| GET | `/weight/history` | All weight entries |
| POST | `/weight/log` | Log weight |
| GET | `/diary/:date` | Diary entry for date |
| GET/POST | `/diary/add` | Add food to diary |
| GET | `/foods/search?q=&limit=` | Search foods |
| GET | `/foods/:id` | Single food |
| GET | `/foods/categories` | All categories |
| GET | `/stats/daily?date=` | Daily nutrition summary |
| GET | `/stats/weekly` | 7-day stats + averages |

## n8n MCP Webhooks

8 webhook workflows exposed as MCP tools for Claude Code CLI:

| Webhook | Method | Purpose |
|---|---|---|
| `nutritrace-search-foods` | GET | Search food database |
| `nutritrace-weight-history` | GET | Weight timeline |
| `nutritrace-daily-stats` | GET | Daily calorie/macro summary |
| `nutritrace-weekly-stats` | GET | 7-day rollup |
| `nutritrace-food-categories` | GET | 37 categories |
| `nutritrace-diary-get` | GET | Full diary entry |
| `nutritrace-food-by-id` | GET | Single food details |
| `nutritrace-diary-add` | POST | Log food to diary |

## Food Database

632+ foods across 37 categories covering what a typical Singaporean eats:
- 🌾 Hawker: Rice, Noodle Soup, Fried, Snacks, Drinks (Hot + Cold)
- 🇯🇵 Japanese: Ramen, Sushi, Donburi, Katsu, Sides
- 🇨🇳 Chinese/Zi Char: Dim Sum, Stir-Fries, Noodles, Congee
- 🇰🇷 Korean: BBQ, Stews, Fried Chicken, Banchan
- 🍝 Western: 12 Pasta Variants, Burgers, Steaks, Salads
- 🇮🇳 Indian: Thali, Biryani, Curries, Naan, Tandoori
- 🇹🇭 Thai: Curries, Pad Thai, Tom Yum, Mango Sticky Rice
- 🇻🇳 Vietnamese: Pho, Banh Mi, Bun Cha, Spring Rolls
- 🍔 Fast Food: McDonald's, KFC, Subway, MOS, Jollibee
- 🍞 Bakery, 🍳 Breakfast, 🧋 Bubble Tea, 🍲 Hot Pot, 🦞 Seafood
- 🧆 Middle Eastern, 🍕 Pizza, 🍪 Desserts, 🥤 Drinks

## Known Quirks

- **Diary items are inlined full food objects** — no `food_id` joins. Read nutrition directly from `item.nutrition`.
- **Nutrition key inconsistency** — some foods use `proteins`/`carbohydrates`, others use `protein`/`carbs`. The stats aggregator normalizes both.
- **Meal slots are numeric:** `0`=breakfast, `1`=lunch, `2`=dinner, `3`=snacks.
- **No `created_at`** on diary table — only `updated_at`.
- **Zero pip dependencies** — everything is Python stdlib.

## License

MIT — do whatever you want. Feed your agents.
