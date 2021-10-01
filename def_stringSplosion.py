def string_splosion(string):
    str_new = ''
    for i in range(len(string)):
        str_new += (string[:i+1])
    return str_new


a = string_splosion("Code")
print(a)