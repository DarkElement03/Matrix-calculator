class matica:

    def __init__():
        m = 1

    def insert():
        if (input("test? (y/n): ")) == "y":
            riadky, stlpceA, stlpceB = 3, 3, 1           #test
            matica = [[12, -1, 5, 30], [3, -13, 2, 21], [7, 2, 3, 15]]          #test
            if (input("simple? (y/n): ")) == "y":
                stlpceB = 0
                matica = [[1, 2, 3], [0, 1, 2], [3, 3, 1]]          #test

        else:
            riadky, stlpceA, stlpceB = int(input("riadky: ")), int(input("stlpce(A): ")), int(input("stlpce(B): "))
            matica = []

            for i in range(riadky):
                matica.append([])
                riadok = input("cisla(oddel medzerou): ")
                riadok = riadok.split(" ")
                for x in range(stlpceA+stlpceB):
                    matica[i].append(int(riadok[x]))
        
                print(matica[i])
        return matica, riadky, stlpceA, stlpceB

    def one(r, first):
        n = matica[r][first]
        print("delim: ", n)
        for s in range(stlpceA + stlpceB):
            matica[r][s] /= n

    def zero(first, source, target):
        x = matica[target][first]
        for s in range(stlpceA + stlpceB - first):
            print(matica[target][first + s], " minus ", matica[source][first + s], matica[target][first], "=", x)
            matica[target][first + s] -= matica[source][first + s] * x

    def calculate(matica):
        print("stlpce:", stlpceA, stlpceB)

        for s in range(stlpceA):
            print("one: ", s, s)
            one(s, s)
            print(matica[s])
    
            for r in range(riadky - s):
                if (r+s+1) < riadky:
                    print(s, s, r + s + 1)
                    zero(s, s, r + s + 1)
                    print(matica)

        print("KROK 1")

        for s in range(stlpceA):
            s1 = (stlpceA-1) - s
            print("s:", s, "s1:", s1)
    
            for r in range(s1):
                print("r=", r)
                if (s1-r-1) < riadky:
                    print(s1, s1, s1 - r - 1)
                    zero(s1, s1, s1 - r - 1)
                    print(matica)
        return matica

    def invert(matica):
        for r in range(riadky):
            for i in range(stlpceA):
                matica[r].append(0)
            matica[r][r+stlpceA] = 1
        print("nova matica:", matica)
        matica = calculate(matica)
        return matica

    def transpon(maticaTemp):
        for i in range(riadky):
            print(maticaTemp[i])
        matica = []
        for r in range(stlpceA):
            matica.append([])
            for s in range(riadky):
                print(f'{s, r}: {maticaTemp[s][r]}')
                matica[r].append(maticaTemp[s][r])
            print(matica, "\n", maticaTemp)
        return matica

    def multiply(matica1, matica2, stlpce1, riadky2):
        maticaf = []
        matica2 = transpon(matica2)
        for rf in range(riadky2):
            maticaf.append([])
            for sf in range(stlpce1):
                cislo = 0
                for i in range(riadky2):
                    cislo += matica1[rf][i]*matica2[rf][i]
                maticaf[rf].append(cislo)
        return maticaf

while True:

    matica, riadky, stlpceA, stlpceB = insert()

    task = input("task? (c/i/t/m): ")

    if task == "c":
        matica = calculate(matica)

    elif task == "i":
        stlpceB = stlpceA
        matica = invert(matica)

    elif task == "t":
        matica = transpon(matica)

    elif task == "m":
        matica2, riadky2, stlpce2, stlpce2 = insert()
        stlpce1 = stlpceA
        matica = multiply(matica, matica2, stlpce1, riadky2)

    for i in matica:
        print(i)

    if (input("continue? (y/n): ")) == "n":
        break