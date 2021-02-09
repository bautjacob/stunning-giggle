import unittest
from string_calc import add

class StringCalcTestCase(unittest.TestCase):
    #1
    def test_empty(self):
        result = add("")
        self.assertEqual(result, 0, "Empty string failed")
    def test_example_input(self): 
        result = add("1,2,5")
        self.assertEqual(result, 8, "Input 1,2,5 failed")
    #2
    def test_example_newline1(self): 
        result = add("1\n,2,3")
        self.assertEqual(result, 6)
    def test_example_newline2(self): 
        result = add("1,\n2,4")
        self.assertEqual(result, 7)
    #3
    def test_example_delimiter1(self): 
        result = add(";\n1;3;4")
        self.assertEqual(result, 8)
    def test_example_delimiter2(self): 
        result = add("$\n1$2$3")
        self.assertEqual(result, 6)
    def test_example_delimiter3(self): 
        result = add("@\n2@3@8")
        self.assertEqual(result, 13)    
    #4
    def test_single_negative_exception_no_delimiter(self):         
        self.assertRaises(Exception, add, "1,2,-3,4")
    def test_single_negative_exception_with_delimiter(self):         
        self.assertRaises(Exception, add, "t\n5t-6t7")
    def test_multiple_negative_exception_no_delimiter(self):         
        self.assertRaises(Exception, add, "-2,1,2,-3,4,-3")
    def test_multiple_negative_exception_with_delimiter(self):         
        self.assertRaises(Exception, add, "t\n5t-6t7t-8")

    #Bonus
    def test_example_ignore_large_numbers(self): 
        result = add("2,1001")
        self.assertEqual(result, 2)
    def test_example_arbitrary_delimiter_length(self): #Could not complete
        result = add("***\n1***2***3")
        self.assertEqual(result, 6)
    def test_example_multiple_delimiters(self): #Could not complete
        result = add("$,@\n1$2@3")
        self.assertEqual(result, 6) 
    def test_multiple_delimiters_arbitrary_length(self): #Could not complete
        result = add("$$$!,@@@@%\n1@@@@%2$$$!3$$$!4")
        self.assertEqual(result, 10) 

if __name__ == '__main__': 
    unittest.main() 