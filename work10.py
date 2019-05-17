  import json

d = {}
n = {}
descript = []
new_list = list
r = 0
with open("news.json", encoding="utf8") as json_file:
      data_json = json.load(json_file)
      tems = data_json["rss"]["channel"]["items"]
      for elements in tems:
          descript = elements["description"]

          for word in descript.split():
            if word not in d.keys():
              d[word] = 1
            else:
              d[word] += 1

for key, value in d.items():
    if len(key) >= 6:
      n[key] = value
      k = sorted(n.items(), key=lambda x: x[1], reverse=True )
      if len(k) <= 10:
        print(k)
