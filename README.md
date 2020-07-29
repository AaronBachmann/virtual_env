# Creating Virtual Environments for Python with Anaconda #

Show conda environments:  
**conda env list**

Create new conda virtual env:  
**conda create -n {name} python=3.7**

Switch to conda virtual environment:  
**conda activate {name}**

Make a clone of a virtual environment:    
**conda create --clone {name} --name {clone_name}**

List history of changes to environment:    
**conda list --revisions**

Restore environment to previous version:    
**conda install --revision {number}**

Delete an environment:    
**conda env remove --name {name}**

Deactivate current environment:    
**deactivate**



