
def perevorot_stroki(stroka_do):
    index = len(stroka_do) - 1
    stroka_posle = ' '
    while index >= 0:
        stroka_posle += stroka_do[index]
        index-=1
    return stroka_posle


def main():
    stroka="kukushka"
    print ("stroka:" + stroka)
    print ("perevorot stroki:" + str(perevorot_stroki(stroka)))
main()