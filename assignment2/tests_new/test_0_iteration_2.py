import pytest
import importlib.util
from pathlib import Path

# 1. Import the function to be tested
# This assumes new_gen_code.py is in the same folder
from generated_code_new.problem_0 import min_path

# 2. The Test Function
# Renamed to 'test_min_path' to be found by pytest
def test_min_path():
    """
    This test will now run ALL assertions and report all failures
    at the end, thanks to 'pytest.assume()'.
    """
    
    if min_path is None:

        pytest.fail("min_path function was not imported correctly.")

    try:
        # 3. All 'assert' statements are changed to 'pytest.assume'
        #    and 'candidate' is changed to 'min_path'
        
        # Check some simple cases
        pytest.assume(min_path([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 3) == [1, 2, 1])
        pytest.assume(min_path([[5, 9, 3], [4, 1, 6], [7, 8, 2]], 1) == [1])
        pytest.assume(min_path([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]], 4) == [1, 2, 1, 2])
        pytest.assume(min_path([[6, 4, 13, 10], [5, 7, 12, 1], [3, 16, 11, 15], [8, 14, 9, 2]], 7) == [1, 10, 1, 10, 1, 10, 1])
        pytest.assume(min_path([[8, 14, 9, 2], [6, 4, 13, 15], [5, 7, 1, 12], [3, 10, 11, 16]], 5) == [1, 7, 1, 7, 1])
        pytest.assume(min_path([[11, 8, 7, 2], [5, 16, 14, 4], [9, 3, 15, 6], [12, 13, 10, 1]], 9) == [1, 6, 1, 6, 1, 6, 1, 6, 1])
        pytest.assume(min_path([[12, 13, 10, 1], [9, 3, 15, 6], [5, 16, 14, 4], [11, 8, 7, 2]], 12) == [1, 6, 1, 6, 1, 6, 1, 6, 1, 6, 1, 6])
        pytest.assume(min_path([[2, 7, 4], [3, 1, 5], [6, 8, 9]], 8) == [1, 3, 1, 3, 1, 3, 1, 3])
        pytest.assume(min_path([[6, 1, 5], [3, 8, 9], [2, 7, 4]], 8) == [1, 5, 1, 5, 1, 5, 1, 5])

        # Check some edge cases that are easy to work out by hand.
        pytest.assume(min_path([[1, 2], [3, 4]], 10) == [1, 2, 1, 2, 1, 2, 1, 2, 1, 2])
        pytest.assume(min_path([[1, 3], [3, 2]], 10) == [1, 3, 1, 3, 1, 3, 1, 3, 1, 3])
        

        # Test case for an empty grid to cover the `if N == 0:` branch
        pytest.assume(min_path([], 5) == [])

        # Test case where k=1 on a 1x1 grid.
        # This ensures the main path-finding loop `for _ in range(k-1)` does not run.
        pytest.assume(min_path([[1]], 1) == [1])

        # Test case where k=0. The loop `range(k-1)` becomes `range(-1)`, which is empty.
        # The code returns the path with just the starting element.
        pytest.assume(min_path([[1, 2], [3, 4]], 0) == [1])

        # Test case where '1' is in the middle, ensuring all 4 directions are checked initially.
        pytest.assume(min_path([[5, 2, 3], [4, 1, 6], [7, 8, 9]], 4) == [1, 2, 1, 2])

        # Test case: 1x1 grid with k > 1.
        # This specifically targets the scenario where N=1, so all 4 neighbor directions
        # will result in out-of-bounds. This consistently hits the `False` branch of
        # `if 0 <= nr < N and 0 <= nc < N:` for every neighbor check in the path-finding loop.
        # The current implementation will append `float('inf')` repeatedly if no valid moves are found.
        pytest.assume(min_path([[1]], 5) == [1, float('inf'), float('inf'), float('inf'), float('inf')])

        # Test '1' at top-right corner of a 2x2 grid
        # Covers specific boundary conditions where (0,1) and (-1,0) are out of bounds.
        pytest.assume(min_path([[2, 1], [3, 4]], 3) == [1, 2, 1])

        # Test '1' at bottom-left corner of a 2x2 grid
        # Covers specific boundary conditions where (1,0) and (0,-1) are out of bounds.
        pytest.assume(min_path([[2, 3], [1, 4]], 3) == [1, 2, 1])

        # Test '1' at bottom-right corner of a 2x2 grid
        # Covers specific boundary conditions where (1,0) and (0,1) are out of bounds.
        pytest.assume(min_path([[2, 3], [4, 1]], 3) == [1, 3, 1])
        
        # Test '1' in the middle of a top edge (not a corner) in a 3x3 grid
        # Covers the case where only one direction (up) is out of bounds initially.
        pytest.assume(min_path([[5, 1, 6], [2, 3, 4], [7, 8, 9]], 4) == [1, 3, 1, 3])

        # Test '1' in the middle of a left edge (not a corner) in a 3x3 grid
        # Covers the case where only one direction (left) is out of bounds initially.
        pytest.assume(min_path([[5, 2, 6], [1, 3, 4], [7, 8, 9]], 4) == [1, 3, 1, 3])


    except TypeError as e:
        # Fails the test if the generated code is so broken
        # it causes a TypeError (e.g., bad arguments)
        pytest.fail(f"Test crashed with TypeError: {e}")