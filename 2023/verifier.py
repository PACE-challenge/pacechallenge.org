import sys

# Read the graph from a file
def read_graph(f):
    file = open(f)

    # find first non-comment line
    line   = find_next_line(file)
    params = line.split()
    if params[0] == "p":
        n = int(params[2])
        m = int(params[3])
    else:
        print("Input contains a non-comment line before the p-line.")
        raise Exception("MalformedInput", line)    
        
    # initialize all edges and fill them with empty sets
    black_edges = {}
    red_edges   = {}
    for i in range(1, n+1):
        black_edges[i] = set()
        red_edges[i]   = set()

    # read the initial black edges
    for line in file.readlines():
        if line[0] != "c":
            (v,w) = line.split()
            add_edge( black_edges, (int(v), int(w)) )
            
    return (black_edges, red_edges)


# Find the next line that does not contain a comment
def find_next_line(f):
    line = f.readline()
    # we have reached the end of the file
    if not line:
        return line
    # comment lines start with c
    while(line[0] == "c"):
        line = f.readline()
    return line

# Read the contraction sequence from a file        
def read_sequence(f):
    seq = []
    file = open(f)
    for line in file.readlines():
        if line[0] == "c":
            continue
        (v,w) = line.split()
        seq.append((int(v), int(w)))
    return seq

# Return the red degree of the now contracted graph
def red_deg(g, e):
    (v,w) = e
    (black_edges, red_edges) = g
    return len(red_edges[v])

# Test whether both endpoints of e are still part of the graph
def check_in_graph(g,e):
    (v,w) = e
    (black_edges, red_edges) = g
    if v not in black_edges and v not in red_edges:
        print("The vertex " + str(v) + " is not part of the graph anymore")
        raise Exception("VertexNotFound", str(v))
    if w not in black_edges and w not in red_edges:
        print("The vertex " + str(w) + " is not part of the graph anymore")
        raise Exception("VertexNotFound", str(w))    
        
# Contracts the vertices in e in g and update the edges
def contract(g, e):
    # We need to consider several different situations regarding vertices z
    # and their relation to v and w
    (v,w) = e
    (black_edges, red_edges) = g
    remove_edge(black_edges, e)
    remove_edge(red_edges,   e)

    to_be_removed_black = []
    for zw in black_edges[w]:
        # If z is connected to w, but not to v, add a red edge
        if zw not in black_edges[v]:
            add_edge(red_edges,(zw,v))
        # As w will be removed, delete the edge
        to_be_removed_black.append((w,zw))

    to_be_removed_red = []            
    for zw in red_edges[w]:
        # All red edges of w are transfered to v
        add_edge(red_edges,(zw,v))
        # Red edges replace black edges
        remove_edge(black_edges,(zw,v))
        # As w will be removed, delete the edge
        to_be_removed_red.append((w,zw))

    for ze in to_be_removed_red:
        remove_edge(red_edges,ze)

    for zv in black_edges[v]:
        # If z is connected to v, but not to w, replace the black edge by an red edge
        if zv not in black_edges[w]:
            add_edge(red_edges,(zv,v))
            to_be_removed_black.append((zv,v))

    for ze in to_be_removed_black:
            remove_edge(black_edges,ze)

    # For simplicity, remove w
    black_edges.pop(w)
    red_edges.pop(w)
    
# Add an edge e to the graph g    
def add_edge(g,e):
    (v,w) = e
    if v != w:
        g[v].add(w)
        g[w].add(v)
        
# Remove an edge e grom the graph g (if it exists)        
def remove_edge(g,e):
    (v,w) = e
    g[v].discard(w)
    g[w].discard(v)

# Check whether a given contraction sequence seq is valid for g.
# The sequence is only invalid if a removed vertex gets contracted or the graph is not contracted completely. 
def check_sequence(g, seq):
    max_red_deg = 0
    for e in seq:
        if len(g[0]) == 1:
            print("The graph is already contracted.")
            raise Exception("AlreadyContracted")
        check_in_graph(g,e)
        contract(g,e)
        rd = red_deg(g,e)
        max_red_deg = max(max_red_deg, rd)

    # check whether the graph is completely contracted
    if len(g[0]) > 1 or len(g[1]) > 1:
        print("The graph was not completely contracted.")
        raise Exception("NotContracted")
    return max_red_deg
    
# Read g and seq and check seq        
if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Usage: verify.py instance contraction_sequence.")
        exit(1)
    g   = read_graph(sys.argv[1])
    seq = read_sequence(sys.argv[2])
    try: 
        d = check_sequence(g,seq)
        print("Width: " + str(d))
        exit(0)
    except Exception as e:
        print(e)
        exit(1)
