# Change Log

All notable changes to the Key Mapper project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Planned Features
- Mouse button mapping support
- Multiple configuration profiles
- Import/export functionality
- Hotkey recording feature
- System tray integration
- Auto-start with Windows
- Dark mode theme
- Logging viewer in GUI

## [1.0.0] - 2025-10-17

### Added
- Initial release of Key Mapper application
- Core keyboard mapping functionality
- User-friendly GUI with Tkinter
- Add, delete, and manage key-to-application mappings
- Start/Stop mapping controls
- Restore original mappings functionality
- Persistent configuration storage (JSON format)
- Browse button for easy application selection
- Visual mapping list with treeview
- Status indicator (active/stopped)
- Real-time hotkey registration
- Error handling and logging
- Build script for creating Windows executable
- PyInstaller configuration
- GitHub Actions workflow for automated builds
- Automated release creation on git tags
- Build artifacts upload
- Comprehensive README documentation
- Sample configuration file generation
- Distribution package creation

### Features
- Map any key combination to launch Windows applications
- Support for common modifiers (Ctrl, Shift, Alt, Win)
- Support for function keys and alphanumeric keys
- Thread-safe hotkey management
- Application launcher for .exe, .lnk, and other file types
- Configuration file validation
- GUI with clear instructions
- Confirmation dialogs for destructive actions

### Technical Details
- Python 3.8+ compatible
- Uses `keyboard` library for global hotkey hooks
- Tkinter-based GUI (no external dependencies)
- JSON-based configuration storage
- Thread-safe operations with locks
- Comprehensive error logging
- Cross-module architecture (key_mapper, gui, build)

### Build System
- PyInstaller-based executable creation
- One-file executable output
- Windowed application (no console)
- Distribution package with documentation
- Sample configuration included
- Clean build process with artifact cleanup

### CI/CD
- GitHub Actions workflow for Windows builds
- Automatic build on push to main/master/develop
- Artifact retention for 30 days
- Automated releases on version tags
- Test framework integration (pytest support)
- Code coverage reporting (optional)

### Documentation
- Comprehensive README with installation instructions
- Usage guide with examples
- Troubleshooting section
- Security notes and best practices
- Architecture overview
- Contributing guidelines
- Feature roadmap

### Known Limitations
- Windows-only (due to OS-specific keyboard hooks)
- Requires administrator privileges for global hotkeys
- Cannot override system-level hotkeys
- No GUI notification for conflicting hotkeys

### Dependencies
- keyboard==0.13.5: For keyboard hook functionality
- pyinstaller==6.10.0: For creating standalone executable

### Security Considerations
- Administrator privileges required
- Global keyboard hook usage documented
- User guidance on trusted applications only
- No telemetry or data collection

---

## Version History

### Version Numbering
- **Major version**: Breaking changes or significant feature additions
- **Minor version**: New features, backward compatible
- **Patch version**: Bug fixes and minor improvements

### Release Process
1. Update version number in this file
2. Commit changes to main branch
3. Create and push git tag (e.g., `v1.0.0`)
4. GitHub Actions automatically builds and creates release
5. Download and test release artifacts
6. Update release notes on GitHub if needed

---

## Future Versions

### [1.1.0] - Planned
- System tray icon support
- Minimize to tray functionality
- Auto-start with Windows option
- Import/export configuration feature
- Enhanced error messages
- Hotkey conflict detection

### [1.2.0] - Planned
- Multiple configuration profiles
- Profile switching
- Mouse button mapping support
- Macro recording (simple sequences)
- Dark mode UI theme

### [2.0.0] - Long-term
- Complete UI redesign
- Plugin system for extensibility
- Scripting support (Python scripts on hotkey)
- Cloud sync for configurations
- Multi-monitor aware application launching
- Advanced scheduling (time-based profiles)

---

## Contributing

To contribute to the changelog:
1. Add entries under [Unreleased] section
2. Use appropriate categories: Added, Changed, Deprecated, Removed, Fixed, Security
3. Keep descriptions clear and concise
4. Include issue/PR references when applicable

## Changelog Categories

- **Added**: New features
- **Changed**: Changes in existing functionality
- **Deprecated**: Soon-to-be removed features
- **Removed**: Removed features
- **Fixed**: Bug fixes
- **Security**: Security fixes or enhancements
