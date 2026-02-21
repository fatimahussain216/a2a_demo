from a2a.server.agent_execution.context import RequestContext
from a2a.utils import new_agent_text_message
from a2a.server.agent_execution import AgentExecutor
from a2a.server.events.event_queue import EventQueue
from pydantic import BaseModel

class HelloWorldAgent(BaseModel):
    async def invoke(self) -> str:
        return "Hello Fatima"

class HelloWorldAgentExecutor:
    def __init__(self):
        self.agent = HelloWorldAgent()

    async def execute(self, request, event_queue, **kwargs):
        result = await self.agent.invoke()

        # Corrected function
        await event_queue.enqueue_event(
            new_agent_text_message(result)
        )

        return result

    async def cancel(self, request_id: str):
        # Agar cancel support nahi chahiye
        return None
