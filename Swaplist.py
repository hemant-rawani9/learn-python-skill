n = int(input("Enter number of elements in the list: "))
lst = [int(input()) for _ in range(n)]

i = int(input("Enter index of first element to swap: "))
j = int(input("Enter index of second element to swap: "))

lst[i], lst[j] = lst[j], lst[i]

print("List after swapping:")
print(lst)
