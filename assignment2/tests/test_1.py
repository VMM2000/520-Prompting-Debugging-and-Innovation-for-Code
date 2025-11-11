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
    glob_pattern="problem_1_*.py", 
    function_name="similar_elements"
)

# --- 3. The Test Function (using parametrize) ---

@pytest.mark.parametrize("similar_elements", all_min_cost_functions)
def test_min_cost(similar_elements):
    """
    This ONE test will run for EVERY function in the 'all_min_cost_functions' list.
    'min_cost_func' will be the function from iteration 1, then iteration 2, etc.
    """
    
    # If loading failed, min_cost_func might be None
    if similar_elements is None:
        pytest.fail("Module loading failed, see console output.")

    try:
        pytest.assume(similar_elements((3, 4, 5, 6),(5, 7, 4, 10)) == (4, 5))
        pytest.assume(similar_elements((1, 2, 3, 4),(5, 4, 3, 7)) == (3, 4))
        pytest.assume(similar_elements((11, 12, 14, 13),(17, 15, 14, 13)) == (13, 14))
        pytest.assume(similar_elements((7, 1, 6, 7), (7, 2, 5, 7)) == (7,))
        pytest.assume(similar_elements((1, 7, 5, 11), (7, 10, 7, 8)) == (7,))
        pytest.assume(similar_elements((7, 6, 6, 2), (3, 2, 4, 13)) == (2,))
        pytest.assume(similar_elements((3, 1, 6, 9), (3, 7, 6, 8)) == (3, 6))
        pytest.assume(similar_elements((8, 5, 4, 9), (7, 3, 8, 7)) == (8,))
        pytest.assume(similar_elements((2, 8, 2, 1), (3, 4, 4, 12)) == ())
        pytest.assume(similar_elements((3, 9, 9, 3), (4, 11, 6, 14)) == ())
        pytest.assume(similar_elements((1, 8, 8, 1), (4, 12, 5, 7)) == ())
        pytest.assume(similar_elements((6, 3, 6, 11), (7, 6, 7, 14)) == (6,))
        pytest.assume(similar_elements((4, 1, 3, 10), (6, 5, 7, 13)) == ())
        pytest.assume(similar_elements((7, 8, 7, 7), (2, 6, 7, 7)) == (7,))
        pytest.assume(similar_elements((6, 2, 4, 1), (9, 9, 2, 9)) == (2,))
        pytest.assume(similar_elements((2, 2, 5, 6), (3, 12, 3, 9)) == ())
        pytest.assume(similar_elements((5, 1, 2, 11), (1, 4, 3, 13)) == (1,))
        pytest.assume(similar_elements((6, 8, 9, 3), (6, 2, 7, 8)) == (8, 6))
        pytest.assume(similar_elements((6, 1, 4, 3), (6, 4, 3, 9)) == (3, 4, 6))
        pytest.assume(similar_elements((3, 3, 4, 3), (7, 3, 4, 10)) == (3, 4))
        pytest.assume(similar_elements((5, 4, 3, 10), (8, 4, 4, 15)) == (4,))
        pytest.assume(similar_elements((4, 5, 9, 3), (4, 7, 7, 15)) == (4,))
        pytest.assume(similar_elements((3, 3, 3, 7), (9, 4, 7, 11)) == (7,))
        pytest.assume(similar_elements((3, 7, 1, 1), (8, 6, 8, 7)) == (7,))
        pytest.assume(similar_elements((6, 2, 4, 10), (3, 10, 4, 14)) == (10, 4))
        pytest.assume(similar_elements((2, 8, 5, 9), (2, 6, 7, 11)) == (2,))
        pytest.assume(similar_elements((2, 2, 10, 5), (10, 5, 5, 13)) == (10, 5))
        pytest.assume(similar_elements((5, 9, 2, 7), (10, 2, 5, 9)) == (9, 2, 5))
        pytest.assume(similar_elements((3, 7, 6, 11), (1, 8, 2, 14)) == ())
        pytest.assume(similar_elements((4, 2, 5, 8), (6, 5, 5, 11)) == (5,))
        pytest.assume(similar_elements((3, 5, 4, 9), (10, 3, 1, 7)) == (3,))
        pytest.assume(similar_elements((5, 5, 6, 4), (5, 4, 1, 5)) == (4, 5))
        pytest.assume(similar_elements((7, 1, 1, 11), (2, 7, 3, 10)) == (7,))
        pytest.assume(similar_elements((4, 7, 5, 1), (1, 8, 5, 6)) == (1, 5))
        pytest.assume(similar_elements((5, 4, 1, 4), (10, 11, 1, 6)) == (1,))
        pytest.assume(similar_elements((3, 5, 1, 5), (5, 10, 8, 10)) == (5,))
        pytest.assume(similar_elements((6, 4, 3, 1), (1, 2, 3, 3)) == (1, 3))
        pytest.assume(similar_elements((6, 6, 7, 2), (7, 6, 6, 6)) == (6, 7))
        pytest.assume(similar_elements((5, 7, 5, 6), (1, 9, 6, 12)) == (6,))
        pytest.assume(similar_elements((1, 4, 8, 2), (6, 4, 8, 5)) == (8, 4))
        pytest.assume(similar_elements((5, 2, 8, 4), (5, 8, 8, 7)) == (8, 5))
        pytest.assume(similar_elements((3, 7, 3, 6), (9, 1, 2, 8)) == ())
        pytest.assume(similar_elements((4, 3, 1, 8), (1, 8, 6, 12)) == (8, 1))
        pytest.assume(similar_elements((5, 2, 4, 7), (9, 9, 4, 10)) == (4,))
        pytest.assume(similar_elements((2, 1, 3, 2), (9, 1, 2, 9)) == (1, 2))
        pytest.assume(similar_elements((4, 3, 4, 9), (9, 1, 4, 11)) == (9, 4))
        pytest.assume(similar_elements((3, 6, 8, 8), (4, 9, 4, 7)) == ())
        pytest.assume(similar_elements((2, 5, 4, 9), (8, 9, 6, 2)) == (9, 2))
        pytest.assume(similar_elements((5, 3, 4, 5), (3, 4, 1, 12)) == (3, 4))
        pytest.assume(similar_elements((6, 4, 5, 2), (1, 7, 4, 2)) == (2, 4))
        pytest.assume(similar_elements((1, 7, 4, 6), (8, 2, 1, 8)) == (1,))
        pytest.assume(similar_elements((4, 7, 6, 4), (5, 4, 7, 8)) == (4, 7))
        pytest.assume(similar_elements((6, 7, 1, 2), (3, 9, 8, 6)) == (6,))
        pytest.assume(similar_elements((2, 5, 3, 3), (2, 4, 6, 10)) == (2,))
        pytest.assume(similar_elements((6, 7, 7, 5), (1, 1, 7, 4)) == (7,))
        pytest.assume(similar_elements((1, 3, 7, 7), (6, 8, 8, 10)) == ())
        pytest.assume(similar_elements((6, 5, 6, 3), (9, 4, 1, 9)) == ())
        pytest.assume(similar_elements((5, 6, 5, 9), (5, 9, 7, 5)) == (9, 5))
        pytest.assume(similar_elements((4, 7, 4, 4), (10, 8, 1, 7)) == (7,))
        pytest.assume(similar_elements((1, 1, 2, 4), (7, 9, 6, 6)) == ())
        pytest.assume(similar_elements((5, 3, 2, 6), (8, 5, 6, 7)) == (5, 6))
        pytest.assume(similar_elements((2, 2, 2, 2), (6, 6, 2, 4)) == (2,))
        pytest.assume(similar_elements((3, 2, 6, 3), (8, 7, 2, 8)) == (2,))
        pytest.assume(similar_elements((2, 1, 1, 3), (6, 5, 5, 2)) == (2,))
        pytest.assume(similar_elements((2, 3, 3, 9), (8, 1, 8, 11)) == ())
        pytest.assume(similar_elements((5, 6, 2, 5), (6, 8, 4, 8)) == (6,))
        pytest.assume(similar_elements((2, 4, 6, 3), (1, 1, 3, 4)) == (3, 4))
        pytest.assume(similar_elements((5, 5, 5, 9), (7, 2, 1, 7)) == ())
        pytest.assume(similar_elements((2, 1, 5, 3), (4, 2, 3, 11)) == (2, 3))
        pytest.assume(similar_elements((6, 7, 18, 15), (21, 10, 11, 12)) == ())
        pytest.assume(similar_elements((14, 8, 18, 11), (17, 13, 18, 16)) == (18,))
        pytest.assume(similar_elements((13, 12, 10, 10), (18, 20, 10, 8)) == (10,))
        pytest.assume(similar_elements((14, 15, 19, 14), (21, 19, 17, 11)) == (19,))
        pytest.assume(similar_elements((9, 7, 9, 14), (22, 16, 10, 15)) == ())
        pytest.assume(similar_elements((10, 10, 16, 8), (16, 14, 16, 12)) == (16,))
        pytest.assume(similar_elements((6, 7, 10, 10), (12, 13, 10, 15)) == (10,))
        pytest.assume(similar_elements((7, 7, 19, 17), (14, 20, 19, 13)) == (19,))
        pytest.assume(similar_elements((14, 11, 11, 8), (21, 14, 14, 17)) == (14,))
        pytest.assume(similar_elements((15, 9, 17, 15), (19, 19, 10, 15)) == (15,))
        pytest.assume(similar_elements((8, 17, 11, 14), (14, 15, 19, 12)) == (14,))
        pytest.assume(similar_elements((13, 11, 9, 11), (20, 13, 14, 15)) == (13,))
        pytest.assume(similar_elements((8, 12, 13, 18), (14, 16, 19, 9)) == ())
        pytest.assume(similar_elements((9, 17, 13, 18), (21, 15, 17, 15)) == (17,))
        pytest.assume(similar_elements((6, 10, 9, 8), (17, 10, 10, 18)) == (10,))
        pytest.assume(similar_elements((14, 11, 17, 13), (17, 18, 12, 15)) == (17,))
        pytest.assume(similar_elements((14, 9, 16, 17), (21, 18, 19, 17)) == (17,))
        pytest.assume(similar_elements((7, 7, 13, 8), (17, 17, 9, 16)) == ())
        pytest.assume(similar_elements((11, 10, 11, 12), (18, 20, 18, 16)) == ())
        pytest.assume(similar_elements((8, 8, 18, 15), (18, 19, 16, 16)) == (18,))
        pytest.assume(similar_elements((6, 10, 15, 18), (12, 13, 11, 16)) == ())
        pytest.assume(similar_elements((13, 12, 15, 14), (17, 17, 11, 14)) == (14,))
        pytest.assume(similar_elements((14, 17, 18, 18), (22, 12, 9, 18)) == (18,))
        pytest.assume(similar_elements((10, 16, 14, 9), (13, 20, 19, 8)) == ())
        pytest.assume(similar_elements((7, 9, 10, 15), (21, 12, 13, 16)) == ())
        pytest.assume(similar_elements((6, 8, 12, 14), (17, 10, 14, 11)) == (14,))
        pytest.assume(similar_elements((7, 10, 10, 12), (21, 17, 18, 17)) == ())
        pytest.assume(similar_elements((12, 12, 13, 18), (14, 17, 16, 15)) == ())
        pytest.assume(similar_elements((13, 7, 17, 11), (18, 20, 9, 10)) == ())
        pytest.assume(similar_elements((10, 11, 14, 13), (16, 19, 9, 13)) == (13,))
        pytest.assume(similar_elements((8, 17, 15, 10), (19, 12, 9, 14)) == ())
        pytest.assume(similar_elements((9, 10, 13, 8), (14, 10, 19, 17)) == (10,))
        pytest.assume(similar_elements((11, 14, 17, 10), (15, 15, 10, 11)) == (10, 11))
    except TypeError as e:
        pytest.fail(f"Test crashed with TypeError: {e}")