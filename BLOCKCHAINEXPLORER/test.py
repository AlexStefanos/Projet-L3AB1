import os, shutil, glob
import subprocess

pathGlob = glob.glob('/home/alexandre/Projet-L3AB1/BLOCKCHAINEXPLORER/datas/*')
if(os.path.exists('/home/alexandre/Projet-L3AB1/BLOCKCHAINEXPLORER/datas')):
   for f in pathGlob:
      if(os.path.isfile(f)):
         os.remove(f)
      if(os.path.isdir(f)):
         shutil.rmtree(f)
subprocess.Popen(["mongod", "--dbpath", "datas/"])
subprocess.Popen(["python3", "manage.py", "runserver"])