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
    glob_pattern="problem_3_*.py", 
    function_name="heap_queue_largest"
)

# --- 3. The Test Function (using parametrize) ---

@pytest.mark.parametrize("heap_queue_largest", all_min_cost_functions)
def test_heap_queue_largest(heap_queue_largest):
    """
    This ONE test will run for EVERY function in the 'all_min_cost_functions' list.
    'heap_queue_largest' will be the function from iteration 1, then iteration 2, etc.
    """
    
    # If loading failed, min_cost_func might be None
    if heap_queue_largest is None:
        pytest.fail("Module loading failed, see console output.")

    try:
        pytest.assume(heap_queue_largest( [25, 35, 22, 85, 14, 65, 75, 22, 58],3)==[85, 75, 65])
        pytest.assume(heap_queue_largest( [25, 35, 22, 85, 14, 65, 75, 22, 58],2)==[85, 75])
        pytest.assume(heap_queue_largest( [25, 35, 22, 85, 14, 65, 75, 22, 58],5)==[85, 75, 65, 58, 35])
        pytest.assume(heap_queue_largest([29, 39, 20, 87, 19, 64, 72, 27, 61], 4) == [87, 72, 64, 61])
        pytest.assume(heap_queue_largest([23, 39, 18, 83, 14, 65, 71, 20, 62], 1) == [83])
        pytest.assume(heap_queue_largest([28, 34, 25, 89, 12, 66, 77, 27, 56], 5) == [89, 77, 66, 56, 34])
        pytest.assume(heap_queue_largest([21, 36, 22, 84, 13, 67, 78, 25, 54], 3) == [84, 78, 67])
        pytest.assume(heap_queue_largest([28, 38, 20, 85, 11, 68, 72, 18, 59], 6) == [85, 72, 68, 59, 38, 28])
        pytest.assume(heap_queue_largest([26, 30, 20, 81, 9, 61, 73, 19, 53], 6) == [81, 73, 61, 53, 30, 26])
        pytest.assume(heap_queue_largest([25, 32, 23, 86, 14, 60, 73, 23, 54], 6) == [86, 73, 60, 54, 32, 25])
        pytest.assume(heap_queue_largest([22, 33, 22, 80, 19, 64, 77, 24, 53], 3) == [80, 77, 64])
        pytest.assume(heap_queue_largest([28, 39, 25, 84, 17, 61, 77, 19, 53], 5) == [84, 77, 61, 53, 39])
        pytest.assume(heap_queue_largest([30, 38, 17, 89, 18, 62, 80, 23, 60], 7) == [89, 80, 62, 60, 38, 30, 23])
        pytest.assume(heap_queue_largest([27, 40, 27, 86, 16, 66, 79, 24, 59], 7) == [86, 79, 66, 59, 40, 27, 27])
        pytest.assume(heap_queue_largest([30, 36, 27, 81, 19, 66, 78, 23, 59], 8) == [81, 78, 66, 59, 36, 30, 27, 23])
        pytest.assume(heap_queue_largest([23, 37, 20, 83, 18, 61, 75, 21, 55], 8) == [83, 75, 61, 55, 37, 23, 21, 20])
        pytest.assume(heap_queue_largest([29, 36, 17, 83, 13, 65, 78, 23, 59], 5) == [83, 78, 65, 59, 36])
        pytest.assume(heap_queue_largest([27, 31, 23, 85, 10, 67, 77, 21, 57], 5) == [85, 77, 67, 57, 31])
        pytest.assume(heap_queue_largest([25, 39, 22, 83, 15, 68, 75, 25, 53], 3) == [83, 75, 68])
        pytest.assume(heap_queue_largest([30, 37, 22, 85, 11, 68, 77, 19, 62], 8) == [85, 77, 68, 62, 37, 30, 22, 19])
        pytest.assume(heap_queue_largest([22, 31, 24, 89, 9, 63, 70, 27, 57], 5) == [89, 70, 63, 57, 31])
        pytest.assume(heap_queue_largest([24, 40, 26, 88, 16, 68, 79, 20, 63], 4) == [88, 79, 68, 63])
        pytest.assume(heap_queue_largest([22, 40, 23, 89, 15, 65, 74, 20, 62], 5) == [89, 74, 65, 62, 40])
        pytest.assume(heap_queue_largest([23, 31, 21, 90, 14, 63, 78, 22, 59], 2) == [90, 78])
        pytest.assume(heap_queue_largest([23, 30, 20, 85, 19, 69, 73, 18, 55], 8) == [85, 73, 69, 55, 30, 23, 20, 19])
        pytest.assume(heap_queue_largest([20, 37, 21, 81, 11, 64, 79, 17, 59], 3) == [81, 79, 64])
        pytest.assume(heap_queue_largest([25, 40, 21, 84, 11, 68, 71, 27, 56], 4) == [84, 71, 68, 56])
        pytest.assume(heap_queue_largest([25, 31, 19, 90, 15, 64, 79, 26, 57], 1) == [90])
        pytest.assume(heap_queue_largest([21, 31, 17, 80, 19, 69, 77, 27, 63], 1) == [80])
        pytest.assume(heap_queue_largest([30, 36, 20, 87, 12, 69, 80, 27, 60], 4) == [87, 80, 69, 60])
        pytest.assume(heap_queue_largest([28, 30, 22, 80, 12, 60, 70, 27, 58], 7) == [80, 70, 60, 58, 30, 28, 27])
        pytest.assume(heap_queue_largest([30, 30, 26, 87, 12, 66, 78, 19, 55], 4) == [87, 78, 66, 55])
        pytest.assume(heap_queue_largest([26, 39, 21, 82, 12, 60, 78, 24, 57], 7) == [82, 78, 60, 57, 39, 26, 24])
        pytest.assume(heap_queue_largest([24, 34, 23, 87, 14, 61, 70, 19, 55], 7) == [87, 70, 61, 55, 34, 24, 23])
        pytest.assume(heap_queue_largest([30, 35, 21, 86, 14, 63, 76, 21, 54], 7) == [86, 76, 63, 54, 35, 30, 21])
        pytest.assume(heap_queue_largest([29, 30, 25, 80, 15, 66, 72, 21, 63], 3) == [80, 72, 66])
        pytest.assume(heap_queue_largest([23, 32, 23, 88, 12, 65, 70, 26, 60], 3) == [88, 70, 65])
        pytest.assume(heap_queue_largest([29, 37, 19, 85, 11, 67, 73, 23, 62], 3) == [85, 73, 67])
        pytest.assume(heap_queue_largest([28, 38, 22, 88, 19, 68, 70, 18, 61], 2) == [88, 70])
        pytest.assume(heap_queue_largest([30, 32, 25, 89, 11, 67, 74, 25, 54], 7) == [89, 74, 67, 54, 32, 30, 25])
        pytest.assume(heap_queue_largest([23, 35, 24, 89, 15, 69, 70, 24, 60], 2) == [89, 70])
        pytest.assume(heap_queue_largest([21, 36, 24, 84, 10, 61, 71, 24, 63], 7) == [84, 71, 63, 61, 36, 24, 24])
        pytest.assume(heap_queue_largest([23, 39, 27, 84, 13, 67, 71, 20, 62], 1) == [84])
        pytest.assume(heap_queue_largest([21, 36, 27, 85, 10, 65, 79, 21, 54], 2) == [85, 79])
        pytest.assume(heap_queue_largest([23, 40, 19, 84, 16, 68, 80, 27, 63], 3) == [84, 80, 68])
        pytest.assume(heap_queue_largest([22, 40, 17, 80, 11, 60, 76, 19, 53], 6) == [80, 76, 60, 53, 40, 22])
        pytest.assume(heap_queue_largest([30, 40, 19, 87, 17, 70, 77, 24, 55], 1) == [87])
        pytest.assume(heap_queue_largest([30, 36, 19, 87, 12, 62, 74, 17, 62], 1) == [87])
        pytest.assume(heap_queue_largest([26, 33, 21, 86, 13, 64, 74, 19, 58], 4) == [86, 74, 64, 58])
        pytest.assume(heap_queue_largest([29, 33, 22, 90, 11, 69, 76, 25, 54], 5) == [90, 76, 69, 54, 33])
        pytest.assume(heap_queue_largest([26, 37, 23, 83, 11, 63, 70, 22, 53], 3) == [83, 70, 63])
        pytest.assume(heap_queue_largest([23, 30, 20, 87, 18, 62, 72, 19, 62], 1) == [87])
        pytest.assume(heap_queue_largest([28, 38, 25, 87, 18, 62, 78, 24, 63], 5) == [87, 78, 63, 62, 38])
        pytest.assume(heap_queue_largest([23, 40, 27, 82, 9, 66, 80, 23, 55], 1) == [82])
        pytest.assume(heap_queue_largest([23, 40, 18, 83, 13, 61, 75, 24, 55], 5) == [83, 75, 61, 55, 40])
        pytest.assume(heap_queue_largest([28, 39, 26, 81, 15, 67, 80, 27, 60], 7) == [81, 80, 67, 60, 39, 28, 27])
        pytest.assume(heap_queue_largest([22, 40, 23, 86, 15, 70, 78, 27, 63], 1) == [86])
        pytest.assume(heap_queue_largest([24, 40, 18, 84, 19, 61, 71, 25, 62], 2) == [84, 71])
        pytest.assume(heap_queue_largest([21, 30, 20, 87, 19, 61, 71, 26, 53], 7) == [87, 71, 61, 53, 30, 26, 21])
        pytest.assume(heap_queue_largest([30, 40, 20, 90, 9, 70, 77, 21, 62], 2) == [90, 77])
        pytest.assume(heap_queue_largest([22, 33, 18, 81, 12, 67, 71, 25, 58], 6) == [81, 71, 67, 58, 33, 25])
        pytest.assume(heap_queue_largest([21, 36, 24, 86, 13, 66, 79, 21, 56], 2) == [86, 79])
        pytest.assume(heap_queue_largest([30, 34, 17, 85, 9, 60, 74, 25, 63], 4) == [85, 74, 63, 60])
        pytest.assume(heap_queue_largest([29, 37, 22, 90, 19, 67, 72, 19, 60], 7) == [90, 72, 67, 60, 37, 29, 22])
        pytest.assume(heap_queue_largest([25, 36, 21, 86, 12, 66, 78, 26, 54], 1) == [86])
        pytest.assume(heap_queue_largest([24, 33, 27, 82, 10, 60, 76, 26, 55], 2) == [82, 76])
        pytest.assume(heap_queue_largest([27, 34, 23, 83, 18, 65, 80, 25, 58], 6) == [83, 80, 65, 58, 34, 27])
        pytest.assume(heap_queue_largest([23, 40, 19, 85, 11, 62, 73, 25, 53], 4) == [85, 73, 62, 53])
        pytest.assume(heap_queue_largest([20, 32, 17, 89, 10, 62, 77, 21, 53], 7) == [89, 77, 62, 53, 32, 21, 20])
        pytest.assume(heap_queue_largest([23, 31, 17, 80, 13, 64, 72, 17, 55], 2) == [80, 72])
        pytest.assume(heap_queue_largest([25, 40, 17, 83, 11, 69, 77, 26, 61], 3) == [83, 77, 69])
        pytest.assume(heap_queue_largest([22, 39, 17, 89, 16, 65, 70, 23, 60], 6) == [89, 70, 65, 60, 39, 23])
        pytest.assume(heap_queue_largest([30, 40, 20, 80, 12, 69, 75, 27, 58], 7) == [80, 75, 69, 58, 40, 30, 27])
        pytest.assume(heap_queue_largest([23, 33, 19, 90, 13, 67, 70, 17, 59], 1) == [90])
        pytest.assume(heap_queue_largest([29, 38, 27, 86, 15, 63, 80, 23, 63], 9) == [86, 80, 63, 63, 38, 29, 27, 23, 15])
        pytest.assume(heap_queue_largest([30, 38, 24, 84, 13, 68, 75, 23, 61], 3) == [84, 75, 68])
        pytest.assume(heap_queue_largest([22, 35, 18, 84, 12, 70, 76, 19, 60], 2) == [84, 76])
        pytest.assume(heap_queue_largest([20, 35, 20, 86, 14, 63, 80, 22, 56], 4) == [86, 80, 63, 56])
        pytest.assume(heap_queue_largest([29, 32, 18, 87, 15, 65, 70, 26, 59], 9) == [87, 70, 65, 59, 32, 29, 26, 18, 15])
        pytest.assume(heap_queue_largest([30, 40, 24, 81, 10, 64, 71, 23, 55], 8) == [81, 71, 64, 55, 40, 30, 24, 23])
        pytest.assume(heap_queue_largest([29, 33, 20, 87, 10, 61, 80, 21, 57], 10) == [87, 80, 61, 57, 33, 29, 21, 20, 10])
        pytest.assume(heap_queue_largest([28, 31, 27, 88, 9, 70, 79, 25, 59], 8) == [88, 79, 70, 59, 31, 28, 27, 25])
        pytest.assume(heap_queue_largest([29, 39, 20, 84, 15, 65, 72, 21, 63], 5) == [84, 72, 65, 63, 39])
        pytest.assume(heap_queue_largest([20, 37, 17, 86, 13, 67, 80, 24, 63], 5) == [86, 80, 67, 63, 37])
        pytest.assume(heap_queue_largest([21, 37, 17, 83, 18, 65, 74, 20, 61], 4) == [83, 74, 65, 61])
        pytest.assume(heap_queue_largest([30, 38, 26, 82, 10, 67, 79, 25, 55], 10) == [82, 79, 67, 55, 38, 30, 26, 25, 10])
        pytest.assume(heap_queue_largest([24, 39, 24, 83, 11, 62, 71, 17, 59], 9) == [83, 71, 62, 59, 39, 24, 24, 17, 11])
        pytest.assume(heap_queue_largest([28, 30, 20, 80, 17, 66, 78, 25, 62], 10) == [80, 78, 66, 62, 30, 28, 25, 20, 17])
        pytest.assume(heap_queue_largest([24, 40, 26, 89, 17, 62, 70, 24, 61], 5) == [89, 70, 62, 61, 40])
        pytest.assume(heap_queue_largest([20, 34, 26, 87, 18, 68, 76, 21, 61], 10) == [87, 76, 68, 61, 34, 26, 21, 20, 18])
        pytest.assume(heap_queue_largest([26, 31, 19, 80, 19, 70, 78, 21, 58], 4) == [80, 78, 70, 58])
        pytest.assume(heap_queue_largest([29, 30, 18, 82, 16, 67, 73, 22, 53], 1) == [82])
        pytest.assume(heap_queue_largest([30, 37, 20, 83, 19, 69, 77, 19, 60], 5) == [83, 77, 69, 60, 37])
        pytest.assume(heap_queue_largest([29, 31, 17, 81, 13, 67, 77, 21, 62], 4) == [81, 77, 67, 62])
        pytest.assume(heap_queue_largest([30, 32, 20, 89, 11, 62, 78, 27, 54], 1) == [89])
        pytest.assume(heap_queue_largest([25, 35, 17, 89, 15, 67, 71, 22, 56], 8) == [89, 71, 67, 56, 35, 25, 22, 17])
        pytest.assume(heap_queue_largest([27, 33, 24, 88, 19, 62, 73, 25, 61], 7) == [88, 73, 62, 61, 33, 27, 25])
        pytest.assume(heap_queue_largest([30, 38, 25, 89, 11, 68, 72, 21, 56], 9) == [89, 72, 68, 56, 38, 30, 25, 21, 11])
        pytest.assume(heap_queue_largest([20, 36, 17, 82, 15, 61, 78, 17, 55], 4) == [82, 78, 61, 55])
        pytest.assume(heap_queue_largest([27, 33, 23, 85, 11, 62, 73, 26, 61], 7) == [85, 73, 62, 61, 33, 27, 26])
        pytest.assume(heap_queue_largest([26, 40, 22, 84, 16, 65, 77, 17, 57], 8) == [84, 77, 65, 57, 40, 26, 22, 17])
        pytest.assume(heap_queue_largest([23, 33, 24, 84, 17, 70, 79, 21, 53], 5) == [84, 79, 70, 53, 33])
    except TypeError as e:
        pytest.fail(f"Test crashed with TypeError: {e}")