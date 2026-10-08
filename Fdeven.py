n = int(input("Enter number of elements in the list: "))
lst = [int(input()) for _ in range(n)]
even_numbers = [x for x in lst if x % 2 == 0]
print("Even numbers in the list:", even_numbers)
