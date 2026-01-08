from fasthtml.common import *

def Layout(title, content):
    """Global Page Layout with PicoCSS"""
    return Html(
        Head(
            Title(title),
            # PicoCSS: Minimalist Semantic CSS
            Link(rel="stylesheet", href="https://cdn.jsdelivr.net/npm/@picocss/pico@latest/css/pico.min.css"),
            # PrismJS: For beautiful JSON Syntax Highlighting
            Link(rel="stylesheet", href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism-tomorrow.min.css"),
            Script(src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js"),
            Script(src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/components/prism-json.min.js"),
            Style("body { max-width: 800px; margin: 0 auto; padding: 20px; }")
        ),
        Body(
            Header(
                H1("🛡️ Structura", style="color: #00E5FF; margin-bottom: 0;"),
                P("The Unbreakable Data Architect", style="opacity: 0.7;"),
                style="border-bottom: 1px solid #333; padding-bottom: 20px; margin-bottom: 40px;"
            ),
            Main(content),
            Footer(
                P("Powered by PydanticAI & Gemini 2.5", style="text-align: center; opacity: 0.5; font-size: 0.8rem;")
            )
        )
    )

def InputForm():
    """The HTMX-powered Input Form"""
    return Form(
        Label("Raw Input Data", cls="label"),
        Textarea(
            name="text_input", 
            placeholder="Paste messy text here (Email, Invoice, Job Post)...",
            rows=8,
            style="font-family: monospace;"
        ),
        
        Label("Target Schema", cls="label"),
        Select(
            Option("Invoice Extraction", value="invoice"),
            Option("Resume Parsing", value="resume"), 
            Option("Email Summary", value="email"),
            name="schema_type"
        ),
        
        Button("Extract Structure ⚡", cls="contrast", type="submit"),
        
        # HTMX Magic: Swaps the result div without reloading page
        hx_post="/extract",
        hx_target="#result-area",
        hx_swap="innerHTML"
    )

def ResultDisplay(json_data=None, error=None):
    """Renders the output or error state"""
    if error:
        return Div(
            H4("❌ Extraction Failed"),
            P(error),
            style="background: #3d1a1a; color: #ff8080; padding: 15px; border-radius: 8px; border: 1px solid #ff4d4d;"
        )
    
    if json_data:
        return Div(
            H4("✅ Validated JSON Output"),
            # Pre/Code blocks triggered PrismJS highlighting
            Pre(Code(json_data, cls="language-json")),
            P("Schema validation passed.", style="color: #00E5FF; font-size: 0.8rem; margin-top: 10px;")
        )
    
    return Div(id="result-area") # Empty placeholder
