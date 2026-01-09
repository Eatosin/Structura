# 1. Base Image
FROM python:3.11-slim

# 2. System Setup (Minimal build dependencies)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# 3. Create Non-Root User (Security Best Practice)
RUN useradd -m -u 1000 user

# 4. Set Workspace
WORKDIR /app

# 5. Install Dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 6. Copy Code & Enforce Ownership
# We use --chown to ensure files belong to the user
COPY --chown=user . .

# 7. CRITICAL FIX: Ensure the user owns the directory (for .sesskey creation)
RUN chown -R user:user /app

# 8. Switch to User & Set Path
USER user
ENV PATH="/home/user/.local/bin:$PATH"
ENV PYTHONPATH=/app

# 9. Run Entry Point
CMD ["python", "run.py"]
