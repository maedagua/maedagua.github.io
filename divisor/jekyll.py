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

        # Create Gemfile from template
        gemfile_template_path = os.path.join(os.path.dirname(__file__), "Gemfile.template")
        gemfile_path = os.path.join(self.path, "Gemfile")
        with open(gemfile_template_path, "r") as f_template, open(gemfile_path, "w") as f_out:
            f_out.write(f_template.read())
