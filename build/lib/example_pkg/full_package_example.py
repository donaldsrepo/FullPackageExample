# stub for new python code
import unittest

def dummy_function(param1, param2): 
    # stuff
    print("function")
    return 1

def test_sum():
    assert sum([1, 2, 3]) == 6, "Should be 6"
    print("test_sum working")
    
if __name__ == '__main__': 
    # "Executed when invoked directly"
    test_sum()
    x = dummy_function(1,2) 
    print("result of function call", x)
else: 
    # "Executed when imported"
    print("using as package")