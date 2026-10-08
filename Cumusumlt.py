n = int(input("Enter number of elements in the list: "))
lst = [int(input()) for _ in range(n)]
cumulative = [lst[0]]
for i in range(1, n):
    cumulative.append(cumulative[-1] + lst[i])
print("Cumulative sum list:", cumulative)
