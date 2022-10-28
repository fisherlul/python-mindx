#inorder preorder postorder traversal
#prufer sequence
#coloring graph

from graph_class import Graph

a = Graph(10)

a.add_edge(0,1)
a.add_edge(1,4)
a.add_edge(1,5)
a.add_edge(1,6)
a.add_edge(1,2)
a.add_edge(2,3)
a.add_edge(2,7)
a.add_edge(3,4)
a.add_edge(3,8)
a.add_edge(4,5)
a.add_edge(4,9)
a.add_edge(6,7)
a.add_edge(7,8)

print(a.get_graph())
b = a.degree()
b =  {k: v for k, v in sorted(b.items(), key=lambda item: item[1], reverse=True)}
print(b)
c = a.get_color()
print(c)

