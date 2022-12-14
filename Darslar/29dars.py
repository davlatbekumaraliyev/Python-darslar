import json


# x = 10
# x_json = json.dumps(x)

# y = 5.5
# y_json = json.dumps(y)

# m = True
# m_json = json.dumps(m)



# f = 'alimov'
# f_json = json.dumps(f)
# ism_json = json.dumps('olimbek')





bemor = {
    'ism': 'Alijon Valiyev', 
    'yosh': 30,
    'oila': True,
    'farzandlar': ('Olim', 'Bonu'), 
    'allergiya': None,
    'dorilar': [
        {'nomi': 'Tremol', 'miqdori': 0.5},
        {'nomi': 'Panadol', 'miqdori': 1.2}
        ],
}

# sonlar = (12, 34, 56, 78, 90)

# bemor_json = json.dumps(bemor)
# # print(bemor_json)

with open('bemor.json', 'w') as f:
    json.dump(bemor, f)

# with open('sonlar2.json', 'w') as f2:
#     json.dump(sonlar, f2)

# son2 = json.loads(sonlar_json)

# m2 = json.loads(m_json)

filename = 'bemor.json'
with open(filename) as f:
    bemor = json.load(f)
print(bemor)
print(type(bemor))







