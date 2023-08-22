def extract_route(string):
    s1 = string.split('\n')[0]
    s2 = s1.split(' ')[1]
    s3 = s2[1:]
    return s3

def read_file(path):
    with open(path,'rb') as file:
        content = file.read()
        return content