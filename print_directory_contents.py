import os

print(os.listdir(os.getcwd()))


# os.path.isfile("bob.txt") # Does bob.txt exist?  Is it a file, or a directory?
# os.path.isdir("bob")


def print_directory_contents(sPath):
    """
    This function takes the name of a directory 
    and prints out the paths files within that 
    directory as well as any files contained in 
    contained directories. 

    This function is similar to os.walk. Please don't
    use os.walk in your answer. We are interested in your 
    ability to work with nested structures. 
    """

    
    currentDirContentList = os.listdir(sPath)
        
    for item in currentDirContentList:

        sChildPath = os.path.join(sPath,item)

        if os.path.isfile(sChildPath):
            print(item)
        if os.path.isdir(sChildPath):
            print_directory_contents(sChildPath)

# print(os.getcwd())
# 
currentDirContentList = "C:/xampp/htdocs/Kitchen/Python"
print_directory_contents(currentDirContentList)            
