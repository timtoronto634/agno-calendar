from agno.agent import Agent
from agno.tools.googlecalendar import GoogleCalendarTools
import datetime
import os
from tzlocal import get_localzone_name

agent = Agent(
    tools=[GoogleCalendarTools(credentials_path="./client_secret_743826733935-9dkeocjinkl2egoa26ufsi1mt9vu6he2.apps.googleusercontent.com.json")],
    show_tool_calls=True,
    instructions=[
        f"""
        You are scheduling assistant . Today is {datetime.datetime.now()} and the users timezone is {get_localzone_name()}.
        You should help users to perform these actions in their Google calendar:
            - get their scheduled events from a certain date and time
            - create events based on provided details
        """
    ],
    add_datetime_to_instructions=True,
)

agent.print_response("on weekday of next week, search for 2 hours from 7 for drinking", markdown=True)
