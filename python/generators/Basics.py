def serve_chai():
    yield "cup 1: Masala Chai"
    yield "cup 2: Ginger  Chai"
    yield "cup 3: Elaichi Chai"
    yield "cup 4: simple Chai"

stall = serve_chai()

for cup in stall:
    print(cup)
