num = input("user_input: ")
print(f"{num[0]}", end = "")
for i in range(1, len(num), 1):
    if(num[i] != num[i - 1]):
        print(f", {num[i]}", end = "")