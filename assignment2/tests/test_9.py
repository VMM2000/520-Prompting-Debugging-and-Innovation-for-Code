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
    glob_pattern="problem_9_*.py", 
    function_name="small_nnum"
)

# --- 3. The Test Function (using parametrize) ---

@pytest.mark.parametrize("small_nnum", all_min_cost_functions)
def test_small_nnum(small_nnum):
    """
    This ONE test will run for EVERY function in the 'all_min_cost_functions' list.
    'small_nnum' will be the function from iteration 1, then iteration 2, etc.
    """
    
    # If loading failed, min_cost_func might be None
    if small_nnum is None:
        pytest.fail("Module loading failed, see console output.")

    try:
        pytest.assume(small_nnum([10, 20, 50, 70, 90, 20, 50, 40, 60, 80, 100],2)==[10,20])
        pytest.assume(small_nnum([10, 20, 50, 70, 90, 20, 50, 40, 60, 80, 100],5)==[10,20,20,40,50])
        pytest.assume(small_nnum([10, 20, 50, 70, 90, 20, 50, 40, 60, 80, 100],3)==[10,20,20])
        pytest.assume(small_nnum([14, 15, 49, 71, 85, 18, 49, 37, 62, 76, 104], 2) == [14, 15])
        pytest.assume(small_nnum([7, 21, 54, 71, 88, 21, 51, 43, 63, 80, 95], 4) == [7, 21, 21, 43])
        pytest.assume(small_nnum([14, 17, 49, 75, 92, 22, 49, 40, 55, 84, 104], 2) == [14, 17])
        pytest.assume(small_nnum([15, 24, 55, 66, 95, 21, 55, 40, 59, 80, 97], 6) == [15, 21, 24, 40, 55, 55])
        pytest.assume(small_nnum([14, 20, 51, 68, 87, 22, 55, 40, 63, 76, 95], 5) == [14, 20, 22, 40, 51])
        pytest.assume(small_nnum([13, 21, 55, 73, 95, 15, 50, 43, 62, 76, 103], 4) == [13, 15, 21, 43])
        pytest.assume(small_nnum([14, 25, 53, 66, 88, 17, 55, 43, 56, 76, 104], 6) == [14, 17, 25, 43, 53, 55])
        pytest.assume(small_nnum([8, 18, 52, 69, 94, 17, 48, 42, 63, 85, 98], 7) == [8, 17, 18, 42, 48, 52, 63])
        pytest.assume(small_nnum([11, 19, 52, 71, 90, 16, 53, 44, 57, 85, 105], 6) == [11, 16, 19, 44, 52, 53])
        pytest.assume(small_nnum([9, 20, 51, 68, 87, 21, 52, 44, 56, 85, 100], 6) == [9, 20, 21, 44, 51, 52])
        pytest.assume(small_nnum([12, 20, 50, 66, 86, 22, 45, 41, 61, 79, 100], 7) == [12, 20, 22, 41, 45, 50, 61])
        pytest.assume(small_nnum([6, 19, 48, 68, 89, 15, 53, 40, 57, 83, 105], 4) == [6, 15, 19, 40])
        pytest.assume(small_nnum([6, 23, 48, 71, 95, 17, 52, 41, 62, 77, 102], 1) == [6])
        pytest.assume(small_nnum([13, 21, 51, 72, 88, 20, 50, 44, 64, 81, 100], 3) == [13, 20, 21])
        pytest.assume(small_nnum([5, 23, 48, 67, 87, 18, 55, 39, 60, 85, 98], 7) == [5, 18, 23, 39, 48, 55, 60])
        pytest.assume(small_nnum([9, 24, 48, 73, 86, 19, 45, 38, 62, 79, 102], 7) == [9, 19, 24, 38, 45, 48, 62])
        pytest.assume(small_nnum([13, 15, 50, 72, 93, 20, 52, 40, 64, 75, 96], 4) == [13, 15, 20, 40])
        pytest.assume(small_nnum([6, 25, 50, 75, 85, 17, 46, 42, 63, 84, 95], 2) == [6, 17])
        pytest.assume(small_nnum([9, 23, 52, 71, 91, 17, 55, 40, 57, 79, 95], 2) == [9, 17])
        pytest.assume(small_nnum([14, 25, 52, 71, 87, 24, 55, 45, 56, 75, 101], 6) == [14, 24, 25, 45, 52, 55])
        pytest.assume(small_nnum([13, 25, 53, 68, 95, 22, 45, 39, 58, 75, 95], 7) == [13, 22, 25, 39, 45, 53, 58])
        pytest.assume(small_nnum([8, 19, 49, 67, 90, 23, 54, 37, 62, 79, 103], 7) == [8, 19, 23, 37, 49, 54, 62])
        pytest.assume(small_nnum([14, 15, 55, 69, 90, 23, 47, 35, 61, 77, 101], 6) == [14, 15, 23, 35, 47, 55])
        pytest.assume(small_nnum([8, 18, 45, 70, 90, 16, 45, 42, 60, 82, 96], 4) == [8, 16, 18, 42])
        pytest.assume(small_nnum([13, 19, 50, 67, 93, 21, 52, 43, 59, 81, 100], 2) == [13, 19])
        pytest.assume(small_nnum([14, 20, 48, 74, 86, 19, 45, 40, 56, 85, 95], 2) == [14, 19])
        pytest.assume(small_nnum([9, 17, 46, 73, 86, 21, 49, 40, 55, 76, 98], 2) == [9, 17])
        pytest.assume(small_nnum([8, 24, 52, 71, 85, 23, 51, 37, 65, 78, 95], 7) == [8, 23, 24, 37, 51, 52, 65])
        pytest.assume(small_nnum([13, 18, 54, 66, 90, 16, 45, 43, 55, 78, 105], 1) == [13])
        pytest.assume(small_nnum([12, 21, 50, 73, 90, 24, 45, 44, 55, 83, 95], 6) == [12, 21, 24, 44, 45, 50])
        pytest.assume(small_nnum([8, 20, 45, 67, 89, 20, 52, 39, 56, 76, 105], 4) == [8, 20, 20, 39])
        pytest.assume(small_nnum([12, 20, 46, 74, 93, 16, 51, 41, 61, 79, 97], 6) == [12, 16, 20, 41, 46, 51])
        pytest.assume(small_nnum([12, 25, 53, 75, 91, 21, 47, 40, 63, 77, 104], 1) == [12])
        pytest.assume(small_nnum([7, 22, 46, 74, 92, 25, 49, 40, 61, 79, 102], 3) == [7, 22, 25])
        pytest.assume(small_nnum([15, 20, 51, 65, 91, 19, 51, 38, 62, 76, 96], 3) == [15, 19, 20])
        pytest.assume(small_nnum([11, 16, 55, 68, 92, 22, 45, 45, 55, 82, 98], 6) == [11, 16, 22, 45, 45, 55])
        pytest.assume(small_nnum([6, 15, 48, 74, 89, 18, 55, 39, 55, 78, 99], 9) == [6, 15, 18, 39, 48, 55, 55, 74, 78])
        pytest.assume(small_nnum([8, 21, 53, 66, 95, 17, 55, 40, 55, 82, 104], 8) == [8, 17, 21, 40, 53, 55, 55, 66])
        pytest.assume(small_nnum([10, 25, 53, 73, 85, 19, 47, 43, 59, 81, 102], 8) == [10, 19, 25, 43, 47, 53, 59, 73])
        pytest.assume(small_nnum([5, 25, 46, 71, 88, 23, 45, 40, 59, 82, 101], 6) == [5, 23, 25, 40, 45, 46])
        pytest.assume(small_nnum([7, 25, 51, 74, 91, 22, 48, 39, 62, 78, 95], 1) == [7])
        pytest.assume(small_nnum([10, 16, 55, 70, 95, 22, 47, 45, 56, 76, 104], 6) == [10, 16, 22, 45, 47, 55])
        pytest.assume(small_nnum([14, 17, 55, 67, 91, 23, 47, 37, 60, 77, 101], 10) == [14, 17, 23, 37, 47, 55, 60, 67, 77, 91])
        pytest.assume(small_nnum([14, 24, 48, 65, 85, 15, 50, 38, 63, 83, 102], 6) == [14, 15, 24, 38, 48, 50])
        pytest.assume(small_nnum([5, 25, 50, 68, 94, 15, 50, 39, 64, 80, 99], 8) == [5, 15, 25, 39, 50, 50, 64, 68])
        pytest.assume(small_nnum([9, 15, 47, 75, 93, 25, 46, 37, 56, 78, 100], 10) == [9, 15, 25, 37, 46, 47, 56, 75, 78, 93])
        pytest.assume(small_nnum([5, 22, 47, 66, 86, 18, 49, 38, 57, 83, 97], 4) == [5, 18, 22, 38])
        pytest.assume(small_nnum([8, 25, 46, 75, 91, 22, 54, 40, 55, 78, 97], 8) == [8, 22, 25, 40, 46, 54, 55, 75])
        pytest.assume(small_nnum([10, 24, 50, 69, 92, 20, 50, 42, 56, 75, 96], 4) == [10, 20, 24, 42])
        pytest.assume(small_nnum([8, 19, 53, 74, 87, 22, 49, 45, 62, 76, 101], 6) == [8, 19, 22, 45, 49, 53])
        pytest.assume(small_nnum([6, 16, 47, 74, 86, 20, 48, 38, 64, 84, 99], 7) == [6, 16, 20, 38, 47, 48, 64])
        pytest.assume(small_nnum([7, 22, 46, 70, 91, 15, 52, 44, 61, 85, 95], 5) == [7, 15, 22, 44, 46])
        pytest.assume(small_nnum([10, 18, 52, 65, 87, 17, 48, 37, 60, 85, 101], 10) == [10, 17, 18, 37, 48, 52, 60, 65, 85, 87])
        pytest.assume(small_nnum([13, 17, 49, 70, 88, 15, 53, 40, 60, 79, 95], 7) == [13, 15, 17, 40, 49, 53, 60])
        pytest.assume(small_nnum([11, 22, 47, 66, 90, 24, 54, 38, 57, 75, 97], 3) == [11, 22, 24])
        pytest.assume(small_nnum([5, 15, 48, 74, 93, 17, 48, 45, 55, 83, 95], 10) == [5, 15, 17, 45, 48, 48, 55, 74, 83, 93])
        pytest.assume(small_nnum([9, 17, 54, 68, 95, 22, 51, 44, 58, 82, 98], 6) == [9, 17, 22, 44, 51, 54])
        pytest.assume(small_nnum([10, 18, 54, 69, 87, 19, 47, 35, 63, 80, 104], 6) == [10, 18, 19, 35, 47, 54])
        pytest.assume(small_nnum([11, 22, 50, 69, 85, 21, 49, 38, 58, 75, 100], 8) == [11, 21, 22, 38, 49, 50, 58, 69])
        pytest.assume(small_nnum([15, 23, 53, 71, 91, 20, 46, 36, 61, 83, 105], 7) == [15, 20, 23, 36, 46, 53, 61])
        pytest.assume(small_nnum([9, 17, 54, 73, 89, 16, 46, 38, 55, 83, 102], 4) == [9, 16, 17, 38])
        pytest.assume(small_nnum([10, 15, 53, 68, 91, 19, 54, 37, 63, 78, 105], 7) == [10, 15, 19, 37, 53, 54, 63])
        pytest.assume(small_nnum([15, 21, 46, 68, 92, 22, 53, 35, 64, 76, 99], 5) == [15, 21, 22, 35, 46])
        pytest.assume(small_nnum([7, 16, 48, 74, 94, 15, 52, 40, 56, 79, 104], 3) == [7, 15, 16])
        pytest.assume(small_nnum([7, 25, 48, 73, 94, 16, 53, 37, 65, 76, 98], 7) == [7, 16, 25, 37, 48, 53, 65])
        pytest.assume(small_nnum([11, 24, 51, 66, 93, 25, 47, 39, 58, 85, 102], 2) == [11, 24])
        pytest.assume(small_nnum([6, 20, 54, 70, 89, 18, 53, 38, 64, 80, 104], 1) == [6])
        pytest.assume(small_nnum([5, 16, 46, 71, 92, 15, 54, 39, 62, 84, 101], 6) == [5, 15, 16, 39, 46, 54])
        pytest.assume(small_nnum([12, 20, 46, 69, 88, 22, 49, 45, 65, 75, 96], 8) == [12, 20, 22, 45, 46, 49, 65, 69])
        pytest.assume(small_nnum([13, 22, 47, 67, 91, 25, 52, 37, 61, 80, 99], 5) == [13, 22, 25, 37, 47])
        pytest.assume(small_nnum([13, 18, 46, 70, 92, 19, 55, 43, 62, 84, 103], 3) == [13, 18, 19])
        pytest.assume(small_nnum([11, 24, 47, 67, 89, 20, 48, 36, 61, 85, 99], 4) == [11, 20, 24, 36])
        pytest.assume(small_nnum([14, 15, 55, 66, 89, 18, 54, 44, 55, 80, 105], 8) == [14, 15, 18, 44, 54, 55, 55, 66])
        pytest.assume(small_nnum([14, 15, 45, 66, 85, 20, 45, 39, 56, 82, 102], 4) == [14, 15, 20, 39])
        pytest.assume(small_nnum([11, 16, 51, 71, 92, 24, 50, 42, 63, 84, 102], 6) == [11, 16, 24, 42, 50, 51])
        pytest.assume(small_nnum([14, 16, 49, 73, 94, 19, 49, 41, 55, 79, 95], 4) == [14, 16, 19, 41])
        pytest.assume(small_nnum([6, 25, 45, 75, 92, 24, 45, 37, 55, 79, 103], 5) == [6, 24, 25, 37, 45])
        pytest.assume(small_nnum([9, 21, 55, 68, 94, 25, 50, 37, 56, 75, 97], 3) == [9, 21, 25])
        pytest.assume(small_nnum([14, 24, 47, 75, 92, 24, 46, 35, 55, 78, 104], 4) == [14, 24, 24, 35])
        pytest.assume(small_nnum([14, 15, 52, 65, 89, 22, 47, 36, 59, 80, 98], 1) == [14])
        pytest.assume(small_nnum([10, 25, 47, 75, 87, 21, 45, 41, 65, 84, 105], 7) == [10, 21, 25, 41, 45, 47, 65])
        pytest.assume(small_nnum([14, 16, 50, 71, 89, 16, 47, 40, 64, 85, 102], 6) == [14, 16, 16, 40, 47, 50])
        pytest.assume(small_nnum([8, 24, 48, 69, 90, 15, 53, 38, 63, 80, 100], 7) == [8, 15, 24, 38, 48, 53, 63])
        pytest.assume(small_nnum([5, 21, 51, 72, 87, 16, 47, 37, 60, 83, 103], 3) == [5, 16, 21])
        pytest.assume(small_nnum([13, 25, 53, 68, 94, 18, 50, 35, 62, 85, 100], 6) == [13, 18, 25, 35, 50, 53])
        pytest.assume(small_nnum([11, 19, 46, 74, 87, 16, 54, 45, 58, 79, 98], 4) == [11, 16, 19, 45])
        pytest.assume(small_nnum([6, 15, 45, 71, 93, 22, 45, 45, 63, 82, 97], 7) == [6, 15, 22, 45, 45, 45, 63])
        pytest.assume(small_nnum([15, 17, 48, 75, 86, 21, 49, 37, 62, 83, 104], 2) == [15, 17])
        pytest.assume(small_nnum([11, 17, 53, 75, 92, 22, 51, 35, 62, 82, 102], 5) == [11, 17, 22, 35, 51])
        pytest.assume(small_nnum([9, 25, 49, 72, 86, 18, 45, 35, 61, 81, 104], 7) == [9, 18, 25, 35, 45, 49, 61])
        pytest.assume(small_nnum([7, 16, 54, 69, 87, 23, 50, 42, 59, 80, 97], 8) == [7, 16, 23, 42, 50, 54, 59, 69])
        pytest.assume(small_nnum([7, 22, 50, 67, 91, 17, 49, 45, 55, 76, 102], 3) == [7, 17, 22])
        pytest.assume(small_nnum([7, 19, 52, 65, 90, 21, 52, 38, 61, 76, 97], 8) == [7, 19, 21, 38, 52, 52, 61, 65])
        pytest.assume(small_nnum([15, 18, 54, 73, 89, 19, 55, 35, 65, 80, 98], 8) == [15, 18, 19, 35, 54, 55, 65, 73])
        pytest.assume(small_nnum([11, 20, 52, 75, 92, 18, 48, 37, 65, 79, 98], 4) == [11, 18, 20, 37])
        pytest.assume(small_nnum([10, 19, 48, 65, 87, 15, 50, 38, 58, 78, 102], 7) == [10, 15, 19, 38, 48, 50, 58])
        pytest.assume(small_nnum([11, 19, 50, 73, 87, 17, 46, 43, 58, 84, 105], 8) == [11, 17, 19, 43, 46, 50, 58, 73])
        pytest.assume(small_nnum([6, 15, 55, 75, 95, 24, 52, 40, 63, 75, 101], 1) == [6])
        pytest.assume(small_nnum([14, 24, 50, 72, 89, 22, 51, 44, 64, 84, 98], 4) == [14, 22, 24, 44])
    except TypeError as e:
        pytest.fail(f"Test crashed with TypeError: {e}")