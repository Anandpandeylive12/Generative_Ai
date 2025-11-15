def infinite_chai():
    count = 1
    while True:
        yield f"Refile #{count}"
        count += 1


refile = infinite_chai()

for _ in range(10):
    print(next(refile))