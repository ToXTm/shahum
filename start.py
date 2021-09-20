import os
import re
import json
from sys import path


v = str(os.system("sudo python3.6 -V"))

os.system("sudo chmod +x *")

if re.search(v,"3.6.13"):
    print(True)
else:
    os.system("sudo ./install.sh")
    os.system("cd "+str(path[0]))
os.system("sudo python3.6 -m pip install setuptools")
os.system("sudo python3.6 -m pip install requests")
os.system("sudo python3.6 -m pip install pyrogram")
os.system("sudo python3.6 -m pip install redis")
os.system("sudo python3.6 -m pip install redis-server")
os.system("sudo systemctl enable redis-server.service")
os.system("sudo service redis-server start")
os.system("sudo python3.6 -m pip install pyTelegramBotAPI")
os.system("sudo python3.6 -m pip install tgcrypto")
os.system("sudo python3.6 -m pip install collections")
os.system("sudo python3.6 -m pip install asyncio")
os.system("sudo python3.6 -m pip install sqlite3")

if os.path.exists(str(path[0])+"/utils/config.py"):
    print(True)
else:
    token = str(input("+ Enter Your Bot Token Here :- "))
    print("===========================================")
    sudo = str(input("+ Enter Your Sudo Id Here :- "))
    sp = token.split(sep=":")
    bot_id = str(sp[0])
    f = open("utils/config.py","w")
    f.write("""
token='{}'
sudo='{}'
bot_id='{}'
    """.format(token,sudo,bot_id))
    f.close()
    os.system("clear")

os.system("screen -S python-media ./ts.sh")
