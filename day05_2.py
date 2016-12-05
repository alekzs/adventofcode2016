import hashlib
def solve(input):
    password = "--------"
    idx = 0
    while password.count("-") > 0:
        m = hashlib.md5()
        m.update(input + str(idx))
        if m.hexdigest()[:5] == "00000":
            passwordIndex = int(m.hexdigest()[5]) if m.hexdigest()[5].isdigit() else -1
            if passwordIndex != -1 and passwordIndex < len(password) and password[passwordIndex] == "-":
                newPassword = list(password)
                newPassword[passwordIndex] = m.hexdigest()[6]
                password = "".join(newPassword)
        idx += 1
    print "DONE", password

input = """abbhdwsy"""
solve(input)
