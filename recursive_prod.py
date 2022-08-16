
def rec_product(a,b):
    negativeness = 0
    if a < 0 and b < 0:
        negativeness = 1
    if a < 0 and b > 0 or a > 0 and b < 0:
        negativeness = -1
    if a > 0 and b > 0:
        negativeness = 1
    a = abs(a)
    b = abs(b)
    productList = []
    #makes list
    for i in range(0,b):
        productList.append(a)
    #base case
    if len(productList) == 0:
        product = 0
    #recursive case
    else:
        product = productList[0] + rec_product(a, b-1)
    return product * negativeness
print(rec_product(10,100))