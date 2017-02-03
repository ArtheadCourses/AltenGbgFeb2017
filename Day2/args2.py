import argparse
def main():
    # Crete an argument parser
    parser = argparse.ArgumentParser()

    # Add an argument to it
    parser.add_argument("echo")

    # Parse the aruments passed to the program
    args = parser.parse_args()

    print(args.echo)
    
if __name__ == '__main__':
    main()