"""
Key Mapper - Map keyboard keys to launch Windows applications
"""

import os
import json
import subprocess
import threading
from pathlib import Path
from typing import Dict, Optional
import keyboard
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


class KeyMapper:
    """Manages keyboard key mappings to applications"""
    
    def __init__(self, config_file: str = "key_mappings.json"):
        self.config_file = Path(config_file)
        self.mappings: Dict[str, str] = {}
        self.original_mappings: Dict[str, str] = {}
        self.active_hooks = []
        self.is_active = False
        self.lock = threading.Lock()
        
        # Load mappings if config file exists
        self.load_mappings()
        
    def load_mappings(self) -> bool:
        """Load key mappings from config file"""
        try:
            if self.config_file.exists():
                with open(self.config_file, 'r') as f:
                    data = json.load(f)
                    self.mappings = data.get('mappings', {})
                    self.original_mappings = data.get('original_mappings', {})
                logger.info(f"Loaded {len(self.mappings)} key mappings")
                return True
        except Exception as e:
            logger.error(f"Error loading mappings: {e}")
        return False
        
    def save_mappings(self) -> bool:
        """Save key mappings to config file"""
        try:
            data = {
                'mappings': self.mappings,
                'original_mappings': self.original_mappings
            }
            with open(self.config_file, 'w') as f:
                json.dump(data, f, indent=2)
            logger.info(f"Saved {len(self.mappings)} key mappings")
            return True
        except Exception as e:
            logger.error(f"Error saving mappings: {e}")
            return False
            
    def add_mapping(self, key_combo: str, app_path: str) -> bool:
        """Add a new key to application mapping"""
        try:
            if not os.path.exists(app_path):
                logger.error(f"Application path does not exist: {app_path}")
                return False
                
            # Store original mapping if this is the first time
            if key_combo not in self.original_mappings:
                self.original_mappings[key_combo] = None  # No original mapping
                
            self.mappings[key_combo] = app_path
            logger.info(f"Added mapping: {key_combo} -> {app_path}")
            return True
        except Exception as e:
            logger.error(f"Error adding mapping: {e}")
            return False
            
    def remove_mapping(self, key_combo: str) -> bool:
        """Remove a key mapping"""
        try:
            if key_combo in self.mappings:
                del self.mappings[key_combo]
                if key_combo in self.original_mappings:
                    del self.original_mappings[key_combo]
                logger.info(f"Removed mapping: {key_combo}")
                return True
        except Exception as e:
            logger.error(f"Error removing mapping: {e}")
        return False
        
    def restore_original(self) -> bool:
        """Restore all keys to their original mappings"""
        try:
            self.stop_mapping()
            self.mappings.clear()
            self.original_mappings.clear()
            self.save_mappings()
            logger.info("Restored all keys to original mappings")
            return True
        except Exception as e:
            logger.error(f"Error restoring mappings: {e}")
            return False
            
    def launch_application(self, app_path: str):
        """Launch an application"""
        try:
            logger.info(f"Launching application: {app_path}")
            
            # Handle different types of applications
            if app_path.endswith('.exe'):
                subprocess.Popen([app_path], shell=True)
            elif app_path.endswith('.lnk'):
                os.startfile(app_path)
            else:
                os.startfile(app_path)
                
        except Exception as e:
            logger.error(f"Error launching application {app_path}: {e}")
            
    def _create_hotkey_handler(self, app_path: str):
        """Create a hotkey handler function"""
        def handler():
            self.launch_application(app_path)
        return handler
        
    def start_mapping(self) -> bool:
        """Start listening for key mappings"""
        try:
            with self.lock:
                if self.is_active:
                    logger.warning("Key mapping is already active")
                    return False
                    
                # Clear existing hooks
                self.stop_mapping()
                
                # Register all hotkeys
                for key_combo, app_path in self.mappings.items():
                    try:
                        handler = self._create_hotkey_handler(app_path)
                        keyboard.add_hotkey(key_combo, handler)
                        self.active_hooks.append(key_combo)
                        logger.info(f"Registered hotkey: {key_combo}")
                    except Exception as e:
                        logger.error(f"Error registering hotkey {key_combo}: {e}")
                        
                self.is_active = True
                logger.info("Key mapping started")
                return True
                
        except Exception as e:
            logger.error(f"Error starting key mapping: {e}")
            return False
            
    def stop_mapping(self) -> bool:
        """Stop listening for key mappings"""
        try:
            with self.lock:
                # Unregister all hotkeys
                for key_combo in self.active_hooks:
                    try:
                        keyboard.remove_hotkey(key_combo)
                    except Exception as e:
                        logger.warning(f"Error removing hotkey {key_combo}: {e}")
                        
                self.active_hooks.clear()
                self.is_active = False
                logger.info("Key mapping stopped")
                return True
                
        except Exception as e:
            logger.error(f"Error stopping key mapping: {e}")
            return False
            
    def get_all_mappings(self) -> Dict[str, str]:
        """Get all current key mappings"""
        return self.mappings.copy()
        
    def is_mapping_active(self) -> bool:
        """Check if key mapping is currently active"""
        return self.is_active
