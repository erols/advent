
class CircularLinkedList:
    def __init__(self):
        self.head = None

    def traverse(self, starting_point=None):
        if starting_point is None:
            starting_point = self.head
        node = starting_point
        while node is not None and (node.next != starting_point):
            yield node
            node = node.next
        yield node

    def print_list(self, starting_point=None):
        nodes = []
        for node in self.traverse(starting_point):
            nodes.append(str(node))
        print(" -> ".join(nodes))


slope_map = []

with open('input3') as data:
    for line in data:
        slope_map.append(list(line.strip('\n')))
    slope_map.append('-------------------------------')

print(slope_map)

map_end = True
cursor = 1
trees = 0
for s in len(slope_map):
    s = s + 1
    if slope_map[s][cursor + 3] == '#':
        trees = trees + 1
    elif slope_map[s][cursor + 3] == '-':
        map_end = False

print("Number of trees is", trees)


