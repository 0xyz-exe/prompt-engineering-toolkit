"""Command-line interface for prompt toolkit."""
import sys
import json
from pathlib import Path
from .validator import validate_library
from .search import search_prompts, list_prompts
from .exporter import export_prompt
from .renderer import render_prompt


def get_repo_root() -> Path:
    """Find repository root."""
    current = Path.cwd()
    while current != current.parent:
        if (current / "pyproject.toml").exists():
            return current
        current = current.parent
    return Path.cwd()


def cmd_list(args):
    """List prompts."""
    repo_root = get_repo_root()
    category = args[1] if len(args) > 1 else None
    prompts = list_prompts(repo_root, category)
    
    if not prompts:
        print("No prompts found")
        return 1
    
    for p in prompts:
        print(f"{p['id']:8} {p['category']:25} {p['title']}")
    print(f"\nTotal: {len(prompts)} prompts")
    return 0


def cmd_search(args):
    """Search prompts."""
    if len(args) < 2:
        print("Usage: prompt-toolkit search <query>")
        return 1
    
    repo_root = get_repo_root()
    query = " ".join(args[1:])
    results = search_prompts(query, repo_root)
    
    if not results:
        print(f"No prompts found matching '{query}'")
        return 1
    
    for r in results:
        print(f"{r['id']:8} {r['title']}")
        print(f"         {r['description'][:70]}")
        print()
    print(f"Found {len(results)} prompts")
    return 0


def cmd_show(args):
    """Show prompt details."""
    if len(args) < 2:
        print("Usage: prompt-toolkit show <prompt-id>")
        return 1
    
    repo_root = get_repo_root()
    prompt_id = args[1]
    
    try:
        json_dir = repo_root / "prompts-json"
        for f in json_dir.glob("*.json"):
            data = json.loads(f.read_text())
            if data.get("id") == prompt_id:
                print(json.dumps(data, indent=2))
                return 0
        print(f"Prompt {prompt_id} not found")
        return 1
    except Exception as e:
        print(f"Error: {e}")
        return 1


def cmd_validate(args):
    """Validate prompt library."""
    repo_root = get_repo_root()
    results = validate_library(repo_root)
    
    if not results:
        print("✓ All prompts valid")
        return 0
    
    print(f"Found {len(results)} files with errors:\n")
    for filename, errors in results.items():
        print(f"{filename}:")
        for error in errors:
            print(f"  - {error}")
        print()
    return 1


def cmd_export(args):
    """Export prompt to format."""
    if len(args) < 2:
        print("Usage: prompt-toolkit export <prompt-id> [--format txt|json]")
        return 1
    
    prompt_id = args[1]
    format = "txt"
    if "--format" in args:
        idx = args.index("--format")
        if idx + 1 < len(args):
            format = args[idx + 1]
    
    repo_root = get_repo_root()
    try:
        output = export_prompt(prompt_id, format, repo_root, repo_root / "exports")
        if format == "txt" and isinstance(output, str) and output.startswith("/"):
            print(f"Exported to {output}")
        else:
            print(output)
        return 0
    except Exception as e:
        print(f"Error: {e}")
        return 1


def cmd_render(args):
    """Render prompt with inputs."""
    if len(args) < 3 or "--input" not in args:
        print("Usage: prompt-toolkit render <prompt-id> --input <input.json>")
        return 1
    
    prompt_id = args[1]
    input_idx = args.index("--input")
    input_file = Path(args[input_idx + 1])
    
    if not input_file.exists():
        print(f"Input file not found: {input_file}")
        return 1
    
    repo_root = get_repo_root()
    try:
        inputs = json.loads(input_file.read_text())
        rendered = render_prompt(prompt_id, inputs, repo_root)
        print(rendered)
        return 0
    except Exception as e:
        print(f"Error: {e}")
        return 1


def main():
    """Main CLI entry point."""
    if len(sys.argv) < 2:
        print("""Prompt Engineering Toolkit

Usage:
  prompt-toolkit list [category]
  prompt-toolkit search <query>
  prompt-toolkit show <prompt-id>
  prompt-toolkit validate
  prompt-toolkit export <prompt-id> [--format txt|json]
  prompt-toolkit render <prompt-id> --input <input.json>
""")
        return 1
    
    command = sys.argv[1]
    commands = {
        "list": cmd_list,
        "search": cmd_search,
        "show": cmd_show,
        "validate": cmd_validate,
        "export": cmd_export,
        "render": cmd_render,
    }
    
    if command not in commands:
        print(f"Unknown command: {command}")
        return 1
    
    try:
        return commands[command](sys.argv[1:])
    except Exception as e:
        print(f"Error: {e}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
