#! /usr/bin/python3

import shapes



# The tests will use this set to detect unexpected aliasing.  Some aliasing is
# expected and required, of course - but spurious aliasing is always an error!

ids = set()



def test_alpha():
    print("Testing shape_alpha()")

    val = shapes.shape_alpha()

    print(f"shape_alpha() returned: {val}")

    if len(val) != 4:
        print("ERROR: Invalid contents")
        return

    if val[0] != [10,20]:
        print("ERROR: Invalid contents")
        return

    if val[1] != 30:
        print("ERROR: Invalid contents")
        return

    if val[2] != 40:
        print("ERROR: Invalid contents")
        return

    if val[3] != [50,60]:
        print("ERROR: Invalid contents")
        return

    print("OK - the shape appears to be correct")



test_alpha()


