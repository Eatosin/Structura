import uvicorn
import os
import logging

# Configure structured logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("Structura")

if __name__ == "__main__":
    # Hugging Face Spaces defaults to 7860, Render uses PORT env var
    port = int(os.getenv("PORT", 7860))
    
    logger.info(f"🚀 Structura System Starting on Port {port}...")
    
    # Run Uvicorn with the FastHTML app factory
    uvicorn.run(
        "app.main:app", 
        host="0.0.0.0", 
        port=port, 
        reload=False,
        log_level="info"
    )
