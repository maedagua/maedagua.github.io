import os
import shutil

class AssetHandler:
    def __init__(self, config):
        self.config = config

    def copy_assets(self, source_repo_dir, dest_media_dir):
        """
        Copies all media assets from the source repository to the destination media directory.
        """
        if not os.path.exists(dest_media_dir):
            os.makedirs(dest_media_dir)

        for root, _, files in os.walk(source_repo_dir):
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
