import re
with open ('/home/bokuto/Documents/access.log.20171103','r') as o:
    text=o.readlines()

pattern1=r'\w"\s4\d{2}\s'
pattern2=r'\w"\s5\d{2}\s'
pattern3=r"GET\s+/admin[^\s]*\s+HTTP/\d\.\d"
pattern4=r"GET\s+[^\s]*/admin[^\s]*\s+HTTP/\d\.\d"
pattern5=r"GET\s+[^\s]*/passw[^\s]*\s+HTTP/\d\.\d"
pattern6=r"GET\s+[^\s]*/login[^\s]*\s+HTTP/\d\.\d"
pattern7=r"GET\s+/login[^\s]*\s+HTTP/\d\.\d"
pattern8=r"\sHTTP/"
pattern9=r"[0-9]+\n"
for line in text:
    if(re.search(pattern9,line)):
        l=re.search(pattern9,line)
        sta=l.start()
        end=len(line)-1
        data=int(line[sta:end])
        if(data > 500000):
            print(f"SUS : {line}  --- < WAY BIG FILE >")

    if(re.search(pattern1,line) or re.search(pattern2,line)):
       print(f"ERROR : {line}  --- < RED FLAG >")

    if(re.search(pattern3,line) or re.search(pattern4,line) or re.search(pattern5,line) or re.search(pattern6,line) or re.search(pattern7,line)):
        print(f"WARNING : {line}  --- < UNUSUAL REQUESR >")

    if(re.search(pattern8,line) == None):
        print(f"OLD : {line}  --- < MISSING OR OLD FILES >")