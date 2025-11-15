from config import load_config

config = load_config()

train_path = config["paths"]["train_folder"]
test_path = config["paths"]["test_folder"]
text_path = config["paths"]["text_file"]

print("Train folder:", train_path)
print("Test folder:", test_path)
print("Text file:", text_path)

# Example: read the text file
with open(text_path, "r") as f:
    content = f.read()

print("\nContent of text.txt:")
print(content)