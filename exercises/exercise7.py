import os

folder = "clutter"

files = os.listdir(folder)

counters = {}

for file in files:
    old_path = os.path.join(folder, file)

    if os.path.isfile(old_path):
        name, extension = os.path.splitext(file)

        if extension:
            extension = extension.lower()

            counters[extension] = counters.get(extension, 0) + 1

            new_name = str(counters[extension]) + extension
            new_path = os.path.join(folder, new_name)

            os.rename(old_path, new_path)

print("Files renamed successfully!")

