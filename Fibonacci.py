n = int(input("\nEnter the number of terms: "))

fibonacci = [0, 1]

for i in range(2, n):
    fibonacci.append(fibonacci[i - 1] + fibonacci[i - 2])

print()

for i, value in enumerate(fibonacci):
    print(i + 1, "\t", value)

print("\n[Python]\n")
