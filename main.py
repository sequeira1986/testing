

# Create a class containing a set of integers. the class should have the following functionality implemented:
# the sum of elements in the set.
#Arithmetic mean of elements in the set
#Maximum of elements in the set
#Minimum of elements in the set
# test all the possibilities of the created class using unit testing (unittest)

class OperationsIntegers:
    def __init__(self, element):
        self.element = set(element)

    def sum_elements(self):
        total_sum = 0
        for num in self.element:
            total_sum += num
        return total_sum
    def arit_mean(self):
        if not self.element:
            return None
        return self.sum_elements() / len(self.element)

    def max_element(self):
        if not self.element:
            return  None
        max_element = float('-inf')
        for num in self.element:
            if num > max_element:
                max_element = num
        return max_element
    def min_element(self):
        if not self.element:
            return None
        min_element = float('inf')
        for num in self.element:
            if num < min_element:
                min_element = num
        return min_element

integer_set = OperationsIntegers([8,9,1,4,7,5,6])
print(f"Sum of elements: {integer_set.sum_elements()}")
print(f"Arithmetic mean: {integer_set.arit_mean()}")
print(f"Maximum element: {integer_set.max_element()}")
print(f"Minimum element: {integer_set.min_element()}")

