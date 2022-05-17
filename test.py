strs = ["adoliscent", "adolize", "adoluminia"]

print(list(zip(*strs)))

for s in zip(*strs):
    print(s)
    print(set(s))