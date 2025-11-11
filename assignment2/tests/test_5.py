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
    glob_pattern="problem_5_*.py", 
    function_name="differ_At_One_Bit_Pos"
)

# --- 3. The Test Function (using parametrize) ---

@pytest.mark.parametrize("differ_At_One_Bit_Pos", all_min_cost_functions)
def test_differ_At_One_Bit_Pos(differ_At_One_Bit_Pos):
    """
    This ONE test will run for EVERY function in the 'all_min_cost_functions' list.
    'differ_At_One_Bit_Pos' will be the function from iteration 1, then iteration 2, etc.
    """
    
    # If loading failed, min_cost_func might be None
    if differ_At_One_Bit_Pos is None:
        pytest.fail("Module loading failed, see console output.")

    try:
        pytest.assume(differ_At_One_Bit_Pos(13,9) == True)
        pytest.assume(differ_At_One_Bit_Pos(15,8) == False)
        pytest.assume(differ_At_One_Bit_Pos(2,4) == False)
        pytest.assume(differ_At_One_Bit_Pos(14, 9) == False)
        pytest.assume(differ_At_One_Bit_Pos(17, 9) == False)
        pytest.assume(differ_At_One_Bit_Pos(15, 7) == True)
        pytest.assume(differ_At_One_Bit_Pos(8, 7) == False)
        pytest.assume(differ_At_One_Bit_Pos(13, 13) == 0)
        pytest.assume(differ_At_One_Bit_Pos(16, 5) == False)
        pytest.assume(differ_At_One_Bit_Pos(17, 10) == False)
        pytest.assume(differ_At_One_Bit_Pos(17, 10) == False)
        pytest.assume(differ_At_One_Bit_Pos(9, 14) == False)
        pytest.assume(differ_At_One_Bit_Pos(17, 14) == False)
        pytest.assume(differ_At_One_Bit_Pos(11, 9) == True)
        pytest.assume(differ_At_One_Bit_Pos(18, 7) == False)
        pytest.assume(differ_At_One_Bit_Pos(18, 6) == False)
        pytest.assume(differ_At_One_Bit_Pos(9, 10) == False)
        pytest.assume(differ_At_One_Bit_Pos(12, 6) == False)
        pytest.assume(differ_At_One_Bit_Pos(12, 12) == 0)
        pytest.assume(differ_At_One_Bit_Pos(13, 10) == False)
        pytest.assume(differ_At_One_Bit_Pos(15, 7) == True)
        pytest.assume(differ_At_One_Bit_Pos(12, 11) == False)
        pytest.assume(differ_At_One_Bit_Pos(15, 10) == False)
        pytest.assume(differ_At_One_Bit_Pos(8, 12) == True)
        pytest.assume(differ_At_One_Bit_Pos(9, 13) == True)
        pytest.assume(differ_At_One_Bit_Pos(10, 5) == False)
        pytest.assume(differ_At_One_Bit_Pos(15, 11) == True)
        pytest.assume(differ_At_One_Bit_Pos(14, 11) == False)
        pytest.assume(differ_At_One_Bit_Pos(9, 10) == False)
        pytest.assume(differ_At_One_Bit_Pos(16, 11) == False)
        pytest.assume(differ_At_One_Bit_Pos(18, 10) == False)
        pytest.assume(differ_At_One_Bit_Pos(15, 11) == True)
        pytest.assume(differ_At_One_Bit_Pos(14, 7) == False)
        pytest.assume(differ_At_One_Bit_Pos(12, 8) == True)
        pytest.assume(differ_At_One_Bit_Pos(10, 4) == False)
        pytest.assume(differ_At_One_Bit_Pos(16, 12) == False)
        pytest.assume(differ_At_One_Bit_Pos(11, 9) == True)
        pytest.assume(differ_At_One_Bit_Pos(13, 4) == False)
        pytest.assume(differ_At_One_Bit_Pos(18, 12) == False)
        pytest.assume(differ_At_One_Bit_Pos(13, 13) == 0)
        pytest.assume(differ_At_One_Bit_Pos(19, 7) == False)
        pytest.assume(differ_At_One_Bit_Pos(16, 9) == False)
        pytest.assume(differ_At_One_Bit_Pos(13, 5) == True)
        pytest.assume(differ_At_One_Bit_Pos(20, 8) == False)
        pytest.assume(differ_At_One_Bit_Pos(16, 12) == False)
        pytest.assume(differ_At_One_Bit_Pos(16, 12) == False)
        pytest.assume(differ_At_One_Bit_Pos(14, 13) == False)
        pytest.assume(differ_At_One_Bit_Pos(20, 6) == False)
        pytest.assume(differ_At_One_Bit_Pos(12, 3) == False)
        pytest.assume(differ_At_One_Bit_Pos(13, 4) == False)
        pytest.assume(differ_At_One_Bit_Pos(19, 12) == False)
        pytest.assume(differ_At_One_Bit_Pos(19, 9) == False)
        pytest.assume(differ_At_One_Bit_Pos(11, 10) == True)
        pytest.assume(differ_At_One_Bit_Pos(16, 13) == False)
        pytest.assume(differ_At_One_Bit_Pos(14, 7) == False)
        pytest.assume(differ_At_One_Bit_Pos(14, 10) == True)
        pytest.assume(differ_At_One_Bit_Pos(14, 7) == False)
        pytest.assume(differ_At_One_Bit_Pos(13, 11) == False)
        pytest.assume(differ_At_One_Bit_Pos(10, 12) == False)
        pytest.assume(differ_At_One_Bit_Pos(17, 11) == False)
        pytest.assume(differ_At_One_Bit_Pos(14, 3) == False)
        pytest.assume(differ_At_One_Bit_Pos(15, 12) == False)
        pytest.assume(differ_At_One_Bit_Pos(19, 9) == False)
        pytest.assume(differ_At_One_Bit_Pos(19, 4) == False)
        pytest.assume(differ_At_One_Bit_Pos(14, 12) == True)
        pytest.assume(differ_At_One_Bit_Pos(17, 3) == False)
        pytest.assume(differ_At_One_Bit_Pos(14, 9) == False)
        pytest.assume(differ_At_One_Bit_Pos(20, 5) == False)
        pytest.assume(differ_At_One_Bit_Pos(11, 10) == True)
        pytest.assume(differ_At_One_Bit_Pos(4, 1) == False)
        pytest.assume(differ_At_One_Bit_Pos(4, 3) == False)
        pytest.assume(differ_At_One_Bit_Pos(4, 6) == True)
        pytest.assume(differ_At_One_Bit_Pos(4, 5) == True)
        pytest.assume(differ_At_One_Bit_Pos(1, 4) == False)
        pytest.assume(differ_At_One_Bit_Pos(7, 9) == False)
        pytest.assume(differ_At_One_Bit_Pos(4, 1) == False)
        pytest.assume(differ_At_One_Bit_Pos(2, 4) == False)
        pytest.assume(differ_At_One_Bit_Pos(4, 6) == True)
        pytest.assume(differ_At_One_Bit_Pos(5, 6) == False)
        pytest.assume(differ_At_One_Bit_Pos(7, 9) == False)
        pytest.assume(differ_At_One_Bit_Pos(3, 8) == False)
        pytest.assume(differ_At_One_Bit_Pos(7, 2) == False)
        pytest.assume(differ_At_One_Bit_Pos(5, 7) == True)
        pytest.assume(differ_At_One_Bit_Pos(6, 1) == False)
        pytest.assume(differ_At_One_Bit_Pos(6, 9) == False)
        pytest.assume(differ_At_One_Bit_Pos(2, 4) == False)
        pytest.assume(differ_At_One_Bit_Pos(4, 2) == False)
        pytest.assume(differ_At_One_Bit_Pos(2, 6) == True)
        pytest.assume(differ_At_One_Bit_Pos(2, 3) == True)
        pytest.assume(differ_At_One_Bit_Pos(6, 8) == False)
        pytest.assume(differ_At_One_Bit_Pos(3, 8) == False)
        pytest.assume(differ_At_One_Bit_Pos(5, 7) == True)
        pytest.assume(differ_At_One_Bit_Pos(1, 1) == 0)
        pytest.assume(differ_At_One_Bit_Pos(1, 2) == False)
        pytest.assume(differ_At_One_Bit_Pos(5, 5) == 0)
        pytest.assume(differ_At_One_Bit_Pos(4, 3) == False)
        pytest.assume(differ_At_One_Bit_Pos(6, 3) == False)
        pytest.assume(differ_At_One_Bit_Pos(3, 1) == True)
        pytest.assume(differ_At_One_Bit_Pos(1, 1) == 0)
        pytest.assume(differ_At_One_Bit_Pos(5, 1) == True)
        pytest.assume(differ_At_One_Bit_Pos(4, 4) == 0)
        pytest.assume(differ_At_One_Bit_Pos(1, 9) == True)
    except TypeError as e:
        pytest.fail(f"Test crashed with TypeError: {e}")