def find_max(array):
    max_value = 0
    if len(array) == 0:
        return -1
    for v in array:
        if v >= max_value:
            max_value = v
    return max_value


def average(array):
    if len(array) == 0:
        return -1
    sum = 0
    for m in array:
        sum += m
    average_value = sum / len(array)
    return average_value


def main():
    mas1 = [1, 2, 3]

    print ("max =" + str(find_max(mas1)))

    print ("average=" + str(average(mas1)))
main()