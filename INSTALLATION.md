# Installation Guide

Complete installation instructions for Key Mapper.

## Table of Contents
- [System Requirements](#system-requirements)
- [Installation Methods](#installation-methods)
- [Post-Installation](#post-installation)
- [Troubleshooting](#troubleshooting)

## System Requirements

### Minimum Requirements
- **OS**: Windows 7 or later (Windows 10/11 recommended)
- **RAM**: 512 MB
- **Disk Space**: 50 MB
- **Privileges**: Administrator access (for keyboard hooks)

### For Running from Source
- **Python**: 3.8 or higher
- **pip**: Latest version
- **Virtual Environment**: Recommended

## Installation Methods

### Method 1: Pre-built Executable (Recommended)

#### Step 1: Download
1. Visit [Releases](https://github.com/yourusername/map_keys/releases)
2. Download the latest `KeyMapper.exe`
3. Optionally download sample configuration

#### Step 2: Install
1. Create a folder (e.g., `C:\Program Files\KeyMapper\`)
2. Copy `KeyMapper.exe` to the folder
3. Create a desktop shortcut (optional)

#### Step 3: Run
1. Right-click `KeyMapper.exe`
2. Select "Run as administrator"
3. Application will launch

**Advantages**:
- No Python installation needed
- Single executable
- Easy to use
- Fast startup

**Disadvantages**:
- Larger file size (~20-30 MB)
- Cannot modify source code

### Method 2: From Source (For Developers)

#### Step 1: Install Python
1. Download Python 3.8+ from [python.org](https://www.python.org/downloads/)
2. During installation:
   - ✅ Check "Add Python to PATH"
   - ✅ Check "Install pip"
3. Verify installation:
   ```bash
   python --version
   pip --version
   ```

#### Step 2: Clone Repository
```bash
# Using Git
git clone https://github.com/yourusername/map_keys.git
cd map_keys

# Or download ZIP
# Extract to desired location
```

#### Step 3: Setup Environment

**Option A: Automatic Setup (Windows)**
```bash
setup.bat
```

**Option B: Manual Setup**
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# Upgrade pip
python -m pip install --upgrade pip

# Install dependencies
pip install -r requirements.txt
```

#### Step 4: Run Application
```bash
# Option A: Using run script
run.bat

# Option B: Manual
venv\Scripts\activate
python gui.py
```

**Advantages**:
- Full source code access
- Easy to modify and extend
- Smaller download size
- Can contribute changes

**Disadvantages**:
- Requires Python installation
- More setup steps
- Larger disk footprint (with venv)

### Method 3: Build Your Own Executable

#### Prerequisites
- Python 3.8+
- All dependencies installed
- PyInstaller

#### Steps
```bash
# 1. Setup environment
setup.bat

# 2. Activate virtual environment
venv\Scripts\activate

# 3. Run build script
python build.py

# 4. Find executable
cd distribution
# KeyMapper.exe is ready to use
```

#### Build Output
```
distribution/
├── KeyMapper.exe              # Your executable
├── README.md                  # Documentation
├── CHANGE_LOG.md             # Version history
└── key_mappings.json.sample  # Sample config
```

## Post-Installation

### First Run

1. **Launch application**
   - Run as administrator (important!)
   - GUI window should appear

2. **Add your first mapping**
   - Key combo: `ctrl+shift+n`
   - Application: Browse to `notepad.exe`
   - Click "Add Mapping"

3. **Start mapping**
   - Click "Start Mapping"
   - Status should turn green

4. **Test**
   - Press `Ctrl+Shift+N`
   - Notepad should launch

### Configuration

#### Location
- **Source install**: Same directory as `gui.py`
- **Executable**: Same directory as `KeyMapper.exe`
- **File name**: `key_mappings.json`

#### Manual Configuration
You can manually edit `key_mappings.json`:
```json
{
  "mappings": {
    "ctrl+shift+n": "C:\\Windows\\System32\\notepad.exe",
    "ctrl+shift+c": "C:\\Windows\\System32\\calc.exe"
  },
  "original_mappings": {}
}
```

**Note**: Edit only when application is not running.

### Creating Desktop Shortcut

#### For Executable
1. Right-click `KeyMapper.exe`
2. Select "Create shortcut"
3. Move shortcut to desktop
4. Right-click shortcut → Properties
5. Check "Run as administrator"
6. Click "Advanced"
7. Check "Run as administrator"
8. Apply and OK

#### For Source Installation
1. Create new shortcut on desktop
2. Target: `C:\path\to\map_keys\run.bat`
3. Start in: `C:\path\to\map_keys`
4. Set to run as administrator

## Verification

### Checklist
- [ ] Application launches without errors
- [ ] Can add new mapping
- [ ] Can browse for applications
- [ ] Mappings are saved (check JSON file)
- [ ] Can start/stop mapping
- [ ] Hotkeys work when mapping is active
- [ ] Can delete mappings
- [ ] Restore original works

### Test Commands
```bash
# Verify Python installation
python --version

# Verify pip
pip --version

# Check installed packages
pip list | findstr keyboard

# Test import
python -c "import keyboard; print('OK')"
```

## Troubleshooting

### Installation Issues

#### "Python is not recognized"
**Problem**: Python not in PATH
**Solution**: 
1. Reinstall Python
2. Check "Add Python to PATH"
3. Or manually add to PATH

#### "pip is not recognized"
**Problem**: pip not installed
**Solution**:
```bash
python -m ensurepip --upgrade
```

#### "Permission denied"
**Problem**: Insufficient privileges
**Solution**:
- Run terminal/cmd as administrator
- Check folder permissions

#### "Virtual environment activation fails"
**Problem**: Execution policy on Windows
**Solution**:
```powershell
# In PowerShell as Administrator
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### Runtime Issues

#### "Failed to start mapping"
**Solution**: Run as administrator

#### "Import error: keyboard"
**Solution**:
```bash
pip install keyboard
```

#### Configuration file errors
**Solution**:
1. Delete `key_mappings.json`
2. Restart application
3. Recreate mappings

### Build Issues

#### PyInstaller not found
**Solution**:
```bash
pip install pyinstaller
```

#### Build fails
**Solution**:
1. Clean previous builds
2. Update PyInstaller: `pip install --upgrade pyinstaller`
3. Check for antivirus interference

## Updating

### Executable Version
1. Download new version
2. Replace old `KeyMapper.exe`
3. Keep `key_mappings.json` (your config)

### Source Version
```bash
# Pull latest changes
git pull origin main

# Update dependencies
venv\Scripts\activate
pip install -r requirements.txt --upgrade
```

## Uninstallation

### Executable Version
1. Close application if running
2. Delete folder containing `KeyMapper.exe`
3. Delete desktop shortcut (if created)
4. Delete `key_mappings.json` (if you don't want to keep config)

### Source Version
1. Deactivate virtual environment: `deactivate`
2. Delete entire project folder
3. No registry changes made

## Advanced Setup

### Auto-start with Windows
1. Press `Win+R`
2. Type `shell:startup`
3. Create shortcut to `KeyMapper.exe` in this folder
4. Set shortcut to run as administrator

### Multiple Configurations
```bash
# Use different config files
python gui.py --config work_mappings.json
python gui.py --config home_mappings.json
```

## Getting Help

If you encounter issues:
1. Check this guide thoroughly
2. Review [README.md](README.md)
3. Check [GitHub Issues](https://github.com/yourusername/map_keys/issues)
4. Create new issue with:
   - Operating system version
   - Python version (if applicable)
   - Error messages
   - Steps to reproduce

## Next Steps

After successful installation:
1. Read [QUICK_START.md](QUICK_START.md)
2. Review [README.md](README.md) for features
3. Check [CONTRIBUTING.md](CONTRIBUTING.md) if you want to contribute

---

**Installation Complete!** 🎉

You're ready to start mapping keys to applications!
