# Project Structure

## Overview
Key Mapper is a Python-based Windows application for mapping keyboard shortcuts to applications.

## Directory Structure

```
map_keys/
│
├── Core Application Files
│   ├── key_mapper.py          # Core keyboard mapping functionality
│   ├── gui.py                 # Tkinter-based GUI
│   └── build.py               # Build script for creating executable
│
├── Configuration & Dependencies
│   ├── requirements.txt        # Python package dependencies
│   ├── .gitignore             # Git ignore rules
│   └── key_mappings.json      # User configuration (generated at runtime)
│
├── Build & Run Scripts (Windows)
│   ├── setup.bat              # Initial setup script
│   └── run.bat                # Quick run script
│
├── Tests
│   ├── tests/
│   │   ├── __init__.py
│   │   └── test_key_mapper.py # Unit tests
│
├── CI/CD
│   └── .github/
│       └── workflows/
│           └── build.yml      # GitHub Actions workflow
│
├── Documentation
│   ├── README.md              # Main documentation
│   ├── CHANGE_LOG.md          # Version history and changes
│   ├── CONTRIBUTING.md        # Contribution guidelines
│   ├── QUICK_START.md         # Quick start guide
│   ├── PROJECT_STRUCTURE.md   # This file
│   └── LICENSE                # License information
│
└── Generated Directories (not in git)
    ├── venv/                  # Virtual environment
    ├── build/                 # PyInstaller build artifacts
    ├── dist/                  # Built executable
    └── distribution/          # Distribution package
```

## File Descriptions

### Core Application Files

#### `key_mapper.py`
- **Purpose**: Core business logic for keyboard mapping
- **Key Classes**: `KeyMapper`
- **Responsibilities**:
  - Managing key-to-application mappings
  - Registering/unregistering keyboard hooks
  - Launching applications
  - Saving/loading configuration
  - Restoring original mappings

#### `gui.py`
- **Purpose**: Graphical user interface
- **Key Classes**: `KeyMapperGUI`
- **Responsibilities**:
  - User interaction
  - Displaying mappings
  - Adding/removing mappings
  - Starting/stopping mapping service
  - Configuration management UI

#### `build.py`
- **Purpose**: Build automation
- **Responsibilities**:
  - Cleaning previous builds
  - Running PyInstaller
  - Creating distribution package
  - Generating sample configuration

### Configuration Files

#### `requirements.txt`
Dependencies:
- `keyboard==0.13.5` - Keyboard hook library
- `pyinstaller==6.10.0` - Executable creator

#### `key_mappings.json` (runtime-generated)
Structure:
```json
{
  "mappings": {
    "key_combo": "app_path"
  },
  "original_mappings": {}
}
```

### Build Scripts

#### `setup.bat`
- Creates virtual environment
- Installs dependencies
- Prepares development environment

#### `run.bat`
- Activates virtual environment
- Runs the application
- Handles errors gracefully

### Tests

#### `tests/test_key_mapper.py`
- Unit tests for KeyMapper class
- Tests for configuration management
- Edge case testing
- Mock-based testing for GUI-less operation

### CI/CD

#### `.github/workflows/build.yml`
GitHub Actions workflow:
- Triggers on push/PR to main branches
- Builds Windows executable
- Runs tests
- Creates releases on tags
- Uploads artifacts

### Documentation

#### `README.md`
- Comprehensive project documentation
- Installation instructions
- Usage guide
- Troubleshooting
- Feature list

#### `CHANGE_LOG.md`
- Version history
- Feature additions
- Bug fixes
- Breaking changes

#### `CONTRIBUTING.md`
- Contribution guidelines
- Development setup
- Code style guide
- Pull request process

#### `QUICK_START.md`
- Quick setup guide
- Common examples
- Troubleshooting tips
- Key combination reference

## Architecture

### Component Diagram
```
┌─────────────────┐
│     GUI (gui.py)│
│  (Tkinter)      │
└────────┬────────┘
         │
         │ uses
         ▼
┌─────────────────┐
│   KeyMapper     │
│ (key_mapper.py) │
└────────┬────────┘
         │
         │ uses
         ▼
┌─────────────────┐
│  keyboard lib   │
│  (system hooks) │
└─────────────────┘
```

### Data Flow
```
User Input (GUI)
    ↓
KeyMapper.add_mapping()
    ↓
Save to key_mappings.json
    ↓
KeyMapper.start_mapping()
    ↓
Register hotkeys with keyboard lib
    ↓
User presses hotkey
    ↓
Callback launches application
```

## Build Process

### Development Build
```bash
python gui.py
```

### Production Build
```bash
python build.py
```

Steps:
1. Clean previous builds
2. Run PyInstaller with options:
   - `--onefile`: Single executable
   - `--windowed`: No console window
   - `--name=KeyMapper`: Executable name
3. Create distribution directory
4. Copy executable and documentation
5. Generate sample configuration

### CI/CD Build
Automated via GitHub Actions:
1. Checkout code
2. Setup Python 3.11
3. Install dependencies
4. Run build script
5. Upload artifacts
6. Create release (on tags)

## Configuration

### User Configuration
- **File**: `key_mappings.json`
- **Location**: Same directory as executable/script
- **Format**: JSON
- **Editable**: Yes (when app not running)

### Build Configuration
- **Tool**: PyInstaller
- **Config**: Generated `.spec` file
- **Options**: Defined in `build.py`

## Dependencies

### Runtime
- Python 3.8+
- keyboard library
- tkinter (included with Python)

### Development
- pytest (testing)
- pyinstaller (building)

### System
- Windows OS
- Administrator privileges (for keyboard hooks)

## Security Considerations

1. **Keyboard Hooks**: Requires admin privileges
2. **Application Launch**: Uses system calls
3. **Configuration**: Plain text JSON (no encryption)
4. **No Network**: Fully offline application

## Performance

- **Memory**: ~50-100 MB (when running)
- **CPU**: Minimal (event-driven)
- **Startup**: < 2 seconds
- **Hotkey Response**: < 100ms

## Future Enhancements

See CHANGE_LOG.md for planned features.

## Support

For issues or questions, see README.md.
