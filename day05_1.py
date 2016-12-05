import hashlib
def solve(input):
    password = ""
    idx = 0
    while len(password) < 8:
        m = hashlib.md5()
        m.update(input + str(idx))
        if m.hexdigest()[:5] == "00000":
            password += m.hexdigest()[5]
        idx += 1
    print "DONE", password

input = """abbhdwsy"""
solve(input)
