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
    glob_pattern="problem_7_*.py", 
    function_name="square_nums"
)

# --- 3. The Test Function (using parametrize) ---

@pytest.mark.parametrize("square_nums", all_min_cost_functions)
def test_square_nums(square_nums):
    """
    This ONE test will run for EVERY function in the 'all_min_cost_functions' list.
    'square_nums' will be the function from iteration 1, then iteration 2, etc.
    """
    
    # If loading failed, min_cost_func might be None
    if square_nums is None:
        pytest.fail("Module loading failed, see console output.")

    try:
        pytest.assume(square_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])==[1, 4, 9, 16, 25, 36, 49, 64, 81, 100])
        pytest.assume(square_nums([10,20,30])==([100,400,900]))
        pytest.assume(square_nums([12,15])==([144,225]))
        pytest.assume(square_nums([3, 5, 7, 8, 4, 11, 10, 13, 14, 11]) == [9, 25, 49, 64, 16, 121, 100, 169, 196, 121])
        pytest.assume(square_nums([2, 3, 4, 2, 1, 8, 2, 3, 5, 11]) == [4, 9, 16, 4, 1, 64, 4, 9, 25, 121])
        pytest.assume(square_nums([2, 3, 6, 3, 7, 9, 3, 11, 12, 7]) == [4, 9, 36, 9, 49, 81, 9, 121, 144, 49])
        pytest.assume(square_nums([5, 2, 8, 6, 5, 9, 4, 11, 7, 7]) == [25, 4, 64, 36, 25, 81, 16, 121, 49, 49])
        pytest.assume(square_nums([6, 1, 2, 9, 9, 7, 6, 10, 5, 9]) == [36, 1, 4, 81, 81, 49, 36, 100, 25, 81])
        pytest.assume(square_nums([1, 6, 8, 8, 9, 2, 5, 12, 6, 12]) == [1, 36, 64, 64, 81, 4, 25, 144, 36, 144])
        pytest.assume(square_nums([2, 2, 6, 2, 6, 4, 11, 6, 12, 5]) == [4, 4, 36, 4, 36, 16, 121, 36, 144, 25])
        pytest.assume(square_nums([1, 4, 7, 7, 10, 9, 12, 5, 4, 14]) == [1, 16, 49, 49, 100, 81, 144, 25, 16, 196])
        pytest.assume(square_nums([4, 3, 2, 8, 9, 2, 5, 3, 12, 11]) == [16, 9, 4, 64, 81, 4, 25, 9, 144, 121])
        pytest.assume(square_nums([1, 6, 4, 2, 2, 1, 6, 11, 8, 10]) == [1, 36, 16, 4, 4, 1, 36, 121, 64, 100])
        pytest.assume(square_nums([3, 1, 4, 6, 10, 1, 12, 12, 11, 8]) == [9, 1, 16, 36, 100, 1, 144, 144, 121, 64])
        pytest.assume(square_nums([6, 6, 6, 9, 7, 7, 4, 12, 9, 13]) == [36, 36, 36, 81, 49, 49, 16, 144, 81, 169])
        pytest.assume(square_nums([6, 2, 1, 3, 10, 2, 6, 12, 9, 9]) == [36, 4, 1, 9, 100, 4, 36, 144, 81, 81])
        pytest.assume(square_nums([1, 2, 6, 8, 5, 5, 10, 10, 14, 11]) == [1, 4, 36, 64, 25, 25, 100, 100, 196, 121])
        pytest.assume(square_nums([5, 1, 2, 6, 6, 7, 8, 6, 6, 14]) == [25, 1, 4, 36, 36, 49, 64, 36, 36, 196])
        pytest.assume(square_nums([3, 2, 3, 6, 5, 6, 3, 12, 4, 15]) == [9, 4, 9, 36, 25, 36, 9, 144, 16, 225])
        pytest.assume(square_nums([4, 5, 2, 9, 8, 2, 9, 10, 5, 14]) == [16, 25, 4, 81, 64, 4, 81, 100, 25, 196])
        pytest.assume(square_nums([2, 1, 5, 8, 6, 1, 4, 9, 4, 9]) == [4, 1, 25, 64, 36, 1, 16, 81, 16, 81])
        pytest.assume(square_nums([4, 2, 2, 1, 4, 4, 4, 10, 7, 7]) == [16, 4, 4, 1, 16, 16, 16, 100, 49, 49])
        pytest.assume(square_nums([6, 3, 2, 7, 6, 11, 10, 8, 14, 8]) == [36, 9, 4, 49, 36, 121, 100, 64, 196, 64])
        pytest.assume(square_nums([4, 6, 7, 5, 3, 10, 12, 9, 7, 9]) == [16, 36, 49, 25, 9, 100, 144, 81, 49, 81])
        pytest.assume(square_nums([3, 1, 7, 4, 6, 9, 3, 3, 4, 8]) == [9, 1, 49, 16, 36, 81, 9, 9, 16, 64])
        pytest.assume(square_nums([6, 4, 8, 9, 8, 6, 8, 5, 14, 11]) == [36, 16, 64, 81, 64, 36, 64, 25, 196, 121])
        pytest.assume(square_nums([2, 6, 2, 1, 8, 1, 5, 6, 4, 7]) == [4, 36, 4, 1, 64, 1, 25, 36, 16, 49])
        pytest.assume(square_nums([1, 2, 5, 1, 8, 8, 5, 9, 6, 15]) == [1, 4, 25, 1, 64, 64, 25, 81, 36, 225])
        pytest.assume(square_nums([1, 5, 4, 7, 2, 3, 10, 4, 14, 13]) == [1, 25, 16, 49, 4, 9, 100, 16, 196, 169])
        pytest.assume(square_nums([6, 4, 1, 6, 2, 1, 7, 7, 14, 15]) == [36, 16, 1, 36, 4, 1, 49, 49, 196, 225])
        pytest.assume(square_nums([6, 5, 3, 2, 6, 11, 7, 3, 7, 5]) == [36, 25, 9, 4, 36, 121, 49, 9, 49, 25])
        pytest.assume(square_nums([6, 2, 4, 6, 2, 9, 11, 4, 10, 12]) == [36, 4, 16, 36, 4, 81, 121, 16, 100, 144])
        pytest.assume(square_nums([3, 2, 8, 2, 3, 9, 9, 8, 4, 13]) == [9, 4, 64, 4, 9, 81, 81, 64, 16, 169])
        pytest.assume(square_nums([6, 3, 7, 1, 5, 8, 9, 4, 12, 6]) == [36, 9, 49, 1, 25, 64, 81, 16, 144, 36])
        pytest.assume(square_nums([4, 6, 4, 5, 9, 8, 3, 4, 5, 13]) == [16, 36, 16, 25, 81, 64, 9, 16, 25, 169])
        pytest.assume(square_nums([4, 7, 3, 9, 4, 5, 9, 8, 8, 5]) == [16, 49, 9, 81, 16, 25, 81, 64, 64, 25])
        pytest.assume(square_nums([14, 17, 27]) == [196, 289, 729])
        pytest.assume(square_nums([6, 16, 32]) == [36, 256, 1024])
        pytest.assume(square_nums([13, 23, 30]) == [169, 529, 900])
        pytest.assume(square_nums([14, 19, 32]) == [196, 361, 1024])
        pytest.assume(square_nums([9, 21, 34]) == [81, 441, 1156])
        pytest.assume(square_nums([6, 22, 26]) == [36, 484, 676])
        pytest.assume(square_nums([12, 21, 27]) == [144, 441, 729])
        pytest.assume(square_nums([13, 20, 28]) == [169, 400, 784])
        pytest.assume(square_nums([12, 23, 26]) == [144, 529, 676])
        pytest.assume(square_nums([8, 16, 32]) == [64, 256, 1024])
        pytest.assume(square_nums([9, 22, 27]) == [81, 484, 729])
        pytest.assume(square_nums([15, 18, 25]) == [225, 324, 625])
        pytest.assume(square_nums([12, 15, 26]) == [144, 225, 676])
        pytest.assume(square_nums([12, 19, 35]) == [144, 361, 1225])
        pytest.assume(square_nums([9, 17, 35]) == [81, 289, 1225])
        pytest.assume(square_nums([7, 18, 27]) == [49, 324, 729])
        pytest.assume(square_nums([12, 16, 29]) == [144, 256, 841])
        pytest.assume(square_nums([6, 17, 34]) == [36, 289, 1156])
        pytest.assume(square_nums([15, 18, 35]) == [225, 324, 1225])
        pytest.assume(square_nums([15, 23, 32]) == [225, 529, 1024])
        pytest.assume(square_nums([10, 25, 29]) == [100, 625, 841])
        pytest.assume(square_nums([8, 18, 29]) == [64, 324, 841])
        pytest.assume(square_nums([11, 18, 26]) == [121, 324, 676])
        pytest.assume(square_nums([14, 17, 32]) == [196, 289, 1024])
        pytest.assume(square_nums([13, 16, 28]) == [169, 256, 784])
        pytest.assume(square_nums([10, 21, 29]) == [100, 441, 841])
        pytest.assume(square_nums([9, 15, 31]) == [81, 225, 961])
        pytest.assume(square_nums([7, 24, 28]) == [49, 576, 784])
        pytest.assume(square_nums([11, 18, 35]) == [121, 324, 1225])
        pytest.assume(square_nums([10, 15, 32]) == [100, 225, 1024])
        pytest.assume(square_nums([10, 21, 30]) == [100, 441, 900])
        pytest.assume(square_nums([6, 17, 29]) == [36, 289, 841])
        pytest.assume(square_nums([5, 20, 28]) == [25, 400, 784])
        pytest.assume(square_nums([12, 17]) == [144, 289])
        pytest.assume(square_nums([16, 13]) == [256, 169])
        pytest.assume(square_nums([16, 12]) == [256, 144])
        pytest.assume(square_nums([9, 18]) == [81, 324])
        pytest.assume(square_nums([10, 19]) == [100, 361])
        pytest.assume(square_nums([8, 12]) == [64, 144])
        pytest.assume(square_nums([13, 19]) == [169, 361])
        pytest.assume(square_nums([10, 11]) == [100, 121])
        pytest.assume(square_nums([7, 18]) == [49, 324])
        pytest.assume(square_nums([7, 20]) == [49, 400])
        pytest.assume(square_nums([17, 18]) == [289, 324])
        pytest.assume(square_nums([10, 19]) == [100, 361])
        pytest.assume(square_nums([16, 10]) == [256, 100])
        pytest.assume(square_nums([15, 15]) == [225, 225])
        pytest.assume(square_nums([10, 10]) == [100, 100])
        pytest.assume(square_nums([11, 16]) == [121, 256])
        pytest.assume(square_nums([15, 17]) == [225, 289])
        pytest.assume(square_nums([11, 20]) == [121, 400])
        pytest.assume(square_nums([17, 14]) == [289, 196])
        pytest.assume(square_nums([16, 10]) == [256, 100])
        pytest.assume(square_nums([7, 20]) == [49, 400])
        pytest.assume(square_nums([8, 17]) == [64, 289])
        pytest.assume(square_nums([13, 10]) == [169, 100])
        pytest.assume(square_nums([13, 17]) == [169, 289])
        pytest.assume(square_nums([14, 18]) == [196, 324])
        pytest.assume(square_nums([15, 20]) == [225, 400])
        pytest.assume(square_nums([16, 14]) == [256, 196])
        pytest.assume(square_nums([10, 13]) == [100, 169])
        pytest.assume(square_nums([16, 13]) == [256, 169])
        pytest.assume(square_nums([10, 13]) == [100, 169])
        pytest.assume(square_nums([12, 17]) == [144, 289])
        pytest.assume(square_nums([9, 15]) == [81, 225])
        pytest.assume(square_nums([8, 13]) == [64, 169])
    except TypeError as e:
        pytest.fail(f"Test crashed with TypeError: {e}")