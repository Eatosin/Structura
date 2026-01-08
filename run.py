import uvicorn
import os
import logging

# Configure production logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("Structura")

if __name__ == "__main__":
    # Hugging Face expects Port 7860. Render expects $PORT.
    port = int(os.getenv("PORT", 7860))
    
    logger.info(f"🚀 Structura System Starting on Port {port}...")
    
    # We import the app string to allow workers to load it dynamically
    uvicorn.run(
        "app.main:app", 
        host="0.0.0.0", 
        port=port, 
        reload=False, # Set to True for local dev
        log_level="info"
    )
