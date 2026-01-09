import os

def load_prompt(filename):
    """
    Reads a prompt file from the ../prompts directory.
    """
    # Get current directory (src/utils)
    current_dir = os.path.dirname(__file__)
    # Go up one level to src, then into prompts
    prompts_dir = os.path.join(os.path.dirname(current_dir), 'prompts')
    file_path = os.path.join(prompts_dir, filename)
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"❌ Critical: Prompt file '{filename}' missing at {file_path}")
