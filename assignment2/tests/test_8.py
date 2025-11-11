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
    glob_pattern="problem_8_*.py", 
    function_name="find_Rotations"
)

# --- 3. The Test Function (using parametrize) ---

@pytest.mark.parametrize("find_Rotations", all_min_cost_functions)
def test_find_Rotations(find_Rotations):
    """
    This ONE test will run for EVERY function in the 'all_min_cost_functions' list.
    'find_Rotations' will be the function from iteration 1, then iteration 2, etc.
    """
    
    # If loading failed, min_cost_func might be None
    if find_Rotations is None:
        pytest.fail("Module loading failed, see console output.")

    try:
        pytest.assume(find_Rotations("aaaa") == 1)
        pytest.assume(find_Rotations("ab") == 2)
        pytest.assume(find_Rotations("abc") == 3)
        pytest.assume(find_Rotations("kcwa") == 4)
        pytest.assume(find_Rotations("ezxpedrz") == 8)
        pytest.assume(find_Rotations("fgluxhtza") == 9)
        pytest.assume(find_Rotations("mjoaexpfz") == 9)
        pytest.assume(find_Rotations("linyxx") == 6)
        pytest.assume(find_Rotations("pay") == 3)
        pytest.assume(find_Rotations("rxmc") == 4)
        pytest.assume(find_Rotations("qkkjahy") == 7)
        pytest.assume(find_Rotations("slcswzxu") == 8)
        pytest.assume(find_Rotations("zoiy") == 4)
        pytest.assume(find_Rotations("rhjaux") == 6)
        pytest.assume(find_Rotations("fkjfimi") == 7)
        pytest.assume(find_Rotations("pbkflfnd") == 8)
        pytest.assume(find_Rotations("rthqixv") == 7)
        pytest.assume(find_Rotations("rej") == 3)
        pytest.assume(find_Rotations("ifhbywu") == 7)
        pytest.assume(find_Rotations("oost") == 4)
        pytest.assume(find_Rotations("nxwjjwsas") == 9)
        pytest.assume(find_Rotations("moockefg") == 8)
        pytest.assume(find_Rotations("qqydevz") == 7)
        pytest.assume(find_Rotations("wwivmp") == 6)
        pytest.assume(find_Rotations("togvvenfp") == 9)
        pytest.assume(find_Rotations("oolvpej") == 7)
        pytest.assume(find_Rotations("tzegpv") == 6)
        pytest.assume(find_Rotations("beahzutke") == 9)
        pytest.assume(find_Rotations("xzwepkip") == 8)
        pytest.assume(find_Rotations("sis") == 3)
        pytest.assume(find_Rotations("qtbflguk") == 8)
        pytest.assume(find_Rotations("jam") == 3)
        pytest.assume(find_Rotations("gqbzuvv") == 7)
        pytest.assume(find_Rotations("abvgipdym") == 9)
        pytest.assume(find_Rotations("ttff") == 4)
        pytest.assume(find_Rotations("jjeu") == 4)
        pytest.assume(find_Rotations("rphw") == 4)
        pytest.assume(find_Rotations("nbgwgz") == 6)
        pytest.assume(find_Rotations("setbdn") == 6)
        pytest.assume(find_Rotations("pscwbl") == 6)
        pytest.assume(find_Rotations("flgboo") == 6)
        pytest.assume(find_Rotations("bfxpdk") == 6)
        pytest.assume(find_Rotations("mofei") == 5)
        pytest.assume(find_Rotations("qyr") == 3)
        pytest.assume(find_Rotations("uxk") == 3)
        pytest.assume(find_Rotations("nbmy") == 4)
        pytest.assume(find_Rotations("ege") == 3)
        pytest.assume(find_Rotations("usoriq") == 6)
        pytest.assume(find_Rotations("wjuwlt") == 6)
        pytest.assume(find_Rotations("bnodui") == 6)
        pytest.assume(find_Rotations("aevvqf") == 6)
        pytest.assume(find_Rotations("iaktug") == 6)
        pytest.assume(find_Rotations("vhufs") == 5)
        pytest.assume(find_Rotations("hiat") == 4)
        pytest.assume(find_Rotations("mzaym") == 5)
        pytest.assume(find_Rotations("xnlqu") == 5)
        pytest.assume(find_Rotations("zqdb") == 4)
        pytest.assume(find_Rotations("flq") == 3)
        pytest.assume(find_Rotations("oar") == 3)
        pytest.assume(find_Rotations("fezfrb") == 6)
        pytest.assume(find_Rotations("ipszr") == 5)
        pytest.assume(find_Rotations("edyr") == 4)
        pytest.assume(find_Rotations("nve") == 3)
        pytest.assume(find_Rotations("yti") == 3)
        pytest.assume(find_Rotations("bmfvr") == 5)
        pytest.assume(find_Rotations("psafv") == 5)
        pytest.assume(find_Rotations("zlhtd") == 5)
        pytest.assume(find_Rotations("pacp") == 4)
        pytest.assume(find_Rotations("qhgsk") == 5)
        pytest.assume(find_Rotations("eyde") == 4)
        pytest.assume(find_Rotations("eyv") == 3)
        pytest.assume(find_Rotations("dxbgtvxq") == 8)
        pytest.assume(find_Rotations("mfdx") == 4)
        pytest.assume(find_Rotations("xask") == 4)
        pytest.assume(find_Rotations("qddp") == 4)
        pytest.assume(find_Rotations("oas") == 3)
        pytest.assume(find_Rotations("fjilakl") == 7)
        pytest.assume(find_Rotations("xwdsk") == 5)
        pytest.assume(find_Rotations("owqgr") == 5)
        pytest.assume(find_Rotations("lxv") == 3)
        pytest.assume(find_Rotations("bxbb") == 4)
        pytest.assume(find_Rotations("jbfisms") == 7)
        pytest.assume(find_Rotations("zqupo") == 5)
        pytest.assume(find_Rotations("qye") == 3)
        pytest.assume(find_Rotations("hhxosqlg") == 8)
        pytest.assume(find_Rotations("zhb") == 3)
        pytest.assume(find_Rotations("iwkj") == 4)
        pytest.assume(find_Rotations("maen") == 4)
        pytest.assume(find_Rotations("lsliyhze") == 8)
        pytest.assume(find_Rotations("doocsri") == 7)
        pytest.assume(find_Rotations("cjc") == 3)
        pytest.assume(find_Rotations("avi") == 3)
        pytest.assume(find_Rotations("rfit") == 4)
        pytest.assume(find_Rotations("tlgffvv") == 7)
        pytest.assume(find_Rotations("vlk") == 3)
        pytest.assume(find_Rotations("ljeftwkpr") == 9)
        pytest.assume(find_Rotations("itzso") == 5)
        pytest.assume(find_Rotations("zxfscko") == 7)
        pytest.assume(find_Rotations("ewzfvb") == 6)
        pytest.assume(find_Rotations("wdk") == 3)
        pytest.assume(find_Rotations("gmlivxfm") == 8)
        pytest.assume(find_Rotations("yvsnt") == 5)
    except TypeError as e:
        pytest.fail(f"Test crashed with TypeError: {e}")