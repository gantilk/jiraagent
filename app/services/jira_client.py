import os
import requests
from app.schemas.create_jira import CreateJiraTicketRequest
from dotenv import load_dotenv

load_dotenv()  # Load values from .env

JIRA_BASE_URL = os.getenv("JIRA_BASE_URL")  # e.g., https://yourdomain.atlassian.net
JIRA_EMAIL = os.getenv("JIRA_EMAIL")
JIRA_API_TOKEN = os.getenv("JIRA_API_TOKEN")

def create_ticket(request: CreateJiraTicketRequest) -> dict:
    url = f"{JIRA_BASE_URL}/rest/api/3/issue"

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }

    auth = (JIRA_EMAIL, JIRA_API_TOKEN)

    payload = {
        "fields": {
            "project": {"key": request.project},
            "summary": request.summary,
            "description": request.description,
            "issuetype": {"name": request.issuetype},
            "assignee": {"name": request.assignee},
            "customfield_10014": request.epic,  # Epic Link (Jira-specific field)
            "customfield_10007": request.sprint  # Sprint (may vary)
        }
    }

    response = requests.post(url, json=payload, headers=headers, auth=auth)
    response.raise_for_status()
    return response.json()
