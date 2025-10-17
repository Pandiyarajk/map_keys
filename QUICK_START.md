# Quick Start Guide

Get up and running with Key Mapper in 5 minutes!

## Option 1: Use Pre-built Executable (Easiest)

1. **Download** the latest `KeyMapper.exe` from [Releases](https://github.com/yourusername/map_keys/releases)
2. **Run** `KeyMapper.exe` (may need administrator privileges)
3. **Add a mapping**:
   - Enter key combo: `ctrl+shift+n`
   - Browse to: `C:\Windows\System32\notepad.exe`
   - Click "Add Mapping"
4. **Start mapping** by clicking "Start Mapping"
5. **Test** by pressing `Ctrl+Shift+N` - Notepad should launch!

## Option 2: Run from Source

### Step 1: Install Python
Download Python 3.8+ from [python.org](https://www.python.org/downloads/)

### Step 2: Setup
```bash
# Clone the repository
git clone https://github.com/yourusername/map_keys.git
cd map_keys

# Run setup script (Windows)
setup.bat
```

### Step 3: Run
```bash
# Option A: Use run script
run.bat

# Option B: Manual run
venv\Scripts\activate
python gui.py
```

## Your First Mappings

### Example 1: Launch Notepad
- **Key**: `ctrl+shift+n`
- **App**: `C:\Windows\System32\notepad.exe`

### Example 2: Launch Calculator
- **Key**: `ctrl+shift+c`
- **App**: `C:\Windows\System32\calc.exe`

### Example 3: Launch Chrome
- **Key**: `alt+c`
- **App**: `C:\Program Files\Google\Chrome\Application\chrome.exe`

## Key Combination Tips

### Format
- Use `+` to combine keys
- Lowercase letters (e.g., `ctrl+a` not `ctrl+A`)

### Examples
```
ctrl+shift+a
alt+f1
win+e
ctrl+alt+del
shift+f12
```

### Modifiers
- `ctrl` - Control key
- `shift` - Shift key
- `alt` - Alt key
- `win` - Windows key

### Special Keys
- `f1` through `f12` - Function keys
- `a-z` - Letter keys
- `0-9` - Number keys
- `space`, `enter`, `tab`, `esc`
- `up`, `down`, `left`, `right`
- `home`, `end`, `pageup`, `pagedown`

## Common Issues

### "Failed to start mapping"
**Solution**: Run as administrator
- Right-click `KeyMapper.exe`
- Select "Run as administrator"

### Hotkey not working
**Solutions**:
1. Check if mapping is started (status should be green)
2. Try a different key combination
3. Close conflicting applications

### Can't find application
**Solution**: Use the "Browse..." button to ensure correct path

## Building Your Own Executable

```bash
# Activate virtual environment
venv\Scripts\activate

# Build
python build.py

# Find executable in distribution/ folder
```

## Next Steps

1. **Explore**: Try different key combinations
2. **Customize**: Map your frequently used applications
3. **Experiment**: Test different workflows
4. **Share**: Create your own configuration and share it!

## Tips & Tricks

### Productivity Boost
Map your most-used apps:
- Email client: `ctrl+shift+e`
- Browser: `ctrl+shift+b`
- Terminal: `ctrl+alt+t`
- File manager: `win+e`

### Avoid Conflicts
- Don't override system hotkeys
- Avoid common application shortcuts
- Use uncommon combinations for safety

### Backup Your Config
Your mappings are in `key_mappings.json`:
```bash
# Backup
copy key_mappings.json key_mappings.backup.json

# Restore
copy key_mappings.backup.json key_mappings.json
```

## Get Help

- 📖 Read the full [README](README.md)
- 🐛 Report issues on [GitHub](https://github.com/yourusername/map_keys/issues)
- 💬 Check existing issues for solutions

## What's Next?

Check out [CONTRIBUTING.md](CONTRIBUTING.md) to help improve Key Mapper!

---

**Happy mapping! 🎯**
