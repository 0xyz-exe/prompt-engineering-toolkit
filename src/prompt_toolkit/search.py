"""Search prompts by keyword, tag, category."""
import json
from pathlib import Path
from typing import List, Dict


def search_prompts(query: str, prompts_dir: Path) -> List[Dict]:
    """Search prompts by keyword in title, description, tags, content."""
    results = []
    query_lower = query.lower()
    
    json_dir = prompts_dir / "prompts-json"
    if not json_dir.exists():
        return results
    
    for json_file in sorted(json_dir.glob("*.json")):
        try:
            data = json.loads(json_file.read_text())
            
            # Search in title, description, tags, prompt text
            searchable = " ".join([
                data.get("title", ""),
                data.get("description", ""),
                " ".join(data.get("tags", [])),
                data.get("prompt", "")
            ]).lower()
            
            if query_lower in searchable:
                results.append({
                    "id": data.get("id"),
                    "title": data.get("title"),
                    "category": data.get("category"),
                    "description": data.get("description"),
                    "file": json_file.name
                })
        except:
            pass
    
    return results


def list_prompts(prompts_dir: Path, category: str = None) -> List[Dict]:  # type: ignore
    """List all prompts, optionally filtered by category."""
    results = []
    json_dir = prompts_dir / "prompts-json"
    
    if not json_dir.exists():
        return results
    
    for json_file in sorted(json_dir.glob("*.json")):
        try:
            data = json.loads(json_file.read_text())
            if category and data.get("category") != category:
                continue
            results.append({
                "id": data.get("id"),
                "title": data.get("title"),
                "category": data.get("category"),
                "version": data.get("version")
            })
        except:
            pass
    
    return results
