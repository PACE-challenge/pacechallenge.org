import tkinter as tk
import networkx as nx
import sys
from utils import read_graph
import time

# DRAWING PARAMETERS
CANVAS_PAD = 5 					# distance to canvas border
NODE_DISTANCE_TOP = 0.5			# distance between nodes (top)
NODE_DISTANCE_BOTTOM = 0.5 		# distance between nodes (bottom)
VERTICAL_DISTANCE = 0.5			# distance between the two layers
NODE_SIZE = 20 					# node size
LINE_WIDTH = 1  				# line thickness
HORIZONTAL_SCALING_FORCE = 0.5  # Horizontal scaling of the force directed drawing
VERTICAL_SCALING_FORCE = 0.5  	# Vertical scaling of the force directed drawing

solution_provided = False
current_mode = None
last_drawing_update_time = time.time()
pos = {}

# A shortcut to draw circles
def _create_circle(self, x, y, r, **kwargs):
	return self.create_oval(x-r, y-r, x+r, y+r, **kwargs)
tk.Canvas.create_circle = _create_circle

# A callback for the window resize
def on_window_resize(event):
	root.update()
	width = canvas.winfo_width()
	draw_with_mode()

# For debugging
def log_graph():
	print("Logging graph")
	print(f"\t{graph}")
	print("Single properties")
	print(f"\t{graph.a}")
	print(f"\t{graph.b}")
	print(f"\t{graph.G}")
	print("End logging")

def log_orders():
	print("Logging orders")
	print(f"\ttop order: {top_order}")
	print(f"\tinput_bottom: {original_bottom_order}")
	print(f"\torder provided: {solution_provided}")
	print(f"\tsolution_bottom: {solution_bottom_order}")
	print(f"\tcurrent: {bottom_order}")
	print("End logging")

# For fixed node positions this draws the edges
def draw_edges(lcenters, rcenters):
	for e in graph.G.edges:
		s = lcenters[top_order[e[0]]]
		t = rcenters[bottom_order[e[1]]]
		canvas.create_line(*s, *t, fill="#AAA", width=LINE_WIDTH*1.5)
		canvas.create_line(*s, *t, width=LINE_WIDTH)

# For fixed node positions this draws the nodes
def draw_nodes(lcenters, rcenters):
	hrs = NODE_SIZE/2.0
	color = "#9fc0de"
	for i in range(1, graph.a+1):
		center = lcenters[top_order[i]]
		canvas.create_circle(center[0], center[1], hrs, width=LINE_WIDTH*1.5, outline="#AAA")
		canvas.create_circle(center[0], center[1], hrs, width=LINE_WIDTH, fill=color)
		canvas.create_text(center, text=f"{i}", fill="black", font=('Arial', int(hrs)))
	color = "#f2c894"
	for i in range(graph.a+1, graph.a+graph.b+1):
		center = rcenters[bottom_order[i]]
		canvas.create_circle(center[0], center[1], hrs, width=LINE_WIDTH*1.5, outline="#AAA")
		canvas.create_circle(center[0], center[1], hrs, width=LINE_WIDTH, fill=color)
		canvas.create_text(center, text=f"{i}", fill="black", font=('Arial', int(hrs)))

# Method draws a graph with the current orders
def draw_graph():
	canvas.delete('all')
	root.update()
	canvas_width = canvas.winfo_width()
	canvas_height = canvas.winfo_height()
	padding_to_center = 2*CANVAS_PAD + 2*NODE_SIZE
	horizontal_distance_top = NODE_DISTANCE_TOP * (canvas_width - padding_to_center) / (graph.a - 1)
	horizontal_distance_top = max(horizontal_distance_top, NODE_SIZE)
	horizontal_distance_bottom = NODE_DISTANCE_BOTTOM * (canvas_width - padding_to_center) / (graph.b - 1)
	horizontal_distance_bottom = max(horizontal_distance_bottom, NODE_SIZE)
	vertical_distance = max(VERTICAL_DISTANCE*canvas_height-padding_to_center, 50)
	horizontal_canvas_padding_top = max(padding_to_center, canvas_width - (horizontal_distance_top*(graph.a-1)))
	horizontal_canvas_padding_bottom = max(padding_to_center, canvas_width - (horizontal_distance_bottom*(graph.b-1)))
	vertical_padding = max(padding_to_center, canvas_height - vertical_distance)
	lcenters = [(horizontal_canvas_padding_top/2 + horizontal_distance_top * i, vertical_padding/2) for i in range(0, graph.a)]
	rcenters = [(horizontal_canvas_padding_bottom/2 + horizontal_distance_bottom * i, vertical_padding/2 + vertical_distance) for i in range(0, graph.b)]
	draw_edges(lcenters, rcenters)
	draw_nodes(lcenters, rcenters)

def draw_with_mode(mode = None):
	current_time = time.time()
	global last_drawing_update_time
	global current_mode
	changed_mode = False
	if current_time - last_drawing_update_time > 0.0417: # 24fps, but theres still flickering
		last_drawing_update_time = current_time
		if mode is not None:
			changed_mode = True
			current_mode = mode
		if current_mode == "input":
			global scale_h_scaling_force
			scale_h_scaling_force['fg'] = "grey"
			scale_v_scaling_force['fg'] = "grey"
			scale_h_scaling_force['state'] = "disabled"
			scale_v_scaling_force['state'] = "disabled"
			scale_node_distance_top['fg'] = "black"
			scale_node_distance_bottom['fg'] = "black"
			scale_vertical_distance['fg'] = "black"
			scale_node_distance_top['state'] = "normal"
			scale_node_distance_bottom['state'] = "normal"
			scale_vertical_distance['state'] = "normal"
			draw_graph_with_order(original_bottom_order)
		elif current_mode == "sol":
			scale_h_scaling_force['fg'] = "grey"
			scale_v_scaling_force['fg'] = "grey"
			scale_h_scaling_force['state'] = "disabled"
			scale_v_scaling_force['state'] = "disabled"
			scale_node_distance_top['fg'] = "black"
			scale_node_distance_bottom['fg'] = "black"
			scale_vertical_distance['fg'] = "black"
			scale_node_distance_top['state'] = "normal"
			scale_node_distance_bottom['state'] = "normal"
			scale_vertical_distance['state'] = "normal"
			if solution_bottom_order == None:
				print("No solution order was provided")
			else:
				draw_graph_with_order(solution_bottom_order)
		elif current_mode == "force":
			scale_node_distance_top['fg'] = "grey"
			scale_node_distance_bottom['fg'] = "grey"
			scale_vertical_distance['fg'] = "grey"
			scale_node_distance_top['state'] = "disabled"
			scale_node_distance_bottom['state'] = "disabled"
			scale_vertical_distance['state'] = "disabled"
			scale_h_scaling_force['fg'] = "black"
			scale_v_scaling_force['fg'] = "black"
			scale_h_scaling_force['state'] = "normal"
			scale_v_scaling_force['state'] = "normal"
			draw_graph_force(changed_mode)

def draw_graph_with_order(order):
	# The method reorders the bottom
	# Assumes that order contains the correct values
	global bottom_order
	bottom_order = order.copy()
	draw_graph()

def draw_graph_force(recompute=False):
	canvas.delete('all')
	root.update()
	canvas_width = canvas.winfo_width()
	canvas_height = canvas.winfo_height()
	padding_to_center = 2*CANVAS_PAD + 2*NODE_SIZE
	hrs = NODE_SIZE/2.0
	global pos
	if recompute:
		pos = nx.spring_layout(graph.G)

	minx, miny, maxx, maxy = float('inf'), float('inf'), float('-inf'), float('-inf')
	for v in graph.G.nodes:
		if pos[v][0] > maxx:
			maxx = pos[v][0]
		if pos[v][0] < minx:
			minx = pos[v][0]
		if pos[v][1] > maxy:
			maxy = pos[v][1]
		if pos[v][1] < miny:
			miny = pos[v][1]

	deltax = (canvas_width * (1 - HORIZONTAL_SCALING_FORCE)) / 2
	deltay = (canvas_height * (1 - VERTICAL_SCALING_FORCE)) / 2

	newpos = {}

	for p in pos:
		newpos[p] = (
			(pos[p][0]-minx)*(HORIZONTAL_SCALING_FORCE*(canvas_width - padding_to_center)/(maxx-minx))+NODE_SIZE + deltax, 
			(pos[p][1]-miny)*(VERTICAL_SCALING_FORCE*(canvas_height - padding_to_center)/(maxy-miny))+NODE_SIZE + deltay
			)

	for e in graph.G.edges:
		s = tuple(newpos[e[0]])
		t = tuple(newpos[e[1]])
		canvas.create_line(*s, *t, fill="#AAA", width=LINE_WIDTH*1.5)
		canvas.create_line(*s, *t, width=LINE_WIDTH)

	for v in graph.G.nodes:
		if v <= graph.a:
			color = "#9fc0de"
		else:
			color = "#f2c894"
		canvas.create_circle(*newpos[v], hrs, width=LINE_WIDTH*1.5, outline="#AAA")
		canvas.create_circle(*newpos[v], hrs, width=LINE_WIDTH, fill=color)
		canvas.create_text(*newpos[v], text=f"{v}", fill="black", font=('Arial', int(hrs)))

# Reading command line arguments
graph = read_graph(sys.argv[1])
graph.G.remove_node(0)

# We keep track of the order in which we draw things using a dict
# Key: Node-ID, which starts at 1 (!)
# Value: position, which starts at 0
## top_order technically not needed, the top is fixed
top_order = {}
for i in range(1, graph.a+1):
	top_order[i] = i-1
## bottom_order can be different between input and output
bottom_order = {}
original_bottom_order = {}
solution_bottom_order = {}

# We save a standard lexigraphical order
for i, value in enumerate(list(range(graph.a+1, graph.a+graph.b+1))):
	original_bottom_order[value] = i

if len(sys.argv) > 2:
	# A solution was given on the commandline
	solution_provided = True

	# This assumes that the file conforms to the specified syntax
	with open(sys.argv[2]) as file:
		counter = 0
		for line in file.readlines():
			if line.startswith('p'):
				continue
			ID = int(line)
			solution_bottom_order[ID] = counter
			counter += 1
else:			
	# No solution was given on the commandline
	solution_provided = False

root = tk.Tk()
root.title("Pace 2024 - Visualizer")

width = root.winfo_screenwidth()
height = root.winfo_screenheight()
root.geometry("%dx%d" % (int(width*0.8), int(height*0.8)))

root.bind("<Configure>", on_window_resize)

tk.Grid.rowconfigure(root, 0, weight=1)
tk.Grid.columnconfigure(root, 0, weight=2)
tk.Grid.columnconfigure(root, 1, weight=1)
tk.Grid.columnconfigure(root, 2, weight=1)
tk.Grid.columnconfigure(root, 3, weight=1)
tk.Grid.columnconfigure(root, 4, weight=1)
tk.Grid.columnconfigure(root, 5, weight=1)
tk.Grid.columnconfigure(root, 6, weight=1)

canvas = tk.Canvas(root, bg="white")
canvas.grid(row=0, column=0, columnspan = 7, sticky="nsew")

canvas_legend_a = tk.Canvas(root, height = 40, width = 40)
canvas_legend_a.grid(row=3, column=3, sticky="e")
canvas_middle = [int(canvas_legend_a['width'])/2, int(canvas_legend_a['height'])/2]
canvas_legend_a.create_circle(*canvas_middle, 15, width=2*1.5, outline="#AAA")
canvas_legend_a.create_circle(*canvas_middle, 15, width=2, fill="#9fc0de")
canvas_legend_a.create_text(*canvas_middle, text=f"ID", fill="black", font=('Arial', int(15)))
legen_label_a = tk.Label (root, text="Fixed layer")
legen_label_a.grid(row=3, column=4, sticky="w")

canvas_legend_b = tk.Canvas(root, height = 40, width = 40)
canvas_legend_b.grid(row=3, column=5, sticky="e")
canvas_middle = [int(canvas_legend_b['width'])/2, int(canvas_legend_b['height'])/2]
canvas_legend_b.create_circle(*canvas_middle, 15, width=2*1.5, outline="#AAA")
canvas_legend_b.create_circle(*canvas_middle, 15, width=2, fill="#f2c894")
canvas_legend_b.create_text(*canvas_middle, text=f"ID", fill="black", font=('Arial', int(15)))
legen_label_b = tk.Label (root, text="Permutable layer")
legen_label_b.grid(row=3, column=6, sticky="w")

button_force = tk.Button(root, text="Force layout", command = lambda: draw_with_mode("force"))
button_force.grid(row=3, column=0, sticky="nsew", pady=5, padx=5)
button_input = tk.Button(root, text="Input", command = lambda: draw_with_mode("input"))
button_input.grid(row=4, column=0, sticky="nsew", pady=5, padx=5)
button_solution = tk.Button(root, text="Solution", command = lambda: draw_with_mode("sol"))
button_solution.grid(row=5, column=0, sticky="nsew", pady=5, padx=5)

def c_distance_top_slider(event):
	global NODE_DISTANCE_TOP
	NODE_DISTANCE_TOP = scale_node_distance_top.get()/100
	draw_with_mode()

scale_node_distance_top = tk.Scale(root, from_=1, to=100, orient=tk.HORIZONTAL, showvalue=0, command=c_distance_top_slider, label="Horizontal distance (top)")
scale_node_distance_top.grid(row=3, column=1, columnspan = 2, sticky='ew', pady=5, padx=5)
scale_node_distance_top.set(50)

def c_distance_bottom_slider(event):
	global NODE_DISTANCE_BOTTOM
	NODE_DISTANCE_BOTTOM = scale_node_distance_bottom.get()/100
	draw_with_mode()

scale_node_distance_bottom = tk.Scale(root, from_=1, to=100, orient=tk.HORIZONTAL, showvalue=0, command=c_distance_bottom_slider, label="Horizontal distance (bottom)")
scale_node_distance_bottom.grid(row=4, column=1, columnspan = 2, sticky='ew', pady=5, padx=5)
scale_node_distance_bottom.set(50)

def c_distance_vertical_slider(event):
	global VERTICAL_DISTANCE
	VERTICAL_DISTANCE = scale_vertical_distance.get()/100
	draw_with_mode()

scale_vertical_distance = tk.Scale(root, from_=1, to=100, orient=tk.HORIZONTAL, showvalue=0, command=c_distance_vertical_slider, label="Vertical distance")
scale_vertical_distance.grid(row=5, column=1, columnspan = 2, sticky='ew', pady=5, padx=5)
scale_vertical_distance.set(50)

def c_node_size_slider(event):
	global NODE_SIZE
	NODE_SIZE = scale_node_size.get()/10
	draw_with_mode()

scale_node_size = tk.Scale(root, from_=10, to=500, orient=tk.HORIZONTAL, showvalue=0, command=c_node_size_slider, label="Node size")
scale_node_size.grid(row=4, column=5, columnspan = 2, sticky='ew', pady=5, padx=5)
scale_node_size.set(200)

def c_line_thickness_slider(event):
	global LINE_WIDTH
	LINE_WIDTH = scale_line_thickness.get()/100
	draw_with_mode()

scale_line_thickness = tk.Scale(root, from_=1, to=500, orient=tk.HORIZONTAL, showvalue=0, command=c_line_thickness_slider, label="Line thickness")
scale_line_thickness.grid(row=5, column=5, columnspan = 2, sticky='ew', pady=5, padx=5)
scale_line_thickness.set(100)

def c_horizontal_scaling_force_slider(event):
	global HORIZONTAL_SCALING_FORCE
	HORIZONTAL_SCALING_FORCE = scale_h_scaling_force.get()/100
	draw_with_mode()

scale_h_scaling_force = tk.Scale(root, from_=1, to=100, orient=tk.HORIZONTAL, showvalue=0, command=c_horizontal_scaling_force_slider, label="Horizontal scaling (force)")
scale_h_scaling_force.grid(row=4, column=3, columnspan = 2, sticky='ew', pady=5, padx=5)
scale_h_scaling_force.set(50)

def c_vertical_scaling_force_slider(event):
	global VERTICAL_SCALING_FORCE
	VERTICAL_SCALING_FORCE = scale_v_scaling_force.get()/100
	draw_with_mode()

scale_v_scaling_force = tk.Scale(root, from_=1, to=100, orient=tk.HORIZONTAL, showvalue=0, command=c_vertical_scaling_force_slider, label="Vertical scaling (force)")
scale_v_scaling_force.grid(row=5, column=3, columnspan = 2, sticky='ew', pady=5, padx=5)
scale_v_scaling_force.set(50)

# log_graph()

k_c = 0
turtle = r"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"
t_image = tk.PhotoImage(data=turtle)
def foxhound(event):
	global k_c
	if k_c == 0 or k_c == 1:
		if event.keysym=='Up':
			k_c += 1
		else:
			k_c = 0
	elif k_c == 2 or k_c == 3:
		if event.keysym=='Down':
			k_c += 1
		else:
			k_c = 0
	elif k_c == 4 or k_c == 6:
		if event.keysym=='Left':
			k_c += 1
		else:
			k_c = 0
	elif k_c == 5 or k_c == 7:
		if event.keysym=='Right':
			k_c += 1
		else:
			k_c = 0
	elif k_c == 8:
		if event.keysym=='A' or event.keysym=='a':
			k_c += 1
		else:
			k_c = 0
	elif k_c == 9:
		if event.keysym=='B' or event.keysym=='b':
			k_c += 1
		else:
			k_c = 0
	elif k_c == 10:
		if event.keysym=='Return':
			top = tk.Toplevel(root)
			top.geometry("%dx%d" % (400, 340))
			top.title("You found us!")
			label = tk.Label(top, image=t_image)
			label.pack()
			k_c = 0
		else:
			k_c = 0

root.bind("<KeyRelease>", foxhound)
root.mainloop()
