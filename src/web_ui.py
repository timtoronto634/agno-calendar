from agno.playground import Playground, serve_playground_app
from open_ai import web_agent
from googlecalendar_tools import calendar_agent

agent_storage: str = "tmp/agents.db"

app = Playground(agents=[web_agent, calendar_agent]).get_app()


if __name__ == "__main__":
    serve_playground_app("web_ui:app", reload=True)