# Contributing to Key Mapper

Thank you for your interest in contributing to Key Mapper! This document provides guidelines and instructions for contributing.

## Code of Conduct

- Be respectful and inclusive
- Provide constructive feedback
- Focus on what's best for the community
- Show empathy towards others

## How to Contribute

### Reporting Bugs

If you find a bug, please create an issue with:
- Clear title and description
- Steps to reproduce
- Expected vs actual behavior
- System information (Windows version, Python version)
- Screenshots if applicable

### Suggesting Features

Feature requests are welcome! Please:
- Check if the feature has already been requested
- Provide a clear use case
- Explain why this would be useful to most users
- Consider implementation complexity

### Pull Requests

1. **Fork the repository**
   ```bash
   git clone https://github.com/yourusername/map_keys.git
   cd map_keys
   ```

2. **Create a feature branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

3. **Set up development environment**
   ```bash
   python -m venv venv
   venv\Scripts\activate  # On Windows
   pip install -r requirements.txt
   pip install pytest pytest-cov  # For testing
   ```

4. **Make your changes**
   - Write clean, readable code
   - Follow existing code style
   - Add comments for complex logic
   - Update documentation as needed

5. **Test your changes**
   ```bash
   # Run tests
   python -m pytest tests/ -v
   
   # Test the GUI
   python gui.py
   
   # Test building
   python build.py
   ```

6. **Commit your changes**
   ```bash
   git add .
   git commit -m "Add feature: your feature description"
   ```

7. **Push to your fork**
   ```bash
   git push origin feature/your-feature-name
   ```

8. **Create a Pull Request**
   - Go to the original repository
   - Click "New Pull Request"
   - Select your feature branch
   - Fill in the PR template

## Development Guidelines

### Code Style

- Follow PEP 8 style guide for Python
- Use meaningful variable and function names
- Keep functions focused and concise
- Add docstrings to classes and functions

Example:
```python
def add_mapping(self, key_combo: str, app_path: str) -> bool:
    """
    Add a new key to application mapping
    
    Args:
        key_combo: The keyboard combination (e.g., 'ctrl+shift+a')
        app_path: Full path to the application executable
        
    Returns:
        True if mapping was added successfully, False otherwise
    """
    # Implementation...
```

### Testing

- Write unit tests for new features
- Ensure existing tests still pass
- Test on Windows (multiple versions if possible)
- Test edge cases and error conditions

### Documentation

- Update README.md if adding user-facing features
- Update CHANGE_LOG.md with your changes
- Add inline comments for complex code
- Update docstrings as needed

### Commit Messages

Write clear commit messages:
- Use present tense ("Add feature" not "Added feature")
- Keep first line under 50 characters
- Provide detailed description if needed

Good examples:
```
Add mouse button mapping support

Implement hotkey recording feature
- Add recording button to GUI
- Capture key presses during recording
- Update configuration system
```

## Project Structure

```
map_keys/
├── key_mapper.py      # Core mapping functionality
├── gui.py             # Tkinter GUI
├── build.py           # Build script for executable
├── requirements.txt   # Python dependencies
├── setup.bat          # Windows setup script
├── run.bat            # Windows run script
├── tests/             # Unit tests
│   ├── __init__.py
│   └── test_key_mapper.py
├── .github/
│   └── workflows/
│       └── build.yml  # CI/CD workflow
├── README.md
├── CHANGE_LOG.md
├── CONTRIBUTING.md
└── LICENSE
```

## Feature Development Workflow

1. **Plan**: Open an issue to discuss the feature
2. **Design**: Consider architecture and user experience
3. **Implement**: Write code following guidelines
4. **Test**: Thoroughly test your changes
5. **Document**: Update all relevant documentation
6. **Review**: Submit PR and address feedback

## Areas for Contribution

### High Priority
- Bug fixes
- Performance improvements
- Documentation improvements
- Test coverage expansion

### Features
- System tray icon
- Dark mode theme
- Profile management
- Mouse button support
- Hotkey recording
- Import/export configurations

### Nice to Have
- Better error messages
- Improved UI/UX
- Additional platform support (if feasible)
- Localization/translations

## Testing Guidelines

### Unit Tests
```bash
# Run all tests
python -m pytest tests/ -v

# Run with coverage
python -m pytest tests/ --cov=. --cov-report=html

# Run specific test
python -m pytest tests/test_key_mapper.py::TestKeyMapper::test_add_mapping -v
```

### Manual Testing Checklist
- [ ] Application launches without errors
- [ ] Can add new mapping
- [ ] Can delete mapping
- [ ] Can start/stop mapping
- [ ] Hotkeys work as expected
- [ ] Configuration persists
- [ ] Restore original works
- [ ] GUI is responsive
- [ ] Error messages are clear

## Building and Distribution

```bash
# Build executable
python build.py

# Test executable
cd distribution
./KeyMapper.exe
```

## Release Process

1. Update version in CHANGE_LOG.md
2. Ensure all tests pass
3. Update documentation
4. Create git tag: `git tag -a v1.x.x -m "Version 1.x.x"`
5. Push tag: `git push origin v1.x.x`
6. GitHub Actions will automatically build and create release

## Getting Help

- Open an issue for questions
- Check existing issues and PRs
- Review documentation thoroughly
- Contact maintainers if needed

## License

By contributing, you agree that your contributions will be licensed under the same license as the project (see LICENSE file).

## Recognition

Contributors will be recognized in:
- GitHub contributors page
- Release notes
- Future acknowledgments section

Thank you for contributing to Key Mapper! 🎉
