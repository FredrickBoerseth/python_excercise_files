def bottles_of_beer(bob):
    """
    prints 99 Bottle of Beer on the Wall lyrics    
    :param bob: must be a positive integer
    """
    if bob < 1: # this is the base case that satisfies the recursive algoriyhm
        print("""No more bottles of beer on the wall. No more bottles of beer.""")
        return
    tmp = bob
    bob -= 1 # this changes its state and moves toward the base case
    print("""{} bottles of beer on the wall. {} bottles of beer. Take on down pass it around, {} bottles of beer on the wall.""".format(tmp, tmp, bob))
    bottles_of_beer(bob) # a function calling itself, that's what recursion is

bottles_of_beer(99)

# to understand recursion, first you must understand recursion