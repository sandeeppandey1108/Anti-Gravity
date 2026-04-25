
memory = []

def store(data):
    memory.append(data)

def best():
    return sorted(memory, key=lambda x: x.get("ctr",0), reverse=True)
