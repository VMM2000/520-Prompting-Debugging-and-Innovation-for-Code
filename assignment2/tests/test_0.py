import pytest
import importlib.util
from pathlib import Path

# --- 1. Helper Function to Load Functions Dynamically ---

def load_all_functions(glob_pattern, function_name):
    """
    Scans for files matching a pattern, imports them dynamically,
    and yields the function (e.g., 'min_cost') from each file.
    """
    
    # Go up one level (from tests/) and find the generated_code folder
    # This path is relative to this test file.
    code_dir = Path(__file__).parent.parent / "generated_code"
    
    # Find all files matching the pattern
    iteration_files = sorted(list(code_dir.glob(glob_pattern)))
    
    print(f"\nFound {len(iteration_files)} files for {glob_pattern}:")
    
    loaded_functions = []
    
    for file_path in iteration_files:
        if not file_path.name.endswith(".py"):
            continue
            
        # Create a unique module name for each file
        module_name = f"generated_code.{file_path.stem}"
        
        try:
            # Import the file as a Python module
            spec = importlib.util.spec_from_file_location(module_name, file_path)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            
            # Get the 'min_cost' function from the module
            func = getattr(module, function_name)
            
            # Add the function to our list
            # We use pytest.param to set a custom ID (the filename)
            # This makes test reports *much* easier to read
            loaded_functions.append(pytest.param(func, id=file_path.name))
            
        except Exception as e:
            print(f"Failed to load {file_path.name}: {e}")
            # You can also fail the test here if a file is broken
            # loaded_functions.append(pytest.param(None, id=f"FAILED_LOAD: {file_path.name}"))

    return loaded_functions

# --- 2. Load all 'min_cost' functions from 'problem_0_it_*.py' files ---

# Pytest runs this *once* when it collects tests
all_min_cost_functions = load_all_functions(
    glob_pattern="problem_0_*.py", 
    function_name="min_cost"
)

# --- 3. The Test Function (using parametrize) ---

@pytest.mark.parametrize("min_cost", all_min_cost_functions)
def test_min_cost(min_cost):
    """
    This ONE test will run for EVERY function in the 'all_min_cost_functions' list.
    'min_cost_func' will be the function from iteration 1, then iteration 2, etc.
    """
    
    # If loading failed, min_cost_func might be None
    if min_cost is None:
        pytest.fail("Module loading failed, see console output.")

    try:
        pytest.assume(min_cost([[1, 2, 3], [4, 8, 2], [1, 5, 3]], 2, 2) == 8)
        pytest.assume(min_cost([[2, 3, 4], [5, 9, 3], [2, 6, 4]], 2, 2) == 12)
        pytest.assume(min_cost([[3, 4, 5], [6, 10, 4], [3, 7, 5]], 2, 2) == 16)
        pytest.assume(min_cost([[4, 5, 7], [6, 8, 1], [5, 9, 5]], 2, 1) == 19)
        pytest.assume(min_cost([[6, 6, 1], [4, 10, 3], [1, 1, 1]], 2, 2) == 12)
        pytest.assume(min_cost([[1, 3, 6], [8, 3, 3], [1, 2, 7]], 1, 2) == 7)
        pytest.assume(min_cost([[2, 1, 4], [3, 13, 5], [1, 1, 1]], 2, 1) == 6)
        pytest.assume(min_cost([[4, 2, 3], [6, 12, 1], [5, 5, 7]], 1, 1) == 16)
        pytest.assume(min_cost([[4, 3, 4], [6, 12, 7], [3, 7, 7]], 1, 2) == 14)
        pytest.assume(min_cost([[4, 3, 8], [3, 6, 5], [6, 4, 1]], 2, 1) == 11)
        pytest.assume(min_cost([[5, 4, 7], [5, 4, 5], [6, 3, 3]], 2, 1) == 12)
        pytest.assume(min_cost([[2, 4, 5], [9, 13, 5], [6, 10, 4]], 2, 1) == 21)
        pytest.assume(min_cost([[6, 3, 8], [6, 9, 7], [1, 1, 7]], 1, 1) == 15)
        pytest.assume(min_cost([[4, 2, 5], [2, 10, 3], [5, 3, 5]], 2, 2) == 14)
        pytest.assume(min_cost([[2, 5, 4], [5, 3, 1], [4, 6, 8]], 1, 1) == 5)
        pytest.assume(min_cost([[3, 6, 6], [3, 10, 7], [5, 5, 7]], 1, 1) == 13)
        pytest.assume(min_cost([[6, 5, 8], [7, 4, 1], [3, 4, 4]], 2, 2) == 14)
        pytest.assume(min_cost([[1, 1, 8], [9, 6, 7], [3, 7, 1]], 1, 1) == 7)
        pytest.assume(min_cost([[1, 1, 1], [1, 13, 7], [6, 2, 4]], 2, 2) == 8)
        pytest.assume(min_cost([[2, 1, 8], [7, 11, 7], [6, 6, 5]], 2, 1) == 15)
        pytest.assume(min_cost([[3, 2, 5], [6, 3, 2], [5, 5, 7]], 1, 2) == 7)
        pytest.assume(min_cost([[2, 3, 8], [1, 6, 7], [4, 2, 8]], 2, 1) == 5)
        pytest.assume(min_cost([[2, 6, 6], [4, 6, 1], [2, 2, 7]], 1, 2) == 9)
        pytest.assume(min_cost([[4, 2, 3], [4, 8, 5], [1, 5, 5]], 2, 1) == 13)
        pytest.assume(min_cost([[4, 2, 5], [6, 11, 6], [2, 9, 7]], 2, 2) == 19)
        pytest.assume(min_cost([[2, 5, 2], [6, 13, 5], [1, 7, 8]], 1, 2) == 12)
        pytest.assume(min_cost([[5, 1, 4], [1, 7, 2], [6, 6, 2]], 2, 1) == 12)
        pytest.assume(min_cost([[5, 6, 8], [4, 5, 4], [5, 3, 4]], 2, 1) == 12)
        pytest.assume(min_cost([[1, 3, 1], [7, 6, 5], [4, 8, 4]], 2, 1) == 15)
        pytest.assume(min_cost([[2, 7, 6], [7, 12, 2], [3, 3, 7]], 2, 2) == 18)
        pytest.assume(min_cost([[4, 6, 2], [4, 13, 5], [4, 10, 4]], 1, 1) == 17)
        pytest.assume(min_cost([[6, 5, 5], [6, 10, 4], [5, 5, 4]], 1, 1) == 16)
        pytest.assume(min_cost([[6, 6, 4], [9, 11, 7], [3, 10, 7]], 2, 2) == 24)
        pytest.assume(min_cost([[6, 3, 2], [8, 5, 3], [2, 1, 4]], 2, 1) == 12)
        pytest.assume(min_cost([[4, 6, 2], [9, 7, 4], [1, 3, 6]], 1, 1) == 11)
        pytest.assume(min_cost([[4, 7, 4], [9, 7, 6], [6, 1, 7]], 1, 1) == 11)
        pytest.assume(min_cost([[2, 5, 6], [10, 11, 7], [7, 3, 4]], 2, 1) == 15)
        pytest.assume(min_cost([[3, 6, 1], [7, 4, 3], [7, 11, 7]], 2, 2) == 14)
        pytest.assume(min_cost([[2, 4, 3], [1, 12, 7], [5, 6, 6]], 2, 1) == 9)
        pytest.assume(min_cost([[5, 5, 6], [8, 11, 1], [6, 11, 8]], 1, 1) == 16)
        pytest.assume(min_cost([[6, 8, 5], [2, 14, 5], [2, 8, 1]], 2, 1) == 16)
        pytest.assume(min_cost([[6, 8, 9], [9, 7, 3], [5, 2, 9]], 2, 2) == 22)
        pytest.assume(min_cost([[3, 2, 7], [7, 9, 8], [1, 6, 3]], 2, 1) == 16)
        pytest.assume(min_cost([[4, 3, 1], [7, 8, 1], [3, 11, 8]], 1, 1) == 12)
        pytest.assume(min_cost([[1, 5, 8], [4, 11, 6], [7, 10, 3]], 1, 2) == 12)
        pytest.assume(min_cost([[2, 7, 8], [5, 6, 7], [2, 3, 2]], 2, 1) == 10)
        pytest.assume(min_cost([[2, 5, 9], [7, 13, 8], [5, 3, 7]], 2, 2) == 19)
        pytest.assume(min_cost([[3, 1, 7], [4, 5, 7], [4, 5, 3]], 2, 1) == 12)
        pytest.assume(min_cost([[4, 7, 5], [2, 13, 1], [6, 5, 4]], 1, 1) == 17)
        pytest.assume(min_cost([[5, 7, 4], [3, 6, 7], [1, 2, 1]], 2, 2) == 11)
        pytest.assume(min_cost([[3, 4, 5], [2, 6, 1], [4, 2, 9]], 2, 2) == 16)
        pytest.assume(min_cost([[4, 7, 2], [1, 4, 4], [4, 11, 2]], 1, 2) == 12)
        pytest.assume(min_cost([[1, 6, 1], [3, 7, 1], [5, 1, 3]], 1, 2) == 8)
        pytest.assume(min_cost([[3, 6, 4], [1, 6, 6], [5, 11, 3]], 2, 2) == 12)
        pytest.assume(min_cost([[5, 7, 5], [9, 6, 8], [5, 8, 1]], 2, 2) == 12)
        pytest.assume(min_cost([[7, 4, 3], [2, 11, 2], [3, 4, 6]], 2, 2) == 19)
        pytest.assume(min_cost([[3, 1, 8], [8, 5, 6], [4, 1, 5]], 2, 1) == 9)
        pytest.assume(min_cost([[7, 4, 6], [10, 8, 5], [2, 1, 2]], 2, 2) == 17)
        pytest.assume(min_cost([[2, 2, 7], [3, 4, 7], [4, 3, 9]], 1, 1) == 6)
        pytest.assume(min_cost([[7, 3, 1], [2, 12, 4], [5, 8, 7]], 2, 1) == 17)
        pytest.assume(min_cost([[4, 5, 2], [7, 14, 2], [5, 7, 4]], 2, 2) == 15)
        pytest.assume(min_cost([[3, 5, 6], [7, 13, 6], [1, 1, 5]], 2, 2) == 16)
        pytest.assume(min_cost([[1, 7, 2], [4, 7, 1], [3, 11, 9]], 1, 1) == 8)
        pytest.assume(min_cost([[5, 2, 5], [3, 4, 2], [6, 9, 1]], 1, 2) == 9)
        pytest.assume(min_cost([[4, 8, 9], [7, 10, 4], [5, 5, 9]], 1, 1) == 14)
        pytest.assume(min_cost([[5, 4, 4], [7, 6, 1], [7, 6, 7]], 2, 1) == 17)
        pytest.assume(min_cost([[3, 3, 4], [7, 11, 6], [3, 11, 1]], 1, 2) == 12)
        pytest.assume(min_cost([[1, 4, 4], [1, 11, 6], [3, 2, 3]], 1, 1) == 12)
        pytest.assume(min_cost([[1, 2, 6], [5, 4, 3], [2, 5, 6]], 1, 1) == 5)
        pytest.assume(min_cost([[6, 4, 3], [1, 14, 6], [5, 6, 10]], 1, 2) == 16)
        pytest.assume(min_cost([[6, 5, 7], [4, 13, 7], [6, 9, 4]], 1, 2) == 18)
        pytest.assume(min_cost([[7, 7, 10], [1, 7, 3], [8, 2, 4]], 1, 2) == 17)
        pytest.assume(min_cost([[3, 6, 9], [3, 5, 5], [2, 7, 6]], 1, 2) == 13)
        pytest.assume(min_cost([[7, 5, 6], [7, 8, 1], [4, 5, 9]], 1, 2) == 13)
        pytest.assume(min_cost([[4, 4, 4], [3, 15, 2], [4, 6, 6]], 2, 1) == 13)
        pytest.assume(min_cost([[7, 7, 10], [1, 14, 5], [4, 9, 7]], 1, 1) == 21)
        pytest.assume(min_cost([[8, 4, 8], [5, 11, 8], [1, 4, 7]], 2, 1) == 17)
        pytest.assume(min_cost([[1, 8, 7], [5, 15, 3], [6, 4, 3]], 2, 2) == 13)
        pytest.assume(min_cost([[1, 8, 7], [7, 10, 3], [1, 11, 7]], 1, 1) == 11)
        pytest.assume(min_cost([[3, 5, 8], [9, 5, 6], [8, 10, 8]], 2, 2) == 16)
        pytest.assume(min_cost([[5, 1, 9], [11, 12, 1], [8, 8, 8]], 2, 2) == 15)
        pytest.assume(min_cost([[4, 1, 7], [2, 13, 6], [5, 9, 2]], 2, 1) == 15)
        pytest.assume(min_cost([[2, 3, 7], [2, 9, 1], [4, 6, 7]], 1, 2) == 6)
        pytest.assume(min_cost([[6, 6, 3], [8, 9, 3], [8, 11, 6]], 1, 1) == 15)
        pytest.assume(min_cost([[2, 9, 9], [11, 12, 9], [6, 12, 4]], 2, 1) == 25)
        pytest.assume(min_cost([[1, 9, 2], [5, 15, 5], [5, 3, 2]], 1, 2) == 15)
        pytest.assume(min_cost([[3, 2, 10], [4, 5, 6], [3, 8, 3]], 1, 2) == 11)
        pytest.assume(min_cost([[8, 5, 1], [7, 9, 2], [2, 8, 4]], 2, 2) == 19)
        pytest.assume(min_cost([[5, 1, 2], [6, 10, 8], [2, 11, 7]], 1, 1) == 15)
        pytest.assume(min_cost([[6, 5, 8], [9, 6, 4], [7, 10, 9]], 2, 2) == 21)
        pytest.assume(min_cost([[1, 6, 5], [3, 5, 7], [3, 5, 7]], 1, 2) == 13)
        pytest.assume(min_cost([[4, 2, 5], [2, 12, 3], [6, 7, 4]], 2, 2) == 13)
        pytest.assume(min_cost([[8, 7, 9], [11, 9, 9], [6, 2, 6]], 2, 1) == 19)
        pytest.assume(min_cost([[8, 9, 2], [1, 5, 3], [5, 2, 3]], 2, 2) == 14)
        pytest.assume(min_cost([[4, 2, 4], [2, 6, 7], [4, 2, 10]], 1, 2) == 13)
        pytest.assume(min_cost([[7, 6, 3], [4, 8, 5], [7, 8, 1]], 2, 1) == 19)
        pytest.assume(min_cost([[8, 9, 4], [8, 5, 9], [6, 8, 6]], 2, 1) == 21)
        pytest.assume(min_cost([[3, 5, 6], [2, 9, 9], [1, 3, 4]], 2, 2) == 12)
        pytest.assume(min_cost([[7, 9, 8], [7, 13, 2], [7, 7, 7]], 2, 1) == 21)
        pytest.assume(min_cost([[7, 2, 2], [6, 15, 1], [8, 4, 2]], 1, 1) == 22)
        pytest.assume(min_cost([[5, 6, 8], [8, 10, 2], [7, 3, 8]], 1, 2) == 13)
        pytest.assume(min_cost([[8, 9, 2], [6, 5, 7], [3, 8, 8]], 2, 2) == 21)
    except TypeError as e:
        pytest.fail(f"Test crashed with TypeError: {e}")