# code your iterative algorithm here
# Define a function called binary_search that takes a list
# and an element. Name the parameters data and el, respectively.

def binary_search(data, el):
    # Create two variables called first and last to store the
    # index values of the first and last positions in the list
    first = 0
    last = len(data) - 1
    # Create a variable called found and set equal to False. We
    # will use this variable to store True if the desired
    # element is found later on
    found = False

    # Create a while loop that runs when first is less than
    # or greater than last and the element is not
    # found (found is False)
    while first <= last and not found:
        mid = (first+last)//2

        if data[mid] == el:
            found = True
        # Write the case for the left half. If the desired
        # element is less than the middle element's value,
        # set last equal to one less than the index of the
        # middle element (mid-1)
        else:
            if el < data[mid]: 
                last = mid-1
            else: 
                first = mid+1
    return found

test_list = [5, 8, 12, 14, 19, 22, 27, 30, 31]

print(binary_search(test_list, 12))

# When the program is run, the output is True. If we
# change the desired element from 12 to 11, then
# the output is False.
