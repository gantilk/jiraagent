from pydantic import BaseModel

class CreateJiraTicketRequest(BaseModel):
    summary: str
    description: str
    assignee: str
    epic: str
    sprint: str
    project: str
    issuetype: str
