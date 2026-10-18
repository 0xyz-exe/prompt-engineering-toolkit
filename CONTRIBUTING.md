# Contributing to Prompt Engineering Toolkit

Thank you for your interest in contributing!

## How to Contribute

### Adding a New Prompt

1. **Create JSON Definition**
   - Create a new file in `prompts-json/` named `XXX-your-prompt-name.json`
   - Use the next available PE-XXX ID (check existing prompts)
   - Follow the schema in `schemas/prompt.schema.json`

2. **Required Fields**
   ```json
   {
     "id": "PE-021",
     "title": "Your Prompt Title",
     "version": "1.0.0",
     "category": "software-engineering|ai-prompt-engineering|business-productivity|specialized-tools",
     "description": "Brief description (10-500 chars)",
     "prompt": "Complete prompt text with {placeholder} syntax",
     "inputs": [
       {
         "name": "placeholder_name",
         "type": "string",
         "required": true,
         "description": "What this input is for"
       }
     ],
     "output_format": "markdown|json|yaml|plain-text|code|structured",
     "quality_checks": [
       "Criterion 1",
       "Criterion 2"
     ],
     "tags": ["tag1", "tag2"]
   }
   ```

3. **Prompt Quality Guidelines**
   - Clear role definition (Act as a...)
   - Specific objective
   - Structured workflow
   - Measurable quality criteria
   - Safe and ethical
   - Minimum 50 characters of actual prompt content
   - Use placeholders for variable inputs: `{variable_name}`

4. **Validate Your Prompt**
   ```bash
   prompt-toolkit validate
   ```

5. **Test Your Prompt**
   - Manually test with real inputs
   - Verify output matches expectations
   - Check all placeholders are defined in inputs

6. **Submit Pull Request**
   - Update CHANGELOG.md with your addition
   - Include example usage in PR description
   - Ensure all tests pass

### Improving Existing Prompts

1. Read the prompt thoroughly
2. Identify the improvement (clarity, completeness, correctness)
3. Update the JSON file
4. Increment the `version` using semantic versioning
5. Run validation: `prompt-toolkit validate`
6. Submit PR with clear explanation of changes

### Reporting Issues

- Use GitHub Issues
- Provide prompt ID and version
- Describe expected vs. actual behavior
- Include example inputs if relevant

### Code Contributions

- Follow existing code style
- Add tests for new features
- Update documentation
- Ensure all tests pass: `pytest tests/ -v`

## Style Guide

### JSON Formatting
- Use 2-space indentation
- Keep lines under 120 characters where possible
- Use double quotes
- No trailing commas

### Prompt Writing
- Use active voice
- Be specific and concrete
- Structure with clear sections
- Include examples where helpful
- Define success criteria explicitly

## Questions?

Open a GitHub Discussion or Issue.
