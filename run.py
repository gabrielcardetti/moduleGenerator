import os
from string import Template

path = os.getcwd()

print ("The current working directory is %s" % path)

def createfolder(name):
    try:
        os.mkdir(name)
    except OSError:
        print ("Creation of the directory %s failed" % name)

def create(rootname):
    subfolders =["controller", "model", "service", "repository"]

    createfolder(rootname)

    for subfolder in subfolders:
        createfolder(os.path.join(rootname, subfolder))
    
    createfolder(os.path.join(rootname, "service", "impl"))
    createModel()
    createRepository()
    createService()
    createServiceImpl()

    projection = input("you want projection? [Y/n] ")
    if (projection == "Y" or projection == "y"):
        createfolder(os.path.join(rootname, "model", "projection"))

    specification = input("you want specification? [Y/n] ")
    if (specification == "Y" or specification == "y"):
        createfolder(os.path.join(rootname, "specification"))

    dto = input("you want dto? [Y/n] ")
    if (dto == "Y" or dto == "y"):
        createfolder(os.path.join(rootname, "dto"))
        createDto()
    return

def createFiles(data):
    #open the file
    filein = open( './templates/'+data['template_name']+'.txt' )
    #read it
    src = Template( filein.read() )
    #document data
    #do the substitution
    result = src.substitute(data)
    try:
        new_file = open(data['path_file'], 'w+')
        new_file.write(result)
        new_file.close()
    except:
        print ("error with FILE")

def createDto():
    file_name = Module_Name+"Dto"
    path_file = os.path.join(path, module_name, 'dto' , file_name+'.java')
    dto = {
        "module_name": module_name,
        "file_name": file_name,
        "path_file": path_file,
        "template_name": "dto"
    }
    createFiles(dto)

def createModel():
    file_name = Module_Name
    path_file = os.path.join(path, module_name, 'model' , file_name+'.java')

    extends_model = input("model extends of BaseOrganizationEntity or BaseEntity [1/2]: ")
    if(extends_model == '1'):
        extends_model = "BaseOrganizationEntity"
    if(extends_model == '2'):
        extends_model = "BaseEntity"

    model = {
        "extends_model": extends_model,
        "module_name": module_name,
        "file_name": file_name,
        "path_file": path_file,
        "template_name": "model"
    }
    createFiles(model)

def createRepository():
    file_name = Module_Name+'Repository'
    path_file = os.path.join(path, module_name, 'repository' , file_name+'.java')

    repository = {
        "model_uri": resolveUri("model", ""),
        "model_name": Module_Name,
        "module_name": module_name,
        "file_name": file_name,
        "path_file": path_file,
        "template_name": "repository"
    }
    createFiles(repository)

def createService():
    file_name = Module_Name+'Service'
    path_file = os.path.join(path, module_name, 'service' , file_name+'.java')

    service = {
        "model_uri": resolveUri("model", ""),
        "model_name": Module_Name,
        "module_name": module_name,
        "file_name": file_name,
        "path_file": path_file,
        "template_name": "service"
    }
    createFiles(service)

def createServiceImpl():
    file_name = Module_Name+'ServiceImpl'
    path_file = os.path.join(path, module_name, 'service/impl' , file_name+'.java')

    serviceimpl = {
        "model_uri": resolveUri("model", ""),
        "repository_uri": resolveUri("repository", "Repository"),
        "service_uri": resolveUri("service", "Service"),
        "service_name": Module_Name+'Service',
        "repository_name": Module_Name+'Repository',
        "repository_var": Module_Name[0].lower()+Module_Name[1:]+'Repository',
        "model_name": Module_Name,
        "module_name": module_name,
        "file_name": file_name,
        "path_file": path_file,
        "template_name": "serviceimpl"
    }
    createFiles(serviceimpl)


    
def resolveUri(module_type, ext):
    return module_name+'.'+module_type+'.'+Module_Name+ext


module_name = input("Ingresa el nombre del modulo en miniscula: ")
Module_Name = input("Ingresa el nombre del modulo en  miniscula y mayuscula: ")

create(module_name)
