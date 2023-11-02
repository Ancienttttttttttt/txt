def srednia(a,b):
    value = int(((2*a*b)/(a+b)))
    return value

def main():
    n = int(input())
    for i in range(n):
        wier = input().split()

        v1 = int(wier)
        v2 = int(wier)
        print(srednia(v1, v2))

if __name__ == '__main__':
    main()
