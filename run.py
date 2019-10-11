import os 

path = os.getcwd()

print ("The current working directory is %s" % path)


def createfolder(name):
    try:
        os.mkdir(name)
    except OSError:
        print ("Creation of the directory %s failed" % name)

def createStructFolders(rootname):
    subfolders =["controller", "model", "service", "repository"]

    createfolder(rootname)

    for subfolder in subfolders:
        createfolder(os.path.join(rootname, subfolder))

    createfolder(os.path.join(rootname, "service", "imp"))

    projection = input("you want projection? [Y/n] ")
    if (projection == "Y" or projection == "y"):
        createfolder(os.path.join(rootname, "model", "projection"))

    specification = input("you want specification? [Y/n] ")
    if (specification == "Y" or specification == "y"):
        createfolder(os.path.join(rootname, "specification"))

    dto = input("you want dto? [Y/n] ")
    if (dto == "Y" or dto == "y"):
        createfolder(os.path.join(rootname, "dto"))


rootname = input("Put the root folder name: ")

createStructFolders(rootname)