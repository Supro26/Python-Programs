import dns.resolver
import threading
import time
import sys
subdom=sys.argv[1]
try:
    with open(f"{subdom}","r") as file:
        words=file.read().split()
except FileNotFoundError:
    print("Wordlist not found..")
    quit()
def enumerator(w):
    dom=sys.argv[2]
    try:
        result=dns.resolver.resolve(f'{w}.{dom}','A')
        if result:
            print(f"FOUND    |    '{w}'")
    except:
        pass       
print("--STARTING THE PROCESS--")
time.sleep(2)
thread_list=[]
for i in range(999):
    t=threading.Thread(target=enumerator, args=[words[i]])
    thread_list.append(t)
for t in thread_list:
    t.start()
