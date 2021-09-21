import requests
from utils.config import token,bot_id,sudo
import pyrogram
from requests import get
from sys import path
import redis


data = redis.Redis("127.0.0.1",6379)

def bot(method: str,datas: dict = None):
    if type(datas).__name__ == "dict":
        r = requests.post(f"https://api.telegram.org/bot{token}/{method}",data=datas)
    else:
        r = requests.get(f"https://api.telegram.org/bot{token}/{method}")
    return r.json()

channel_id = str(data.get(bot_id+"-mediapy-channel").decode()) if data.get(bot_id+"-mediapy-channel") else None

def channel(user_id=None):
    if user_id == None or channel_id == None:
        return True
    else:
        try:
            url = get("https://api.telegram.org/bot{}/getChatMember?chat_id={}&user_id={}".format(token,channel_id,str(user_id))).json()['result']['status']
            res = True if str(url) == "creator" or str(url) == "administrator" or str(url) == "member" else False
            return res
        except Exception:
            return False

def motors(user_id):
    if str(user_id) == str(sudo) or data.sismember(bot_id+"-mediapy-motor",str(user_id)):
        return True
    else:
        return False

def sudos(chat_id,user_id):
    if motors(user_id) or str(bot("getChatMember",{"chat_id":chat_id,"user_id":user_id})['result']['status']) == "creator":
        return True
    else:
        return False

def manager(chat_id,user_id):
    if sudos(chat_id,user_id) or data.sismember(bot_id+"-mediapy-su-"+str(chat_id),str(user_id)):
        return True
    else:
        return False

def admins(chat_id,user_id):
    if manager(chat_id,user_id) or data.sismember(bot_id+"-mediapy-sudos-"+str(chat_id),str(user_id)):
        return True
    else:
        return False

api_id = 1543684

api_hash = "763a60d1e12f79b9794c918d7c90b0da"

app = pyrogram.Client(session_name=path[0]+"/"+str(bot_id)+"mediapy",api_id=api_id,api_hash=api_hash,bot_token=token)

