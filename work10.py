# -*- coding: utf-8 -*-
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
        t = {i.casefold() for i in descript.split()}
        for word in descript.split():
          if len(word) >= 6:
            if word.casefold() in t:
              if word in d.keys():
                d[word.casefold()] += 1
              else:
                d[word.casefold()] = 1
             
for key, value in d.items():
      n[key] = value
      k = sorted(n.items(), key=lambda x: x[1], reverse=True )
      print(k)
