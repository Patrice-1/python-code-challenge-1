#A list of tuples where each tuple contains a name and an age, write a Python function named sort_by_age that sorts the list of tuples by age in ascending order.

def sort_by_age(people):
    return sorted(people, key=lambda x: x[1])

#test the function with a list of tuples
people = [("Alice", 25), ("Bob", 30), ("Charlie", 28)]
print(sort_by_age(people))

people = [("David", 35), ("Emily", 20), ("Frank", 30)]
print(sort_by_age(people))