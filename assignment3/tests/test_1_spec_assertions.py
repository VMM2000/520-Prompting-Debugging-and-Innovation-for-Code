import pytest
import importlib.util
from pathlib import Path

# 1. Import the function to be tested
# --- ASSUMPTION ---
# I am assuming the function in 'new_gen_code.py' is named 'gpa_to_letter'
# If it has a different name, please change it here.
from assignment3.generated_code.problem_1 import numerical_letter_grade

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
        #pytest.assume(True)

        # Added Test with spec assertions
        # 1. Assertion 1: Output list length and element types.
        # Demonstrates that the output has the same length as input and all elements are strings.
        pytest.assume(numerical_letter_grade([0.0, 4.0, 2.5]) == ['E', 'A+', 'C+'])

        # 2. Assertion 2: Specific mapping for the highest exact GPA.
        # Demonstrates that a GPA of exactly 4.0 maps to 'A+'.
        pytest.assume(numerical_letter_grade([4.0]) == ['A+'])

        # 3. Assertion 3: Specific mapping for a typical mid-range GPA interval.
        # Demonstrates that GPAs strictly greater than 2.7 and less than or equal to 3.0 map to 'B'.
        pytest.assume(numerical_letter_grade([2.8, 3.0]) == ['B', 'B'])

        # 4. Assertion 4: Specific mapping for the lowest exact GPA.
        # Demonstrates that a GPA of exactly 0.0 maps to 'E'.
        pytest.assume(numerical_letter_grade([0.0]) == ['E'])

        # 5. Assertion 5: Comprehensive check for a broad range of high-tier grades.
        # Demonstrates correct mappings for GPAs > 2.7 across multiple defined intervals.
        pytest.assume(numerical_letter_grade([4.0, 3.8, 3.4, 3.1, 2.9]) == ['A+', 'A', 'A-', 'B+', 'B'])



    except Exception as e:
        # Fails the test if the generated code is so broken
        # it causes a TypeError, NameError, IndexError, etc.
        pytest.fail(f"Test crashed with an unhandled exception: {type(e).__name__}: {e}")