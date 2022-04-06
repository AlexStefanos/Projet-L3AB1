import os, shutil, glob
import subprocess, time, webbrowser

pathGlob = glob.glob('/home/alexandre/Projet-L3AB1/BLOCKCHAINEXPLORER/datas/*')
if(os.path.exists('/home/alexandre/Projet-L3AB1/BLOCKCHAINEXPLORER/datas')):
   for f in pathGlob:
      if(os.path.isfile(f)):
         os.remove(f)
      if(os.path.isdir(f)):
         shutil.rmtree(f)
processMongoDB = subprocess.Popen(["mongod", "--dbpath", "datas/"])
processDjango = subprocess.Popen(["python3", "manage.py", "runserver"])
time.sleep(8)
webbrowser.open('http://127.0.0.1:8000/')
time.sleep(5)
close = int(input("Si vous voulez fermer le site, tapez 1"))
if(close == 1):
   processMongoDB.kill()
   processDjango.kill()
   if(os.path.exists('/home/alexandre/Projet-L3AB1/BLOCKCHAINEXPLORER/datas')):
      for f in pathGlob:
         if(os.path.isfile(f)):
            os.remove(f)
         if(os.path.isdir(f)):
            shutil.rmtree(f)