import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

# Load dataset
file_path = "networks_assignment.csv"
df = pd.read_csv(file_path)

# Create graph
G = nx.Graph()

# Add edges from dataset
for _, row in df.iterrows():
    G.add_edge(row['Source'], row['Target'])

# Define node groups
blue_nodes = {'D', 'F', 'I', 'N', 'S'}
green_nodes = {'BIH', 'GEO', 'ISR', 'MNE', 'SRB', 'CHE', 'TUR', 'UKR', 'GBR', 'AUS', 'HKG', 'USA'}
yellow_nodes = {'AUT', 'BEL', 'BGR', 'HRV', 'CZE', 'EST', 'FRA', 'DEU', 'GRC', 'HUN', 'IRL', 'ITA', 'LVA', 'LUX', 'NLD', 'PRT', 'ROU', 'SVK', 'SVN', 'ESP'}

# Assign colors
node_colors = []
for node in G.nodes():
    if node in blue_nodes:
        node_colors.append('blue')
    elif node in green_nodes:
        node_colors.append('green')
    elif node in yellow_nodes:
        node_colors.append('yellow')
    else:
        node_colors.append('gray')

# Define positions
pos = nx.spring_layout(G)
for node in blue_nodes:
    pos[node] = (0, 0)  # Center pentagram positioning

# Draw graph
plt.figure(figsize=(10, 10))
nx.draw(G, pos, with_labels=True, node_color=node_colors, edge_color='gray', node_size=800, font_size=8)
plt.title("Network Graph")
plt.savefig("network_graph.png", dpi=300)
plt.show()
