def P(a,t):
    val = a[-1]
    for c in a[-2::-1]:
        val = c + t*val
    return val
c = [1.7,-2.3,0.6]
x = 1.0

print ("le polynome de coefficients", c, "vaut", P(c,x), "en", x)

