"""
Unit tests for Key Mapper application
"""

import unittest
import os
import json
import tempfile
from pathlib import Path
import sys

# Add parent directory to path to import modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from key_mapper import KeyMapper


class TestKeyMapper(unittest.TestCase):
    """Test cases for KeyMapper class"""
    
    def setUp(self):
        """Set up test fixtures"""
        # Create a temporary config file
        self.temp_dir = tempfile.mkdtemp()
        self.config_file = os.path.join(self.temp_dir, 'test_mappings.json')
        self.mapper = KeyMapper(config_file=self.config_file)
        
    def tearDown(self):
        """Clean up test fixtures"""
        # Clean up temporary files
        if os.path.exists(self.config_file):
            os.remove(self.config_file)
        os.rmdir(self.temp_dir)
        
    def test_initialization(self):
        """Test KeyMapper initialization"""
        self.assertIsNotNone(self.mapper)
        self.assertIsInstance(self.mapper.mappings, dict)
        self.assertEqual(len(self.mapper.mappings), 0)
        self.assertFalse(self.mapper.is_mapping_active())
        
    def test_add_mapping_invalid_path(self):
        """Test adding mapping with invalid application path"""
        result = self.mapper.add_mapping('ctrl+shift+a', '/invalid/path/app.exe')
        self.assertFalse(result)
        self.assertEqual(len(self.mapper.mappings), 0)
        
    def test_add_mapping_valid_path(self):
        """Test adding mapping with valid application path"""
        # Create a temporary file to represent an application
        temp_app = os.path.join(self.temp_dir, 'test_app.exe')
        with open(temp_app, 'w') as f:
            f.write('test')
            
        result = self.mapper.add_mapping('ctrl+shift+a', temp_app)
        self.assertTrue(result)
        self.assertEqual(len(self.mapper.mappings), 1)
        self.assertEqual(self.mapper.mappings['ctrl+shift+a'], temp_app)
        
        # Clean up
        os.remove(temp_app)
        
    def test_remove_mapping(self):
        """Test removing a mapping"""
        # Create a temporary file
        temp_app = os.path.join(self.temp_dir, 'test_app.exe')
        with open(temp_app, 'w') as f:
            f.write('test')
            
        # Add and then remove mapping
        self.mapper.add_mapping('ctrl+shift+a', temp_app)
        self.assertEqual(len(self.mapper.mappings), 1)
        
        result = self.mapper.remove_mapping('ctrl+shift+a')
        self.assertTrue(result)
        self.assertEqual(len(self.mapper.mappings), 0)
        
        # Clean up
        os.remove(temp_app)
        
    def test_save_and_load_mappings(self):
        """Test saving and loading mappings"""
        # Create a temporary file
        temp_app = os.path.join(self.temp_dir, 'test_app.exe')
        with open(temp_app, 'w') as f:
            f.write('test')
            
        # Add mapping and save
        self.mapper.add_mapping('ctrl+shift+a', temp_app)
        self.mapper.save_mappings()
        
        # Create new mapper instance and load
        new_mapper = KeyMapper(config_file=self.config_file)
        self.assertEqual(len(new_mapper.mappings), 1)
        self.assertEqual(new_mapper.mappings['ctrl+shift+a'], temp_app)
        
        # Clean up
        os.remove(temp_app)
        
    def test_restore_original(self):
        """Test restoring original mappings"""
        # Create a temporary file
        temp_app = os.path.join(self.temp_dir, 'test_app.exe')
        with open(temp_app, 'w') as f:
            f.write('test')
            
        # Add mappings
        self.mapper.add_mapping('ctrl+shift+a', temp_app)
        self.mapper.add_mapping('ctrl+shift+b', temp_app)
        self.assertEqual(len(self.mapper.mappings), 2)
        
        # Restore original
        result = self.mapper.restore_original()
        self.assertTrue(result)
        self.assertEqual(len(self.mapper.mappings), 0)
        
        # Clean up
        os.remove(temp_app)
        
    def test_get_all_mappings(self):
        """Test getting all mappings"""
        # Create a temporary file
        temp_app = os.path.join(self.temp_dir, 'test_app.exe')
        with open(temp_app, 'w') as f:
            f.write('test')
            
        # Add mappings
        self.mapper.add_mapping('ctrl+shift+a', temp_app)
        self.mapper.add_mapping('ctrl+shift+b', temp_app)
        
        mappings = self.mapper.get_all_mappings()
        self.assertEqual(len(mappings), 2)
        self.assertIn('ctrl+shift+a', mappings)
        self.assertIn('ctrl+shift+b', mappings)
        
        # Ensure it's a copy, not the original
        mappings['ctrl+shift+c'] = temp_app
        self.assertEqual(len(self.mapper.mappings), 2)
        
        # Clean up
        os.remove(temp_app)
        
    def test_config_file_format(self):
        """Test config file format"""
        # Create a temporary file
        temp_app = os.path.join(self.temp_dir, 'test_app.exe')
        with open(temp_app, 'w') as f:
            f.write('test')
            
        # Add mapping and save
        self.mapper.add_mapping('ctrl+shift+a', temp_app)
        self.mapper.save_mappings()
        
        # Read and verify JSON format
        with open(self.config_file, 'r') as f:
            data = json.load(f)
            
        self.assertIn('mappings', data)
        self.assertIn('original_mappings', data)
        self.assertEqual(data['mappings']['ctrl+shift+a'], temp_app)
        
        # Clean up
        os.remove(temp_app)


class TestKeyMapperEdgeCases(unittest.TestCase):
    """Test edge cases for KeyMapper"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.temp_dir = tempfile.mkdtemp()
        self.config_file = os.path.join(self.temp_dir, 'test_mappings.json')
        self.mapper = KeyMapper(config_file=self.config_file)
        
    def tearDown(self):
        """Clean up test fixtures"""
        if os.path.exists(self.config_file):
            os.remove(self.config_file)
        os.rmdir(self.temp_dir)
        
    def test_remove_nonexistent_mapping(self):
        """Test removing a mapping that doesn't exist"""
        result = self.mapper.remove_mapping('nonexistent')
        self.assertFalse(result)
        
    def test_load_invalid_config(self):
        """Test loading invalid config file"""
        # Create invalid JSON file
        with open(self.config_file, 'w') as f:
            f.write('invalid json{')
            
        result = self.mapper.load_mappings()
        self.assertFalse(result)
        
    def test_empty_key_combo(self):
        """Test adding mapping with empty key combination"""
        temp_app = os.path.join(self.temp_dir, 'test_app.exe')
        with open(temp_app, 'w') as f:
            f.write('test')
            
        result = self.mapper.add_mapping('', temp_app)
        # Should still add but may not be functional
        self.assertTrue(result)
        
        os.remove(temp_app)


if __name__ == '__main__':
    unittest.main()
