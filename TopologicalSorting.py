import copy


class TopologicalSorting:
    '''
    Reads in the specified input file containing
    adjacent edges in a directed graph and constructs an
    adjacency list.

    The adjacency list is a dictionary that maps
    a vertex to its adjacent vertices.
    '''

    def __init__(self, fileName):
        # file name
        self.name = fileName

        graphFile = open(fileName)

        '''
        create an initially empty dictionary representing
        an adjacency list of the graph
        '''
        self.adjacencyList = {}

        '''
        collection of vertices in the graph (there may be duplicates)
        '''
        self.vertices = []
        self.paths = 0

        for line in graphFile:
            '''
            Get the two vertices
        
            Python lets us assign two variables with one
            assignment statement.
            '''
            (firstVertex, secondVertex) = line.split()

            '''
            Add the two vertices to the list of vertices
            At this point, duplicates are ok as later
            operations will retrieve the set of vertices.
            '''
            self.vertices.append(firstVertex)
            self.vertices.append(secondVertex)

            '''
            Check if the first vertex is in the adjacency list.
            If not, add it to the adjacency list.
            '''
            if firstVertex not in self.adjacencyList:
                self.adjacencyList[firstVertex] = []

            '''
            Add the second vertex to the adjacency list of the first vertex.
            '''
            self.adjacencyList[firstVertex].append(secondVertex)

        # creates and sort a set of vertices (removes duplicates)
        self.vertices = list(set(self.vertices))
        self.vertices.sort()

        # sort adjacency list for each vertex
        for vertex in self.adjacencyList:
            self.adjacencyList[vertex].sort()

        # sorted list
        self.sortedList = []

    def print_and_save(self):
        # print(self.vertices)
        # print(self.adjacencyList)
        self.sort()
        print(self.sortedList)
        with open('result_' + str(self.name), 'w') as file_handler:
            for node in self.sortedList:
                file_handler.write("{}\n".format(node))

                # Topological sorting using decrease-by-one-and-conquer.

    def sort(self):
        # Your code goes here:
        #print(self.vertices)
        #print(self.adjacencyList)

        while self.vertices:
            parent = []
            children = set()
            keys_to_delete = set()

            for vertex in self.vertices:
                parent.append(vertex)
                if vertex in self.adjacencyList:
                    children.update(self.adjacencyList[vertex])
            #print(parent)
            #print(children)

            # this removed all leaves
            '''for key in self.adjacencyList:
                for value in self.adjacencyList[key]:
                    if value not in parent:
                        tree[key].remove(value)
                        #print("Removed", value)
                    #else:
                        #print(value)'''

            # remove all parents without any parents
            for p in parent:
                if p not in children:
                    self.sortedList.append(p)
                    keys_to_delete.add(p)

            #print(keys_to_delete)
            for key in keys_to_delete:
                self.vertices.remove(key)
            #print()


    # How many different ways can the spider reach the fly by moving along the web’s lines in the directions indicated by the arrow?
    def spider(self, start, end):
        if start in self.adjacencyList: #assume that the spider is on the web
            for vertex in self.adjacencyList[start]:
                self.spider(vertex, end)
        else:
            self.paths += 1
        return self.paths


if __name__ == "__main__":
    s = TopologicalSorting("graph_example.txt")
    s.print_and_save()

    # Be careful! graph-courses.txt is incomplete. Please finish this txt file at first. 
    s = TopologicalSorting("graph_courses.txt")
    s.print_and_save()

    s = TopologicalSorting("graph_spider.txt")
    s.print_and_save()

    print(s.spider(s.sortedList[0], s.sortedList[-1]))