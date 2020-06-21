# THIS IS A WRONG ANSWER!

alphabets = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
# a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z
# 0, 1, 2, 3, 4, 5, 6, 7, 8, 9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,

N = int(input())
result = ""

a = N
while True:
    quotient = a // 26  # quotioent: 商
    mod = a % 26
    print("q " + str(quotient) + " mod " + str(mod))
    if quotient == 0:
        if mod == 0:
            # result = "z" + result
            if quotient // 26 == 0:
                break
        result = alphabets[mod - 1] + result
        a = quotient
    else:
        result = alphabets[mod - 1] + result
        a = quotient
        if a // 26 == 0 and a % 26 == 0:
            break

"""
    if mod > 0:   
        result = alphabets[mod - 1] + result
        a = quotient
    else:
        if quotient == 0:
            break
        else:
            result = "z" + result
            a = quotient
            if a // 26 == 0:
                break
            else:
                continue
        # result = alphabets[quotient] + result
"""
print(result)
