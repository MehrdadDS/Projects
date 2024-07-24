import pandas as pd
import networkx as nx
import numpy as np


db = pd.read_excel(r'Input\db.xlsx')
db = db.iloc[1:,:]
db = db[db['Pieces']>600000]
division_notations= {
                    'ATLANTIC':"ATL",
                    'QUEBEC':"QBC" ,
                    'GREATER TORONTO AREA':"GTA",
                    'NORTH EASTERN ONTARIO':"NEO",
                    'SOUTH WESTERN ONTARIO':"SWO",
                    'PACIFIC':"PAC",
                    'PRAIRIES':"PRA"
                    }


# Replace Origin Division and Dest Division with notations
db['Origin Division'] = db['Origin Division'].map(division_notations)
db['Dest Division'] = db['Dest Division'].map(division_notations)

import networkx as nx
import matplotlib.pyplot as plt

# Separate data for 2023 and 2024
db_2023 = db[db['Year'] == 2023.0]
db_2024 = db[db['Year'] == 2024.0]

def plot_network_graph_bidirectional_colored_arrows(data, year):
    G = nx.DiGraph()
    for _, row in data.iterrows():
        G.add_edge(row['Origin Division'], row['Dest Division'], weight=row['Pieces'])
    
    pos = {
        'GTA': [0, 0],
        'SWO': [-0.5, -1],
        'NEO': [0, 1],
        'ATL': [1, 1],
        'QBC': [1, -1],
        'PRA': [-0.75, 1],
        'PAC': [-1, 0]
    }
    
    # Define color scheme for edges based on origin
    color_scheme = {
        'GTA': 'green',
        'QBC': 'purple',
        'SWO': 'blue',
        'NEO': 'red',
        'ATL': 'yellow',
        'PRA': 'orange',
        'PAC': 'pink'
    }
    
    plt.figure(figsize=(14, 10))
    
    nx.draw_networkx_nodes(G, pos, node_size=1000, node_color='skyblue')
    nx.draw_networkx_labels(G, pos, font_size=12, font_weight='bold')
    
    edge_labels = {}
    
    def get_edge_angle(pos, node1, node2):
        x1, y1 = pos[node1]
        x2, y2 = pos[node2]
        return np.arctan2(y2 - y1, x2 - x1)
    
    edge_width = 2  # Fixed edge width
    edge_alpha = 1  # Fixed edge transparency
    
    for (u, v, d) in G.edges(data=True):
        weight = d['weight']
        
        nx.draw_networkx_edges(G, pos, edgelist=[(u, v)], width=edge_width, alpha=edge_alpha, 
                               edge_color=color_scheme[u], arrows=True, arrowstyle='-|>', 
                               arrowsize=40, connectionstyle='arc3,rad=0.1')
        
        nx.draw_networkx_edges(G, pos, edgelist=[(v, u)], width=edge_width, alpha=edge_alpha, 
                               edge_color=color_scheme[v], arrows=True, arrowstyle='-|>', 
                               arrowsize=30, connectionstyle='arc3,rad=-0.1')
        
        edge_labels[(u, v)] = f"{weight / 1e6:.1f}M"
    
    label_pos = {}
    for (u, v), label in edge_labels.items():
        x1, y1 = pos[u]
        x2, y2 = pos[v]
        x_mid = (x1 + x2) / 2
        y_mid = (y1 + y2) / 2
        
        angle = get_edge_angle(pos, u, v)
        offset = 0.1  # Adjust this value to control label distance from edge
        
        label_x = x_mid + offset * np.cos(angle + np.pi/2)
        label_y = y_mid + offset * np.sin(angle + np.pi/2)
        
        label_pos[(u, v)] = (label_x, label_y)
    
    # Adjust label positions to avoid overlap
    def get_dist(pos1, pos2):
        return np.sqrt((pos1[0] - pos2[0])**2 + (pos1[1] - pos2[1])**2)
    
    min_dist = 0.1  # Minimum distance between labels
    max_iterations = 50  # Maximum number of iterations for adjustment
    
    for _ in range(max_iterations):
        overlaps = False
        for (u1, v1), pos1 in label_pos.items():
            for (u2, v2), pos2 in label_pos.items():
                if (u1, v1) != (u2, v2):
                    dist = get_dist(pos1, pos2)
                    if dist < min_dist:
                        # Move labels apart
                        angle = np.arctan2(pos2[1] - pos1[1], pos2[0] - pos1[0])
                        label_pos[(u1, v1)] = (pos1[0] - 0.01 * np.cos(angle), pos1[1] - 0.01 * np.sin(angle))
                        label_pos[(u2, v2)] = (pos2[0] + 0.01 * np.cos(angle), pos2[1] + 0.01 * np.sin(angle))
                        overlaps = True
        if not overlaps:
            break
    
    # Add edge labels with adjusted positions
    for (u, v), label in edge_labels.items():
        x, y = label_pos[(u, v)]
        plt.annotate(label, (x, y), xytext=(0, 0), textcoords="offset points",
                     bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="gray", alpha=0.7),
                     ha='center', va='center', fontsize=8)
    
    legend_elements = [plt.Line2D([0], [0], color=color, lw=4, label=origin)
                       for origin, color in color_scheme.items()]
    plt.legend(handles=legend_elements, title="Origin Colors", loc="best")
    
    plt.title(f'Network Graph for {year}', fontsize=16)
    plt.axis('off')
    plt.tight_layout()
    plt.savefig(f'network_graph_{year}.png', dpi=300, bbox_inches='tight')
    plt.show()
    
# Plot network graph for 2023 with custom positions, edge transparency, labels under edges, bidirectional arrows with different colors, and visible arrows
plot_network_graph_bidirectional_colored_arrows(db_2023, '2023')

# Plot network graph for 2024 with custom positions, edge transparency, labels under edges, bidirectional arrows with different colors, and visible arrows
#plot_network_graph_bidirectional_visible_arrows(db_2024, '2024')
