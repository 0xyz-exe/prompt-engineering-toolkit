# Prompt Engineering Toolkit

A professional, open-source library of 20+ high-quality, reusable prompts for software engineering, AI systems, business productivity, and specialized workflows. Includes a Python CLI for searching, validating, rendering, and exporting prompts.

Repository: https://github.com/0xyz-exe/prompt-engineering-toolkit

## Screenshots

### CLI Interactive Search & Prompt Explorer
![CLI Search](docs/screenshots/01_cli_search.png)

### Prompt Template Rendering & Placeholders
![Prompt Rendering](docs/screenshots/02_prompt_render.png)

### JSON Schema Validation & Verification
![Schema Validation](docs/screenshots/03_schema_validation.png)

### Markdown & Text Export Pipeline
![Export Pipeline](docs/screenshots/04_export_prompts.png)

## Features

- **20+ Professional Prompts** organized into 4 categories
- **Multiple Formats**: JSON (machine-readable), Markdown (human-readable), TXT (copy-paste)
- **JSON Schema Validation** ensures prompt quality and consistency
- **Python CLI** for search, validation, rendering, and export
- **Safe Placeholder Rendering** with input validation
- **Zero Cost** - no paid APIs or subscriptions required
- **Open Source** - MIT licensed

## Prompt Categories

### Software Engineering (8 prompts)
- **PE-001**: PRD Generator - Comprehensive product requirements documents
- **PE-002**: Full-Stack Application Builder - Complete application implementation
- **PE-003**: UI/UX Design Brief Generator - Detailed design specifications
- **PE-004**: Debugging and Root-Cause Analysis - Evidence-based debugging workflow
- **PE-005**: Code Review and Refactoring - Comprehensive code quality analysis
- **PE-006**: Playwright E2E Test Engineer - Browser-based end-to-end tests
- **PE-007**: API Design and Documentation - REST API specifications
- **PE-008**: Security Audit - Application security review

### AI & Prompt Engineering (6 prompts)
- **PE-009**: Master Prompt Generator - Convert vague requests to structured prompts
- **PE-010**: Prompt Optimizer - Analyze and improve existing prompts
- **PE-011**: AI Agent Workflow Architect - Design autonomous agent workflows
- **PE-012**: RAG Application Designer - Retrieval-Augmented Generation systems
- **PE-013**: AI Evaluation Framework - Test cases, scoring rubrics, failure analysis
- **PE-014**: Data Analysis and Research Assistant - Evidence-based research methodology

### Business & Productivity (4 prompts)
- **PE-015**: Business Idea Validator - Market analysis and validation experiments
- **PE-016**: Startup MVP Planner - MVP backlog, architecture, launch checklist
- **PE-017**: Technical Documentation Generator - Installation guides, API docs, troubleshooting
- **PE-018**: Professional Writing Assistant - Emails, proposals, reports with tone control

### Specialized Tools (2 prompts)
- **PE-019**: Data Cleaning and Transformation - ETL pipelines with validation
- **PE-020**: Deployment and CI/CD Engineer - Deployment plans, rollback strategies, monitoring

## Quick Start

### Installation

```bash
# Clone the repository
git clone <repository-url>
cd prompt-engineering-toolkit

# Install the CLI
pip install -e .
```

### Using Prompts Manually

Browse prompts in the `prompts/` directory (Markdown format) or `prompts-json/` (JSON format).

Copy the prompt text and substitute placeholders like `{product_name}` with your values.

### Using the CLI

```bash
# List all prompts
prompt-toolkit list

# Search for prompts
prompt-toolkit search "debugging"

# Show a specific prompt
prompt-toolkit show PE-004

# Validate the entire library
prompt-toolkit validate

# Export a prompt to TXT
prompt-toolkit export PE-004 --format txt

# Render a prompt with inputs
prompt-toolkit render PE-004 --input my-inputs.json
```

### Example: Rendering a Prompt

Create an input file `inputs.json`:

```json
{
  "error_message": "TypeError: Cannot read property 'id' of undefined",
  "error_context": "User profile page when user is not logged in",
  "reproduction_steps": "1. Log out\n2. Navigate to /profile\n3. Error occurs"
}
```

Render the prompt:

```bash
prompt-toolkit render PE-004 --input inputs.json > rendered-prompt.txt
```

## Prompt Structure

Each prompt includes:

1. **Role Definition** - Who the AI should act as
2. **Context** - Background information and constraints
3. **Objective** - Clear goal and expected outcome
4. **Workflow** - Step-by-step execution plan
5. **Output Format** - Structure of the deliverable
6. **Quality Criteria** - Verification checklist
7. **Input Placeholders** - Required and optional inputs

## File Formats

### JSON (Canonical)
Machine-readable format in `prompts-json/`:
- Complete prompt definitions
- Input/output specifications
- Validation rules
- Metadata and tags

### Markdown (Human-Readable)
Coming soon in `prompts/`: Formatted for easy reading and editing.

### TXT (Copy-Paste)
Export any prompt to plain text for immediate use.

## Validation

Run validation to ensure all prompts meet quality standards:

```bash
prompt-toolkit validate
```

Checks:
- JSON schema compliance
- Unique prompt IDs
- Required fields present
- Prompt text is substantive
- No duplicate content

## CLI Reference

### `list [category]`
List all prompts or filter by category.

**Example:**
```bash
prompt-toolkit list software-engineering
```

### `search <query>`
Search prompts by keyword in title, description, tags, and content.

**Example:**
```bash
prompt-toolkit search "security audit"
```

### `show <prompt-id>`
Display complete prompt definition in JSON format.

**Example:**
```bash
prompt-toolkit show PE-009
```

### `validate`
Validate all prompts against the JSON schema.

**Example:**
```bash
prompt-toolkit validate
```

### `export <prompt-id> [--format txt|json]`
Export a prompt to the specified format.

**Example:**
```bash
prompt-toolkit export PE-001 --format txt
```

### `render <prompt-id> --input <file.json>`
Render a prompt by substituting placeholders with values from a JSON file.

**Example:**
```bash
prompt-toolkit render PE-015 --input business-idea.json
```

## Prompt Engineering Principles

These prompts follow best practices:

- **Clarity**: Specific, unambiguous instructions
- **Completeness**: All necessary context provided
- **Verifiability**: Measurable success criteria
- **Safety**: Security and permission boundaries
- **Reusability**: Adaptable to different contexts
- **Evidence-Based**: Request verification, not claims

## Contributing

Contributions welcome! To add a new prompt:

1. Create a JSON file in `prompts-json/` following the schema
2. Assign the next available PE-XXX ID
3. Include all required fields: id, title, version, category, description, prompt
4. Define inputs with clear descriptions
5. Specify quality_checks for verification
6. Run `prompt-toolkit validate` to ensure compliance
7. Submit a pull request

## Testing

Run tests to verify functionality:

```bash
# Install test dependencies
pip install pytest

# Run all tests
pytest tests/ -v
```

Tests cover:
- Schema validation
- Prompt inventory (count and uniqueness)
- Search functionality
- Export functionality
- CLI commands

## License

MIT License - see LICENSE file for details.

## Limitations

- Prompts improve clarity and structure but cannot guarantee AI output quality
- Model capabilities and available tools affect results
- Some prompts are optimized for specific AI systems (noted in metadata)
- Validation catches structural issues, not semantic quality
- Manual review recommended for production use

## Roadmap

- [ ] Generate Markdown versions of all prompts
- [ ] Add prompt templates with common patterns
- [ ] Build static web UI for browsing prompts
- [ ] Add example inputs and outputs for each prompt
- [ ] Create prompt composition tools
- [ ] Add version history and changelog per prompt

## Support

- **Documentation**: This README
- **Issues**: GitHub Issues
- **Discussions**: GitHub Discussions

---

Built with focus on accuracy, security, maintainability, and verified results.
