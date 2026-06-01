# n8n Workflow Exports

14 JSON files — clean exports of the n8n webhook workflows that power NutriBridge's MCP integration for Claude.

## Import into n8n

1. In n8n, go to **Workflows → Import from File**
2. Select the `.json` file
3. After import, set `availableInMCP: true`, `callerPolicy: workflowsFromSameOwner`
4. Click **Active** to enable the webhook

## Workflows

### REST-backed (hits nutritrace-api:3002)
| File | Method | Description |
|:---|:---|:---|
| `nutritrace-diary-add-mcp.json` | POST | Log food to diary by name |
| `nutritrace-diary-get-mcp.json` | GET | Full diary for a date |
| `nutritrace-search-foods-mcp.json` | GET | Search food database |
| `nutritrace-daily-stats-mcp.json` | GET | Daily calorie/macro summary + net kcal |
| `nutritrace-weekly-stats-mcp.json` | GET | 7-day stats with averages |
| `nutritrace-food-categories-mcp.json` | GET | All 37 food categories |
| `nutritrace-food-by-id-mcp.json` | GET | Single food by ID |
| `nutritrace-weight-history-mcp.json` | GET | All weight entries |
| `nutritrace-weight-log-mcp.json` | POST | Log a weight entry |

### MCP-backed (JSON-RPC via nutritrace-mcp:3003)
| File | Method | Description |
|:---|:---|:---|
| `nutritrace-health-mcp.json` | GET | API health check |
| `nutritrace-diary-range-mcp.json` | GET | Diary date range |
| `nutritrace-activity-get-mcp.json` | GET | Activities for a date |
| `nutritrace-activity-sum-mcp.json` | GET | Activity calorie summary |
| `nutritrace-activity-log-mcp.json` | POST | Log a manual activity |

## Notes

- Exported from tech-vm's n8n instance on 2026-06-01
- Ephemeral fields (IDs, timestamps) stripped — n8n regenerates on import
- MCP-backed workflows unwrap JSON-RPC `result.content[0].text` before returning
- REST-backed workflows target `http://100.111.123.105:3002` — change for other hosts
- MCP-backed workflows target `http://100.111.123.105:3003/mcp` — same caveat
