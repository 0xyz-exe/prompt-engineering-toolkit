"""Validate prompt definitions against schema."""
import json
from pathlib import Path
from typing import Dict, List, Tuple
import jsonschema


def load_schema() -> dict:
    """Load JSON schema."""
    schema_path = Path(__file__).parent.parent.parent / "schemas" / "prompt.schema.json"
    return json.loads(schema_path.read_text())


def validate_prompt(prompt_data: dict, schema: dict) -> Tuple[bool, List[str]]:
    """Validate single prompt. Returns (is_valid, errors)."""
    errors = []
    try:
        jsonschema.validate(instance=prompt_data, schema=schema)
    except jsonschema.ValidationError as e:
        errors.append(f"Schema validation: {e.message}")
    except jsonschema.SchemaError as e:
        errors.append(f"Schema error: {e.message}")
    return len(errors) == 0, errors


def validate_library(prompts_dir: Path) -> Dict[str, List[str]]:
    """Validate all prompts in library. Returns dict of filename -> errors."""
    schema = load_schema()
    results = {}
    seen_ids = set()
    
    json_dir = prompts_dir / "prompts-json"
    if not json_dir.exists():
        return {"_global": ["prompts-json directory not found"]}
    
    for json_file in sorted(json_dir.glob("*.json")):
        try:
            data = json.loads(json_file.read_text())
            is_valid, errors = validate_prompt(data, schema)
            
            # Check duplicate IDs
            if data.get("id") in seen_ids:
                errors.append(f"Duplicate ID: {data.get('id')}")
            seen_ids.add(data.get("id"))
            
            if errors:
                results[json_file.name] = errors
        except json.JSONDecodeError as e:
            results[json_file.name] = [f"Invalid JSON: {e}"]
        except Exception as e:
            results[json_file.name] = [f"Error: {e}"]
    
    return results
