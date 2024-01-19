lst = []
index = []
output = ""

for i in range(5):
    lst.append(input("Enter a string: "))

for i in range(3):
    index.append(int(input("Enter a number: ")))

for i in range(len(index)):
    output = output + lst[index[i]]

print(output)