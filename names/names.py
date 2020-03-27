import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

# Create binary search tree to place into a data structure which we can then use contain to compare the
# names1 and names 2 lists in order to parse out the duplicates


class BST:
    # Tree starts from initial node value given, place value of None to start
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

    # place values from list given into tree when called
    def insert(self, value):
        if self.value == None:
            self.value = value
        # BST behavior of greater values being places on right
        elif value >= self.value:
            if self.right:
                self.right.insert(value)
            else:
                # no insert if value is equal continue with passing in values recursively calling BST
                self.right = BST(value)
        elif value < self.value:
            if self.left:
                self.left.insert(value)
            else:
                self.left = BST(value)

    # Create contains_value to be used when comparing tree with names list with other names list and populate duplicates[]
    # this wil be used to compare names_2 and names_1 and append to duplicates list with append_duplicates function below
    def contains_value(self, target):
        if target == self.value:
            return True
        if target > self.value and self.right:
            return self.right.contains_value(target)
        if target < self.value and self.left:
            return self.left.contains_value(target)
        return False


def append_duplicates():
    names_1_tree = BST()
    for name_1 in names_1:
        names_1_tree.insert(name_1)
    for name_2 in names_2:
        if names_1_tree.contains_value(name_2):
            duplicates.append(name_2)


append_duplicates()

end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")


# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
