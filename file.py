
def read(file_name):
    with open(file_name, "r") as f:
        return f.read()

    return None

def write(file_name, data):
    with open(file_name, "w") as f:
        f.write(data)


def read_list(file_name, delim="\n"):
    fc = read(file_name)

    return fc.split(delim)

def write_list(str_collection, file_name, delim="\n"):
    with open(file_name, "w") as f:
        for entry in str_collection:
            f.write(entry + delim)

