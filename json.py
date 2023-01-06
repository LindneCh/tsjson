import json
print("")
print("Aufgabe json wir ausgegeben: ")
print("")
#data = json.load(open("accounts.json"))

with open("tsjson/accounts.json", "r") as f:
  f = json.load(f)
  print(f)
  #print(json.dumps(json.load(f), indent=4))

## Fehler ausgabe, warum? vielleicht Klammernproblem in accounts.json {}