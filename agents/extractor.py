import os
from pydantic_ai import Agent
from .models import InvoiceSchema, ResumeSchema, GenericSchema
from utils.client import get_api_key
from utils.prompt_loader import load_prompt

# Ensure API key is loaded into environment for the library
os.environ["GOOGLE_API_KEY"] = get_api_key()

# Load Externalized Prompt
master_system_prompt = load_prompt("system.yaml")

# Initialize Agent (Gemini 2.5 Flash)
# Note: Using the model ID compatible with Google's GenAI SDK
agent = Agent(
    'google-gla:models/gemini-2.5-flash',
    system_prompt=master_system_prompt
)

async def process_data(text: str, schema_type: str):
    """
    Orchestrates the extraction process.
    Selects the correct Pydantic schema and enforces type-safety.
    """
    # 1. Router Logic
    if schema_type == "invoice":
        target_model = InvoiceSchema
    elif schema_type == "resume":
        target_model = ResumeSchema
    else:
        target_model = GenericSchema

    try:
        # 2. Execution (With Schema Enforcement)
        # Using 'output_type' as required by PydanticAI v1.40+
        result = await agent.run(text, output_type=target_model)
        
        # 3. Result Parsing (Handle version differences in return object)
        if hasattr(result, 'data'):
            return result.data
        elif hasattr(result, 'output'):
            return result.output
        else:
            return result
            
    except Exception as e:
        return {"error": f"Extraction Logic Failed: {str(e)}"}
