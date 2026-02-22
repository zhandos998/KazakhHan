import os

root_folder = r"C:\path\to\your\folder"  # ← укажи путь к папке

for root, dirs, files in os.walk(root_folder):
    print(f"\nПапка: {root}")
    for file in files:
        print(f"  └─ {file}")