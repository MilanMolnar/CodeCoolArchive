import json
from treelib import Tree


def json_read(filePath):
    with open(filePath) as f:
        data = json.load(f)
    return data


def convert(listOfDict_to_dict):
    list = []
    for index in range(len(listOfDict_to_dict)):
        for key in listOfDict_to_dict[index]:
            list.append(listOfDict_to_dict[index][key])
    it = iter(list)
    res_dct = dict(zip(it, it))
    return res_dct


def buildTree(dictOfDatas):
    tree = Tree()
    used_datas = []

    while dictOfDatas:
        for key, value in dictOfDatas.items():
            if value in used_datas:
                tree.create_node(key, key, parent=value)
                used_datas.append(key)
                dictOfDatas.pop(key)
                break
            elif value is None:
                tree.create_node(key, key)
                used_datas.append(key)
                dictOfDatas.pop(key)
                break
    tree.show()
    return tree.to_dict()

edges = []

def recursion_builTree(customDict, parent=None):
    loop = next(iter(customDict.keys()))
    if parent is not None:
        edges.append((parent, loop))
    for x in customDict[loop]['children']:
        if isinstance(x, dict):
            recursion_builTree(x, parent=loop)
        else:
            edges.append((loop, x))
    return edges


data = json_read('datas.json')
x = buildTree(convert(data))
result = recursion_builTree(x)
for row in result:
    print(' {0} --> {1} '.format(*row))





