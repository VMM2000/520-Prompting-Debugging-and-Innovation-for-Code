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
    glob_pattern="problem_4_*.py", 
    function_name="count_ways"
)

# --- 3. The Test Function (using parametrize) ---

@pytest.mark.parametrize("count_ways", all_min_cost_functions)
def test_count_ways(count_ways):
    """
    This ONE test will run for EVERY function in the 'all_min_cost_functions' list.
    'count_ways' will be the function from iteration 1, then iteration 2, etc.
    """
    
    # If loading failed, min_cost_func might be None
    if count_ways is None:
        pytest.fail("Module loading failed, see console output.")

    try:
        pytest.assume(count_ways(2) == 3)
        pytest.assume(count_ways(8) == 153)
        pytest.assume(count_ways(12) == 2131)
        pytest.assume(count_ways(4) == 11)
        pytest.assume(count_ways(2) == 3)
        pytest.assume(count_ways(4) == 11)
        pytest.assume(count_ways(7) == 0)
        pytest.assume(count_ways(2) == 3)
        pytest.assume(count_ways(5) == 0)
        pytest.assume(count_ways(1) == 0)
        pytest.assume(count_ways(4) == 11)
        pytest.assume(count_ways(1) == 0)
        pytest.assume(count_ways(6) == 41)
        pytest.assume(count_ways(2) == 3)
        pytest.assume(count_ways(3) == 0)
        pytest.assume(count_ways(4) == 11)
        pytest.assume(count_ways(5) == 0)
        pytest.assume(count_ways(2) == 3)
        pytest.assume(count_ways(1) == 0)
        pytest.assume(count_ways(2) == 3)
        pytest.assume(count_ways(2) == 3)
        pytest.assume(count_ways(6) == 41)
        pytest.assume(count_ways(5) == 0)
        pytest.assume(count_ways(2) == 3)
        pytest.assume(count_ways(7) == 0)
        pytest.assume(count_ways(3) == 0)
        pytest.assume(count_ways(3) == 0)
        pytest.assume(count_ways(7) == 0)
        pytest.assume(count_ways(3) == 0)
        pytest.assume(count_ways(2) == 3)
        pytest.assume(count_ways(4) == 11)
        pytest.assume(count_ways(7) == 0)
        pytest.assume(count_ways(1) == 0)
        pytest.assume(count_ways(3) == 0)
        pytest.assume(count_ways(2) == 3)
        pytest.assume(count_ways(3) == 0)
        pytest.assume(count_ways(3) == 0)
        pytest.assume(count_ways(4) == 11)
        pytest.assume(count_ways(4) == 11)
        pytest.assume(count_ways(10) == 571)
        pytest.assume(count_ways(7) == 0)
        pytest.assume(count_ways(10) == 571)
        pytest.assume(count_ways(7) == 0)
        pytest.assume(count_ways(7) == 0)
        pytest.assume(count_ways(8) == 153)
        pytest.assume(count_ways(4) == 11)
        pytest.assume(count_ways(10) == 571)
        pytest.assume(count_ways(8) == 153)
        pytest.assume(count_ways(9) == 0)
        pytest.assume(count_ways(11) == 0)
        pytest.assume(count_ways(6) == 41)
        pytest.assume(count_ways(4) == 11)
        pytest.assume(count_ways(6) == 41)
        pytest.assume(count_ways(8) == 153)
        pytest.assume(count_ways(9) == 0)
        pytest.assume(count_ways(13) == 0)
        pytest.assume(count_ways(11) == 0)
        pytest.assume(count_ways(6) == 41)
        pytest.assume(count_ways(13) == 0)
        pytest.assume(count_ways(13) == 0)
        pytest.assume(count_ways(13) == 0)
        pytest.assume(count_ways(12) == 2131)
        pytest.assume(count_ways(5) == 0)
        pytest.assume(count_ways(8) == 153)
        pytest.assume(count_ways(6) == 41)
        pytest.assume(count_ways(5) == 0)
        pytest.assume(count_ways(7) == 0)
        pytest.assume(count_ways(3) == 0)
        pytest.assume(count_ways(13) == 0)
        pytest.assume(count_ways(10) == 571)
        pytest.assume(count_ways(10) == 571)
        pytest.assume(count_ways(15) == 0)
        pytest.assume(count_ways(17) == 0)
        pytest.assume(count_ways(16) == 29681)
        pytest.assume(count_ways(9) == 0)
        pytest.assume(count_ways(17) == 0)
        pytest.assume(count_ways(9) == 0)
        pytest.assume(count_ways(17) == 0)
        pytest.assume(count_ways(13) == 0)
        pytest.assume(count_ways(12) == 2131)
        pytest.assume(count_ways(7) == 0)
        pytest.assume(count_ways(14) == 7953)
        pytest.assume(count_ways(9) == 0)
        pytest.assume(count_ways(13) == 0)
        pytest.assume(count_ways(11) == 0)
        pytest.assume(count_ways(15) == 0)
        pytest.assume(count_ways(16) == 29681)
        pytest.assume(count_ways(7) == 0)
        pytest.assume(count_ways(14) == 7953)
        pytest.assume(count_ways(12) == 2131)
        pytest.assume(count_ways(9) == 0)
        pytest.assume(count_ways(11) == 0)
        pytest.assume(count_ways(14) == 7953)
        pytest.assume(count_ways(12) == 2131)
        pytest.assume(count_ways(11) == 0)
        pytest.assume(count_ways(11) == 0)
        pytest.assume(count_ways(7) == 0)
        pytest.assume(count_ways(12) == 2131)
        pytest.assume(count_ways(17) == 0)
        pytest.assume(count_ways(9) == 0)
        pytest.assume(count_ways(12) == 2131)
        pytest.assume(count_ways(8) == 153)
    except TypeError as e:
        pytest.fail(f"Test crashed with TypeError: {e}")