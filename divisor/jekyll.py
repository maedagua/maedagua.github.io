import os

class JekyllSite:
    def __init__(self, path: str, config):
        self.path = path
        self.config = config

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

        # Create _config.yml
        config_path = os.path.join(self.path, "_config.yml")
        with open(config_path, "w") as f:
            f.write(f"title: {self.config.site_metadata.title}\n")
            f.write(f"description: {self.config.site_metadata.description}\n")
            f.write(f"theme: {self.config.site_metadata.theme}\n")
            f.write(f"url: {self.config.site_metadata.github_pages_url}\n")

        # Copy layout and includes
        self.copy_template_files()

        # Create about page
        self.create_about_page()

    def create_about_page(self):
        """
        Creates the about page from the config.
        """
        about_path = os.path.join(self.path, "about.md")
        with open(about_path, "w") as f:
            f.write("---\n")
            f.write("layout: page\n")
            f.write(f"title: {self.config.site_metadata.about_page_title}\n")
            f.write("---\n")
            f.write(f"\n{self.config.site_metadata.about_page_body}\n")

    def copy_template_files(self):
        """
        Copies the template files (_layouts, _includes, assets) to the generated site.
        """
        template_dir = os.path.dirname(__file__)
        for dir_name in ["_includes"]:
            source_dir = os.path.join(template_dir, dir_name)
            dest_dir = os.path.join(self.path, dir_name)
            if os.path.exists(source_dir):
                import shutil
                if os.path.exists(dest_dir):
                    shutil.rmtree(dest_dir)
                shutil.copytree(source_dir, dest_dir, dirs_exist_ok=True)
