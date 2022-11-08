import math


def factorise(num):
    factors = []
    for tri in range(1, round(math.sqrt(num)) + 1):
        if num / tri == round(num / tri):
            factors.append(tri)
            factors.append(num / tri)
    return factors
def hcf(num1,num2):

    factors = []
    def factorise(num):
        factors = []
        for tri in range(1,round(math.sqrt(num))+1):
            if num/ tri == round(num/tri):
                factors.append(tri)
                factors.append(num/tri)
        return factors

    fact1 = factorise(num1)
    print(fact1)
    fact2 = factorise(num2)
    print(fact2)
    comm = []
    for item in factorise(num1):

        if item not in fact2:

            fact1.remove(item)

    for item in factorise(num2):

        if item not in fact1:

            fact2.remove(item)
    print(fact1)
    print(fact2)
def lcm(num1,num2):


    for i in range(1, 100):

        if (num1 * i) / num2 == round((num1 * i) / num2):
            return num1 * i
            break


def ismagicnot2_5(number):
    test = factorise(number)
    test.remove(number)
    count = 0
    for item in range(len(test)):
        count+= test[item]
    #print(count)
    if count >= number and not(round(number/2)== number/2) and not(round(number/5)== number/5):
        return True
    else:
        return False

print(factorise(81081))
#for i in range(1,1000000):
#    if ismagic(i):
#        print(i)
