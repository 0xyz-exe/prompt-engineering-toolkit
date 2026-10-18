"""Tests for CLI functionality."""
import json
import subprocess
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from prompt_toolkit.search import search_prompts, list_prompts


def test_list_prompts():
    """Test listing prompts."""
    repo_root = Path(__file__).parent.parent
    prompts = list_prompts(repo_root)
    
    assert len(prompts) >= 20
    assert all("id" in p for p in prompts)
    assert all("title" in p for p in prompts)


def test_search_prompts():
    """Test searching prompts."""
    repo_root = Path(__file__).parent.parent
    results = search_prompts("debugging", repo_root)
    
    assert len(results) > 0
    assert any("debug" in r["title"].lower() for r in results)


def test_search_by_category():
    """Test filtering by category."""
    repo_root = Path(__file__).parent.parent
    results = list_prompts(repo_root, category="software-engineering")
    
    assert len(results) > 0
    assert all(p["category"] == "software-engineering" for p in results)
