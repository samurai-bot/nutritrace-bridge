.PHONY: deploy api-restart mcp-restart logs food-db n8n-webhooks test

# Deploy all containers
deploy:
	cd config && docker compose up -d

# Restart services
api-restart:
	cd config && docker compose restart nutritrace-api

mcp-restart:
	cd config && docker compose restart nutritrace-mcp

# View logs
logs:
	docker logs nutritrace-api --tail 50

# Rebuild food database
food-db:
	scp scripts/build-sg-food-db-v2.py ck@100.111.123.105:/home/ck/nutritrace/
	ssh ck@100.111.123.105 'docker cp /home/ck/nutritrace/build-sg-food-db-v2.py nutritrace:/tmp/ && docker exec nutritrace python3 /tmp/build-sg-food-db-v2.py'

# Create n8n MCP webhook workflows
n8n-webhooks:
	python3 scripts/create-nutritrace-n8n.py

# Quick smoke test
test:
	curl -s http://100.111.123.105:3002/health | python3 -m json.tool
	curl -s "http://100.111.123.105:3002/foods/search?q=prata&limit=2" | python3 -m json.tool
