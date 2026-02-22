import os

def print_tree(path, prefix=""):
    items = sorted(os.listdir(path))
    for index, item in enumerate(items):
        full_path = os.path.join(path, item)
        is_last = index == len(items) - 1

        connector = "└─ " if is_last else "├─ "
        print(prefix + connector + item)

        if os.path.isdir(full_path):
            extension = "   " if is_last else "│  "
            print_tree(full_path, prefix + extension)


root_folder = r"C:\Users\zhandos\OneDrive\Документы\Unreal Projects\KazakhHan\Content"  # ← путь к папке Content

print(os.path.basename(root_folder) + "/")
print_tree(root_folder)