import json

with open("conversations.json", encoding="utf-8") as f:
    data = json.load(f)

messages = []

for convo in data:
    mapping = convo.get("mapping", {})
    for node_id, node in mapping.items():
        message = node.get("message")
        if not message:
            continue
        content = message.get("content", {})
        parts = content.get("parts", [])
        # Filter out empty or system-generated messages
        if parts and isinstance(parts, list):
            messages.extend(parts)

print(f"Total messages found: {len(messages)}")
print("Sample messages:", messages[:5])


with open("messages.json", "w", encoding="utf-8") as f:
    json.dump(messages, f, indent=2)
