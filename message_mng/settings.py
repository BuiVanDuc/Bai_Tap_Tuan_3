import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PATH_CONFIG= os.getenv("PATH_CONFIG", os.path.join(BASE_DIR, "configs"))
