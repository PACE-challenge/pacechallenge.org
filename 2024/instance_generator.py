#!/bin/python
import itertools
import random
import subprocess
import re

from itertools import product, chain, combinations
import click
import networkx as nx
import math
import numpy as np
from typing import TypeVar, TextIO, Tuple, List, Dict

from pace2024_verifier.pace import PaceGraph, write_graph, write_graph_cutwidth, read_graph

from alive_progress import alive_bar, alive_it


@click.group()
def cli():
    pass

@cli.command()
@click.option("-a", default=5, type=int, help="Size of left bipartition.")
@click.option("-b", default=5, type=int, help="Size of right bipartition.")
@click.option("-m", default=10, type=int, help="Number of edges.")
@click.option("-sl", is_flag=True, default=False, help="Shuffle left side")
@click.option("-sr", is_flag=True, default=False, help="Shuffle right side")
@click.argument("outfile", required=False)
def uniform(a, b, m, sl, sr, outfile):
    if not outfile:
        outfile = f"test_set/uniform-{a}-{b}-{m}.gr"
    all_edges = list(product(range(a), range(a,a+b)))
    edges = sorted(random.sample(all_edges, k=m))

    edges = shuffle(edges, a, b, sl, sr)
    graph = PaceGraph(a, b, edges)

    write_graph(graph,outfile)

@cli.command()
@click.option("-length", default=6, type=int, help="Number of vertices in cycle (must be even).")
@click.option("-sl", is_flag=True, default=False, help="Shuffle left side")
@click.option("-sr", is_flag=True, default=False, help="Shuffle right side")
@click.argument("outfile", required=False)
def cycle(length, sl, sr, outfile):
    if not outfile:
        outfile = f"test_set/cycle-{length}.gr"

    if length % 2 != 0:
        print("Odd cycles are not bipartite")
        return

    edges = []
    a = int(length/2)
    for i in range(a-1):
        edges.append([i,a+i])
        edges.append([i+1,a+i])
    edges.append([a-1,length-1])
    edges.append([0,length-1])

    edges = shuffle(edges, a, a, sl, sr)
    graph = PaceGraph(a, a, edges)

    write_graph(graph,outfile)

@cli.command()
@click.option("-length", default=6, type=int, help="Number of vertices in cycle (must be even).")
@click.option("-k", default=5, type=int, help="Number of flips")
@click.option("-sl", is_flag=True, default=False, help="Shuffle left side")
@click.option("-sr", is_flag=True, default=False, help="Shuffle right side")
@click.argument("outfile", required=False)
def cycle_flip(length, k, sl, sr, outfile):
    if not outfile:
        outfile = f"test_set/cycle-flip-{length}.gr"

    if length % 2 != 0:
        print("Odd cycles are not bipartite")
        return

    edges = []
    a = int(length/2)
    for i in range(a-1):
        edges.append([i,a+i])
        edges.append([i+1,a+i])
    edges.append([a-1,length-1])
    edges.append([0,length-1])

    # flip k vertices on A
    order = [i for i in range(a+a)]
    for _ in range(k):
        u = random.randint(0,a-1)
        v = random.randint(0,a-1)
        while u == v:
            u = random.randint(0,a-1)
            v = random.randint(0,a-1)
        temp = order[u]
        order[u] = order[v]
        order[v] = temp

    new_edges = []
    for edge in edges:
        new_edges.append([order[edge[0]],order[edge[1]]])

    edges = shuffle(new_edges, a, a, sl, sr)
    graph = PaceGraph(a, a, edges)

    write_graph(graph,outfile)

# @cli.command()
# @click.option("-k", default=3, type=int, help="Number of paths.")
# @click.option("-lengthmin", default=4, type=int, help="Min number of vertices in a path.")
# @click.option("-lengthmax", default=8, type=int, help="Max number of vertices in a path.")
# @click.option("-starmin", default=4, type=int, help="Min size of star.")
# @click.option("-starmax", default=8, type=int, help="Max size of star.")
# @click.option("-starprob", default=0, type=float, help="Probability of added stars.")
# @click.option("-sl", is_flag=True, default=False, help="Shuffle left side")
# @click.option("-sr", is_flag=True, default=False, help="Shuffle right side")
# @click.argument("outfile")
# def multipath(k, lengthmin, lengthmax, starmin, starmax, starprob, sl, sr, outfile):
#     counter = 0
#     temp_edges = []
#     starts = []
#     ends = []
#     a = 0
#     b = 0
#     lengths = []
#     for j in range(k):
#         starts.append(counter)
#         length = random.randint(lengthmin, lengthmax)
#         if length % 2 == 1:
#             length += 1
#         lengths.append(length)
#         a += int(length/2)-1
#         b += int(length/2)-1
#     for i in range()

#         for i in range(counter, int(length/2)-1 + counter):
#             temp_edges.append([i,int(length/2)+i])
#             temp_edges.append([i+1,int(length/2)+i])
#         temp_edges.append([int(length/2)-1 + counter,length-1+ counter])
#         ends.append(length-1)
#         counter = length
#     edges = []
#     for e in temp_edges:
#         u = e[0]
#         if e[0] in starts:
#             u = 0
#         v = e[1]
#         if e[1] in ends:
#             v = ends[0]
#         edges.append([u,v])
#     graph = PaceGraph(a, b, shuffle(edges, a, b, sl, sr))
#     write_graph(graph, outfile)

# def join_paths(gone, gtwo, sl, sr, jl, jr, outfile):
#     graph1 = read_graph(gone)
#     graph2 = read_graph(gtwo)

#     # one_right_bottom = graph1.left
#     # one_right_top = graph1.left + len(graph1.right)
#     # two_left_bottom = 1
#     # two_left_top = graph2.left + 1

#     new_a = graph1.left + graph2.left
#     new_b = len(graph1.right) + len(graph2.right)
#     mapping_one = {}
#     mapping_two = {}
#     for i in range(1, graph1.left+1):
#         if i == 1:
#             mapping_one[i] = 0
#         else:
#             mapping_one[i] = i - 1
#     for i in range(1, graph2.left+1):
#         if i == 1:
#             mapping_one[i] = 0
#         else:
#             mapping_two[i] = i + graph1.left - 2
#     for i in graph1.right:
#         if i == graph1.left:
#             mapping_one[i] = i + graph2.left - 2
#     for i in graph2.right:
#         new_value = i + graph1.left + len(graph1.right) - 1
#         if jl:
#             new_value -= 1
#         if jr:
#             new_value -= 1
#         mapping_two[i] = new_value

#     print(mapping_one)
#     print()
#     print(mapping_two)

#     edges = []
#     for u, v in graph1.edgeset:
#         edges.append([mapping_one[u], mapping_one[v]])
#     print()
#     for u, v in graph2.edgeset:
#         edges.append([mapping_two[u], mapping_two[v]])

#     graph = PaceGraph(new_a, new_b, shuffle(edges, new_a, new_b, sl, sr))
#     write_graph(graph, outfile)


@cli.command()
@click.option("-length", default=6, type=int, help="Number of vertices in path")
@click.option("-sl", is_flag=True, default=False, help="Shuffle left side")
@click.option("-sr", is_flag=True, default=False, help="Shuffle right side")
@click.argument("outfile", required=False)
def path(length, sl, sr, outfile):
    if not outfile:
        outfile = f"test_set/path-{length}.gr"
    edges = []
    a = math.ceil(length/2)
    b = math.floor(length/2)
    for i in range(a-1):
        edges.append([i,a+i])
        edges.append([i+1,a+i])
    if length % 2 == 1:
        edges.append([a-1,length-1])

    edges = shuffle(edges, a, b, sl, sr)
    graph = PaceGraph(a, b, edges)

    write_graph(graph,outfile)

@cli.command()
@click.option("-a", default=5, type=int, help="Size of left bipartition.")
@click.option("-b", default=5, type=int, help="Size of right bipartition.")
@click.option("-sl", is_flag=True, default=False, help="Shuffle left side")
@click.option("-sr", is_flag=True, default=False, help="Shuffle right side")
@click.argument("outfile", required=False)
def completebipartite(a, b, sl, sr, outfile):
    if not outfile:
        outfile = f"test_set/completebipartite-{a}-{b}.gr"
    g = nx.complete_bipartite_graph(a,b)
    edges = shuffle(g.edges, a, b, sl, sr)
    graph = PaceGraph(a, b, edges)

    write_graph(graph,outfile)

@cli.command()
@click.option("-b", default=5, type=int, help="Number of leaves.")
@click.option("-sl", is_flag=True, default=False, help="Shuffle left side")
@click.option("-sr", is_flag=True, default=False, help="Shuffle right side")
@click.argument("outfile", required=False)
def star(b, sl, sr, outfile):
    if not outfile:
        outfile = f"test_set/star-{b}.gr"
    g = nx.complete_bipartite_graph(1,b)
    edges = shuffle(g.edges, 1, b, sl, sr)
    graph = PaceGraph(1, b, edges)

    write_graph(graph,outfile)

@cli.command()
@click.option("-size", default=5, type=int, help="Size of matching (number of edges).")
@click.option("-sl", is_flag=True, default=False, help="Shuffle left side")
@click.option("-sr", is_flag=True, default=False, help="Shuffle right side")
@click.argument("outfile", required=False)
def matching(size, sl, sr, outfile):
    if not outfile:
        outfile = f"test_set/matching-{size}.gr"
    edges = []
    for i in range(size):
        edges.append([i,size+i])
    edges = shuffle(edges, size, size, sl, sr)
    graph = PaceGraph(size, size, edges)

    write_graph(graph,outfile)

@cli.command()
@click.option("-n", default=15, type=int, help="Number of vertices.")
@click.option("-sl", is_flag=True, default=False, help="Shuffle left side")
@click.option("-sr", is_flag=True, default=False, help="Shuffle right side")
@click.argument("outfile", required=False)
def tree(n, sl, sr, outfile):
    if not outfile:
        outfile = f"test_set/tree-{n}.gr"

    G = nx.random_unlabeled_tree(n)

    a, b, edges = pace_from_nx(G)
    graph = PaceGraph(a, b, shuffle(edges, a, b, sl, sr))
    write_graph(graph, outfile)

@cli.command()
@click.option("-n", default=15, type=int, help="Number of vertices.")
@click.option("-d", default=5, type=int, help="Maximum degree.")
@click.option("-sl", is_flag=True, default=False, help="Shuffle left side")
@click.option("-sr", is_flag=True, default=False, help="Shuffle right side")
@click.argument("outfile", required=False)
def treemaxdeg(n, d, sl, sr, outfile):
    if not outfile:
        outfile = f"test_set/treemaxdeg-{n}-{d}.gr"

    maxdeg = d + 1
    print("Sampling random trees")
    i = 0
    step = 10
    while maxdeg > d:
        G = nx.random_unlabeled_tree(n)
        maxdeg = len(nx.degree_histogram(G)) - 1
        i += 1

    a, b, edges = pace_from_nx(G)
    graph = PaceGraph(a, b, shuffle(edges, a, b, sl, sr))
    write_graph(graph, outfile)

@cli.command()
@click.option("-n", default=15, type=int, help="Number of vertices on the spine")
@click.option("-p1", default=0.5, type=float, help="Probability of adding an edge to the spine")
@click.option("-p2", default=0.5, type=float, help="Probability of adding an edge one level beyond spine")
@click.option("-sl", is_flag=True, default=False, help="Shuffle left side")
@click.option("-sr", is_flag=True, default=False, help="Shuffle right side")
@click.argument("outfile", required=False)
def lobster(n, p1, p2, sl, sr, outfile):
    if not outfile:
        outfile = f"test_set/lobster-{n}.gr"

    p1, p2 = abs(p1), abs(p2)
    if any(p >= 1 for p in [p1, p2]):
        print("Probability values for `p1` and `p2` must both be < 1.")
        return

    G = nx.path_graph(n)
    # build caterpillar: add edges to path graph with probability p1
    current_node = n - 1
    for i in range(n):
        while random.random() < p1:  # add fuzzy caterpillar parts
            current_node += 1
            G.add_edge(i, current_node)
            cat_node = current_node
            while random.random() < p2:  # add crunchy lobster bits
                current_node += 1
                G.add_edge(cat_node, current_node)

    a, b, edges = pace_from_nx(G)
    graph = PaceGraph(a, b, shuffle(edges, a, b, sl, sr))
    write_graph(graph, outfile)

@cli.command()
@click.option("-n", default=15, type=int, help="Number of vertices on the spine.")
@click.option("-p", default=0.5, type=float, help="Probability of adding an edge to the spine")
@click.option("-sl", is_flag=True, default=False, help="Shuffle left side")
@click.option("-sr", is_flag=True, default=False, help="Shuffle right side")
@click.argument("outfile", required=False)
def caterpillar(n, p, sl, sr, outfile):
    if not outfile:
        outfile = f"test_set/caterpillar-{n}.gr"

    p = abs(p)
    if p >= 1:
        print("Probability value for `p` < 1.")
        return

    G = nx.path_graph(n)
    relabel_mapping = {i : i*n for i in range(n)}
    G = nx.relabel_nodes(G, relabel_mapping)
    # build caterpillar: add edges to path graph with probability p1
    for i in range(n):
        c = 1
        while random.random() < p:  # add fuzzy caterpillar parts
            G.add_edge(i*n, i*n+c)
            c += 1

    a, b, edges = pace_from_nx(G)
    graph = PaceGraph(a, b, shuffle(edges, a, b, sl, sr))
    write_graph(graph, outfile)

@cli.command()
@click.option("-n", default=15, type=int, help="Number of vertices on the spine.")
@click.option("-p", default=0.5, type=float, help="Probability of adding an edge to the spine")
@click.option("-k", default=5, type=int, help="Number of flips")
@click.option("-sl", is_flag=True, default=False, help="Shuffle left side")
@click.option("-sr", is_flag=True, default=False, help="Shuffle right side")
@click.argument("outfile", required=False)
def caterpillar_flip(n, p, k, sl, sr, outfile):
    if not outfile:
        outfile = f"test_set/caterpillar-flip-{n}-{k}.gr"

    p = abs(p)
    if p >= 1:
        print("Probability value for `p` < 1.")
        return

    G = nx.path_graph(n)
    relabel_mapping = {i : i*n for i in range(n)}
    G = nx.relabel_nodes(G, relabel_mapping)
    # build caterpillar: add edges to path graph with probability p1
    for i in range(n):
        c = 1
        while random.random() < p:  # add fuzzy caterpillar parts
            G.add_edge(i*n, i*n+c)
            c += 1

    a, b, edges = pace_from_nx(G)
    # flip k vertices on A
    order = [i for i in range(a+b)]
    for _ in range(k):
        u = random.randint(0,a-1)
        v = random.randint(0,a-1)
        while u == v:
            u = random.randint(0,a-1)
            v = random.randint(0,a-1)
        temp = order[u]
        order[u] = order[v]
        order[v] = temp

    new_edges = []
    for edge in edges:
        new_edges.append([order[edge[0]],order[edge[1]]])

    graph = PaceGraph(a, b, shuffle(new_edges, a, b, sl, sr))
    write_graph(graph, outfile)

@cli.command()
@click.option("-n", default=15, type=int, help="Number of vertices on the spine.")
@click.option("-p", default=0.5, type=float, help="Probability of adding an edge to the spine")
@click.option("-sl", is_flag=True, default=False, help="Shuffle left side")
@click.option("-sr", is_flag=True, default=False, help="Shuffle right side")
@click.argument("outfile", required=False)
def doublecaterpillar(n, p, sl, sr, outfile):
    if not outfile:
        outfile = f"test_set/doublecaterpillar-{n}.gr"

    p = abs(p)
    if p >= 1:
        print("Probability value for `p` < 1.")
        return

    G1 = nx.path_graph(n)
    relabel_mapping = {i : i*n for i in range(n)}
    G1 = nx.relabel_nodes(G1, relabel_mapping)
    # build caterpillar: add edges to path graph with probability p1
    for i in range(n):
        c = 1
        while random.random() < p:  # add fuzzy caterpillar parts
            G1.add_edge(i*n, i*n+c)
            c += 1

    a1, b1, edges1 = pace_from_nx(G1)

    G2 = nx.path_graph(n)
    G2 = nx.relabel_nodes(G2, relabel_mapping)
    # build caterpillar: add edges to path graph with probability p1
    for i in range(n):
        c = 1
        while random.random() < p:  # add fuzzy caterpillar parts
            G2.add_edge(i*n, i*n+c)
            c += 1

    a2, b2, edges2 = pace_from_nx(G2)

    a, b, edges = merge_edges(a1, b1, edges1, a2, b2, edges2)

    graph = PaceGraph(a, b, shuffle(edges, a, b, sl, sr))
    write_graph(graph, outfile)

def merge_edges(a1, b1, edges1, a2, b2, edges2):
    a = max(a1,a2)
    b = max(b1,b2)
    edges = []
    if a1 < a2:
        for edge in edges1:
            edges.append([min(edge[0],edge[1]),max(edge[0],edge[1])-a1+a2])
        edges.extend(edges2)
    else:
        edges.extend(edges1)
        for edge in edges2:
            edges.append([min(edge[0],edge[1]),max(edge[0],edge[1])-a2+a1])

    return a, b, edges


@cli.command()
@click.option("-a", default=5, type=int, help="Size of left bipartition.")
@click.option("-b", default=5, type=int, help="Size of right bipartition.")
@click.option("-m", default=10, type=int, help="Number of edges.")
@click.option("-f", is_flag=True, default=False, help="Keep graph even if too few edges")
@click.option("-sl", is_flag=True, default=False, help="Shuffle left side")
@click.option("-sr", is_flag=True, default=False, help="Shuffle right side")
@click.argument("outfile", required=False)
def uniformplanar(a, b, m, f, sl, sr, outfile):
    if not outfile:
        outfile = f"test_set/uniformplanar-{a}-{b}-{m}.gr"

    all_edges = list(product(range(a), range(a,a+b)))
    random.shuffle(all_edges)
    G = nx.empty_graph()
    G.add_nodes_from(range(a+b))
    edges = []

    i = 0
    with alive_bar(m) as bar:
        for edge in all_edges:
            G.add_edge(edge[0], edge[1])
            if not nx.is_planar(G):
                G.remove_edge(edge[0], edge[1])
            else:
                edges.append(edge)
                i += 1
                bar()
                if i == m:
                    break

    edges = shuffle(edges, a, b, sl, sr)
    graph = PaceGraph(a, b, edges)

    write_graph(graph, outfile)


@cli.command()
@click.option("-a", default=5, type=int, help="Size of left bipartition.")
@click.option("-b", default=5, type=int, help="Size of right bipartition.")
@click.option("-d", default=3, type=int, help="Max degree.")
@click.option("-f", is_flag=True, default=False, help="Keep graph even if too few edges")
@click.option("-m", default=10, type=int, help="Number of edges.")
@click.option("-sl", is_flag=True, default=False, help="Shuffle left side")
@click.option("-sr", is_flag=True, default=False, help="Shuffle right side")
@click.argument("outfile", required=False)
def planardeg(a, b, d, f, m, sl, sr, outfile):
    if not outfile:
        outfile = f"test_set/planardeg-{a}-{b}-{d}-{m}.gr"
    if min(a,b) * d < m:
        print("Degree too small to get number of edges")
        return

    i = 0
    edges = []

    while i < m:
        i = 0
        edges = []
        all_edges = list(product(range(a), range(a,a+b)))
        random.shuffle(all_edges)
        G = nx.empty_graph()
        G.add_nodes_from(range(a+b))

        with alive_bar(m) as bar:
            for edge in all_edges:
                if G.degree(edge[0]) < d and G.degree(edge[1]) < d:
                    G.add_edge(edge[0], edge[1])
                    if not nx.is_planar(G):
                        G.remove_edge(edge[0], edge[1])
                    else:
                        i += 1
                        edges.append(edge)
                        bar()
                        if i == m:
                            break
        if f:
            i = m


    edges = shuffle(edges, a, b, sl, sr)
    graph = PaceGraph(a, b, edges)

    write_graph(graph, outfile)

@cli.command()
@click.option("-n", default=5, type=int, help="Number of columns")
@click.option("-m", default=5, type=int, help="Number of rows")
@click.option("-sl", is_flag=True, default=False, help="Shuffle left side")
@click.option("-sr", is_flag=True, default=False, help="Shuffle right side")
@click.argument("outfile", required=False)
def grid(n, m, sl, sr, outfile):
    if not outfile:
        outfile = f"test_set/grid-{m}-{n}.gr"

    G = nx.grid_2d_graph(m, n)
    #a = math.ceil(n * m / 2)
    #b = math.floor(n * m / 2)
    print("match nodes to integers")
    a = 0
    b = math.ceil(n * m / 2)
    a_nodes: Dict[Tuple[int, int], int]
    a_nodes = {}
    b_nodes: Dict[Tuple[int, int], int]
    b_nodes = {}
    # this works, but gives them unordered:
    # bottom_nodes, top_nodes = bipartite.sets(G)
    for node in G.nodes:
        if (node[0] + node[1]) % 2 == 0:
            a_nodes[node] = a
            a+=1
        else:
            b_nodes[node] = b
            b+=1

    print("extract edges")
    edges = []
    for edge in G.edges:
        u = edge[0]
        v = edge[1]
        if (u[0] + u[1]) % 2 == 1:
            u = edge[1]
            v = edge[0]
        edges.append([a_nodes[u], b_nodes[v]])

    edges = shuffle(edges, a, b-a, sl, sr)
    graph = PaceGraph(a, b-a, edges)

    write_graph(graph, outfile)

@cli.command()
@click.option("-n", default=12, type=int, help="Number of vertices")
@click.option("-m1", default=1, type=int, help="Lower bound on number of edges")
@click.option("-m2", default=1000000, type=int, help="Upper bound on number of edges")
@click.option("-c", default=10, type=int, help="Number of graphs to generate")
@click.option("-sl", is_flag=True, default=False, help="Shuffle left side")
@click.option("-sr", is_flag=True, default=False, help="Shuffle right side")
@click.option("-wsl", is_flag=True, default=False, help="Use wsl")
@click.argument("outfile", required=False)
def bipartiteplanar(n, m1, m2, c, sl, sr, wsl, outfile):
    # ./plantri -bp -e18:18 12
    command = ["plantri/plantri_s", "-bp", f"-e{m1}:{m2}", str(n)]
    if wsl:
        command.insert(0,"wsl")
    #print(" ".join(command))
    proc = subprocess.run(command, capture_output=True)
    #print(proc.stderr.decode())
    total_number = int(proc.stderr.decode().split("\n")[1].split(" ")[0])
    time_per_split = float(re.search(r"cpu=[\d]+\.[\d]+",proc.stderr.decode()).group().split("=")[1])

    command = ["plantri/plantri", "-bp", f"-e{m1}:{m2}", str(n)]
    if time_per_split * total_number > 10:
        number_splits = math.ceil(total_number * time_per_split / 10)
        command.append(f"0/{total_number}")
    if wsl:
        command.insert(0,"wsl")
    #print(" ".join(command))
    proc = subprocess.run(command, capture_output=True)
    #print(proc.stderr.decode())
    graphs = extract_graphs_from_plantri(proc.stdout)

    if wsl:
        command.insert(0,"wsl")
    proc = subprocess.run(command, stdout=subprocess.PIPE)
    graphs = extract_graphs_from_plantri(proc.stdout)

    graphs_export = random.sample(graphs, min(len(graphs),c))
    i = 1
    for G in graphs_export:
        a, b, edges = pace_from_nx(G)
        graph = PaceGraph(a, b, shuffle(edges, a, b, sl, sr))
        if outfile:
            write_graph(graph, outfile.replace(".gr",f"-{i}.gr"))
        else:
            write_graph(graph, f"test_set/bipartite-{n}-{i}-{len(edges)}.gr")
        i += 1
@cli.command()
@click.option("-n", default=12, type=int, help="Number of vertices")
@click.option("-c", default=10, type=int, help="Number of graphs to generate")
@click.option("-sl", is_flag=True, default=False, help="Shuffle left side")
@click.option("-sr", is_flag=True, default=False, help="Shuffle right side")
@click.option("-wsl", is_flag=True, default=False, help="Use wsl")
@click.argument("outfile", required=False)
def cubicplanar(n, c, sl, sr, wsl, outfile):
    # ./plantri -bd 12

    command = ["plantri/plantri_s", "-bd", str(n)]
    if wsl:
        command.insert(0,"wsl")
    #print(" ".join(command))
    proc = subprocess.run(command, capture_output=True)
    #print(proc.stderr.decode())
    total_number = int(proc.stderr.decode().split("\n")[1].split(" ")[0])
    time_per_split = float(re.search(r"cpu=[\d]+\.[\d]+",proc.stderr.decode()).group().split("=")[1])

    command = ["plantri/plantri", "-bd", str(n)]
    if time_per_split * total_number > 10:
        number_splits = math.ceil(total_number * time_per_split / 10)
        command.append(f"0/{total_number}")
    if wsl:
        command.insert(0,"wsl")
    #print(" ".join(command))
    proc = subprocess.run(command, capture_output=True)
    #print(proc.stderr.decode())
    graphs = extract_graphs_from_plantri(proc.stdout)

    graphs_export = random.sample(graphs, min(len(graphs),c))
    i = 1
    for G in graphs_export:
        a, b, edges = pace_from_nx(G)
        graph = PaceGraph(a, b, shuffle(edges, a, b, sl, sr))
        if outfile:
            write_graph(graph, outfile.replace(".gr",f"-{i}.gr"))
        else:
            write_graph(graph, f"test_set/cubic-{n}-{i}.gr")
        i += 1

@cli.command()
@click.option("-n", default=12, type=int, help="Number of vertices")
@click.option("-c", default=10, type=int, help="Number of graphs to generate")
@click.option("-sl", is_flag=True, default=False, help="Shuffle left side")
@click.option("-sr", is_flag=True, default=False, help="Shuffle right side")
@click.option("-wsl", is_flag=True, default=False, help="Use wsl")
@click.argument("outfile", required=False)
def quadrangulation(n, c, sl, sr, wsl, outfile):
    # ./plantri -q 12

    command = ["plantri/plantri_s", "-q", str(n)]
    if wsl:
        command.insert(0,"wsl")
    #print(" ".join(command))
    proc = subprocess.run(command, capture_output=True)
    #print(proc.stderr.decode())
    total_number = int(proc.stderr.decode().split("\n")[1].split(" ")[0])
    time_per_split = float(re.search(r"cpu=[\d]+\.[\d]+",proc.stderr.decode()).group().split("=")[1])

    command = ["plantri/plantri", "-q", str(n)]
    if time_per_split * total_number > 10:
        number_splits = math.ceil(total_number * time_per_split / 10)
        command.append(f"0/{total_number}")
    if wsl:
        command.insert(0,"wsl")
    #print(" ".join(command))
    proc = subprocess.run(command, capture_output=True)
    #print(proc.stderr.decode())
    graphs = extract_graphs_from_plantri(proc.stdout)

    graphs_export = random.sample(graphs, min(len(graphs),c))
    i = 1
    for G in graphs_export:
        a, b, edges = pace_from_nx(G)
        graph = PaceGraph(a, b, shuffle(edges, a, b, sl, sr))
        if outfile:
            write_graph(graph, outfile.replace(".gr",f"-{i}.gr"))
        else:
            write_graph(graph, f"test_set/quadrangulation-{n}-{i}.gr")
        i += 1

@cli.command()
@click.option("-n", default=12, type=int, help="Number of vertices")
@click.option("-c", default=10, type=int, help="Number of graphs to generate")
@click.option("-sl", is_flag=True, default=False, help="Shuffle left side")
@click.option("-sr", is_flag=True, default=False, help="Shuffle right side")
@click.option("-wsl", is_flag=True, default=False, help="Use wsl")
@click.argument("outfile", required=False)
def planarthreetree(n, c, sl, sr, wsl, outfile):
    # ./plantri -A 12

    command = ["plantri/plantri_s", "-A", str(n)]
    if wsl:
        command.insert(0,"wsl")
    #print(" ".join(command))
    proc = subprocess.run(command, capture_output=True)
    #print(proc.stderr.decode())
    total_number = int(proc.stderr.decode().split("\n")[1].split(" ")[0])
    time_per_split = float(re.search(r"cpu=[\d]+\.[\d]+",proc.stderr.decode()).group().split("=")[1])

    command = ["plantri/plantri", "-A", str(n)]
    if time_per_split * total_number > 10:
        number_splits = math.ceil(total_number * time_per_split / 10)
        command.append(f"0/{total_number}")
    if wsl:
        command.insert(0,"wsl")
    #print(" ".join(command))
    proc = subprocess.run(command, capture_output=True)
    #print(proc.stderr.decode())
    graphs = extract_graphs_from_plantri(proc.stdout)

    graphs_export = random.sample(graphs, min(len(graphs),c))
    i = 1
    for G in graphs_export:
        a, b, edges = pace_from_nx(G)
        graph = PaceGraph(a, b, shuffle(edges, a, b, sl, sr))
        if outfile:
            write_graph(graph, outfile.replace(".gr",f"-{i}.gr"))
        else:
            write_graph(graph, f"test_set/planar3tree-{n}-{i}.gr")
        i += 1

def pace_from_nx(G):
    if not nx.is_bipartite(G):
        print("graph is not bipartite")
        return 0, 0, []
    nodes_a, nodes_b = nx.bipartite.sets(G)
    nodes_a = sorted(nodes_a)
    nodes_b = sorted(nodes_b)
    map_nodes = {}
    a = 0
    for node in nodes_a:
        map_nodes[node] = a
        a += 1
    b = a
    for node in nodes_b:
        map_nodes[node] = b
        b += 1
    edges = []
    for edge in G.edges:
        edges.append([map_nodes[edge[0]],map_nodes[edge[1]]])
    return a, b-a, edges

def extract_graphs_from_plantri(text):
    # Byte encoding starts with Byte 15
    pos = 15
    graphs = []
    while len(text) > pos:
        #print(len(text))
        # Format:
        # number of vertices
        # for each vertex: edges followed by 0
        # example: 3 vertices, edges [1,2], [2,3]
        # 3 2 3 0 1 0 1 0
        byte = text[pos]
        # number of nodes
        N = byte
        G = nx.empty_graph()
        # nodes are 1,...,N
        G.add_nodes_from(range(N))
        node = 1
        while node <= N:
            # read adjacencies until 0
            pos += 1
            byte = text[pos]
            while byte != 0:
                # only add edges once
                if byte > node:
                    #print(f"[{node},{byte}]")
                    # shift by 1
                    G.add_edge(node-1,byte-1)
                byte = text[pos]
                pos += 1
            # read all edges
            node += 1
        # graph done
        graphs.append(G)
        #print(G)
    return graphs


@cli.command()
@click.option("-n", default=10, type=click.IntRange(4,), help="Number of vertices")
@click.option("-s", default=1, type=int, help="Number of subdivision")
@click.option("-sl", is_flag=True, default=False, help="Shuffle left side")
@click.option("-sr", is_flag=True, default=False, help="Shuffle right side")
@click.argument("outfile", required=False)
def wheel(n, s, sl, sr, outfile):
    if s % 2 == 0:
        print("Must be odd number of subdivisions")
        return

    if not outfile:
        outfile = f"test_set/wheel-{n}-{s}.gr"

    G = nx.wheel_graph(n)
    i = n
    #print(list(G.edges))
    for edge in list(G.edges):
        path = [edge[0]]
        path.extend([i+j for j in range(s)])
        path.append(edge[1])
        nx.add_path(G,path)
        G.remove_edge(edge[0],edge[1])
        i += s

    a, b, edges = pace_from_nx(G)
    graph = PaceGraph(a, b, shuffle(edges, a, b, sl, sr))
    write_graph(graph, outfile)


def shuffle(edges, a, b, left=False, right=True):
    edges_s = []
    if left:
        order_a = np.random.permutation(range(a)).tolist()
    else:
        order_a = [i for i in range(a)]

    if right:
        order_b = np.random.permutation(range(a, a + b)).tolist()
    else:
        order_b = [i for i in range(a, a + b)]
    order = order_a + order_b

    for edge in edges:
        edges_s.append([order[edge[0]],order[edge[1]]])

    return edges_s

# @cli.command("")
# @click.option("-a", default=5, type=int, help="Number of star centers.")
# @click.option("-b", default=5, type=int, help="Number of leaves per star.")
# @click.argument("outfile")
# def disjointstars_left(a, b, outfile):
#     edges = []
#     for i in range(a):
#         for j in range(b):
#             edges.append([i, a + i*b + j])

#     edges = shuffle(edges, a, a * b)
#     graph = PaceGraph(a, a * b, edges)
#     write_graph(graph, outfile)

@cli.command("")
@click.option("-a", default=5, type=int, help="Number of star centers.")
@click.option("-b", default=5, type=int, help="Minimum number of leaves per star.")
@click.option("-c", default=5, type=int, help="Maximum number of leaves per star.")
@click.option("-sl", is_flag=True, default=False, help="Shuffle left side")
@click.option("-sr", is_flag=True, default=False, help="Shuffle right side")
@click.argument("outfile", required=False)
def disjointstars_left(a, b, c, sl, sr, outfile):
    edges = []
    total_leaves = 0
    for i in range(a):
        leaf_count = random.randint(b, c)
        for j in range(leaf_count):
            edges.append([i, a + total_leaves + j])
        total_leaves += leaf_count

    if not outfile:
        outfile = f"test_set/disjointstars_left-{a}-{total_leaves}.gr"

    edges = shuffle(edges, a, total_leaves, sl, sr)
    graph = PaceGraph(a, total_leaves, edges)
    write_graph(graph, outfile)

@cli.command("")
@click.option("-a", default=5, type=int, help="Number of star centers.")
@click.option("-b", default=5, type=int, help="Minimum number of leaves per star.")
@click.option("-c", default=5, type=int, help="Maximum number of leaves per star.")
@click.option("-sl", is_flag=True, default=False, help="Shuffle left side")
@click.option("-sr", is_flag=True, default=False, help="Shuffle right side")
@click.argument("outfile", required=False)
def connectedstars_left(a, b, c, sl, sr, outfile):
    edges = []
    total_leaves = 0
    for i in range(a):
        leaf_count = random.randint(b, c)
        for j in range(leaf_count):
            offset = 0 if i == 0 else 1
            edges.append([i, a + total_leaves + j - i])
        total_leaves += leaf_count

    if not outfile:
        outfile = f"test_set/connectedstars_left-{a}-{total_leaves-a+1}.gr"

    edges = shuffle(edges, a, total_leaves-a+1, sl, sr)
    graph = PaceGraph(a, total_leaves-a+1, edges)
    write_graph(graph, outfile)

@cli.command("")
@click.option("-a", default=5, type=int, help="Number of star centers.")
@click.option("-b", default=5, type=int, help="Minimum number of leaves per star.")
@click.option("-c", default=5, type=int, help="Maximum number of leaves per star.")
@click.option("-sl", is_flag=True, default=False, help="Shuffle left side")
@click.option("-sr", is_flag=True, default=False, help="Shuffle right side")
@click.argument("outfile", required=False)
def disjointstars_right(a, b, c, sl, sr, outfile):
    if not outfile:
        outfile = f"test_set/disjointstarsright-{a}-{b}-{c}.gr"

    G = nx.complete_bipartite_graph(random.randint(b, c+1),1)
    a1, b1, edges = pace_from_nx(G)
    graph = PaceGraph(a1, b1, edges)

    for j in range(a):
        G = nx.complete_bipartite_graph(random.randint(b, c+1),1)
        a2, b2, edges = pace_from_nx(G)
        pg = PaceGraph(a2, b2, edges)
        graph = join_graphs(graph, pg, False, False)

    ag = graph.left
    bg = len(graph.right)
    edges = graph.edgeset

    edges = shuffle(edges, ag, bg, sl, sr)
    graph = PaceGraph(ag, bg, edges)
    write_graph(graph, outfile)

@cli.command("")
@click.option("-amin", default=5, type=int, help="Min number of star centers per star forest.")
@click.option("-amax", default=5, type=int, help="Min number of star centers per star forest.")
@click.option("-b", default=5, type=int, help="Minimum number of leaves per star.")
@click.option("-c", default=5, type=int, help="Maximum number of leaves per star.")
@click.option("-num", default=5, type=int, help="Number of star forests.")
@click.option("-sl", is_flag=True, default=False, help="Shuffle left side")
@click.option("-sr", is_flag=True, default=False, help="Shuffle right side")
@click.argument("outfile", required=False)
def starforests_connected(amin, amax, b, c, num, sl, sr, outfile):
    if not outfile:
        outfile = f"test_set/starforests-connected-{num}-{math.floor((amin+amax)/2)}-{b}-{c}.gr"

    G = nx.complete_bipartite_graph(random.randint(b, c),1)
    a1, b1, edges = pace_from_nx(G)
    graph = PaceGraph(a1, b1, edges)
    a = random.randint(amin,amax)

    for j in range(a-1):
        G = nx.complete_bipartite_graph(random.randint(b, c),1)
        a2, b2, edges = pace_from_nx(G)
        pg = PaceGraph(a2, b2, edges)
        graph = join_graphs(graph, pg, False, False)

    ag = graph.left
    bg = len(graph.right)
    edges = graph.edgeset

    edges = shuffle(edges, ag, bg, sl, sr)
    graph = PaceGraph(ag, bg, edges)

    for _ in range(num-1):
        G = nx.complete_bipartite_graph(random.randint(b, c),1)
        a1, b1, edges = pace_from_nx(G)
        graph2 = PaceGraph(a1, b1, edges)

        a = random.randint(amin,amax)
        for j in range(a-1):
            G = nx.complete_bipartite_graph(random.randint(b, c),1)
            a2, b2, edges = pace_from_nx(G)
            pg = PaceGraph(a2, b2, edges)
            graph2 = join_graphs(graph2, pg, False, False)

        ag = graph2.left
        bg = len(graph2.right)
        edges = graph2.edgeset

        edges = shuffle(edges, ag, bg, sl, sr)
        graph2 = PaceGraph(ag, bg, edges)
        graph = join_graphs(graph, graph2, False, False)


    ag = graph.left
    bg = len(graph.right)
    edges = graph.edgeset
    edges = shuffle(edges, ag, bg, False, sr)
    graph = PaceGraph(ag, bg, edges)

    write_graph(graph, outfile)

@cli.command("")
@click.option("-amin", default=20, type=int, help="Minimum number of leaves per component.")
@click.option("-amax", default=20, type=int, help="Maximum number of leaves per component.")
@click.option("-bmin", default=5, type=int, help="Minimum number of star centers per component.")
@click.option("-bmax", default=5, type=int, help="Maximum number of star centers per component.")
@click.option("-cmin", default=5, type=int, help="Minimum number of leaves per star.")
@click.option("-cmax", default=5, type=int, help="Maximum number of leaves per star.")
@click.option("-num", default=5, type=int, help="Number of components.")
@click.option("-sl", is_flag=True, default=False, help="Shuffle left side")
@click.option("-sr", is_flag=True, default=False, help="Shuffle right side")
@click.argument("outfile", required=False)
def starsets_connected(amin, amax, bmin, bmax, cmin, cmax, num, sl, sr, outfile):
    if not outfile:
        outfile = f"test_set/starsets-connected-{num}-{math.floor((amin+amax)/2)}-{math.floor((bmin+bmax)/2)}-{math.floor((cmin+cmax)/2)}.gr"

    a = random.randint(amin, amax)
    b = random.randint(bmin, bmax)
    edges = []

    # each center to random niehgbors
    for j in range(a,a+b):
        neighbors = random.sample(range(a),k=random.randint(cmin,cmax))
        for i in neighbors:
            edges.append([i,j])


    edges = shuffle(edges, a, b, sl, sr)
    graph = PaceGraph(a, b, edges)

    for _ in range(num):
        a = random.randint(amin, amax)
        b = random.randint(bmin, bmax)
        edges = []

        # each center to random niehgbors
        for j in range(a,a+b):
            neighbors = random.sample(range(a),k=random.randint(cmin,cmax))
            for i in neighbors:
                edges.append([i,j])


        edges = shuffle(edges, a, b, sl, sr)
        graph2 = PaceGraph(a, b, edges)
        graph = join_graphs(graph, graph2, False, False)


    a = graph.left
    b = len(graph.right)
    edges = graph.edgeset
    edges = shuffle(edges, a, b, False, sr)
    graph = PaceGraph(a, b, edges)

    write_graph(graph, outfile)

@cli.command("")
@click.option("-a", default=5, type=int, help="Number of star centers.")
@click.option("-b", default=5, type=int, help="Minimum number of leaves per star.")
@click.option("-c", default=5, type=int, help="Maximum number of leaves per star.")
@click.option("-sl", is_flag=True, default=False, help="Shuffle left side")
@click.option("-sr", is_flag=True, default=False, help="Shuffle right side")
@click.argument("outfile", required=False)
def connectedstars_right(a, b, c, sl, sr, outfile):
    if not outfile:
        outfile = f"test_set/connectedstarsright-{a}-{b}-{c}.gr"

    G = nx.complete_bipartite_graph(random.randint(b, c+1),1)
    a1, b1, edges = pace_from_nx(G)
    graph = PaceGraph(a1, b1, edges)

    for j in range(a):
        G = nx.complete_bipartite_graph(random.randint(b, c+1),1)
        a2, b2, edges = pace_from_nx(G)
        pg = PaceGraph(a2, b2, edges)
        graph = join_graphs(graph, pg, True, False)

    ag = graph.left
    bg = len(graph.right)
    edges = graph.edgeset

    edges = shuffle(edges, ag, bg, sl, sr)
    graph = PaceGraph(ag, bg, edges)
    write_graph(graph, outfile)

@cli.command("")
@click.option("-a", default=5, type=int, help="Number of vertices left")
@click.option("-b", default=5, type=int, help="Number of vertices right")
@click.option("-r", default=1, type=int, help="Size of containing square")
@click.option("-l", default=1, type=float, help="Minimum disk size")
@click.option("-u", default=1, type=float, help="Maximum disk size")
@click.option("-sl", is_flag=True, default=False, help="Shuffle left side")
@click.option("-sr", is_flag=True, default=False, help="Shuffle right side")
@click.argument("outfile", required=False)
def disk_intersection_graph(a, b, r, l, u, sl, sr, outfile):
    if not outfile:
        outfile = f"test_set/diskintersection-{a+b}-{r}.gr"
    ac = np.random.uniform(low=0, high=r, size=(a,2))
    bc = np.random.uniform(low=0, high=r, size=(b,2))
    # ax = random.sample(range(0, r), a)
    # ay = random.sample(range(0, r), a)
    # bx = random.sample(range(0, r), b)
    # by = random.sample(range(0, r), b)
    sizes_a = np.random.uniform(low=l, high=u, size=(a,))
    sizes_b = np.random.uniform(low=l, high=u, size=(b,))
    edges = []
    for i in range(a):
        for j in range(b):
            if math.sqrt((ac[i][0]-bc[j][0])**2 + (ac[i][1]-bc[j][1])**2) <= (sizes_a[i]+sizes_b[j])/2:
                edges.append([i,j+a])

    #print(edges)

    graph = PaceGraph(a, b, shuffle(edges, a, b, sl, sr))
    write_graph(graph, outfile)

@cli.command("")
@click.option("-a", default=5, type=int, help="Number of vertices left")
@click.option("-b", default=5, type=int, help="Number of vertices right")
@click.option("-r", default=5, type=int, help="Range")
@click.option("-l", default=1, type=float, help="Minimum interval size")
@click.option("-u", default=1, type=float, help="Maximum interval size")
@click.option("-sl", is_flag=True, default=False, help="Shuffle left side")
@click.option("-sr", is_flag=True, default=False, help="Shuffle right side")
@click.argument("outfile", required=False)
def interval_bigraph(a, b, r, l, u, sl, sr, outfile):
    left = []
    left_sizes = []
    right = []
    right_sizes = []
    edges = []
    for i in range(a):
        left.append(random.randint(0,r))
        left_sizes.append(random.uniform(l, u))
    for i in range(b):
        right.append(random.randint(0,r))
        right_sizes.append(random.uniform(l, u))
    for i in range(a):
        for j in range(b):
            #print(f"i: {i}")
            #print(f"j: {j}")
            #print(f"i: {left[i]}, {left_sizes[i]}, j: {right[j]}, {right_sizes[j]}")
            if abs(left[i]-right[j]) <= (left_sizes[i]+right_sizes[j])/2:
                edges.append([i,j+a])
   
    if not outfile:
        outfile = f"test_set/bigraph-{a+b}-{r}-{l}-{u}.gr"

    #print(edges)

    graph = PaceGraph(a, b, shuffle(edges, a, b, sl, sr))
    write_graph(graph, outfile)


@cli.command()
@click.option("-n", default=16, type=int, help="Number of vertices.")
@click.option("-sl", is_flag=True, default=False, help="Shuffle left side")
@click.option("-sr", is_flag=True, default=False, help="Shuffle right side")
@click.argument("outfile", required=False)
def circularladder(n, sl, sr, outfile):
    if not outfile:
        outfile = f"test_set/circularladder-{n}.gr"

    G = nx.circular_ladder_graph(n)

    a, b, edges = pace_from_nx(G)
    graph = PaceGraph(a, b, shuffle(edges, a, b, sl, sr))
    write_graph(graph, outfile)

@cli.command()
@click.option("-n", default=3, type=int, help="dimensions")
@click.option("-sl", is_flag=True, default=False, help="Shuffle left side")
@click.option("-sr", is_flag=True, default=False, help="Shuffle right side")
@click.argument("outfile", required=False)
def hypercube(n, sl, sr, outfile):
    if not outfile:
        outfile = f"test_set/hypercube-{n}.gr"

    G = nx.hypercube_graph(n)

    a, b, edges = pace_from_nx(G)
    graph = PaceGraph(a, b, shuffle(edges, a, b, sl, sr))
    write_graph(graph, outfile)

@cli.command()
@click.option("-n", default=16, type=int, help="Number of vertices.")
@click.option("-sl", is_flag=True, default=False, help="Shuffle left side")
@click.option("-sr", is_flag=True, default=False, help="Shuffle right side")
@click.argument("outfile", required=False)
def cograph(n, sl, sr, outfile):
    if not outfile:
        outfile = f"test_set/cograph-{n}.gr"

    G = nx.random_cograph(n)

    a, b, edges = pace_from_nx(G)
    graph = PaceGraph(a, b, shuffle(edges, a, b, sl, sr))
    write_graph(graph, outfile)

@cli.command()
@click.option("-n", default=16, type=int, help="The number of nodes in the first bipartite set (nodes)")
@click.option("-m", default=16, type=int, help="The number of nodes in the second bipartite set (attributes)")
@click.option("-p", default=0.5, type=click.FloatRange(0,1), help="Probability of connecting nodes between bipartite sets")
@click.option("-sl", is_flag=True, default=False, help="Shuffle left side")
@click.option("-sr", is_flag=True, default=False, help="Shuffle right side")
@click.argument("outfile", required=False)
def intersectiongraph(n, m, p, sl, sr, outfile):
    if not outfile:
        outfile = f"test_set/intersectiongraph-{n}-{m}-{p}.gr"

    G = nx.uniform_random_intersection_graph(n, m, p)

    a, b, edges = pace_from_nx(G)
    graph = PaceGraph(a, b, shuffle(edges, a, b, sl, sr))
    write_graph(graph, outfile)

@cli.command()
@click.option("-a", default=10, type=int, help="Number of vertices on A.")
@click.option("-b", default=10, type=int, help="Number of vertices on A.")
@click.option("-k", default=3, type=int, help="k as in k-tree.")
#@click.option("-pa", default=0.5, type=click.FloatRange(0,1), help="Probability to add vertex to set a")
@click.option("-sl", is_flag=True, default=False, help="Shuffle left side")
@click.option("-sr", is_flag=True, default=False, help="Shuffle right side")
@click.argument("outfile", required=False)
def ktree(a, b, k, sl, sr, outfile):
    # Note: this is not really a k-tree, as it would not be bipartite.
    # We start with a complete bipartite graph K_k,k which has treewidth k
    if not outfile:
        outfile = f"test_set/{k}-tree-{a}-{b}.gr"

    if a < k or b < k:
        print("k must be smaller than a and b.")
        return

    # start with k-clique
    sets = []
    edges = []
    set = []
    for i in range(math.ceil(k/2)):
        set.append(i)
        for j in range(a,a+math.floor(k/2)):
            edges.append([i,j])
    for j in range(a,a+math.floor(k/2)):
        set.append(j)
    sets.append(set)
    curr_a = math.ceil(k/2)
    curr_b = math.floor(k/2)

    while curr_a < a or curr_b < b:
        # randomly choose set from sets
        set = random.choice(sets)
        #print(sets)
        # randomly pick which side to add to
        if curr_b == b or (curr_a < a and random.random() < 0.5):
            # add to A
            for neighbor in set:
                if neighbor > a-1:
                    edges.append([curr_a,neighbor])
                new_set = list(filter(lambda x : x != neighbor, set))
                new_set.append(curr_a)
                sets.append(new_set)
            curr_a += 1
        else:
            # add to B
            for neighbor in set:
                if neighbor < a:
                    edges.append([neighbor,a+curr_b])
                new_set = list(filter(lambda x : x != neighbor, set))
                new_set.append(a+curr_b)
                sets.append(new_set)
            curr_b += 1

    graph = PaceGraph(a, b, shuffle(edges, a, b, sl, sr))
    write_graph(graph, outfile)

@cli.command()
@click.option("-a", default=10, type=int, help="Number of vertices on A.")
@click.option("-b", default=10, type=int, help="Number of vertices on A.")
@click.option("-k", default=3, type=int, help="k as in k-tree.")
@click.option("-p", default=0.5, type=click.FloatRange(0,1), help="Probability of edges to be added (1 will always be added)")
@click.option("-sl", is_flag=True, default=False, help="Shuffle left side")
@click.option("-sr", is_flag=True, default=False, help="Shuffle right side")
@click.argument("outfile", required=False)
def partialktree(a, b, k, p, sl, sr, outfile):
    # Note: this is not really a k-tree, as it would not be bipartite.
    # We start with a complete bipartite graph K_k,k which has treewidth k
    if not outfile:
        outfile = f"test_set/partial-{k}-tree-{a}-{b}.gr"

    if a < k or b < k:
        print("k must be smaller than a and b.")
        return

    # start with k-clique
    sets = []
    edges = []
    set = []
    for i in range(math.ceil(k/2)):
        set.append(i)
        for j in range(a,a+math.floor(k/2)):
            if random.random() <= p:
                edges.append([i,j])
    for j in range(a,a+math.floor(k/2)):
        set.append(j)
    sets.append(set)
    curr_a = math.ceil(k/2)
    curr_b = math.floor(k/2)

    while curr_a < a or curr_b < b:
        # randomly choose set from sets
        set = random.choice(sets)
        #print(sets)
        # randomly pick which side to add to
        if curr_b == b or (curr_a < a and random.random() < 0.5):
            # add to A
            for neighbor in set:
                if neighbor > a-1:
                    if random.random() <= p:
                        edges.append([curr_a,neighbor])
                new_set = list(filter(lambda x : x != neighbor, set))
                new_set.append(curr_a)
                sets.append(new_set)
            curr_a += 1
        else:
            # add to B
            for neighbor in set:
                if neighbor < a:
                    if random.random() <= p:
                        edges.append([neighbor,a+curr_b])
                new_set = list(filter(lambda x : x != neighbor, set))
                new_set.append(a+curr_b)
                sets.append(new_set)
            curr_b += 1

    graph = PaceGraph(a, b, shuffle(edges, a, b, sl, sr))
    write_graph(graph, outfile)

@cli.command()
@click.option("-n", default=5, type=int, help="Number of vertices per bipartition.")
@click.option("-p", default=4, type=int, help="Number of bipartitions.")
@click.option("-m", default=10, type=int, help="Number of edges per layer.")
@click.argument("outfile", required=False)
def multipartiteplanar(n, p, m, outfile):
    if not outfile:
        outfile = f"test_set/multipartiteplanar-{p}-{n}-{m}.gr"
    layers_a = math.ceil(p/2)
    layers_b = math.floor(p/2)
    a = layers_a * n
    b = layers_b * n
    all_edges: List[List[int, int]]
    all_edges = []
    for i in range(layers_b) :
        all_edges.append(list(product(range(i*n,i*n+n), range(a + i*n, a + i*n + n))))
    for i in range(1,layers_a) :
        all_edges.append(list(product(range(i*n,i*n+n), range(a + (i-1)*n, a + (i-1)*n + n))))
    G = nx.empty_graph()
    G.add_nodes_from(range(a+b))
    edges = []

    with alive_bar(m * (p-1)) as bar:
        for this_edges in all_edges:
            random.shuffle(this_edges)

            i = 0
            for edge in this_edges:
                G.add_edge(edge[0], edge[1])
                if not nx.is_planar(G):
                    G.remove_edge(edge[0], edge[1])
                else:
                    edges.append(edge)
                    i += 1
                    bar()
                    if i == m:
                        break

    edges = sorted(edges)
    graph = PaceGraph(a, b, edges)

    write_graph(graph, outfile)

@cli.command()
@click.option("-n", default=5, type=int, help="Number of vertices per bipartition.")
@click.option("-p", default=4, type=int, help="Number of bipartitions.")
@click.option("-m", default=10, type=int, help="Number of edges per layer.")
@click.argument("outfile", required=False)
def multipartite(n, p, m, outfile):
    if not outfile:
        outfile = f"test_set/multipartite-{p}-{n}-{m}.gr"
    layers_a = math.ceil(p/2)
    layers_b = math.floor(p/2)
    a = layers_a * n
    b = layers_b * n
    all_edges: List[List[int, int]]
    all_edges = []
    for i in range(layers_b) :
        all_edges.append(list(product(range(i*n,i*n+n), range(a + i*n, a + i*n + n))))
    for i in range(1,layers_a) :
        all_edges.append(list(product(range(i*n,i*n+n), range(a + (i-1)*n, a + (i-1)*n + n))))
    edges = []

    for this_edges in all_edges:
        edges.extend(random.sample(this_edges, k=m))

    edges = sorted(edges)
    graph = PaceGraph(a, b, edges)

    write_graph(graph, outfile)

@cli.command()
@click.option("-k", default=4, type=int, help="2(k^2 - k - 2) vertices.")
@click.option("-sl", is_flag=True, default=False, help="Shuffle left side")
@click.option("-sr", is_flag=True, default=False, help="Shuffle right side")
@click.argument("outfile", required=False)
def barycenter(k, sl, sr, outfile):
    # worst case for barycenter heuristic, extended by a star (sqrt{n} approximation)
    if not outfile:
        outfile = f"test_set/barycenter-{k}.gr"

    a = k*k + k - 2
    b = k*k + k - 2

    u = a + math.floor((k*k - k - 2) / 2)
    v = u + 1

    edges = []

    # star before
    for i in range(a, u):
        edges.append([0, i])
    # edge (0, u)
    edges.append([0, u])
    # edge to v
    edges.append([k*k - 1,v])
    # other edges to u
    for i in range(k*k,a):
        edges.append([i,u])
    # star after
    for i in range(v+1, a+b):
        edges.append([a-1,i])

    edges = shuffle(edges, a, b, sl, sr)
    graph = PaceGraph(a, b, edges)

    write_graph(graph, outfile)

@cli.command()
@click.option("-k", default=4, type=int, help="Size of the construction.")
@click.option("-sl", is_flag=True, default=False, help="Shuffle left side")
@click.option("-sr", is_flag=True, default=False, help="Shuffle right side")
@click.argument("outfile", required=False)
def barycenter_connected(k, sl, sr, outfile):
    # worst case for barycenter heuristic, extended by a star (sqrt{n} approximation)
    # from https://www.sciencedirect.com/science/article/abs/pii/S0020019001002976?via%3Dihub
    if not outfile:
        outfile = f"test_set/barycenter-connected-{k}.gr"

    # relabel: our k is called m in the paper
    m = k
    k = int((2 + m + m * m) / 2)
    s = k - 1

    a = k + m
    b = s + 2

    t = a
    u = a + 1
    v = [a + 2 + i for i in range(s)]

    edges = []

    # 0,...,k-1 to t
    for i in range(k):
        edges.append([i,t])
    # 0 to u
    edges.append([0,u])
    # k,...,k+m-1 to u
    for i in range(m):
        edges.append([k+i,u])
    # k-1 to v_1,...,v_s
    for i in range(s):
        edges.append([k-1,v[i]])

    edges = shuffle(edges, a, b, sl, sr)
    graph = PaceGraph(a, b, edges)

    write_graph(graph, outfile)

@cli.command()
@click.option("-k", default=4, type=int, help="8k+4 vertices.")
@click.option("-sl", is_flag=True, default=False, help="Shuffle left side")
@click.option("-sr", is_flag=True, default=False, help="Shuffle right side")
@click.argument("outfile", required=False)
def median(k, sl, sr, outfile):
    # worst case for median heuristic, extended by a star (3-approximation)
    if not outfile:
        outfile = f"test_set/median-{k}.gr"

    a = 4*k + 2
    b = 4*k + 2

    u = a + 2 * k + 1
    v = u + 1

    edges = []

    for i in range(a, u):
        edges.append([0, i])
    for i in range(k):
        edges.append([i,v])
    for i in range(2*k+1,3*k+2):
        edges.append([i,v])
    for i in range(k,2*k+1):
        edges.append([i,u])
    for i in range(3*k+2,a):
        edges.append([i,u])
    for i in range(v+1, a+b):
        edges.append([a-1,i])

    edges = shuffle(edges, a, b, sl, sr)
    edges = sorted(edges)
    graph = PaceGraph(a, b, edges)

    write_graph(graph, outfile)



@cli.command()
@click.option("-k", default=4, type=int, help="Size of the construction.")
@click.option("-sl", is_flag=True, default=False, help="Shuffle left side")
@click.option("-sr", is_flag=True, default=False, help="Shuffle right side")
@click.argument("outfile", required=False)
def barycenter_median(k, sl, sr, outfile):
    # Barycenter
    # worst case for barycenter heuristic, extended by a star (sqrt{n} approximation)
    # from https://www.sciencedirect.com/science/article/abs/pii/S0020019001002976?via%3Dihub
    if not outfile:
        outfile = f"test_set/barycenter-median-{k}.gr"

    old_k = k
    # relabel: our k is called m in the paper
    m = k
    k = int((2 + m + m * m) / 2)
    s = k - 1

    a = k + m
    b = s + 2

    t = a
    u = a + 1
    v = [a + 2 + i for i in range(s)]

    edges = []

    # 0,...,k-1 to t
    for i in range(k):
        edges.append([i,t])
    # 0 to u
    edges.append([0,u])
    # k,...,k+m-1 to u
    for i in range(m):
        edges.append([k+i,u])
    # k-1 to v_1,...,v_s
    for i in range(s):
        edges.append([k-1,v[i]])

    graph = PaceGraph(a, b, edges)

    # Median
    k = old_k
    a = 4*k + 2
    b = 4*k + 2

    u = a + 2 * k + 1
    v = u + 1

    edges = []

    for i in range(a, u):
        edges.append([0, i])
    for i in range(k):
        edges.append([i,v])
    for i in range(2*k+1,3*k+2):
        edges.append([i,v])
    for i in range(k,2*k+1):
        edges.append([i,u])
    for i in range(3*k+2,a):
        edges.append([i,u])
    for i in range(v+1, a+b):
        edges.append([a-1,i])

    edges = sorted(edges)
    graph2 = PaceGraph(a, b, edges)

    gg = join_graphs(graph, graph2, True, True)

    a = gg.left
    b = len(gg.right)
    edges = gg.edgeset
    edges = shuffle(edges, a, b, sl, sr)
    edges = sorted(edges)
    graph = PaceGraph(a, b, edges)

    write_graph(graph, outfile)

@cli.command()
@click.option("-n", default=8, type=int, help="Number of vertices")
@click.option("-p", default=0.5, type=click.FloatRange(0,1), help="Probability of opening a parenthesis")
@click.option("-sl", is_flag=True, default=False, help="Shuffle left side")
@click.option("-sr", is_flag=True, default=False, help="Shuffle right side")
@click.argument("outfile", required=False)
def bipartitepermutation(n, p, sl, sr, outfile):
    # following https://11011110.github.io/blog/2012/12/08/notation-for-321-avoiding.html

    # first generate a dyck_word
    dyck_word = dyck(2 * n, p)
    #print(dyck_word)
    # put pairs together
    dyck_2 = [dyck_word[2*i] + dyck_word[2*i + 1] for i in range(n)]
    #print(dyck_2)
    # ">" → "(("
    # "<" → "))"
    # "|" → "()"
    # "/" → "()"
    # "\" → ")("
    sequence = []
    opening = 0
    for d in dyck_2:
        if d == '((':
            sequence.append('>')
            opening += 2
        elif d == '))':
            sequence.append('<')
            opening -= 2
        elif d == ')(':
            sequence.append('\\')
        elif d == '()':
            if opening == 0:
                sequence.append('|')
            else:
                sequence.append('/')
        else:
            print("Invalid dyck word")
            return

    #print(sequence)

    edges = []
    a = 0
    b = 0

    # first count number of vertices in a
    for c in sequence:
        if c == "/" or c == ">":
            b += 1

    a_start = 0
    a_end = 0
    b_start = b
    b_end = b

    for c in sequence:
        if c == "/":
            for i in range(b_start,b_end):
                edges.append([a_end-1, i])
            a_end += 1
            b_start += 1
        elif c == "\\":
            for i in range(a_start,a_end):
                edges.append([i, b_end-1])
            a_start += 1
            b_end += 1
        elif c == ">":
            a_end += 1
            b_end += 1
        elif c == "<":
            for i in range(a_start,a_end):
                edges.append([i, b_end-1])
            for i in range(b_start,b_end):
                edges.append([a_end-1, i])
            a_start += 1
            b_start += 1

    a = a_end
    b = b_end - a_end
    edges = shuffle(edges, a, b, sl, sr)
    edges = sorted(edges)
    #print(a)
    #print(b)
    #print(edges)

    if not outfile:
        outfile = f"test_set/bipartitepermutation-{n}-{a}-{b}.gr"

    #print(outfile)
    graph = PaceGraph(a, b, edges)
    write_graph(graph, outfile)


def dyck(n, p):
    #Generator for Dyck words.
    if n % 2 == 1:
        print("n must be even")
        return
    dyck_word = ['(']
    opening = 1
    pos = 1
    while n > pos:
        if n - pos == opening:
            dyck_word.append(')')
            opening -= 1
        elif opening <= 1:
            # open another parenthesis
            dyck_word.append('(')
            opening += 1
        elif random.random() < p:
            # open another parenthesis
            dyck_word.append('(')
            opening += 1
        else:
            # close a parenthesis
            dyck_word.append(')')
            opening -= 1
        pos += 1
    return dyck_word

@cli.command()
@click.option("-a", default=10, type=int, help="Number of vertices on A.")
@click.option("-b", default=10, type=int, help="Number of vertices on A.")
@click.option("-k", default=4, type=int, help="Size of the vertex cover.")
@click.option("-m", default=20, type=int, help="NUmber of edges.")
@click.option("-sl", is_flag=True, default=False, help="Shuffle left side")
@click.option("-sr", is_flag=True, default=False, help="Shuffle right side")
@click.argument("outfile", required=False)
def vertexcover(a, b, k, m, sl, sr, outfile):
    if not outfile:
        outfile = f"test_set/vertex-cover-{k}-{a}-{b}-{m}.gr"
    possible_edges = []
    centers_a = []
    centers_b = []
    while len(centers_a) == 0 or len(centers_b) == 0 or len(possible_edges) < m:
        centers = random.sample(range(a+b), k=k)
        centers_a = list(filter(lambda x : x < a, centers))
        centers_b = list(filter(lambda x : x >= a, centers))
        possible_edges = list(product(centers_a, range(a,a+b)))
        possible_edges.extend(list(product(range(a), centers_b)))
    edges = sorted(random.sample(possible_edges, k=m))

    graph = PaceGraph(a, b, shuffle(edges, a, b, sl, sr))
    write_graph(graph, outfile)

@cli.command()
@click.option("-a", default=10, type=int, help="Size of left bipartition.")
@click.option("-b", default=10, type=int, help="Size of right bipartition.")
@click.option("-k", default=5, type=int, help="Cutwidth.")
@click.option("-m", default=20, type=int, help="Number of edges.")
@click.option("-sl", is_flag=True, default=False, help="Shuffle left side")
@click.option("-sr", is_flag=True, default=False, help="Shuffle right side")
@click.argument("outfile", required=False)
def cutwidth(a, b, k, m, sl, sr, outfile):
    if not outfile:
        outfile = f"test_set_cutwidth/cutwidth-{k}-{a}-{b}-{m}.gr"
    permutation = []
    i = 0
    j = 0
    while i < a and j < b:
        if random.random() < 0.5:
            permutation.append(i)
            i += 1
        else:
            permutation.append(j+a)
            j += 1
    if i < a:
        permutation.extend(range(i,a))
    if j < b:
        permutation.extend(range(a+j,a+b))
    permutation_map = [0 for _ in range(a+b)]
    for i in permutation:
        permutation_map[permutation[i]] = i

    all_edges = list(product(range(a), range(a,a+b)))

    i = 0
    edges = []
    random.shuffle(all_edges)
    # count how many edges are between i and i+1
    cutwidth = [0 for _ in range(a+b-1)]
    for edge in all_edges:
        u = permutation_map[edge[0]]
        v = permutation_map[edge[1]]
        if u > v:
            u = v
            v = permutation_map[edge[0]]
        max_c = np.max(cutwidth[u:v])
        if max_c < k:
            edges.append(edge)
            for j in range(u,v):
                cutwidth[j] += 1
            i += 1
            if i == m:
                break


    c = np.max(cutwidth)
    edges = sorted(edges)
    #print(permutation)
    #print(cutwidth)
    #print(edges)

    graph = PaceGraph(a, b, shuffle(edges, a, b, sl, sr))
    write_graph_cutwidth(graph, permutation, c, outfile)

@cli.command()
@click.option("-a", default=10, type=int, help="Size of left bipartition.")
@click.option("-b", default=10, type=int, help="Size of right bipartition.")
@click.option("-k", default=5, type=int, help="Cutwidth.")
@click.option("-span", default=5, type=int, help="Max span of edges")
@click.option("-m", default=20, type=int, help="Number of edges.")
@click.option("-f", is_flag=True, default=False, help="Take graph even if too few edges")
@click.option("-sl", is_flag=True, default=False, help="Shuffle left side")
@click.option("-sr", is_flag=True, default=False, help="Shuffle right side")
@click.argument("outfile", required=False)
def cutwidth_span(a, b, k, span, m, f, sl, sr, outfile):
    if not outfile:
        outfile = f"test_set_cutwidth/cutwidth-span-{k}-{a}-{b}-{m}.gr"
    permutation = []
    i = 0
    j = 0
    while i < a and j < b:
        if random.random() < 0.5:
            permutation.append(i)
            i += 1
        else:
            permutation.append(j+a)
            j += 1
    if i < a:
        permutation.extend(range(i,a))
    if j < b:
        permutation.extend(range(a+j,a+b))
    permutation_map = [0 for _ in range(a+b)]
    for i in permutation:
        permutation_map[permutation[i]] = i

    all_edges = list(product(range(a), range(a,a+b)))
    print(len(all_edges))

    i = 0
    while i < m:
        i = 0
        edges = []
        random.shuffle(all_edges)
        # count how many edges are between i and i+1
        cutwidth = [0 for _ in range(a+b-1)]
        with alive_bar(m) as bar:
            for edge in all_edges:
                u = permutation_map[edge[0]]
                v = permutation_map[edge[1]]
                if u > v:
                    u = v
                    v = permutation_map[edge[0]]
                # only add edges with span at most span
                if v < u + span + 1:
                    max_c = np.max(cutwidth[u:v])
                    if max_c < k:
                        edges.append(edge)
                        for j in range(u,v):
                            cutwidth[j] += 1
                        i += 1
                        bar()
                        if i == m:
                            break
        if f:
            break


    c = np.max(cutwidth)
    edges = sorted(edges)
    #print(permutation)
    #print(cutwidth)
    #print(edges)

    graph = PaceGraph(a, b, shuffle(edges, a, b, sl, sr))
    write_graph_cutwidth(graph, permutation, c, outfile)

@cli.command()
@click.option("-a", default=10, type=int, help="Size of left bipartition.")
@click.option("-b", default=10, type=int, help="Size of right bipartition.")
@click.option("-k", default=5, type=int, help="Cutwidth.")
@click.option("-m", default=20, type=int, help="Number of edges.")
@click.option("-sl", is_flag=True, default=False, help="Shuffle left side")
@click.option("-sr", is_flag=True, default=False, help="Shuffle right side")
@click.argument("outfile", required=False)
def cutwidth_force(a, b, k, m, sl, sr, outfile):
    if not outfile:
        outfile = f"test_set_cutwidth/cutwidth-{k}-{a}-{b}-{m}.gr"
    permutation = []
    i = 0
    j = 0
    while i < a and j < b:
        if random.random() < 0.5:
            permutation.append(i)
            i += 1
        else:
            permutation.append(j+a)
            j += 1
    if i < a:
        permutation.extend(range(i,a))
    if j < b:
        permutation.extend(range(a+j,a+b))
    permutation_map = [0 for _ in range(a+b)]
    for i in permutation:
        permutation_map[permutation[i]] = i

    all_edges = list(product(range(a), range(a,a+b)))

    i = 0
    edges = []
    random.shuffle(all_edges)
    # count how many edges are between i and i+1
    cutwidth = [0 for _ in range(a+b-1)]
    with alive_bar(m) as bar:
        for edge in all_edges:
            u = permutation_map[edge[0]]
            v = permutation_map[edge[1]]
            if u > v:
                u = v
                v = permutation_map[edge[0]]
            max_c = np.max(cutwidth[u:v])
            if max_c < k:
                edges.append(edge)
                for j in range(u,v):
                    cutwidth[j] += 1
                i += 1
                bar()
                if i == m:
                    break


    c = np.max(cutwidth)
    edges = sorted(edges)
    #print(permutation)
    #print(cutwidth)
    #print(edges)

    graph = PaceGraph(a, b, shuffle(edges, a, b, sl, sr))
    write_graph_cutwidth(graph, permutation, c, outfile)

@cli.command()
@click.option("-gone", type=click.STRING, help="First graph.")
@click.option("-gtwo", type=click.STRING, help="Second graph.")
@click.option("-jl", is_flag=True, default=False, help="Join at fixed side.")
@click.option("-jr", is_flag=True, default=False, help="Join at flexible side.")
@click.option("-sl", is_flag=True, default=False, help="Shuffle left side.")
@click.option("-sr", is_flag=True, default=False, help="Shuffle right side.")
@click.argument("outfile", required=False)
def join_graphs_from_files(gone, gtwo, sl, sr, jl, jr, outfile):
    graph1 = read_graph(gone)
    graph2 = read_graph(gtwo)
    new_a = graph1.left + graph2.left
    if jl:
        new_a -= 1
    new_b = len(graph1.right) + len(graph2.right)
    if jr:
        new_b -= 1
    if not outfile:
        outfile = f"test_set/joined-{graph1.left}-{graph2.left}.gr"

    graph = join_graphs(graph1, graph2, jl, jr)
    edges = graph.edgeset

    graph = PaceGraph(new_a, new_b, shuffle(edges, new_a, new_b, sl, sr))
    write_graph(graph, outfile)

def join_graphs(graph1, graph2, jl, jr):

    # one_right_bottom = graph1.left
    # one_right_top = graph1.left + len(graph1.right)
    # two_left_bottom = 1
    # two_left_top = graph2.left + 1

    new_a = graph1.left + graph2.left
    if jl:
        new_a -= 1
    new_b = len(graph1.right) + len(graph2.right)
    if jr:
        new_b -= 1
    mapping_one_left = lambda x : x
    mapping_one_right = lambda x : x + graph2.left - (1 if jl else 0)
    mapping_two_left = lambda x : x + graph1.left - (1 if jl else 0)
    mapping_two_right = lambda x : x + graph1.left + len(graph1.right) - (1 if jl else 0) - (1 if jr else 0)
    # for i in range(graph1.left):
    #     mapping_one[i] = i
    # for i in range(graph2.left):
    #     new_value = i + graph1.left
    #     if jl:
    #         new_value -= 1
    #     mapping_two[i] = new_value
    # for i in graph1.right:
    #     new_value = i + graph2.left - 1
    #     if jl:
    #         new_value -= 1
    #     mapping_one[i-1] = new_value
    # for i in graph2.right:
    #     new_value = i + graph1.left + len(graph1.right) - 1
    #     if jl:
    #         new_value -= 1
    #     if jr:
    #         new_value -= 1
    #     mapping_two[i-1] = new_value

    #print(mapping_one)
    #print()
    #print(mapping_two)

    edges = []
    for u, v in graph1.edgeset:
        edges.append([mapping_one_left(u), mapping_one_right(v)])
    for u, v in graph2.edgeset:
        edges.append([mapping_two_left(u), mapping_two_right(v)])

    edges = set(map(tuple, edges))

    return PaceGraph(new_a, new_b, edges)

@cli.command()
@click.option("-n", default=6, type=int, help="Number of cycles")
@click.option("-min", default=4, type=int, help="Min length")
@click.option("-max", default=12, type=int, help="Max length")
@click.option("-sl", is_flag=True, default=False, help="Shuffle left side")
@click.option("-sr", is_flag=True, default=False, help="Shuffle right side")
@click.argument("outfile", required=False)
def joined_cycles(n, min, max, sl, sr, outfile):
    if not outfile:
        outfile = f"test_set/joinedcycles-{n}-{min}-{max}.gr"

    edges = []
    a = random.randint(int(min/2), int(max/2))
    for i in range(a-1):
        edges.append([i,a+i])
        edges.append([i+1,a+i])
    edges.append([a-1,a+a-1])
    edges.append([0,a+a-1])
    graph = PaceGraph(a, a, edges)

    for j in range(1,n):
        edges = []
        a = random.randint(int(min/2), int(max/2))
        for i in range(a-1):
            edges.append([i,a+i])
            edges.append([i+1,a+i])
        edges.append([a-1,a+a-1])
        edges.append([0,a+a-1])
        graph2 = PaceGraph(a, a, edges)
        graph = join_graphs(graph, graph2, True, True)

    edges = graph.edgeset
    a = graph.left
    b = len(graph.right)
    shuffle(edges, a, b, sl, sr)
    graph = PaceGraph(a, b, edges)

    write_graph(graph,outfile)

@cli.command()
@click.option("-a", default=8, type=int, help="vertices in A")
@click.option("-b", default=8, type=int, help="vertices in B")
@click.option("-s", default=4, type=int, help="Maximum number of neighbors")
@click.option("-k", default=2, type=int, help="Neighborhood diversity")
@click.option("-sl", is_flag=True, default=False, help="Shuffle left side")
@click.option("-sr", is_flag=True, default=False, help="Shuffle right side")
@click.argument("outfile", required=False)
def neighborhood_diversity(a, b, k, s, sl, sr, outfile):
    if not outfile:
        outfile = f"test_set/neighborhooddiversity-{a}-{b}-{k}.gr"

    # could produce the same set twice, but unlikely. otherwise too slow

    right = range(a,a+b)
    num_sets = math.ceil(a / k)
    sets: List[List]
    sets = [[] for _ in range(num_sets)]
    for i in range(num_sets):
        sets[i] = sorted(random.sample(right, k=random.randint(1,s)))
    edges = []
    for i in range(a):
        for v in sets[math.floor(i / k)]:
            edges.append([i,v])
    #print(edges)

    shuffle(edges, a, b, sl, sr)
    graph = PaceGraph(a, b, edges)

    write_graph(graph,outfile)



    #shuffle(edges, a, b, sl, sr)
    #graph = PaceGraph(a, b, edges)

    #write_graph(graph,outfile)

@cli.command()
@click.option("-n1", default=10, type=int, help="Min number of vertices of planar graphs.")
@click.option("-n2", default=20, type=int, help="Max number of vertices of planar graphs.")
@click.option("-d1", default=1.2, type=click.FloatRange(1,1.95), help="Min density of planar graphs.")
@click.option("-d2", default=1.8, type=click.FloatRange(1,1.95), help="Max density of planar graphs.")
@click.option("-k", default=5, type=int, help="Number of planar graphs")
@click.option("-ka", default=2, type=int, help="a in K_{a,b} connectors.")
@click.option("-kb", default=3, type=int, help="b in K_{a,b} connectors.")
@click.option("-sl", is_flag=True, default=False, help="Shuffle left side")
@click.option("-sr", is_flag=True, default=False, help="Shuffle right side")
@click.argument("outfile", required=False)
def uniformplanar_connected_kabs(n1, n2, d1, d2, k, ka, kb, sl, sr, outfile):

    n = random.randint(n1,n2+1)
    a = math.floor(n / 2)
    b = math.ceil(n / 2)
    m = math.floor(random.uniform(d1,d2) * n)

    all_edges = list(product(range(a), range(a,a+b)))
    random.shuffle(all_edges)
    G = nx.empty_graph()
    G.add_nodes_from(range(a+b))
    edges = []

    i = 0
    with alive_bar(m) as bar:
        for edge in all_edges:
            G.add_edge(edge[0], edge[1])
            if not nx.is_planar(G):
                G.remove_edge(edge[0], edge[1])
            else:
                edges.append(edge)
                i += 1
                bar()
                if i == m:
                    break

    graph = PaceGraph(a, b, edges)

    for j in range(k):
        Kabx = nx.complete_bipartite_graph(ka, kb)
        a, b, edges = pace_from_nx(Kabx)
        Kab = PaceGraph(a, b, edges)
        graph = join_graphs(graph, Kab, True, True)


        n = random.randint(n1,n2+1)
        a = math.floor(n / 2)
        b = math.ceil(n / 2)
        m = math.floor(random.uniform(d1,d2) * n)

        all_edges = list(product(range(a), range(a,a+b)))
        random.shuffle(all_edges)
        G = nx.empty_graph()
        G.add_nodes_from(range(a+b))
        edges = []

        i = 0
        with alive_bar(m) as bar:
            for edge in all_edges:
                G.add_edge(edge[0], edge[1])
                if not nx.is_planar(G):
                    G.remove_edge(edge[0], edge[1])
                else:
                    edges.append(edge)
                    i += 1
                    bar()
                    if i == m:
                        break

        pg = PaceGraph(a, b, edges)
        graph = join_graphs(graph, pg, True, True)

    if not outfile:
        outfile = f"test_set/uniform-planar-connected-{graph.left}-{len(graph.right)}-{len(graph.edgeset)}.gr"

    write_graph(graph, outfile)

@cli.command()
@click.option("-n1", default=10, type=int, help="Min number of vertices of graphs.")
@click.option("-n2", default=20, type=int, help="Max number of vertices of graphs.")
@click.option("-d1", default=1.2, type=click.FloatRange(1,1.95), help="Min density of graphs.")
@click.option("-d2", default=2, type=float, help="Max density of graphs.")
@click.option("-k", default=5, type=int, help="Number of graphs")
@click.option("-ka", default=2, type=int, help="a in K_{a,b} connectors.")
@click.option("-kb", default=3, type=int, help="b in K_{a,b} connectors.")
@click.option("-sl", is_flag=True, default=False, help="Shuffle left side")
@click.option("-sr", is_flag=True, default=False, help="Shuffle right side")
@click.argument("outfile", required=False)
def uniform_connected_kabs(n1, n2, d1, d2, k, ka, kb, sl, sr, outfile):

    n = random.randint(n1,n2+1)
    a = math.floor(n / 2)
    b = math.ceil(n / 2)
    m = math.floor(random.uniform(d1,d2) * n)

    all_edges = list(product(range(a), range(a,a+b)))
    edges = sorted(random.sample(all_edges, k=m))

    graph = PaceGraph(a, b, edges)

    for j in range(k):
        Kabx = nx.complete_bipartite_graph(ka, kb)
        a, b, edges = pace_from_nx(Kabx)
        Kab = PaceGraph(a, b, edges)
        graph = join_graphs(graph, Kab, True, True)


        n = random.randint(n1,n2+1)
        a = math.floor(n / 2)
        b = math.ceil(n / 2)
        m = math.floor(random.uniform(d1,d2) * n)

        all_edges = list(product(range(a), range(a,a+b)))
        edges = sorted(random.sample(all_edges, k=m))

        pg = PaceGraph(a, b, edges)
        graph = join_graphs(graph, pg, True, True)

    if not outfile:
        outfile = f"test_set/uniform-connected-{graph.left}-{len(graph.right)}-{len(graph.edgeset)}.gr"

    write_graph(graph, outfile)

@cli.command()
@click.option("-k1", default=3, type=int, help="Min k for barycenter.")
@click.option("-k2", default=8, type=int, help="Max k for barycenter.")
@click.option("-k", default=5, type=int, help="Number of graphs")
@click.option("-ka", default=2, type=int, help="a in K_{a,b} connectors.")
@click.option("-kb", default=2, type=int, help="b in K_{a,b} connectors.")
@click.option("-sl", is_flag=True, default=False, help="Shuffle left side")
@click.option("-sr", is_flag=True, default=False, help="Shuffle right side")
@click.argument("outfile", required=False)
def barycenter_connected_kabs(k1, k2, k, ka, kb, sl, sr, outfile):
    m = random.randint(k1,k2+1)
    K = int((2 + m + m * m) / 2)
    s = K - 1

    a = K + m
    b = s + 2

    t = a
    u = a + 1
    v = [a + 2 + i for i in range(s)]

    edges = []

    # 0,...,k-1 to t
    for i in range(K):
        edges.append([i,t])
    # 0 to u
    edges.append([0,u])
    # k,...,k+m-1 to u
    for i in range(m):
        edges.append([K+i,u])
    # k-1 to v_1,...,v_s
    for i in range(s):
        edges.append([K-1,v[i]])

    graph = PaceGraph(a, b, edges)

    for j in range(k):
        Kabx = nx.complete_bipartite_graph(ka, kb)
        a, b, edges = pace_from_nx(Kabx)
        Kab = PaceGraph(a, b, edges)
        graph = join_graphs(graph, Kab, True, False)

        m = random.randint(k1,k2+1)
        K = int((2 + m + m * m) / 2)
        s = K - 1

        a = K + m
        b = s + 2

        t = a
        u = a + 1
        v = [a + 2 + i for i in range(s)]

        edges = []

        # 0,...,k-1 to t
        for i in range(K):
            edges.append([i,t])
        # 0 to u
        edges.append([0,u])
        # k,...,k+m-1 to u
        for i in range(m):
            edges.append([K+i,u])
        # k-1 to v_1,...,v_s
        for i in range(s):
            edges.append([K-1,v[i]])

        pg = PaceGraph(a, b, edges)
        graph = join_graphs(graph, pg, True, False)

    if not outfile:
        outfile = f"test_set/barycenter-connected-kabs-{graph.left}-{len(graph.right)}-{len(graph.edgeset)}.gr"

    write_graph(graph, outfile)
@cli.command()
@click.option("-a1", default=10, type=int, help="Min number of vertices of A.")
@click.option("-a2", default=20, type=int, help="Max number of vertices of A.")
@click.option("-b1", default=10, type=int, help="Min number of vertices of B.")
@click.option("-b2", default=20, type=int, help="Max number of vertices of B.")
@click.option("-k", default=3, type=int, help="k-tree")
@click.option("-num", default=5, type=int, help="Number of graphs")
@click.option("-sl", is_flag=True, default=False, help="Shuffle left side")
@click.option("-sr", is_flag=True, default=False, help="Shuffle right side")
@click.argument("outfile", required=False)
def connected_ktrees(a1, a2, b1, b2, k, num, sl, sr, outfile):

    a = random.randint(a1-1,a2)
    b = random.randint(b1-1,b2)

    # start with k-clique
    sets = []
    edges = []
    set = []
    for i in range(math.ceil(k/2)):
        set.append(i)
        for j in range(a,a+math.floor(k/2)):
            edges.append([i,j])
    for j in range(a,a+math.floor(k/2)):
        set.append(j)
    sets.append(set)
    curr_a = math.ceil(k/2)
    curr_b = math.floor(k/2)

    while curr_a < a or curr_b < b:
        # randomly choose set from sets
        set = random.choice(sets)
        #print(sets)
        # randomly pick which side to add to
        if curr_b == b or (curr_a < a and random.random() < 0.5):
            # add to A
            for neighbor in set:
                if neighbor > a-1:
                    edges.append([curr_a,neighbor])
                new_set = list(filter(lambda x : x != neighbor, set))
                new_set.append(curr_a)
                sets.append(new_set)
            curr_a += 1
        else:
            # add to B
            for neighbor in set:
                if neighbor < a:
                    edges.append([neighbor,a+curr_b])
                new_set = list(filter(lambda x : x != neighbor, set))
                new_set.append(a+curr_b)
                sets.append(new_set)
            curr_b += 1

    graph = PaceGraph(a, b, edges)

    for j in range(num-1):

        a = random.randint(a1-1,a2)
        b = random.randint(b1-1,b2)

        # start with k-clique
        sets = []
        edges = []
        set = []
        for i in range(math.ceil(k/2)):
            set.append(i)
            for j in range(a,a+math.floor(k/2)):
                edges.append([i,j])
        for j in range(a,a+math.floor(k/2)):
            set.append(j)
        sets.append(set)
        curr_a = math.ceil(k/2)
        curr_b = math.floor(k/2)

        while curr_a < a or curr_b < b:
            # randomly choose set from sets
            set = random.choice(sets)
            #print(sets)
            # randomly pick which side to add to
            if curr_b == b or (curr_a < a and random.random() < 0.5):
                # add to A
                for neighbor in set:
                    if neighbor > a-1:
                        edges.append([curr_a,neighbor])
                    new_set = list(filter(lambda x : x != neighbor, set))
                    new_set.append(curr_a)
                    sets.append(new_set)
                curr_a += 1
            else:
                # add to B
                for neighbor in set:
                    if neighbor < a:
                        edges.append([neighbor,a+curr_b])
                    new_set = list(filter(lambda x : x != neighbor, set))
                    new_set.append(a+curr_b)
                    sets.append(new_set)
                curr_b += 1

        graph2 = PaceGraph(a, b, edges)
        graph = join_graphs(graph, graph2, True, True)

    if not outfile:
        outfile = f"test_set/connected-{k}-tree-{num}-{graph.left}-{len(graph.right)}-{len(graph.edgeset)}.gr"

    write_graph(graph, outfile)

if __name__ == "__main__":
    cli()


# even cycle
# star
# ladder
# complete bipartite
# random bipartite
# forest of 4 stars
# matching
# larger tree
# grid
# crown graph
# path
