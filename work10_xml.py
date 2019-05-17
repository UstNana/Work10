import xml.etree.ElementTree as ET

frequency = {}
n = {}
tree = ET.parse("filexml.xml")
items = tree.findall("channel/item")
print(len(items))
for item in items:
  list_xml = []
  list_xml = item.find("description").text
  for word in list_xml.split():
    if word not in frequency.keys():
      frequency[word] = 1
    else:
      frequency[word] += 1

for key, value in frequency.items():
    if len(key) >= 6:
      n[key] = value
      k = sorted(n.items(), key=lambda x: x[1], reverse=True )
      if len(k) <= 10:
        print(k)
