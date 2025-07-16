import os
import re
import yaml

class Converter:
    def __init__(self, config):
        self.config = config

    def convert_file(self, source_path, dest_path):
        """
        Converts a single file.
        """
        with open(source_path, "r") as f:
            content = f.read()

        # Separate front matter from content
        match = re.search(r"^---\n(.*?)\n---\n(.*)", content, re.DOTALL)
        if match:
            front_matter_str = match.group(1)
            content_body = match.group(2)
            # Parse existing front matter
            try:
                front_matter = yaml.safe_load(front_matter_str)
            except yaml.YAMLError:
                front_matter = {}
        else:
            front_matter = {}
            content_body = content

        # Adapt front matter
        front_matter["layout"] = "default"
        if "title" not in front_matter:
            front_matter["title"] = self.get_title_from_content(content_body)

        # Rewrite internal links
        content_body = self.rewrite_internal_links(content_body)

        # Re-assemble the file
        new_content = self.add_front_matter(content_body, front_matter)

        with open(dest_path, "w") as f:
            f.write(new_content)

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
        # Rewrite page links
        content = content.replace(".md", "")
        # Rewrite media links
        content = re.sub(r"\(/(assets/media/.*?)\)", r"(/{{ site.baseurl }}/\1)", content)
        return content
