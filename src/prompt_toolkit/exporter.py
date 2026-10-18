"""Export prompts to different formats."""
import json
from pathlib import Path


def export_to_txt(prompt_data: dict) -> str:
    """Export prompt to plain text."""
    lines = [
        f"# {prompt_data['title']}",
        f"ID: {prompt_data['id']} | Version: {prompt_data['version']} | Category: {prompt_data['category']}",
        "",
        prompt_data['description'],
        "",
        "=" * 80,
        "",
        prompt_data['prompt'],
    ]
    
    if prompt_data.get('inputs'):
        lines.extend(["", "", "REQUIRED INPUTS:", ""])
        for inp in prompt_data['inputs']:
            req = "REQUIRED" if inp['required'] else "optional"
            lines.append(f"- {inp['name']} ({inp['type']}, {req}): {inp['description']}")
    
    if prompt_data.get('quality_checks'):
        lines.extend(["", "", "QUALITY CHECKS:", ""])
        for check in prompt_data['quality_checks']:
            lines.append(f"- {check}")
    
    return "\n".join(lines)


def export_prompt(prompt_id: str, format: str, prompts_dir: Path, output_dir: Path = None) -> str:
    """Export single prompt to specified format."""
    json_dir = prompts_dir / "prompts-json"
    json_file = json_dir / f"{prompt_id.lower().replace('pe-', '')}.json"
    
    if not json_file.exists():
        # Try searching by ID
        for f in json_dir.glob("*.json"):
            data = json.loads(f.read_text())
            if data.get("id") == prompt_id:
                json_file = f
                break
    
    if not json_file.exists():
        raise FileNotFoundError(f"Prompt {prompt_id} not found")
    
    data = json.loads(json_file.read_text())
    
    if format == "txt":
        content = export_to_txt(data)
        if output_dir:
            out_file = output_dir / "txt" / f"{json_file.stem}.txt"
            out_file.parent.mkdir(parents=True, exist_ok=True)
            out_file.write_text(content)
            return str(out_file)
        return content
    elif format == "json":
        return json.dumps(data, indent=2)
    else:
        raise ValueError(f"Unsupported format: {format}")
