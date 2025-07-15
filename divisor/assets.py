import os
import shutil

class AssetHandler:
    def __init__(self, config):
        self.config = config

    def copy_assets(self, source_dir, dest_dir):
        """
        Copies all assets from the source directory to the destination directory.
        """
        if not os.path.exists(source_dir):
            print(f"Warning: Source directory '{source_dir}' not found. Skipping asset copy.")
            return

        if not os.path.exists(dest_dir):
            os.makedirs(dest_dir)

        for item in os.listdir(source_dir):
            s = os.path.join(source_dir, item)
            d = os.path.join(dest_dir, item)
            if os.path.isdir(s):
                shutil.copytree(s, d, dirs_exist_ok=True)
            else:
                shutil.copy2(s, d)
