from four_func_calculator.four_function import four_function

def test_four_function():
    assert four_function(2, 3, 1) == 5
    assert four_function(2, 3, 2) != 5
    