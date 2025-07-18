import os
import unittest
import yaml
from divisor.config import load_config
from divisor.converter import Converter

class TestNestedSubpages(unittest.TestCase):
    def setUp(self):
        self.config_path = "test_config.yml"
        with open(self.config_path, "w") as f:
            f.write("""
site_metadata:
  title: "Test Site"
  description: "A test site."
  theme: "minima"
  github_pages_url: "https://example.com"
  github_repository_url: "https://github.com/user/repo.git"

source_repository: "https://example.com/repo.git"

content_mapping:
  home_page_source: "projetos/maedagua.md"
  subpages_folder: "projetos/maedagua"
  destination_folder: "site"
  media_destination_folder: "assets/media"

license: "MIT"
""")
        self.config = load_config(self.config_path)
        self.converter = Converter(self.config)

    def tearDown(self):
        os.remove(self.config_path)

    def test_rewrite_nested_subpage_links(self):
        content = "[link](/projetos/maedagua/diarios/julho.md)"
        rewritten_content = self.converter.rewrite_internal_links(content)
        self.assertEqual(rewritten_content, "[link]({{ '/diarios/julho' | relative_url }})")

if __name__ == '__main__':
    unittest.main()
