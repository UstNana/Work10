import xml.etree.ElementTree as ET

tree = ET.parse("filexml.xml")
items = tree.findall("channel/item")
print(len(items))
for item in items:
  list_xml = []
  list_xml = item.find("description").text
  print(list_xml)
  for element in list_xml:
    frequency = {}
    count = frequency.get(element,0)
    frequency[element] = count + 1
    print(frequency)
frequency_list = frequency.keys()
for element in frequency_list:
  if len(element) > len(shortest):
    shortest = element
    print (element, frequency[element])
