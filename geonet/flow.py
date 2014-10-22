'''
Utilities for network flow
'''

import networkx as nx
import numpy as np
import scipy as sp

def find_arc_flow(net, demand):
    '''Determine flow on arcs.

    Values are unique for tree networks.

    net: a (tree) network
    demand: maps node IDs to demand (or supply if negative)
    '''

    assert sum(demand.values()) == 0.0, 'flow not balanced'

    # TODO: is this still necessary?
    nods = sorted(net.dg.nodes())
    edgs = sorted(net.dg.edges())
    
    im = nx.incidence_matrix(net.dg, nodelist=nods, edgelist=edgs, oriented=True)
    im = im[1:, :] # skip any (redundant) row
    
    dem = np.array([demand.get(n, 0.0) for n in nods])
    dem = dem[1:] # skip same (redundant) row

    sol = sp.sparse.linalg.spsolve(im, dem)
    return dict(zip(edgs, sol))
