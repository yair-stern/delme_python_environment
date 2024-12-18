"""
This program gets a number from the user
"""

arr = [3, 5, 7, 1, 10, 12, 34, 15]

def checkAgain():
    print("Do you want to check more one? (Enter y/n)")
    

def check():
    index = int(input()) - 1  # Convert input to int and adjust for 0-based indexing
    
    if 0 <= index < len(arr):  # Ensure the index is valid
        print(f"The number is {arr[index]}. It is", end=" ")
        if arr[index] % 2 == 0:
            print("even.")
        else:
            print("odd.")
    else:
        print("Invalid input. Please enter a number between 1 and 8.")
        check()

if __name__ == "__main__":
    print("Welcome to my program!")
    print("I have 8 numbers in my memory.")
    print("I will ask you to choose one of them,")
    print("and I will tell you if it is odd or even.")
    print("Let's start.")
    print("Enter a number between 1 and 8:")
    check()
    
