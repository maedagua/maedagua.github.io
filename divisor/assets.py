import os
import shutil

class AssetHandler:
    def __init__(self, config):
        self.config = config

    def copy_assets(self, source_repo_dir, dest_media_dir):
        """
        Copies media assets from the specified subpages_folder to the destination media directory.
        """
        subpages_folder = os.path.join(source_repo_dir, self.config.content_mapping.subpages_folder)
        if not os.path.exists(subpages_folder):
            print(f"Warning: Subpages folder '{subpages_folder}' not found. Skipping asset copy.")
            return

        if not os.path.exists(dest_media_dir):
            os.makedirs(dest_media_dir)

        for root, _, files in os.walk(subpages_folder):
            for file in files:
                if self.is_media_file(file):
                    source_path = os.path.join(root, file)
                    dest_path = os.path.join(dest_media_dir, file)
                    shutil.copy2(source_path, dest_path)

    def is_media_file(self, filename):
        """
        Checks if a file is a media file based on its extension.
        """
        media_extensions = [".jpg", ".jpeg", ".png", ".gif", ".pdf", ".mp3", ".mp4"]
        return any(filename.lower().endswith(ext) for ext in media_extensions)
