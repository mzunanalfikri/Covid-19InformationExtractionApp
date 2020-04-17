def load(filepath):
    #mengembalikan string yang di load dari txt
    #"test/berita1.txt"
    f = open(filepath, "r")
    contents = f.read()
    f.close
    contents = contents.replace('\n', '')
    return contents.split('.')

def load_file(file):
    contents = file.read()
    file.close
    contents = contents.decode('utf-8')
    contents = contents.replace('\n', '')
    return contents.split('.')

# print(parsing(load()))