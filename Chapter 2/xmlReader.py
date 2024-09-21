from xml.etree import ElementTree

with open("./pokemonXml.xml") as f:
    doc = ElementTree.parse(f)

    for node in doc.findall("row"):
        print(f"id: {node.find('id').text}")
        print(f"name: {node.find('name').text}")
        print(f"type: {node.find('type').text}")
        print(f"typeTwo: {node.find('typeTwo').text}")
        print("-"*40)
