import os
import re

class Converter:
    def __init__(self, config):
        self.config = config

    def convert_file(self, source_path, dest_path):
        """
        Converts a single file.
        """
        with open(source_path, "r") as f:
            content = f.read()

        # Adapt front matter (simple implementation)
        front_matter = {
            "layout": "default",
            "title": self.get_title_from_content(content),
        }
        content = self.add_front_matter(content, front_matter)

        # Rewrite internal links (simple implementation)
        content = self.rewrite_internal_links(content)

        with open(dest_path, "w") as f:
            f.write(content)

    def get_title_from_content(self, content):
        """
        Extracts the title from the first heading in the content.
        """
        match = re.search(r"^#\s+(.*)", content, re.MULTILINE)
        if match:
            return match.group(1)
        return "Untitled"

    def add_front_matter(self, content, front_matter):
        """
        Adds front matter to the beginning of the content.
        """
        fm_string = "---\n"
        for key, value in front_matter.items():
            fm_string += f"{key}: {value}\n"
        fm_string += "---\n\n"
        return fm_string + content

    def rewrite_internal_links(self, content):
        """
        Rewrites internal links to be compatible with Jekyll.
        """
        # This is a placeholder for a more sophisticated implementation
        return content.replace(".md", ".html")
