import hashlib # library to hash passwords

with open('/***/****/**/10-million-password-list-top-100.txt','r') as f:   #opening password_list file
    passwords=f.read().splitlines()

uhlist=[]
with open('usrname&hash.txt','r') as u:
    username=u.read().splitlines()
    for a in username:
        usrhash=a.split(":")
        uhlist.append(usrhash)

for a in uhlist:
    for pas in passwords:   
        hash= hashlib.sha256(pas.encode('utf-8')).hexdigest()
        if(hash==a[1]):
            print(f"[+] Password for user '{a[0]}' is {pas}")
            break    

