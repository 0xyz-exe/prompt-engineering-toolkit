"""Tests for prompt schema validation."""
import json
import pytest
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from prompt_toolkit.validator import validate_library, validate_prompt, load_schema


def test_schema_loads():
    """Test that schema loads successfully."""
    schema = load_schema()
    assert schema is not None
    assert "$schema" in schema
    assert "properties" in schema


def test_all_prompts_valid():
    """Test that all prompts pass schema validation."""
    repo_root = Path(__file__).parent.parent
    results = validate_library(repo_root)
    
    if results:
        for filename, errors in results.items():
            print(f"\n{filename}:")
            for error in errors:
                print(f"  - {error}")
    
    assert len(results) == 0, f"Found {len(results)} prompts with validation errors"


def test_unique_ids():
    """Test that all prompt IDs are unique."""
    repo_root = Path(__file__).parent.parent
    json_dir = repo_root / "prompts-json"
    
    ids = []
    for json_file in json_dir.glob("*.json"):
        data = json.loads(json_file.read_text())
        ids.append(data.get("id"))
    
    assert len(ids) == len(set(ids)), "Duplicate prompt IDs found"


def test_prompt_count():
    """Test that we have at least 20 prompts."""
    repo_root = Path(__file__).parent.parent
    json_dir = repo_root / "prompts-json"
    
    count = len(list(json_dir.glob("*.json")))
    assert count >= 20, f"Expected at least 20 prompts, found {count}"


def test_prompt_fields_not_empty():
    """Test that prompt text is not empty."""
    repo_root = Path(__file__).parent.parent
    json_dir = repo_root / "prompts-json"
    
    for json_file in sorted(json_dir.glob("*.json")):
        data = json.loads(json_file.read_text())
        assert len(data.get("prompt", "")) > 100, f"{json_file.name}: prompt text too short"
        assert data.get("title"), f"{json_file.name}: missing title"
        assert data.get("description"), f"{json_file.name}: missing description"
