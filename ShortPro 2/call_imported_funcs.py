"""
File: call_imported_funcs.py
Author: Rustambek Sobithanov
Purpose: The following code imports a file and performs some operations
         using the input provided by the user and the functions from the
         imported file.
"""


import short1_thing
input1 = input()
first_result = short1_thing.foo(input1)
print(first_result)
input2 = input()
input3 = input()
second_result = short1_thing.bar(input1, input2, input3)
print(second_result)
third_result = short1_thing.baz(first_result, second_result)
print(third_result)