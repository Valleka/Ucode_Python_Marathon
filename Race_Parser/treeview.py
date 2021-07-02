def to_view(data, tree, extension, parent):
    # print(data)
    if parent == '':
        head = tree.insert(parent='', index='end', text=f"0")
    for d in data:
        if not isinstance(d, dict):
            if parent != '':
                node = tree.insert(parent, 'end', text=d)
            else:
                node = tree.insert(head, 'end', text=d)
        # node = tree.insert(head, 'end', text=d)
        # print(d)
        if isinstance(data, dict):
            # print(data[d])
            # i += 1
            if isinstance(data[d], list):
                for it in data[d][0]:
                    # print(data[d][0][it])
                    if isinstance(data[d][0][it], dict):
                        item = data[d][0][it]
                        dictnode = tree.insert(node, 'end', text=it)
                        to_view(item, tree, extension, dictnode)

                    else:
                        nodein = tree.insert(node, 'end', text=it)
                        tree.insert(nodein, 'end', text=data[d][0][it])
            else:
                for it in data[d]:
                    print(it)
                    dit = tree.insert(node, 'end', text=it)
                    tree.insert(dit, 'end', text=data[d][it])
        else:
            for it in data:
                for i in it.items():
                    if isinstance(i[1], dict):
                        item = i[1]
                        dictnode = tree.insert(head, 'end', text=i[0])
                        to_view(item, tree, extension, dictnode)
                    else:
                        dit = tree.insert(head, 'end', text=i[0])
                        tree.insert(dit, 'end', text=i[1])
