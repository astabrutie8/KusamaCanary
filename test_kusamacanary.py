# test_kusamacanary.py
"""
Tests for KusamaCanary module.
"""

import unittest
from kusamacanary import KusamaCanary

class TestKusamaCanary(unittest.TestCase):
    """Test cases for KusamaCanary class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = KusamaCanary()
        self.assertIsInstance(instance, KusamaCanary)
        
    def test_run_method(self):
        """Test the run method."""
        instance = KusamaCanary()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
