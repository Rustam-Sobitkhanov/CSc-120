#! /usr/bin/python3

""" Code to test the tree_depth() function

    Author: Russ Lewis
"""

import tree_funcs_short



###########################################################
#                       INPUT                             #
###########################################################

from tree_node import TreeNode

root = None



###########################################################
#                     TEST CODE                           #
###########################################################
def main():
    print("Testing tree_depth()...")
    print()

    retval = tree_funcs_short.tree_depth(root)

    print(f"Returned value: {retval}")
    print()

    print("TESTCASE COMPLETED")



if __name__ == "__main__":
    main()


