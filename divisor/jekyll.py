import os

class JekyllSite:
    def __init__(self, path: str):
        self.path = path

    def create_structure(self):
        """
        Creates the basic directory structure for a Jekyll website.
        """
        os.makedirs(os.path.join(self.path, "_layouts"), exist_ok=True)
        os.makedirs(os.path.join(self.path, "_includes"), exist_ok=True)
        os.makedirs(os.path.join(self.path, "_sass"), exist_ok=True)
