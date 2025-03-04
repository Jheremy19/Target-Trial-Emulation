import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# Load saved images
bar_img = mpimg.imread("bar_chart.png")
sankey_img = mpimg.imread("sankey_diagram.png")
network_img = mpimg.imread("network_graph.png")

# Create figure for combined layout
fig, axes = plt.subplots(3, 1, figsize=(8.5, 14))

# Display each graph
axes[0].imshow(bar_img)
axes[0].axis('off')
axes[0].set_title("Stacked Bar Chart")

axes[1].imshow(sankey_img)
axes[1].axis('off')
axes[1].set_title("Sankey Diagram")

axes[2].imshow(network_img)
axes[2].axis('off')
axes[2].set_title("Network Graph")

plt.tight_layout()
plt.savefig("combined_graphs.png", dpi=300)
plt.show()
