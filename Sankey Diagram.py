import pandas as pd
import plotly.graph_objects as go

# Load dataset
file_path = "sankey_assignment.csv"
df = pd.read_csv(file_path)

# Define node labels
source_labels = ['PS', 'OMP', 'CNP', 'NRP', 'NMCCC', 'PEC', 'NCDM', 'RGS']
target_labels = ['Reg', 'Aca', 'Oth']
all_labels = source_labels + target_labels

# Map labels to indices
label_to_index = {label: i for i, label in enumerate(all_labels)}

# Create source and target lists
sources = df['Source'].map(label_to_index).tolist()
targets = df['Target'].map(label_to_index).tolist()
values = df['Value'].tolist()

# Create Sankey diagram
fig = go.Figure(go.Sankey(
    node=dict(
        pad=15,
        thickness=20,
        line=dict(color='black', width=0.5),
        label=all_labels
    ),
    link=dict(
        source=sources,
        target=targets,
        value=values
    )
))

fig.update_layout(title_text="Sankey Diagram", font_size=10)
fig.write_html("sankey_diagram.html")
fig.show()
