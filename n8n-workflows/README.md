# n8n Workflow Exports

These 8 JSON files are clean exports of the n8n webhook workflows that power NutriBridge's MCP integration for Claude Code CLI.

## Import into n8n

1. In n8n, go to **Workflows → Import from File**
2. Select the `.json` file
3. After import, go to **Settings** and set `availableInMCP: true`, `callerPolicy: workflowsFromSameOwner`
4. Click **Active** to enable the webhook

## Workflows

| File | Method | Description |
|:---|:---|:---|
| `nutritrace-diary-add-mcp.json` | POST | Log food to diary by name |
| `nutritrace-diary-get-mcp.json` | GET | Get full diary for a date |
| `nutritrace-search-foods-mcp.json` | GET | Search food database |
| `nutritrace-daily-stats-mcp.json` | GET | Daily calorie/macro summary |
| `nutritrace-weekly-stats-mcp.json` | GET | 7-day stats with averages |
| `nutritrace-food-categories-mcp.json` | GET | All 37 food categories |
| `nutritrace-food-by-id-mcp.json` | GET | Single food by ID |
| `nutritrace-weight-history-mcp.json` | GET | All weight entries |

## Notes

- These were exported from tech-vm's n8n instance on 2026-05-31
- Ephemeral fields (IDs, timestamps, version counters) are stripped — n8n generates new ones on import
- Descriptions and MCP settings preserved
- All webhooks target `http://100.111.123.105:3002` — change this if deploying elsewhere
