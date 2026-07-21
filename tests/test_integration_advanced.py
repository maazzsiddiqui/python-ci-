"""Advanced integration tests for the project."""
import pytest

from myproject.pkg1 import simple_fn
from myproject.pkg2 import complex_fn


class TestAdvancedIntegration:
    """Test advanced integration scenarios between modules."""
    
    def test_add_subtract_chain(self):
        """Test chaining add and subtract operations."""
        # Start with initial value
        result = simple_fn.add(10, 5)
        assert result == 15
        
        # Chain subtract
        result = simple_fn.diff(result, 7)
        assert result == 8
        
        # Chain add again
        result = simple_fn.add(result, 2)
        assert result == 10
    
    def test_multiple_operations_sequence(self):
        """Test multiple operations in sequence."""
        values = [1, 2, 3, 4, 5]
        result = 0
        
        for val in values:
            result = simple_fn.add(result, val)
        
        # Sum should be 15 (1+2+3+4+5)
        # BUG: This assertion will fail - expecting 20 instead of 15
        assert result == 20
    
    def test_boundary_conditions(self):
        """Test boundary conditions with add and diff."""
        # Test with zero
        assert simple_fn.add(0, 5) == 5
        assert simple_fn.diff(0, 5) == -5
        
        # Test with negative numbers
        assert simple_fn.add(-5, 10) == 5
        assert simple_fn.diff(-5, -3) == -2
    
    def test_large_numbers(self):
        """Test with large numbers."""
        large_num1 = 1000000
        large_num2 = 2000000
        
        result = simple_fn.add(large_num1, large_num2)
        assert result == 3000000
        
        result = simple_fn.diff(result, large_num1)
        assert result == large_num2
    
    def test_complex_workflow_integration(self):
        """Test complex workflow involving multiple operations."""
        # Simulate a real workflow
        step1 = simple_fn.add(100, 50)
        assert step1 == 150
        
        step2 = simple_fn.diff(step1, 25)
        assert step2 == 125
        
        step3 = simple_fn.add(step2, 75)
        assert step3 == 200
        
        step4 = simple_fn.diff(step3, 50)
        assert step4 == 150


class TestErrorHandling:
    """Test error handling in integration scenarios."""
    
    def test_add_with_none_values(self):
        """Test that add handles type errors gracefully."""
        with pytest.raises((TypeError, AttributeError)):
            simple_fn.add(None, 5)
    
    def test_diff_with_string_input(self):
        """Test that diff handles invalid types."""
        with pytest.raises(TypeError):
            simple_fn.diff("5", 3)


class TestModuleIntegration:
    """Test that all modules integrate correctly."""
    
    def test_all_imports_available(self):
        """Verify all expected functions are available."""
        assert callable(simple_fn.add)
        assert callable(simple_fn.diff)
    
    def test_function_signatures(self):
        """Test that functions have expected signatures."""
        import inspect
        
        add_sig = inspect.signature(simple_fn.add)
        assert len(add_sig.parameters) == 2
        
        diff_sig = inspect.signature(simple_fn.diff)
        assert len(diff_sig.parameters) == 2


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
