from fasthtml.common import *
from agents.extractor import process_data
from app.components import PageLayout, HeroSection, ExtractionForm, SuccessDisplay, ErrorDisplay, LoadingIndicator
import json

# Initialize App
app, rt = fast_app(
    hdrs=(picolink,) 
)

@rt('/')
def get():
    """Renders the Home Page"""
    return PageLayout(
        "Structura | AI Data Architect",
        [
            HeroSection(),
            ExtractionForm(),
            LoadingIndicator(),
            Div(id="result-area") # Target for HTMX results
        ]
    )

@rt('/extract')
async def post(text_input: str, schema_type: str):
    """
    Handles the HTMX POST request.
    Returns ONLY the result component (HTML snippet), not the full page.
    """
    if not text_input:
        return ErrorDisplay("Please provide input text to analyze.")
    
    try:
        # 1. Call the PydanticAI Agent
        data = await process_data(text_input, schema_type)
        
        # 2. Check for Agent-level errors
        if isinstance(data, dict) and "error" in data:
            return ErrorDisplay(f"Agent Error: {data['error']}")
        
        # 3. Serialize Pydantic Model to JSON
        # Robust check: if it's already a dict/list, dump it; if it's a Pydantic model, use model_dump_json
        if hasattr(data, 'model_dump_json'):
            json_str = data.model_dump_json(indent=2)
        else:
            json_str = json.dumps(data, indent=2)
        
        # 4. Return Success Component
        return SuccessDisplay(json_str)
        
    except Exception as e:
        # 5. Handle System Crashes
        return ErrorDisplay(f"System Critical: {str(e)}")

# Expose app for Uvicorn
target = app
