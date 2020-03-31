"""
image_compression/start.py
Accept path in system argument --path and compress images and overwrite them using the compression level specified in path
"""

import os
import sys
import Image

for root, dirs, files in os.walk(sys.argv[1].split("--path=")[1]):
    path = root.split(os.sep)
    print((len(path) - 1) * '***', os.path.basename(root))
    for file in files:
        if ".jpg" in file.lower() or ".jpeg" in file.lower() and os.path.getsize(os.path.join(root, file)) > 500*1024:
            print(len(path) * '---', file)
            try:
                img = Image.open(os.path.join(root, file))
                img.save(os.path.join(root, file), 'JPEG', quality=int(sys.argv[2].split("--quality=")[1]))
            except IOError:
                print("exception in " + str(root) + "/" + str(file))
                continue