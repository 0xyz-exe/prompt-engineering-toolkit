"""Tests for export functionality."""
import json
from pathlib import Path
import sys

import pytest

sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from prompt_toolkit.exporter import export_prompt, export_to_txt


def test_export_to_txt():
    """Test exporting prompt to TXT format."""
    repo_root = Path(__file__).parent.parent
    json_dir = repo_root / "prompts-json"
    
    # Get first prompt
    json_file = list(json_dir.glob("*.json"))[0]
    data = json.loads(json_file.read_text())
    
    txt = export_to_txt(data)
    
    assert data["title"] in txt
    assert data["id"] in txt
    assert data["description"] in txt
    assert data["prompt"] in txt


def test_export_prompt_json():
    """Test exporting prompt to JSON format."""
    repo_root = Path(__file__).parent.parent
    json_dir = repo_root / "prompts-json"
    
    # Get first prompt
    json_file = list(json_dir.glob("*.json"))[0]
    data = json.loads(json_file.read_text())
    prompt_id = data["id"]
    
    result = export_prompt(prompt_id, "json", repo_root)
    
    exported_data = json.loads(result)
    assert exported_data["id"] == prompt_id
