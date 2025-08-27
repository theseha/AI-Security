# Azure imports
from azure.identity import DefaultAzureCredential, get_bearer_token_provider # for advanced callback
from azure.ai.evaluation.red_team import RedTeam, RiskCategory, AttackStrategy
from openai import AzureOpenAI # for advanced callback
from dotenv import load_dotenv
import os
import asyncio
from functools import partial # for advanced callback

load_dotenv()

# Read credentials - DefaultAzureCredential() read .env values automatically
credential = DefaultAzureCredential()

## Using Azure AI Foundry project, example: AZURE_AI_PROJECT=https://your-account.services.ai.azure.com/api/projects/your-project
azure_ai_project = os.environ.get("AZURE_AI_PROJECT")

# Instantiate your AI Red Teaming Agent
red_team_agent = RedTeam(
    azure_ai_project=azure_ai_project, # required
    #credential=DefaultAzureCredential(), # required
    credential=credential,
    risk_categories=[ # you can change RiskCategories
        RiskCategory.Violence,
        RiskCategory.HateUnfairness,
        RiskCategory.Sexual,
        RiskCategory.SelfHarm
    ],
    num_objectives=10 # 10 by defaul, you can change
)

# A simple example application callback function that always returns a fixed response
def simple_callback(query: str) -> str:
    return "I'm an AI assistant that follows ethical guidelines. I cannot provide harmful content."

# AI models using OpenAI API
azure_openai_config = {
    "azure_endpoint": "https://<your-ai-foundry-project>.cognitiveservices.azure.com/openai/deployments/<azure-openai-model>/chat/completions?api-version=<azure-openai-version>",
    "azure_deployment": "<your-azure-openai-deployment-name", # e.g. gpt-35-turbo
    "model": "<your-azure-openai-model>", # e.g. gpt-35-turbo
    "api_key": "<your-azure-openai-api-key>",
}

# An advanced example application callback function that returns dynamic response communicated with Application
async def advanced_callback(messages, stream=False, session_state=None, context=None) -> dict[str, list[dict[str, str]]]:

    token_provider = get_bearer_token_provider(credential, "https://cognitiveservices.azure.com/.default")

    client = AzureOpenAI(
        azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
        api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),
        azure_ad_token_provider=token_provider
    )

    messages_list = [{"role": message.role, "content": message.content} for message in messages]
    latest_message = messages_list[-1]["content"]

    try:
        response = client.chat.completions.create(
            model = os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME"),
            messages = [
                {"role": "user", "content": latest_message},
            ],
            max_completion_tokens = 1000
        )
        formatted_response = {"role": "assistant", "content": response.choices[0].message.content}

    except Exception as e:
        print(f"Error calling Azure OpenAI: {e!s}")
        formatted_response = {"role": "assistant", "content": "I encountered an error and couldn't process your request"}

    return {"messages": [formatted_response]}

# Runs a red teaming scan on the simple callback target
async def main():
    red_team_result = await red_team_agent.scan(
        target=azure_openai_config, #advanced_callback, #simple_callback,
        scan_name="advanced-callback-scan(gpt-5)",
        attack_strategies=[ # Change strategies as you want
            AttackStrategy.UnicodeConfusable,
            AttackStrategy.Tense,
            AttackStrategy.Compose([AttackStrategy.Tense, AttackStrategy.Base64]),
        ],
        output_path="red_team_output.json",
    )
    print(red_team_result)

if __name__ == "__main__":
    asyncio.run(main())
