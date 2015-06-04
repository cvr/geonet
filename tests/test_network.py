from geonet.network import Net, SteinerTree

def test_Net():
    nodes = ['a', 'b', 'c', 'd']
    arcs = [('a', 'b'), ('b', 'c'), ('c', 'd'), ('a', 'c')]

    net = Net(nodes, arcs)
    assert set(net.get_nodes()) == set(nodes)
    assert set(net.get_arcs()) == set(arcs)

    assert net.get_degree('a') == 2
    assert net.get_degree('b') == 2
    assert net.get_degree('c') == 3
    assert net.get_degree('d') == 1

    assert set(net.get_neighbors('a')) == set('bc')
    assert set(net.get_neighbors('b')) == set('ac')
    assert set(net.get_neighbors('c')) == set('abd')
    assert set(net.get_neighbors('d')) == set(['c'])

def test_SteinerTree():
    nodes = ['a', 'b', 'c', 's']
    arcs = [('a', 's'), ('b', 's'), ('c', 's')]
    pos = {'a': (0,0), 'b': (1,0), 'c': (0,1)}

    tree = SteinerTree(nodes, arcs, pos)

    for n in 'abc':
        assert tree.is_terminal(n)
    assert tree.is_steiner('s')

    assert set(tree.get_terminal_nodes()) == set('abc')
    assert set(tree.get_steiner_nodes()) == set(['s'])

    assert tree.is_full_steiner_topology()

def test_full_steiner_tree():
    O = (0, 0)

    point = SteinerTree(['a'], [], {'a':O})
    assert point.is_full_steiner_topology()

    line = SteinerTree('ab', ['ab'], {'a':O, 'b':O})
    assert line.is_full_steiner_topology()

    path = SteinerTree('abs', ['as', 'sb'], {'a':O, 'b':O})
    assert not path.is_full_steiner_topology()

    star = SteinerTree('abcs', ['as', 'bs', 'cs'], {'a':0, 'b':O, 'c':O})
    assert star.is_full_steiner_topology()

    V = SteinerTree('abc', ['ab', 'bc'], {'a':0, 'b':O, 'c':O})
    assert not V.is_full_steiner_topology()

    H = SteinerTree('abcdst', ['as', 'bs', 'st', 'ct', 'dt'],
                    {'a':O, 'b':O, 'c':O, 'd':O})
    assert H.is_full_steiner_topology()

    X = SteinerTree('abcds', ['as', 'bs', 'cs', 'ds'],
                    {'a':O, 'b':O, 'c':O, 'd':O})

    assert not X.is_full_steiner_topology()
