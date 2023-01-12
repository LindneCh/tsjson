
import json
#öffnet die Datei

# Aufgabe:
# 1. neue datei json.py
# 2. Import json 
# 3. print json
# 4. upload to github


print("")
print("Aufgabe json wir ausgegeben: ")
print("")
#data = json.load(open("accounts.json"))

with open("accounts.json", "r") as f:
  #lade die Json.Daten aus der Datei
  
  data = json.load(f)
  #print(f)
  #print(json.dumps(json.load(f), indent=4))
for account in data:
  print("Der Name ist:", account["name"])

##