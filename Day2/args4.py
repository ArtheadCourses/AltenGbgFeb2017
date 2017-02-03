import argparse
def main():
    # Crete an argument parser
    parser = argparse.ArgumentParser()

    # Add an argument to it
    parser.add_argument("base", type=int, help="the base number")
    parser.add_argument("pow", type=int, help="the power")

    # Parse the aruments passed to the program
    args = parser.parse_args()

    print(args.base**args.pow)
    
if __name__ == '__main__':
    main()