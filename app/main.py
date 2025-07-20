from fastapi import FastAPI
from app.tools import jira_create, jira_query  # (You’ll create these files next)

app = FastAPI(
    title="MCP Tool Server for Jira",
    description="Exposes MCP-compatible tools like create_jira_ticket and list_jira_tickets.",
    version="1.0.0"
)

# Register your tools (routes)
app.include_router(jira_create.router, prefix="/tools")
app.include_router(jira_query.router, prefix="/tools")
    