import asyncio
import os
from dotenv import load_dotenv
# from langchain_openai import ChatOpenAI
from mcp_use import MCPAgent, MCPClient
from langchain_groq import ChatGroq

async def main():
    # Load environment variables
    load_dotenv()

    # Create MCPClient from config file
    client = MCPClient.from_config_file(
        os.path.join(os.path.dirname(__file__), "mcp.json")
    )

    # Create LLM
    # llm = ChatOpenAI(model="gpt-4o")
    # Alternative models:
    # llm = ChatAnthropic(model="claude-3-5-sonnet-20240620")
    llm = ChatGroq(model="qwen-qwq-32b")

    # Create agent with the client
    agent = MCPAgent(llm=llm, client=client, max_steps=30,memory_enabled=True)

    # Run the query
    while True:
        if (query := input("Enter your query (or 'exit' to quit): ").strip().lower()) == "exit":
            print("Exiting...")
            break
        result = await agent.run(
        query,
        max_steps=15,
    )
        print(f"\nResult: {result}")  

if __name__ == "__main__":
    asyncio.run(main())