n = int (input("Enter number:\n"))
m = n
while n > 0:
            if n%2 == 0:
                print("🟩", end ="")
            else:
                print("🟨", end ="")
            n = n-1
print("\n")
for i in range(m):
    print("🐍",end=" ")
    m = m-1