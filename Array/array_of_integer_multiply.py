def array_of_integer_multiply_bforce(arr1, arr2):
    i_conversion = 0
    sign = 1
    for i in range(len(arr1)):
        if (arr1[i] != -1):
            for k in range(len(arr2)):
                if if (arr2[k] != -1):
                    i_conversion += arr1[i] * arr2[k] * (10**k)
                else:
                    sign *= -1
        else:
            sign *= -1
    return i_conversion * sign
    

def array_of_integer_multiply(arr1, arr2):
    i_conversion = arr1[len(arr1) -1] + arr2[len(arr2) -1]
    sign = 1
    temp1, temp2 = arr1[len(arr1) -1], arr2[len(arr2) -1]

    for i in range(min(len(arr1), len(arr2))):
        add_on = arr1[i] * (10 ** i) * arr2[i] * (10 ** i) + (temp1 * arr1[i] + temp2 * arr2[i]) * (10 ** (2*i -1))
        i_conversion += add_on
        temp1, temp2 = arr1[i], arr2[i]
    #assume arr2 is larger. Should do compare
    for i in range(len(arr2)- len(arr1)):
        add_on = (temp2 * arr2[i]) * (10 ** (2*i -1))
        i_conversion += add_on
        temp2 = arr2[i]
    return i_conversion


arrOne = [1,4]
arrTwo = [-1,1,0]

print (array_of_integer_multiply(arrOne, arrTwo))