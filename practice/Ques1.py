# list, lambda, map, filter.

# list create.
# square function in map.
# seperating even no function from list using filter.

lst = []
n = int(input("Enter no of elements in list: "))
for i in range(n):
    elm = int(input(f"Enter {i+1}st element: "))
    lst.append(elm)
print("You entered list: ", end="")
print(lst)

lst = list(filter(lambda x : x%2==0, lst))
print("list after removing odd numbers: ", end="")
print(lst)

lst = list(map(lambda x : x*x, lst))
print("list containing the square of only even numbers: ", end="")
print(lst)