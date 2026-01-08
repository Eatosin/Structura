from fasthtml.common import *
from app.components import Layout, InputForm, ResultDisplay

app, rt = fast_app()

@rt('/')
def get():
    return Layout(
        "Structura | AI Data Architect",
        Div(
            InputForm(),
            Br(),
            Div(id="result-area") # The target for HTMX
        )
    )

@rt('/extract')
async def post(text_input: str, schema_type: str):
    if not text_input:
        return ResultDisplay(error="Please provide input text.")

    # --- AGENT CONNECTION ---
    try:
        # TODO: Connect to PydanticAI Agent here
        # real_data = await process_data(text_input, schema_type)
        
        # Mock Response to prove UI works
        import json
        mock_data = {
            "status": "success", 
            "schema": schema_type, 
            "extracted_data": "Agent logic coming in Batch 3"
        }
        json_str = json.dumps(mock_data, indent=2)
        
        return ResultDisplay(json_data=json_str)
        
    except Exception as e:
        return ResultDisplay(error=str(e))

# Expose 'app' for the runner
target = app
