  import json

d = {}
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

print(sorted(d.items(), key=lambda x: (len(x[0]), x[1]), reverse=True ))
print(sorted(d.items(), key=lambda x: x[1], reverse=True ))
