import os, shutil, glob
import subprocess, time, webbrowser
import platform

monOS = platform.system()
pathGlob = glob.glob('datas/*')
if(os.path.exists('datas')):
   for f in pathGlob:
      if(os.path.isfile(f)):
         os.remove(f)
      if(os.path.isdir(f)):
         shutil.rmtree(f)
if(monOS == 'Linux' or monOS == 'Darwin'):
   processMongoDB = subprocess.Popen(["mongod", "--dbpath", "datas/"], stderr = subprocess.DEVNULL)
   time.sleep(5)
processDjango = subprocess.Popen(["python3", "manage.py", "runserver"], stdout = subprocess.DEVNULL, stderr = subprocess.DEVNULL)
time.sleep(8)
webbrowser.open('http://127.0.0.1:8000/')
close = 0
while(close != 1):
   time.sleep(5)
   close = int(input("Si vous voulez fermer le site, tapez 1\n"))
if(close == 1):
   if(monOS == 'Linux' or monOS == 'Darwin'):
      processMongoDB.kill()
   processDjango.kill()
   if(os.path.exists('datas')):
      for f in pathGlob:
         if(os.path.isfile(f)):
            os.remove(f)
         if(os.path.isdir(f)):
            shutil.rmtree(f)
