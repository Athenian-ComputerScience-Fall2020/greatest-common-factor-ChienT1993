# Collaborators (including web sites where you got help: https://www.w3resource.com/python-exercises/python-basic-exercise-31.php
#  

def find_gcf(x,y):   # Do not change function name!
    gcf = 1
    
    for z in range (int(y / 2), 0, -1):
        if x % z:
            gcf = z
            break
        return gcf



if __name__ == '__main__':
    # Test your code with this first
    # Change the argument to try different values
    find_gcf(6,10)

    # After you are satisfied with your results, use input() to prompt the user for two values:
    #x = int(input("Enter a number: "))
    #y = int(input("Enter another number: "))

