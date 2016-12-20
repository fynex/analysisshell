
def read(file_name):
    with open(file_name, "r") as f:
        return f.read()

    return None

def write(file_name, data):
    with open(file_name, "w") as f:
        f.write(data)


