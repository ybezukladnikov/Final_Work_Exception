from pathlib import Path

import os



path = Path("repository")


for filename in os.listdir(path):
  # f = os.path.join(path, filename)
  # if os.path.isfile(f):
  print(filename[:-4])

