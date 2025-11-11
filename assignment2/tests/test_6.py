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
    glob_pattern="problem_6_*.py", 
    function_name="find_char_long"
)

# --- 3. The Test Function (using parametrize) ---

@pytest.mark.parametrize("find_char_long", all_min_cost_functions)
def test_find_char_long(find_char_long):
    """
    This ONE test will run for EVERY function in the 'all_min_cost_functions' list.
    'find_char_long' will be the function from iteration 1, then iteration 2, etc.
    """
    
    # If loading failed, min_cost_func might be None
    if find_char_long is None:
        pytest.fail("Module loading failed, see console output.")

    try:
        pytest.assume(find_char_long('Please move back to stream') == ['Please', 'move', 'back', 'stream'])
        pytest.assume(find_char_long('Jing Eco and Tech') == ['Jing', 'Tech'])
        pytest.assume(find_char_long('Jhingai wulu road Zone 3') == ['Jhingai', 'wulu', 'road', 'Zone'])
        pytest.assume(find_char_long(" BGBKxLZVVthfphWmiQlSzrk") == ['BGBKxLZVVthfphWmiQlSzrk'])
        pytest.assume(find_char_long("oamnvNIOEluWpxgZjQMgjU") == ['oamnvNIOEluWpxgZjQMgjU'])
        pytest.assume(find_char_long("sSAFCZAXyXogXCyFvSVPSokK") == ['sSAFCZAXyXogXCyFvSVPSokK'])
        pytest.assume(find_char_long("iMfssAbLsbTESTfMgSAulTql") == ['iMfssAbLsbTESTfMgSAulTql'])
        pytest.assume(find_char_long("kSPCWfEtMHhPiBiBSoDvv") == ['kSPCWfEtMHhPiBiBSoDvv'])
        pytest.assume(find_char_long("DMqMVHYDsSAWWyKW ndNmUsLUYv") == ['DMqMVHYDsSAWWyKW', 'ndNmUsLUYv'])
        pytest.assume(find_char_long("GdWBslQdRIsZ pxW Ofysf") == ['GdWBslQdRIsZ', 'Ofysf'])
        pytest.assume(find_char_long("gLLpeKctHMWjkxjTRsCus") == ['gLLpeKctHMWjkxjTRsCus'])
        pytest.assume(find_char_long("QXrgeewOnbwmcFUQvqgJAic") == ['QXrgeewOnbwmcFUQvqgJAic'])
        pytest.assume(find_char_long("ryioUEshBzmGnpDIdOHHJ") == ['ryioUEshBzmGnpDIdOHHJ'])
        pytest.assume(find_char_long("XnOPHydAzVMZTCQSDKssUcomo") == ['XnOPHydAzVMZTCQSDKssUcomo'])
        pytest.assume(find_char_long("vpYBYlYpuIzKaHttbXWBrRiOttrz") == ['vpYBYlYpuIzKaHttbXWBrRiOttrz'])
        pytest.assume(find_char_long("MtxMXTIUVXEFqYpHJnDdLxfYO") == ['MtxMXTIUVXEFqYpHJnDdLxfYO'])
        pytest.assume(find_char_long("WvmLHJVYZGIDpYoSzFi oT") == ['WvmLHJVYZGIDpYoSzFi'])
        pytest.assume(find_char_long("yQbwLOngQvQkBIPxPFTKm") == ['yQbwLOngQvQkBIPxPFTKm'])
        pytest.assume(find_char_long("bcfDiOoWItswdQjAMCjvybetn") == ['bcfDiOoWItswdQjAMCjvybetn'])
        pytest.assume(find_char_long("zEzrWDnnHQxPCCDAvqgJSzJSiZ") == ['zEzrWDnnHQxPCCDAvqgJSzJSiZ'])
        pytest.assume(find_char_long("XUMYQigKNsKsyuSXNUxds mCsomL") == ['XUMYQigKNsKsyuSXNUxds', 'mCsomL'])
        pytest.assume(find_char_long("qudIjtprlcRGtnodTLeqWUqhYDIer") == ['qudIjtprlcRGtnodTLeqWUqhYDIer'])
        pytest.assume(find_char_long("SyQjtNbykksnaRUwqPi fXa DUn") == ['SyQjtNbykksnaRUwqPi'])
        pytest.assume(find_char_long("IOT gniYJobPkdtOUlCQ EbJMLeu") == ['gniYJobPkdtOUlCQ', 'EbJMLeu'])
        pytest.assume(find_char_long("bBjMoMZjEtPuRArhenzwig") == ['bBjMoMZjEtPuRArhenzwig'])
        pytest.assume(find_char_long("RgiOIGheVJPfpNVhQHeYdvOdyxzUn") == ['RgiOIGheVJPfpNVhQHeYdvOdyxzUn'])
        pytest.assume(find_char_long("fySkwzWkBMZYQIOHHoubRB") == ['fySkwzWkBMZYQIOHHoubRB'])
        pytest.assume(find_char_long("VuFUUVThHNlfAqmmmRyvcWAhdx") == ['VuFUUVThHNlfAqmmmRyvcWAhdx'])
        pytest.assume(find_char_long("TXzjZvYxSKHsXJOcyjtHGttpSAL") == ['TXzjZvYxSKHsXJOcyjtHGttpSAL'])
        pytest.assume(find_char_long("vYagwqRuUbCSZNKkMYeFKVypKoZlq") == ['vYagwqRuUbCSZNKkMYeFKVypKoZlq'])
        pytest.assume(find_char_long("voWObMMsZCvwsUvcVuCSVICHxwMmfk") == ['voWObMMsZCvwsUvcVuCSVICHxwMmfk'])
        pytest.assume(find_char_long("uLKzIMePKMGZumtvTiPcWCrKGPhwh") == ['uLKzIMePKMGZumtvTiPcWCrKGPhwh'])
        pytest.assume(find_char_long("BFRcHuB VnZvGHnaAOozjBgysw") == ['BFRcHuB', 'VnZvGHnaAOozjBgysw'])
        pytest.assume(find_char_long("oWBAShXgiCiLtfrWdWqiKH") == ['oWBAShXgiCiLtfrWdWqiKH'])
        pytest.assume(find_char_long("IssAlvUbCFrGVcpqKuS fZ") == ['IssAlvUbCFrGVcpqKuS'])
        pytest.assume(find_char_long("ibtxsjUuPbNwztOffYsuWt") == ['ibtxsjUuPbNwztOffYsuWt'])
        pytest.assume(find_char_long("cBGFZguckCiSAUYoPRRm") == ['cBGFZguckCiSAUYoPRRm'])
        pytest.assume(find_char_long("CMcrqzrgCBLotDzriXfmf") == ['CMcrqzrgCBLotDzriXfmf'])
        pytest.assume(find_char_long("cSIYINRSskeZdCMh") == ['cSIYINRSskeZdCMh'])
        pytest.assume(find_char_long("OlmGgybIpGPtPDrxZsV") == ['OlmGgybIpGPtPDrxZsV'])
        pytest.assume(find_char_long("XqtuZsSyY AhoC mg") == ['XqtuZsSyY', 'AhoC'])
        pytest.assume(find_char_long("WYILarumXpvEAeNcHp") == ['WYILarumXpvEAeNcHp'])
        pytest.assume(find_char_long("QbCEnZJtyqCBCxoiWrzY") == ['QbCEnZJtyqCBCxoiWrzY'])
        pytest.assume(find_char_long("bBxvbvtObdnWDNkqOet") == ['bBxvbvtObdnWDNkqOet'])
        pytest.assume(find_char_long("MUiSyjXXtDDuchY") == ['MUiSyjXXtDDuchY'])
        pytest.assume(find_char_long("ekYCiJJHOkfxEkSoRnVYj") == ['ekYCiJJHOkfxEkSoRnVYj'])
        pytest.assume(find_char_long("kMAz ESSibVUVDzFe") == ['kMAz', 'ESSibVUVDzFe'])
        pytest.assume(find_char_long("OxVgakvaDUCVyO") == ['OxVgakvaDUCVyO'])
        pytest.assume(find_char_long("ljtXwUgoFdVgXnA") == ['ljtXwUgoFdVgXnA'])
        pytest.assume(find_char_long("XMqBLEJAPTUbhrupv") == ['XMqBLEJAPTUbhrupv'])
        pytest.assume(find_char_long("mrEr CZHOOH ") == ['mrEr', 'CZHOOH'])
        pytest.assume(find_char_long("RW aYlcLwlnQEHdNnlHt") == ['aYlcLwlnQEHdNnlHt'])
        pytest.assume(find_char_long("MhhdfeFEWjtdt") == ['MhhdfeFEWjtdt'])
        pytest.assume(find_char_long("RDpF QfPcZoQs") == ['RDpF', 'QfPcZoQs'])
        pytest.assume(find_char_long("ndJvdTjHhtCI") == ['ndJvdTjHhtCI'])
        pytest.assume(find_char_long("aOsuOMxYiRZAdzWgWbx") == ['aOsuOMxYiRZAdzWgWbx'])
        pytest.assume(find_char_long("faZRcFXwrFLtmbfqj") == ['faZRcFXwrFLtmbfqj'])
        pytest.assume(find_char_long("RGmDjHYQVEtX") == ['RGmDjHYQVEtX'])
        pytest.assume(find_char_long("ScyqmPCFPTnRpXJxyvJP") == ['ScyqmPCFPTnRpXJxyvJP'])
        pytest.assume(find_char_long("fLgAvYkrzHDP") == ['fLgAvYkrzHDP'])
        pytest.assume(find_char_long("yqwdggznmFmSRdftt") == ['yqwdggznmFmSRdftt'])
        pytest.assume(find_char_long("GatHmsxjDGF SdVk") == ['GatHmsxjDGF', 'SdVk'])
        pytest.assume(find_char_long("sYWVPMJsrIMzGZR Yb") == ['sYWVPMJsrIMzGZR'])
        pytest.assume(find_char_long(" ADjwOiAWjTln ") == ['ADjwOiAWjTln'])
        pytest.assume(find_char_long("kLWtMQNjpnPMU") == ['kLWtMQNjpnPMU'])
        pytest.assume(find_char_long("veWSCrvwgmWogCZGv") == ['veWSCrvwgmWogCZGv'])
        pytest.assume(find_char_long("VuHyLuVXNCEIyCJmwnXC") == ['VuHyLuVXNCEIyCJmwnXC'])
        pytest.assume(find_char_long("RYKFMhSoROfdWIGH") == ['RYKFMhSoROfdWIGH'])
        pytest.assume(find_char_long("WsLHAYwhNOSHVGNDCv") == ['WsLHAYwhNOSHVGNDCv'])
        pytest.assume(find_char_long("bmCMVkuUtWFfYmsY4gFC1YUjYX6") == ['bmCMVkuUtWFfYmsY4gFC1YUjYX6'])
        pytest.assume(find_char_long("KoiP5tipiG5QlacNMb85k3T") == ['KoiP5tipiG5QlacNMb85k3T'])
        pytest.assume(find_char_long("iMrfyQgsFrmLHC mP3mdqrLVz") == ['iMrfyQgsFrmLHC', 'mP3mdqrLVz'])
        pytest.assume(find_char_long("6NiziL5Z4m4514ctvbYX3VxtB1cN") == ['6NiziL5Z4m4514ctvbYX3VxtB1cN'])
        pytest.assume(find_char_long("RwjqCngF2 bD5wb 8WqE5xXViiiL") == ['RwjqCngF2', 'bD5wb', '8WqE5xXViiiL'])
        pytest.assume(find_char_long("O4jDlqmnCyVFco8RNsaIeeXvJciot") == ['O4jDlqmnCyVFco8RNsaIeeXvJciot'])
        pytest.assume(find_char_long("kyhvz7qJomhxxSS3vu ZNL") == ['kyhvz7qJomhxxSS3vu'])
        pytest.assume(find_char_long("ggQudeSwAEr6n88igRT9py7ZuJ") == ['ggQudeSwAEr6n88igRT9py7ZuJ'])
        pytest.assume(find_char_long("gKMiRILsylpickrxtCOHhnBhB ") == ['gKMiRILsylpickrxtCOHhnBhB'])
        pytest.assume(find_char_long("2RQhS3holFQbf1WVTon8loqidM") == ['2RQhS3holFQbf1WVTon8loqidM'])
        pytest.assume(find_char_long("9JSvLjie4UCPUYH 2ZL2ydwun") == ['9JSvLjie4UCPUYH', '2ZL2ydwun'])
        pytest.assume(find_char_long("evBxZWXd6mWPU8dL97gzf") == ['evBxZWXd6mWPU8dL97gzf'])
        pytest.assume(find_char_long("4tgLUTNhQeT2xuaeGk96rXP") == ['4tgLUTNhQeT2xuaeGk96rXP'])
        pytest.assume(find_char_long("5Dj0NMcqk Dtu5enQ42RnDKdBcOX") == ['5Dj0NMcqk', 'Dtu5enQ42RnDKdBcOX'])
        pytest.assume(find_char_long(" Zsd4OxG8uostqSAYeQzs6jf") == ['Zsd4OxG8uostqSAYeQzs6jf'])
        pytest.assume(find_char_long("ty1pSwdTDkRLeh0inWf q") == ['ty1pSwdTDkRLeh0inWf'])
        pytest.assume(find_char_long("nEzuAjwEnAxa6q9HChSwj8 gJMmM") == ['nEzuAjwEnAxa6q9HChSwj8', 'gJMmM'])
        pytest.assume(find_char_long("Y4zHrho2ouwMyW830JSFp") == ['Y4zHrho2ouwMyW830JSFp'])
        pytest.assume(find_char_long("YIi7EhQTOvmI0sL0tASvJeiNYRmfw") == ['YIi7EhQTOvmI0sL0tASvJeiNYRmfw'])
        pytest.assume(find_char_long("rggZeq1Q0 cwEmit5FlgCI ") == ['rggZeq1Q0', 'cwEmit5FlgCI'])
        pytest.assume(find_char_long("KkxFPRfGyaj1xti6kigB5s") == ['KkxFPRfGyaj1xti6kigB5s'])
        pytest.assume(find_char_long("NkIxwu2l7xaIXuZCGG unRhU1S") == ['NkIxwu2l7xaIXuZCGG', 'unRhU1S'])
        pytest.assume(find_char_long("mq7w8BQtAKp8jlMJTgo8DgkYeR5xJp") == ['mq7w8BQtAKp8jlMJTgo8DgkYeR5xJp'])
        pytest.assume(find_char_long("Wejmw4AUuyKLxwvEa4u3Z8hF") == ['Wejmw4AUuyKLxwvEa4u3Z8hF'])
        pytest.assume(find_char_long("y4MDozGfjTAN 32vA91SJpU") == ['y4MDozGfjTAN', '32vA91SJpU'])
        pytest.assume(find_char_long("jErEXzWh T I3F3s1YgQ9ZRyy") == ['jErEXzWh', 'I3F3s1YgQ9ZRyy'])
        pytest.assume(find_char_long("NBb6QuYgC0sFvvt0faDsu") == ['NBb6QuYgC0sFvvt0faDsu'])
        pytest.assume(find_char_long("EZl4C3z1r8AI8SUN37UK4J") == ['EZl4C3z1r8AI8SUN37UK4J'])
        pytest.assume(find_char_long("kPG1vOyH9c07X9yv88JyY aIfB6") == ['kPG1vOyH9c07X9yv88JyY', 'aIfB6'])
        pytest.assume(find_char_long(" 3HzHRB4mh2NVCmfO9vgWfzp") == ['3HzHRB4mh2NVCmfO9vgWfzp'])
        pytest.assume(find_char_long("JfN9mdKj3Kfv29rMNswWJYpfW3WTi") == ['JfN9mdKj3Kfv29rMNswWJYpfW3WTi'])
        pytest.assume(find_char_long("ui7 OLqnKFX1RZHlShM7 6") == ['OLqnKFX1RZHlShM7'])
        pytest.assume(find_char_long("z4k9ubpb1KgR5kyVxne8b") == ['z4k9ubpb1KgR5kyVxne8b'])
    except TypeError as e:
        pytest.fail(f"Test crashed with TypeError: {e}")