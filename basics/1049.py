def getValues():
    str1 = input()
    str2 = input()
    str3 = input()

    return str1, str2, str3

def getAnimal(str1, str2, str3):
    if str1 == "vertebrado":
        if str2 == "ave":
            if str3 == "carnivoro":
                return "aguia"
            else:
                return "pomba"
        else:
            if str3 == "onivoro":
                return "homem"
            else:
                return "vaca"
    else:
        if str2 == "inseto":
            if str3 == "hematofago":
                return "pulga"
            else:
                return "lagarta"
        else:
            if str3 == "hematofago":
                return "sanguessuga"
            else:
                return "minhoca"
            

def main():
    plv1, plv2, plv3 = getValues()
    print(getAnimal(plv1, plv2, plv3))
    
if __name__ == "__main__":
    main()