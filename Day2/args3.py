import argparse
def main():
    # Crete an argument parser
    parser = argparse.ArgumentParser()

    # Add an argument to it
    parser.add_argument("square", type=int, help="display the square of this number")

    # Parse the aruments passed to the program
    args = parser.parse_args()

    print(args.square**2)
    
if __name__ == '__main__':
    main()