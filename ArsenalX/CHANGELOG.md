# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- GitHub standard files: README rewrite, CONTRIBUTING, SECURITY, LICENSE, CHANGELOG, and .gitignore.
- GitHub issue templates and pull request template.

## [1.1.0] - 2026-06-26

### Added
- Expanded `DEFAULT_TOOLS` database from 24 to 118+ real, commonly used ethical hacking tools.
- Organized tools into a robust two-level hierarchy (10 Categories → 34 Subcategories).
- Introduced a 3-level interactive hierarchical browser (`cmd_browse_default_tools`) to navigate categories and subcategories.
- Added paginated display for large subcategories (10 tools per page) to eliminate endless scrolling.
- Enabled custom tags input (comma-separated) when adding a new tool to My Tools.
- Added a comprehensive `help` command documenting the purpose, workflows, available commands, and examples.
- Updated the inline command parser to support `help` and `?`.

### Changed
- Refactored `print_tools_by_category` to display tool counts and support the new category structure.
- Updated `My Tools` display to render custom tags alongside tool descriptions.
- Modified the main menu and unknown-command hint to include the new `help` command.

## [1.0.0] - Initial Release

### Added
- Fast, minimal, hacker-themed CLI tool manager.
- Fuzzy search across tool names, descriptions, and categories.
- Preloaded with 24 default cybersecurity tools.
- Custom tool addition to a local `tools.json` file.
- OS-aware (Linux, macOS, Windows) installation execution with confirmation prompts.
- Export and import functionality for `tools.json`.
- Dual input mode supporting menu numbers or inline typed commands.
