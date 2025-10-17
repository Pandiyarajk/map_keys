# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Fixed
- Fixed UnicodeEncodeError in build.py that occurred on Windows systems with cp1252 encoding
  - Replaced Unicode checkmark (✓) and cross (✗) characters with ASCII alternatives ([SUCCESS] and [FAILED])
  - This resolves the build failure: `'charmap' codec can't encode character '\u2713'`

### Changed
- Updated README.md with correct GitHub repository URL (Pandiyarajk/map_keys)
- Added build script compatibility note in README.md

---

## [1.0.0] - Initial Release

### Added
- Key mapping functionality for Windows
- User-friendly GUI built with Tkinter
- Persistent configuration storage in JSON format
- Ability to restore original mappings
- Real-time activation/deactivation of hotkeys
- Visual feedback for active mappings
- Build script for creating standalone executable
- GitHub Actions workflow for automated builds
- Comprehensive documentation and troubleshooting guide

### Features
- Map keyboard shortcuts to launch any Windows application
- Support for modifier keys (Ctrl, Shift, Alt, Win)
- Support for function keys (F1-F12)
- Browse functionality for easy application selection
- Status indicator for mapping state
- Delete and refresh mapping capabilities

### Requirements
- Windows OS (7/8/10/11)
- Python 3.8+ (for running from source)
- Administrator privileges for keyboard hook functionality
