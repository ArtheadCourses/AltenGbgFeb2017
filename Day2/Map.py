def c2f(t):
    return (9.0/5) * t + 32
def f2c(t):
    return (5.0/9) * (t - 32)

def main():
    temp_in_c = [16.3, 21.3, 19.7, 15.4]
    print(temp_in_c)
    temp_in_f = list(map(c2f, temp_in_c))
    print(temp_in_f)
    temp_in_c = list(map(lambda t: (5.0/9) * (t - 32), temp_in_f))
    print(temp_in_c)
    temp_in_c = [(5.0/9) * (t - 32) for t in temp_in_f]
    print(temp_in_c)

if __name__ == '__main__':
    main()