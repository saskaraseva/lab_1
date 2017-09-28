def perevorot_stroki(stroka_do):
    m = len(stroka_do)
    n = 0
    stroka_posle = stroka_do[m - 1]
    while m != 1:
        m = m - 1
        stroka_posle = stroka_posle + stroka_do[m - 1]
        n += 1
    return stroka_posle

def main():
    stroka="kukushka"
    print ("stroka:" + stroka)
    print ("perevorot stroki:" + str(perevorot_stroki(stroka)))
main()