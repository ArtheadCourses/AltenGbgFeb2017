import argparse
def main():
    # Crete an argument parser
    parser = argparse.ArgumentParser()

    # Add an argument to it
    parser.add_argument("base", type=int, help="the base number")
    parser.add_argument("pow", type=int, help="the power")

    parser.add_argument("-v", "--verbose", action="store_true", help="increase output verbosity")

    # Parse the aruments passed to the program
    args = parser.parse_args()

    answer = args.base**args.pow
    if args.verbose:
        print("{0}^{1}={2}".format(args.base, args.pow, answer))
    else:
        print(answer)
    
if __name__ == '__main__':
    main()