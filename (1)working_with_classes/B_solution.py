import json
import re
s1 = "max_value         | Sorceress	| Knight  | Barbarian | Warlock\n"
s2 = "----------------------------------------------------------\n"
s3 = "max_health        | 50        | 100     | 120       | 70\n"
s4 = "----------------------------------------------------------\n"
s5 = "max_defence_power | 42        | 170     | 150       | 50\n"
s6 = "----------------------------------------------------------\n"
s7 = "max_attack_power  | 90        | 150     | 180       | 100\n"
s8 = "----------------------------------------------------------\n"
s9 = "max_mana          | 200       | -       | -         | 180"
s = s1 + s2 + s3 + s4 + s5 + s6 + s7 + s8 + s9
s = s.split('\n')
f = re.split('(\t)|( )', s[0])
h = []
dick = {}

for x in f:
    if x is None:
        continue
    if (len(x) > 1):
        h.append(x.split("_power")[0])

for i in range(1, len(s)):
    if (i % 2 == 1):
        continue
    l = s[i].split(' ')
    d = []
    for x in l:
        if len(x) > 1 or x == "-":
            d.append(x)
    d[0] = d[0].split("max_")[1]
    what = d[0].split("_power")[0]
    for j in range(1, len(d)):
        if d[j] == '-':
            d[j] = 0
        can = False
        for k in dick.keys():
            if k == h[j]:
                can = True
                break
        if can is False:
            dick[h[j]] = {}
        dick[h[j]][what] = int(d[j])

a = json.loads(open("input.txt", "r").read())
for i in range(len(a["battle_steps"])):
    id_from = a["battle_steps"][i]['id_from']
    id_to = a["battle_steps"][i]['id_to']
    power = a["battle_steps"][i]['power']
    action = a["battle_steps"][i]['action']
    if (a["armies"][id_from]["health"] <= 0):
        continue
    if action == "attack":
        a["armies"][id_from]["attack"] -= power
        val_d = min([power, a["armies"][id_to]["defence"]])
        a["armies"][id_to]["defence"] -= val_d
        power -= val_d
        a["armies"][id_to]["health"] -= power
        if (a["armies"][id_to]["health"] <= 0):
            a["armies"][id_from]["experience"] += 5
        else:
            a["armies"][id_from]["experience"] += 1
            a["armies"][id_to]["experience"] += 1
    elif action == "cast_health_spell":
        a["armies"][id_from]["mana"] -= power
        if a["armies"][id_to]["health"] <= 0:
            continue
        val1 = dick[a["armies"][id_to]["race"]]["health"]
        val2 = a["armies"][id_to]["health"] + power
        a["armies"][id_to]["health"] = max([val1, val2])
        a["armies"][id_from]["experience"] += 1.
    else:
        a["armies"][id_from]["mana"] -= power
        val_d = min([power, a["armies"][id_to]["defence"]])
        a["armies"][id_to]["defence"] -= val_d
        power -= val_d
        a["armies"][id_to]["health"] -= power
        if (a["armies"][id_to]["health"] <= 0):
            a["armies"][id_from]["experience"] += 5
        else:
            a["armies"][id_from]["experience"] += 1
            a["armies"][id_to]["experience"] += 1

win = {"Ronald": 0, "Archibald": 0}
for x in a["armies"].items():
    x = x[1]
    if x["health"] <= 0:
        continue
    win[x["lord"]] += x["experience"] + x["defence"] * 2 + x["attack"] * 3
    can = False
    for k in x.keys():
        if k == "mana":
            can = True
            break

    if can is True:
        win[x["lord"]] += x["mana"] * 10

name = "Ronald"
if win["Archibald"] > win[name]:
    name = "Archibald"
elif win["Archibald"] == win[name]:
    name = "unknown"
print(name)
