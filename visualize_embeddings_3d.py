import json
import pandas as pd
import plotly.express as px
import umap

with open("embeddings.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Limit to 1000 items for performance
# low end devices may struggle with larger datasets
data = data[:1000]

texts = [item["text"] for item in data]
vectors = [item["embedding"] for item in data]

#Reduce to 3D using UMAP
reducer = umap.UMAP(n_components=3, random_state=42)
reduced_vectors = reducer.fit_transform(vectors)

df = pd.DataFrame(reduced_vectors, columns=["x", "y", "z"])
df["text"] = texts

fig = px.scatter_3d(
    df,
    x="x",
    y="y",
    z="z",
    hover_name="text",  
    opacity=0.6
)
fig.update_traces(marker=dict(size=3, color='royalblue'))
fig.update_layout(title="3D Visualization of Chat Embeddings")

# ✅ Display in browser
fig.show()

# Save the figure as an HTML file
fig.write_html("3d_plot.html", auto_open=True)
