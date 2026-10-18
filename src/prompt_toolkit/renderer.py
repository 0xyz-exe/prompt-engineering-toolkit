"""Safe prompt rendering with placeholder substitution."""
import json
import re
from pathlib import Path
from typing import Dict, Any


def render_prompt(prompt_id: str, inputs: Dict[str, Any], prompts_dir: Path) -> str:
    """Render prompt with safe placeholder substitution."""
    json_dir = prompts_dir / "prompts-json"
    json_file = None
    
    for f in json_dir.glob("*.json"):
        data = json.loads(f.read_text())
        if data.get("id") == prompt_id:
            json_file = f
            break
    
    if not json_file:
        raise FileNotFoundError(f"Prompt {prompt_id} not found")
    
    data = json.loads(json_file.read_text())
    prompt_text = data['prompt']
    
    # Validate required inputs
    required_inputs = [inp['name'] for inp in data.get('inputs', []) if inp['required']]
    missing = [name for name in required_inputs if name not in inputs]
    if missing:
        raise ValueError(f"Missing required inputs: {', '.join(missing)}")
    
    # Safe substitution - only replace declared placeholders
    declared_names = [inp['name'] for inp in data.get('inputs', [])]
    for name in declared_names:
        if name in inputs:
            # Simple string replacement, no eval
            placeholder = "{" + name + "}"
            prompt_text = prompt_text.replace(placeholder, str(inputs[name]))
    
    return prompt_text
