import os
import nest_asyncio
from pydantic_ai import Agent
from .models import InvoiceSchema, ResumeSchema, GenericSchema
from utils.client import get_api_key
from utils.prompt_loader import load_prompt

# Fix loop for some environments
nest_asyncio.apply()

# Ensure key is available
os.environ["GOOGLE_API_KEY"] = get_api_key()

# Load the SOTA Master Prompt from YAML
master_system_prompt = load_prompt("system.yaml")

# Initialize Agent with GEMINI 2.5 FLASH (The 2026 Standard)
agent = Agent(
    'google-gla:models/gemini-2.5-flash',
    system_prompt=master_system_prompt 
)

async def process_data(text: str, schema_type: str):
    """
    Orchestrates the extraction process using the Externalized Prompt.
    """
    if schema_type == "invoice":
        target_model = InvoiceSchema
    elif schema_type == "resume":
        target_model = ResumeSchema
    else:
        target_model = GenericSchema

    try:
        # Run Agent with Type-Safe Output
        result = await agent.run(text, output_type=target_model)
        
        # Access Data (Universal Access)
        try:
            return result.data
        except:
            return result.output
            
    except Exception as e:
        return {"error": f"Agent Failure: {str(e)}"}
