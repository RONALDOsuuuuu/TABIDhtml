n = int(input("How many charecters to preview? "))
file = open("E:/PYTHON/Codingal.txt", "r")
print(file.read(n))
file.close()
print()
file = open("E:/PYTHON/Codingal.txt", "r")
lines = file.readlines()
file.close()
print("Totle lines:", len(lines))
for i in range(len(lines)):
    print(i + 1, "->", lines[i].strip())
print()
word = input("Skip lines starting with: ")
file = open("E:/PYTHON/Codingal.txt", "r")
for line in file:
    if line.startswith(word):
        print("skip ->", line.strip())
    else:
        print("keep ->", line.strip())
file.close()
print()
file = open("E:/PYTHON/Codingal.txt", "r")
lines = file.readlines()
file.close()
out = open("E:/PYTHON/Codingal.txt", "w")
for i in range(0, len(lines), 2):
    out.write(lines[i])
out.close()
print("Odd lines saved to od-lines.txt")