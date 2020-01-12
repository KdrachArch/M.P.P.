#!/etc/bin/python3
from scipy import stats

def main():
    inp = input("\nPRESS\n[1] for finding area under normal curve [1] \n[2] for area between two SD [2]\n[3]to get bellow Z[3]\n[x]to exit[x]\n:: ")
    if inp == '1':
        return norm()
    elif inp == '2':
        return betw()
    elif inp == '3':
        return bellz()
    elif inp == 'x' or 'X':
        return
    else:
        print("Please choose correctly between choices...")
        return main()

def norm():

    inp = input("Z-Score: ")

    """finds the area under normal curve"""
    finp = stats.norm.cdf(float(inp))

    """subtracts 0.5 to get the area under
    normal curve"""
    zsc = finp - 0.5

    """converts it to string to cut out unwanted
    numbers and converts it back to float"""
    out = str(zsc)
    aout = out[:7]
    bout = float(aout)

    print(bout)

    return main()

def betw():

    print("\nInput the two SD that you want to find the area of, lowest integer first: \n")

    a_inp = input("First SD: ")
    b_inp = input("Second SD: ")

    c_inp = stats.norm.cdf(float(a_inp))
    d_inp = stats.norm.cdf(float(b_inp))

    cn_inp = c_inp - 0.5
    cd_inp = d_inp - 0.5

    sc_inp =  str(cn_inp)
    sd_inp = str(cd_inp)

    oc_inp = sc_inp[:7]
    od_inp = sd_inp[:7]

    fin_inp = float(oc_inp)
    fin1_inp = float(od_inp)

    fou_inp = (fin_inp - fin1_inp)*-1*-1

    print(fou_inp)

    return main()

def bellz():

    inp = input("Bellow Z-Score: ")

    """finds the area under normal curve"""
    finp = stats.norm.cdf(float(inp))

    """subtracts 0.5 to get the area under
    normal curve"""
    finpz = finp * finp / finp
    zsc2 = 0.5 - finpz
    zsc3 = 0.5 - zsc2

    """converts it to string to cut out unwanted
    numbers and converts it back to float"""
    out = str(zsc3)
    aout = out[:7]
    bout = float(aout)

    print(zsc3)

    return main()

if __name__ == '__main__':
    main()
