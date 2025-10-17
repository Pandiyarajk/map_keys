# Key Mapper

A Python-based Windows application that allows you to map keyboard key combinations to launch applications. Features include a user-friendly GUI, persistent configuration storage, and the ability to restore original mappings on demand.

## Features

- 🎯 **Map keyboard shortcuts to applications**: Create custom hotkeys to launch any Windows application
- 💾 **Persistent storage**: Mappings are saved and restored between sessions
- 🔄 **Restore original**: Remove all custom mappings and return to default
- 🖥️ **User-friendly GUI**: Easy-to-use graphical interface built with Tkinter
- ⚡ **Real-time activation**: Enable or disable mappings without restarting
- 📝 **Visual feedback**: See all your mappings in an organized list

## Requirements

- Windows OS (7/8/10/11)
- Python 3.8+ (for running from source)
- Administrator privileges (required for keyboard hook functionality)

## Installation

### Option 1: Download Pre-built Executable (Recommended)

1. Go to the [Releases](https://github.com/yourusername/map_keys/releases) page
2. Download the latest `KeyMapper.exe`
3. Run the executable (you may need to run as administrator)

### Option 2: Run from Source

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/map_keys.git
   cd map_keys
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   python gui.py
   ```

## Usage

### Adding a Key Mapping

1. **Enter Key Combination**: Type the desired key combination (e.g., `ctrl+shift+a`, `alt+f1`)
   - Use `+` to combine keys
   - Common modifiers: `ctrl`, `shift`, `alt`, `win`
   - Function keys: `f1`, `f2`, etc.

2. **Select Application**: 
   - Click "Browse..." to select an application
   - Or manually enter the full path to the executable

3. **Add Mapping**: Click "Add Mapping" to save the configuration

### Starting/Stopping Key Mapping

- Click **"Start Mapping"** to activate all configured hotkeys
- Click **"Stop Mapping"** to deactivate hotkeys
- The status indicator shows whether mapping is active (green) or stopped (red)

### Managing Mappings

- **Delete**: Select a mapping from the list and click "Delete Selected"
- **Restore Original**: Click "Restore Original" to remove all custom mappings
- **Refresh**: Click "Refresh" to reload the mappings list

### Example Key Combinations

- `ctrl+shift+n` - Launch Notepad
- `ctrl+shift+c` - Launch Calculator
- `alt+f1` - Launch Chrome
- `win+e` - Launch File Explorer (Windows default)
- `ctrl+alt+t` - Launch Terminal

## Configuration File

Mappings are stored in `key_mappings.json` in the application directory:

```json
{
  "mappings": {
    "ctrl+shift+n": "C:\\Windows\\System32\\notepad.exe",
    "ctrl+shift+c": "C:\\Windows\\System32\\calc.exe"
  },
  "original_mappings": {}
}
```

You can manually edit this file if needed (when the application is not running).

## Building from Source

To create your own executable:

```bash
# Install build dependencies
pip install -r requirements.txt

# Run the build script
python build.py
```

The executable will be created in the `distribution/` directory.

## GitHub Actions Workflow

This project includes a GitHub Actions workflow that:
- Automatically builds the Windows executable on push/PR
- Runs tests (if available)
- Creates releases when tags are pushed
- Uploads build artifacts

To trigger a release:
```bash
git tag -a v1.0.0 -m "Release version 1.0.0"
git push origin v1.0.0
```

## Troubleshooting

### "Failed to start key mapping"
- Make sure you're running the application with administrator privileges
- Check that no other hotkey applications are conflicting

### "Application path does not exist"
- Verify the path to your application is correct
- Use the "Browse..." button to ensure the correct path

### Hotkeys not working
- Ensure mapping is started (status should be green)
- Check if another application is using the same hotkey
- Try a different key combination

### Permission errors
- Run the application as administrator
- On Windows 11, check if the app has necessary permissions

## Security Notes

- The application requires administrator privileges to register global hotkeys
- Keyboard hooks can potentially capture sensitive input - use responsibly
- Only map keys to trusted applications

## Architecture

The application consists of three main components:

1. **key_mapper.py**: Core functionality for managing key mappings and launching applications
2. **gui.py**: Tkinter-based graphical user interface
3. **build.py**: Build script for creating standalone executable

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Built with [keyboard](https://github.com/boppreh/keyboard) library for keyboard hook functionality
- GUI created with Python's built-in Tkinter library
- Packaged with [PyInstaller](https://www.pyinstaller.org/)

## Support

If you encounter any issues or have questions:
- Open an issue on GitHub
- Check existing issues for solutions
- Review the troubleshooting section above

## Roadmap

Future enhancements:
- [ ] Support for mouse button mappings
- [ ] Multiple profiles for different workflows
- [ ] Import/export configuration
- [ ] Hotkey recording feature
- [ ] System tray icon and minimize to tray
- [ ] Auto-start with Windows option
- [ ] Dark mode theme

---

**Note**: This application is designed for Windows only due to OS-specific keyboard hook requirements.
