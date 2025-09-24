import sys
import hashlib # library to hash passwords
with open('/home/bokuto/Downloads/10-million-password-list-top-100.txt','r') as f:
    passwords=f.read().splitlines()
# print(passwords)
uhlist=[]
with open('usrname&hash.txt','r') as u:
    username=u.read().splitlines()
    for a in username:
        usrhash=a.split(":")
        uhlist.append(usrhash)
uh2=uhlist
# pas = "summer"
# hash= hashlib.sha256(pas.encode('utf-8'))
# print(hash.hexdigest())
for a in uh2:
    for pas in passwords:   
        hash= hashlib.sha256(pas.encode('utf-8')).hexdigest()
        if(hash==a[1]):
            print(f"[+] Password for user '{a[0]}' is {pas}")
            break    

