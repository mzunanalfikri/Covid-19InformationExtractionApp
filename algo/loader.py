def load():
    #mengembalikan string yang di load dari txt
    f = open("../test/berita1.txt", "r")
    contents = f.read()
    f.close
    contents = contents.replace('\n', '')
    return contents.split('.')

# print(parsing(load()))