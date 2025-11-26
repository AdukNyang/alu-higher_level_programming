#!/usr/bin/python3
def print_list_integer(my_list=[]):
    for i in my_list:
        print("{:d}".format(i))

if __name__ == "__main__":
    # Example usage so the script prints when executed directly
    sample = [1, 2, 3, 4]
    print_list_integer(sample)
