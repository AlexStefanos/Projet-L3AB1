import os, platform

monOS = platform.system()
if(monOS == 'Linux' or monOS == 'Darwin'):
    os.system('sudo apt install python3-pip')
os.system('pip install djangorestframework')
os.system('pip install requests')
os.system('pip install djongo')
os.system('pip install pymongo==3.12.1')
if(monOS == 'Linux' or monOS == 'Darwin'):
    os.system('sudo apt-get install npm')
if(monOS == 'Linux' or monOS == 'Darwin'):
    os.system('npm install bootstrap')
os.system('pip install dnspython')
os.system('pip install seaborn')
os.system('pip install django-rest-swagger')
os.system('pip install pyyaml')
os.system('pip install uritemplate')
os.system('pip install plotly==5.7.0')