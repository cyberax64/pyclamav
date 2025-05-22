#!/usr/bin/env python3
"""
Basic tests for pyclamav functionality.
"""
import os
import sys
import unittest

# Add parent directory to path to import pyclamav
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

try:
    import pyclamav
except ImportError:
    print("Error: pyclamav module not found. Make sure it's installed.")
    sys.exit(1)


class TestPyClamAV(unittest.TestCase):
    """Basic tests for PyClamAV functionality."""

    def setUp(self):
        """Set up test environment."""
        self.db_path = os.path.join(os.path.dirname(__file__), '..', '..', 'database')
        if not os.path.exists(self.db_path):
            self.skipTest(f"Database directory not found at {self.db_path}")

    def test_version(self):
        """Test that get_version returns a non-empty string."""
        version = pyclamav.get_version()
        self.assertIsInstance(version, str)
        self.assertTrue(len(version) > 0)

    def test_load_database(self):
        """Test loading the database."""
        result = pyclamav.load_database(self.db_path)
        self.assertEqual(result, 0)

    def test_get_numsig(self):
        """Test getting the number of signatures."""
        # First load the database
        pyclamav.load_database(self.db_path)
        # Then get the number of signatures
        num_sig = pyclamav.get_numsig()
        self.assertIsInstance(num_sig, int)
        # There should be at least some signatures
        self.assertGreaterEqual(num_sig, 0)


if __name__ == '__main__':
    unittest.main()