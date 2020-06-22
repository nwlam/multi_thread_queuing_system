import json


data_raw = ['abcdef',
            'cdefab',
            #'bcaacdfe'
            ]


tree = {}


def recurr(sub_tree, suffix, curr_layer=0):
    if len(suffix) == 0:
        print(f'==> {sub_tree}')
        return sub_tree
    curr_node = suffix[0]
    print('================================')
    print(f'sub_tree: {sub_tree}')
    print(f'suffix: {suffix}')
    print(f'curr_layer: {curr_layer}')
    print(f'curr_node: {curr_node}')
    print('================================')
    if curr_node not in sub_tree:           #if no record
        sub_tree[curr_node] = {}            #make an empty subtree
    
    sub_tree[curr_node] = recurr(sub_tree[curr_node], suffix[1:], curr_layer+1)
    return sub_tree



#for i, d in enumerate(data_raw):


#recurr(tree, 'abcdefg')

#print(tree)

for i, d in enumerate(data_raw):
    for j in range(0, len(d)):
        tree = recurr(tree, d[j:])
print(json.dumps(tree, indent=4, ensure_ascii=False))