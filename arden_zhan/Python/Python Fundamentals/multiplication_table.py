'''Multiplication Table'''


for x in range(13):
    if x == 0:
        result = "x"
    else:
        result = str(x)
    for y in range(1,13):
        if x == 0:
            x = 1
        product = str(y * x)
        result += "{}{}".format(" ", product)
    print result