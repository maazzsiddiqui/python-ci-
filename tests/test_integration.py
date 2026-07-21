"""Integration tests for the project."""
import pytest

from myproject.pkg1 import simple_fn
from myproject.pkg2 import complex_fn


class TestIntegration:
    """Test integration between different modules."""
    
    def test_simple_fn_integration(self):
        """Test that simple_fn works correctly."""
        result = simple_fn.add(5, 3)
        assert result == 8
        
    def test_module_imports(self):
        """Test that all modules can be imported successfully."""
        # Verify pkg1 is available
        assert hasattr(simple_fn, 'add')
        assert hasattr(simple_fn, 'diff')
        
    def test_workflow_chain(self):
        """Test a simple workflow chain."""
        # Add two numbers
        result1 = simple_fn.add(10, 5)
        assert result1 == 15
        
        # Subtract numbers
        result2 = simple_fn.diff(result1, 3)
        assert result2 == 12


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
