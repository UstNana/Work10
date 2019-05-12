    
# -*- coding: utf-8 -*-
import json

d = {}
new_list = list
r = 0
with open("newsafr.json", encoding="utf8") as json_file:
      data_json = json.load(json_file)
      tems = data_json["rss"]["channel"]["items"]
      for elements in tems:
          for key, value in elements.items():
              if key == "description":

                for key in reversed(sorted(value.split())):
                  if key:
                    word = key
                    r += 1
                  if word not in d.keys():
                    d[word] = []
                  d[word].append(r)
list_i = list
for key, value in d.items():
  sort_d = sorted([(key, len(key)) for (key,value) in d.items()])
#print(w)
shortest = ""
for numbers in sort_d:
  if len(numbers[0]) > len(shortest):
    shortest = numbers[0]
    print(shortest)
