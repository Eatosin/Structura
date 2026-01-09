from fasthtml.common import *

def PageLayout(title: str, content: list):
    """
    The Base Layout.
    Injects PicoCSS (Styling), PrismJS (Syntax Highlight), and HTMX (Interactivity).
    """
    return Html(
        Head(
            Title(title),
            # 1. PicoCSS: Semantic minimalist framework
            Link(rel="stylesheet", href="https://cdn.jsdelivr.net/npm/@picocss/pico@latest/css/pico.min.css"),
            
            # 2. HTMX (CRITICAL FIX: Prevents page reloads)
            Script(src="https://unpkg.com/htmx.org@1.9.10"),

            # 3. PrismJS: For beautiful JSON highlighting
            Link(rel="stylesheet", href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism-tomorrow.min.css"),
            Script(src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js"),
            Script(src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/components/prism-json.min.js"),
            
            # Custom Styles
            Style("""
                body { max-width: 900px; margin: 0 auto; padding: 20px; background-color: #11191f; }
                .json-box { border-radius: 8px; overflow: hidden; margin-top: 20px; }
                h1 { color: #00E5FF; }
                button.contrast { background-color: #00E5FF; border-color: #00E5FF; color: black; font-weight: bold; }
                .error-box { background: #3d1a1a; color: #ff8080; padding: 15px; border-radius: 8px; border: 1px solid #ff4d4d; }
            """)
        ),
        Body(
            Header(
                H1("🛡️ Structura"),
                P("The Unbreakable Data Architect", style="opacity: 0.7;"),
                style="border-bottom: 1px solid #333; padding-bottom: 20px; margin-bottom: 40px;"
            ),
            Main(*content),
            Footer(
                P("Powered by PydanticAI & Gemini 2.5", style="text-align: center; opacity: 0.5; font-size: 0.8rem; margin-top: 50px;")
            )
        )
    )

# ... (Rest of components.py remains the same)
def HeroSection():
    return Div(
        H2("Turn Chaos into Structure"),
        P("Paste messy emails, invoices, or resumes below. Get guaranteed, type-safe JSON back."),
        style="margin-bottom: 30px;"
    )

def ExtractionForm():
    """
    The Interactive Form.
    Uses HTMX (hx-post) to swap the result area without a page reload.
    """
    return Form(
        Label("Raw Input Data"),
        Textarea(
            name="text_input", 
            placeholder="e.g. Invoice #909 from CloudFix for $500...",
            rows=8,
            style="font-family: monospace; background: #0b0f13; color: white; border: 1px solid #333;"
        ),
        
        Grid(
            Label("Target Schema", 
                Select(
                    Option("Invoice Extraction", value="invoice"),
                    Option("Resume Parsing", value="resume"), 
                    Option("Generic Data", value="generic"),
                    name="schema_type"
                )
            ),
            # Empty div for grid balance or future features
            Div() 
        ),
        
        Button("Extract Structure ⚡", cls="contrast", type="submit"),
        
        # HTMX Configuration
        hx_post="/extract",
        hx_target="#result-area",
        hx_swap="innerHTML",
        hx_indicator="#loading"
    )

def LoadingIndicator():
    return Div("⚙️ AI is processing...", id="loading", cls="htmx-indicator", style="color: #00E5FF; margin-top: 10px;")

def SuccessDisplay(json_str: str):
    return Div(
        H4("✅ Validated Output", style="color: #4ade80; margin-bottom: 10px;"),
        Div(
            Pre(Code(json_str, cls="language-json")),
            cls="json-box"
        ),
        P("Schema Verified by PydanticAI", style="color: grey; font-size: 0.8rem; margin-top: 10px; text-align: right;")
    )

def ErrorDisplay(error_msg: str):
    return Div(
        H4("❌ Extraction Failed"),
        P(error_msg),
        cls="error-box"
    )
