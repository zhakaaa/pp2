import json 
f = open("sample-data.json","r").read()
y = json.loads(f)

print("Interface Status\n============================================================================\nDN                                         Description      Speed     MTU\n------------------------------------------ ---------------- -------   -----\n")
for i in y["imdata"] :
    for j in i.values() :
        for k in  j.values() :
            print(k["dn"],"               ", k["descr"] , k["speed"],"  ", k["mtu"])