from pathfinder.generate_matrix import *

def main():
    size = None
    while size is None:
        size = get_matrix_size()
    
    matrix = generate_matrix(size)
    display_matrix(matrix)

def get_matrix_size():
    size = input("Enter the desired matrix size (between 5 and 20, inclusive): ")
    try:
        size = int(size)
    except ValueError:
        print("Please enter a valid integer.")
        return None
    
    if size < 5 or size > 20:
        print("Please enter a valid integer.")
        return None
    
    return size

if __name__ == "__main__":
    main()