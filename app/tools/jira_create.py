from fastapi import APIRouter
from app.schemas.create_jira import CreateJiraTicketRequest
from app.services.jira_client import create_ticket

router = APIRouter()

@router.post("/create_jira_ticket")
def create_jira_ticket(request: CreateJiraTicketRequest):
    """
    MCP Tool: Creates a Jira ticket based on input fields.
    """
    try:
        result = create_ticket(request)
        return {"issueKey": result.get("key"), "message": "✅ Ticket created successfully."}
    except Exception as e:
        return {"error": str(e)}
