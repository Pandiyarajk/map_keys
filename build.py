"""
Build script for Key Mapper application
Creates a Windows executable using PyInstaller
"""

import os
import sys
import subprocess
import shutil
from pathlib import Path


def clean_build_dirs():
    """Clean previous build directories"""
    dirs_to_clean = ['build', 'dist']
    for dir_name in dirs_to_clean:
        if os.path.exists(dir_name):
            print(f"Cleaning {dir_name}...")
            shutil.rmtree(dir_name)
    
    # Clean spec file
    spec_file = 'gui.spec'
    if os.path.exists(spec_file):
        os.remove(spec_file)
        print(f"Removed {spec_file}")


def build_executable():
    """Build the executable using PyInstaller"""
    print("Building Key Mapper executable...")
    
    # PyInstaller command
    cmd = [
        'pyinstaller',
        '--name=KeyMapper',
        '--onefile',
        '--windowed',
        '--icon=NONE',
        '--add-data=key_mappings.json;.' if os.path.exists('key_mappings.json') else '',
        'gui.py'
    ]
    
    # Remove empty strings from command
    cmd = [arg for arg in cmd if arg]
    
    try:
        result = subprocess.run(cmd, check=True, capture_output=True, text=True)
        print(result.stdout)
        print("\n✓ Build successful!")
        print(f"Executable created: dist/KeyMapper.exe")
        return True
    except subprocess.CalledProcessError as e:
        print(f"\n✗ Build failed!")
        print(e.stderr)
        return False


def create_distribution():
    """Create distribution package"""
    if not os.path.exists('dist/KeyMapper.exe'):
        print("Error: Executable not found")
        return False
        
    # Create distribution directory
    dist_dir = Path('distribution')
    dist_dir.mkdir(exist_ok=True)
    
    # Copy executable
    shutil.copy('dist/KeyMapper.exe', dist_dir / 'KeyMapper.exe')
    
    # Copy README if exists
    if os.path.exists('README.md'):
        shutil.copy('README.md', dist_dir / 'README.md')
    
    # Create a sample config
    sample_config = dist_dir / 'key_mappings.json.sample'
    with open(sample_config, 'w', encoding='utf-8') as f:
        f.write('''{
  "mappings": {
    "ctrl+shift+n": "C:\\\\Windows\\\\System32\\\\notepad.exe",
    "ctrl+shift+c": "C:\\\\Windows\\\\System32\\\\calc.exe"
  },
  "original_mappings": {}
}
''')
    
    print(f"\n✓ Distribution package created in '{dist_dir}' directory")
    return True


def main():
    """Main build process"""
    print("=" * 60)
    print("Key Mapper - Build Script")
    print("=" * 60)
    
    # Clean previous builds
    clean_build_dirs()
    
    # Build executable
    if not build_executable():
        sys.exit(1)
    
    # Create distribution package
    if not create_distribution():
        sys.exit(1)
    
    print("\n" + "=" * 60)
    print("Build process completed successfully!")
    print("=" * 60)


if __name__ == "__main__":
    main()
