from agno.playground import Playground, serve_playground_app
from open_ai import web_agent

app = Playground(agents=[web_agent]).get_app()


if __name__ == "__main__":
    serve_playground_app("web_ui:app", reload=True)