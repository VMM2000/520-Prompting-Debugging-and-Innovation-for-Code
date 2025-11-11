import pytest
import importlib.util
from pathlib import Path

# 1. Import the function to be tested
# --- ASSUMPTION ---
# I am assuming the function in 'new_gen_code.py' is named 'gpa_to_letter'
# If it has a different name, please change it here.
from generated_code_new.problem_1 import numerical_letter_grade

# 2. The Test Function
def test_gpa_converter():
    """
    Tests the GPA to Letter Grade conversion.
    Uses 'pytest.assume()' to run all checks without stopping.
    """
    
    if numerical_letter_grade is None:
        pytest.fail("Could not import 'gpa_to_letter' from new_gen_code.py. Make sure the file and function name are correct.")

    try:
        # Check some simple cases
        pytest.assume(numerical_letter_grade([4.0, 3, 1.7, 2, 3.5]) == ['A+', 'B', 'C-', 'C', 'A-'])
        pytest.assume(numerical_letter_grade([1.2]) == ['D+'])
        pytest.assume(numerical_letter_grade([0.5]) == ['D-'])
        pytest.assume(numerical_letter_grade([0.0]) == ['E'])
        pytest.assume(numerical_letter_grade([1, 0.3, 1.5, 2.8, 3.3]) == ['D', 'D-', 'C-', 'B', 'B+'])
        pytest.assume(numerical_letter_grade([0, 0.7]) == ['E', 'D-'])

        # Check some edge cases that are easy to work out by hand.
        pytest.assume(True)

        pytest.assume(numerical_letter_grade([3.8, 2.4, 2.1, -1.0]) == ['A', 'B-', 'C+', 'E'])


    except Exception as e:
        # Fails the test if the generated code is so broken
        # it causes a TypeError, NameError, IndexError, etc.
        pytest.fail(f"Test crashed with an unhandled exception: {type(e).__name__}: {e}")