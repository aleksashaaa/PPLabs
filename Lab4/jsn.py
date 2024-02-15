import json

file = open("sample_data.json")

f_json = file.read()
f = json.loads(f_json)

print("Interface Status\n================================================================================")
print("DN                                                 Description           Speed    MTU  \n-------------------------------------------------- --------------------  ------  ------")
for i in f["imdata"]:
    print(f'{i["l1PhysIf"]["attributes"]["dn"]}\t\t\t\t{i["l1PhysIf"]["attributes"]["speed"]}\t  {i["l1PhysIf"]["attributes"]["mtu"]}')