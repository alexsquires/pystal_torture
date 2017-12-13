from crystal_torture.node import  Node
import copy

class Cluster:
    """
    Cluster class: group of connected nodes within graph
    """

    def __init__(self,nodes):
        """
        Initialise a cluster.

        Args:
            nodes (set(Node)): set of nodes in the cluster.
        """

        self.nodes = nodes
        self.periodic = [False, False, False]

    def merge(self, other_cluster):
        """
        Merge two clusters into one
 
        Args:
            other_cluster (Cluster): cluster to be joined
        """
        
        new_cluster =  Cluster(self.nodes|other_cluster.nodes )
        

        return new_cluster

    def is_neighbour(self, other_cluster):
        """
        Check if one cluster of nodes is connected to another
        """

        return bool( self.nodes & other_cluster.nodes ) 

    def grow_cluster(self):
        """
        Grow cluster by adding neighbours
 
        Args:
            None
        """

        nodes_to_visit = [ self.nodes.pop() ]
        visited = set()       

        while nodes_to_visit:
            node = nodes_to_visit.pop(0)
            
            if node not in visited:
               nodes_to_visit += [ node for node in node.neighbours ]
            visited.add(node)             
        
        self.nodes = visited

 
