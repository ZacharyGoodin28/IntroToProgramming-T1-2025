x = input("Write a sentence\n>")

print(x.upper())
print(x.strip())
print(x.replace("bad", "good"))

if x.endswith("."):
    print(True)
else:
    print(False)