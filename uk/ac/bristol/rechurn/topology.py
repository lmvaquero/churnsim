import networkx as nx
import csv
import os.path
import collections

class Topology(nx.Graph):

    def load_from_csvs(self, nodes_csv, edges_csv):
        """
           This function generates a Graph object based on a list of nodes and a list of adjacency pairs
           inputs:
               nodes_csv: Absolute path to a CSV file with the following structure
                          Name,Historical Significance,Gender,Birthdate,Deathdate,ID
                          Joseph Wyeth,religious writer,male,1663,1731,10013191
                          Alexander Skene of Newtyle,local politician and author,male,1621,1694,10011149
               edges_csv: Absolute path to a CSV file with the following structure
                          Source,Target
                          George Keith,Robert Barclay
                          George Keith,Benjamin Furly
           return successful: boolean indicating whether the load of both files was successful or not
        """
        if (not(os.path.exists(nodes_csv) and os.path.isfile(nodes_csv)
                and os.path.exists(edges_csv) and os.path.isfile(edges_csv))):
            return False

        # Name,Historical Significance,Gender,Birthdate,Deathdate,ID
        node_headers = []

        with open(nodes_csv, 'r') as nodecsv:
            nodereader = csv.reader(nodecsv)
            node_headers = nodereader.next()
            nodes = [n for n in nodereader][1:]

        node_names = [n[0] for n in nodes]
        with open(edges_csv, 'r') as edgecsv:
            edgereader = csv.reader(edgecsv)
            edges = [tuple(e) for e in edgereader][1:]

        self.add_nodes_from(node_names)
        self.add_edges_from(edges)

        # load attributes of the nodes
        attributes = collections.defaultdict(dict)

        for i in range(1,len(node_headers)):
            for node in nodes:
                attributes[node_headers[i]][node[0]] = node[i]

        for i in range(1, len(node_headers)):
            nx.set_node_attributes(self, name=node_headers[i], values=dict(attributes[node_headers[i]]))

        return True


