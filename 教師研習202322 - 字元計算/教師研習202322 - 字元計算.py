num = input("user_input: ")
sum = [0]*128
for i in range(0, len(num), 1):
    sum[ord(num[i])] += 1
for i in range(0, 128, 1):
    if(sum[i] != 0):
        print(f"{chr(i)}:{sum[i]}  ", end = "")