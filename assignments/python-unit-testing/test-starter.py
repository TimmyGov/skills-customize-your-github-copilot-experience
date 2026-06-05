from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path


module_path = Path(__file__).with_name("starter-code.py")
spec = spec_from_file_location("starter_code", module_path)
starter_code = module_from_spec(spec)
spec.loader.exec_module(starter_code)

add = starter_code.add
is_even = starter_code.is_even
format_username = starter_code.format_username
calculate_total = starter_code.calculate_total


# TODO: Write tests for add()
# TODO: Write tests for is_even()
# TODO: Write tests for format_username()
# TODO: Write tests for calculate_total()


def test_example_add():
    assert add(2, 3) == 5
