class Graph:
    def __init__(self, sodinh: int):
        self.sodinh = sodinh
        self.socanh = 0
        self.graph = {}
        self.chech_vertex = {}
        self.degree_graph = {}
        self.vertex_color = []
        self.init_graph()

    
    def init_graph(self) -> None:
        
        for dinh in range(self.sodinh):
            self.graph[str(dinh)] = []
        
        for dinh in range(self.sodinh):
            self.chech_vertex[str(dinh)] = False

        for i in range(self.sodinh):
            self.vertex_color.append(-1)

    def add_edge(self, vertex_one: int, vertex_two: int) -> None:
        self.socanh += 1
        self.graph[str(vertex_one)].append(vertex_two)
        self.graph[str(vertex_two)].append(vertex_one)

    def get_graph(self) -> dict:
        return self.graph

    def get_sodinh(self) -> int:
        return self.sodinh
    
    def get_socanh(self) -> int:
        return self.socanh

    def explore(self, firstV = int):
        self.chech_vertex[str(firstV)] = True
        
        print(str(firstV))
        print(self.graph[str(firstV)])
        for ele in self.graph[str(firstV)]:
            if self.chech_vertex(str(firstV)) == False:
                self.explore(str(ele))

    def exploreStack(self, firstV: int):
        stack = []
        stack.append(firstV)
        self.chech_vertex[str(firstV)] = True

        while(len(stack) >= 1):
            vertex = stack[-1]
            stack.pop(-1)
            print(vertex)

            for ele in self.graph[str(vertex)]:
                if self.chech_vertex(str(ele)) == False:
                    stack.append(ele)
                    self.chech_vertex[str(ele)] = True
                    return stack

    def degree(self): 
        for x, y in self.graph.items():
            self.degree_graph[x] = len(y)
        return self.degree_graph

    def get_color(self):
        return self.vertex_color