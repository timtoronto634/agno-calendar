from agno.agent import Agent
from agno.models.anthropic import Claude
from agno.tools.googlecalendar import GoogleCalendarTools
import datetime
import os
from tzlocal import get_localzone_name
from agno.storage.sqlite import SqliteStorage
from storage import agent_storage

calendar_agent = Agent(
    name="Calendar Agent",
    model=Claude(id="claude-3-5-haiku-20241022"),
    tools=[GoogleCalendarTools(credentials_path="./client_secret.json")],
    show_tool_calls=True,
    instructions=[
        f"""
        You are scheduling assistant . Today is {datetime.datetime.now()} and the users timezone is {get_localzone_name()}.
        The user is
        - working on weekday and holidays are weekends
        - working from 9am to 7pm
        - Japanese national holidays apply
        You should help users to perform these actions in their Google calendar:
            - get their scheduled events from a certain date and time
            - create events based on provided details
        """
    ],
    add_datetime_to_instructions=True,
    storage=SqliteStorage(table_name="web_agent", db_file=agent_storage),
)
