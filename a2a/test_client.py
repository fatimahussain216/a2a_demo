import asyncio
from uuid import uuid4
import httpx
from a2a.client import A2AClient, A2ACardResolver
from a2a.types import SendMessageRequest, MessageSendParams


async def main():
    base_url = "http://localhost:8000"

    async with httpx.AsyncClient() as httpx_client:
        # Resolve agent card
        resolver = A2ACardResolver(
            httpx_client=httpx_client,
            base_url=base_url,
        )

        agent_card = await resolver.get_agent_card()
        print("Agent card loaded")

        # Create client
        client = A2AClient(
            httpx_client=httpx_client,
            agent_card=agent_card
        )

        # Build request
        send_message_payload = {
    "message": {
        "role": "user",
        "parts": [
            {"kind": "text", "text": "hi?"}
        ],
        "messageId": uuid4().hex
    }
}




        request = SendMessageRequest(
            id=str(uuid4()),
            params=MessageSendParams(**send_message_payload)
        )

        # Send message
        response = await client.send_message(request)
        print(response.model_dump(mode="json", exclude_none=True))


if __name__ == "__main__":
    asyncio.run(main())
