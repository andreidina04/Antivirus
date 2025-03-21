import hashlib
import os
folder_path = "C://"
if not os.path.exists(folder_path) :
    os.makedirs(folder_path)
    print(f"Directorul {folder_path} a fost creat.")
else:
    print(f"Directorul {folder_path} exista deja.")
files = os.listdir(folder_path)
if not files :
    print(f"Folderul {folder_path} este gol. Nu se poate scana.")
else:
    print(f"Folderul {folder_path} are fisiere. Se incepe scanarea.")
for filename in files:
    file_path = os.path.join(folder_path, filename)
if os.path.isfile(file_path):
     with open(file_path, "rb") as f:
        content = f.read()
        result = hashlib.md5(content).hexdigest()
print(f"Fisierul {filename}")
print(f"{result}")
print(f"{content}")
print("-")

