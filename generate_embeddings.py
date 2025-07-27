from sentence_transformers import SentenceTransformer
import json
from tqdm import tqdm
import time

model = SentenceTransformer("all-MiniLM-L6-v2")

with open("messages.json", encoding="utf-8") as f:
    messages = json.load(f)

# remove empty messages and those that are too short
filtered_messages = [msg for msg in messages if isinstance(msg, str) and len(msg.strip()) > 10]

print(f"Generating embeddings for {len(filtered_messages)} messages...\n")

# Generate embeddings
embeddings = []
for msg in tqdm(filtered_messages):
    try:
        vector = model.encode(msg).tolist()
        embeddings.append({"text": msg, "embedding": vector})
    except Exception as e:
        print(f"⚠️ Error with message: {msg[:50]} -> {e}")
        continue
    time.sleep(0.005)  # Optional: throttle if needed

with open("embeddings.json", "w", encoding="utf-8") as f:
    json.dump(embeddings, f)

print(f"\nSaved {len(embeddings)} embeddings to embeddings.json")
