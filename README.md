# ChatGPT History Visualizer

This project visualizes your ChatGPT chat history in 3D using Plotly and embeddings from `embeddings.json`.

## Features

- 3D interactive scatter plot
- Visualizes semantic similarity
- Zoom and rotate functionality

## How to Use

1. First, download your chatgpt history by going to settings -> data history -> export data, then you will get a zip folder to your email, extract it, then copy the conversations.json file to your directory
2. Then run the clean.py. This script extracts only the actual human and assistant messages from the raw conversations.json file and writes them to a simpler messages.json file.
3. Next, run the generate_embeddings.json script, it will create the embeddings.json file.
4. Run `visualize_embeddings_3d.py`.

## NOTE

This project requires a conversations.json file (not included for privacy).
To use it, copy conversations_template.json to conversations.json and add your own data.

## Requirements

- Python
- Plotly
- NumPy
