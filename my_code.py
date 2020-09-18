# Collaborators (including web sites where you got help: https://www.w3resource.com/python-exercises/python-basic-exercise-31.php
#  

def find_gcf(x,y):   # Do not change function name!
    for z in range (x, 0, -1):
        if x % z == 0 and y % z == 0:
            gcf = z
            return gcf



if __name__ == '__main__':
    # Test your code with this first
    # Change the argument to try different values
    x= int(input("Enter a number: "))
    y= int(input("Enter another number: "))
    answer= find_gcf(x,y)
    print (answer)
    # After you are satisfied with your results, use input() to prompt the user for two values:
    #x = int(input("Enter a number: "))
    #y = int(input("Enter another number: "))

