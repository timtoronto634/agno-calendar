from agno.agent import Agent
from agno.tools.googlecalendar import GoogleCalendarTools
import datetime
import os
from tzlocal import get_localzone_name

agent = Agent(
    tools=[GoogleCalendarTools(credentials_path="./client_secret.json")],
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

agent.print_response("on Sunday this week, create a plan at 6:00～7:00 PM online meeting with X-san. here is the video link https://meet.google.com/xxx-xxxx-xxx", markdown=True)
