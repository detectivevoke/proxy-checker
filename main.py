import requests
import json
import random
import time
try:
    import threading
except:
    print("Install threading! (pip install threading)")
try:
    import os
except:
    pass

class Checker:
    def __init__(self):
        self.config = json.loads(open("config.json","r").read())
        

        self.threads = int(self.config["threads"])
        self.timeout = int(self.config["timeout"])
        self.test_url = self.config["test_url"]

        self.alive = 0
        self.dead = 0
        self.check = []

        

    def checker(self):
        try:
            os.system("cls")
        except:
            pass
        
        self.file_name = self.config["file_name"]

        if not self.file_name:
            print("{} is not a file!".format(self.file_name))
            return ""
        else:
            pass
        
        self.proxy_type = self.config["proxy_type"]

        os.system("cls")

        with open(self.file_name, "r") as f:
            self.count = sum(1 for proxy in f)
            print("Loaded {} proxies!".format(self.count))
        with open(self.file_name, "r+") as f:
            lines = f
            for proxy in lines:
                self.check.append(proxy.strip("\n"))
        threads = []
        
        for i in range(self.threads):
            threads.append(threading.Thread(target=self.check_proxies))
            threads[i].setDaemon(True)
            threads[i].start()

        self.checking = True

        while self.checking:
            if len(threading.enumerate())-1==0:
                self.checking = False
            else:
                os.system("title "+f"""Detective Voke#9732 - Working: {self.alive} - Not Working: {self.dead}""")


    def check_proxies(self):
        while len(self.check) > 0:
            proxy = self.check[0]
            self.check.pop(0)
            try:
                r= requests.get(self.test_url, proxies={"https": "http://{}".format(proxy)},timeout=int(self.timeout))
            except:self.dead = self.dead + 1
            else:
                print("Proxy Working ({}) - Time Taken: {}".format(proxy, r.elapsed))
                self.alive = self.alive + 1
                with open("checked.txt","a") as w:
                    w.write(proxy+"\n")




r = Checker()
r.checker()