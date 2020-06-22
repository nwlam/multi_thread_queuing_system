class tree(object):
    def __init__(self, val, next = None):
        self.next = next
        self.value = val
        self.children = []
    
    def add_child(self, obj):
        self.children.append(obj)


txt = {"aa", "ab", "ac"}

head = tree("Root")
current = head

L = list(txt)

for i in L: 
    starting = True
    temp = list(i)
    print(temp)
    
    for j in temp:
        if(starting):
            current = head
            starting=False
            if( not current.children or j not in current.children):
                current.add_child(j)
                item = tree(j)
                current.next=item
                print(current.next.value, "added to 1st level")
            elif(j in current.children):
                item = tree(j)
                current.next=item
                print(current.next.value, "already exist in 1st level")      

        else:
            current = current.next
            print("current val", current.value)
            if( not current.children or j not in current.children):
                current.add_child(j)
                item = tree(j)
                current.next=item
                print("current val's children", current.children)
                print(current.next.value, "added to 2nd level")
            elif(j in current.children):
                item = tree(j)
                current.next=item
                print(current.next.value, "already exist in 2nd level")


# print("1st lv")
# current = head
# print(current.value)
# print(current.children)

# current=current.next

# print("2nd lv")
# print(current.value)
# print(current.children)


# def recurse(){
#     #if

# }


# pointer = head

# while(pointer):
#     print(pointer.value)
#     print(pointer.children)
#     pointer = pointer.next
