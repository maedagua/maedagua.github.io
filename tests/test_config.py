import os
import unittest
from divisor.config import load_config, Config, SiteMetadata, ContentMapping

class TestConfig(unittest.TestCase):
    def setUp(self):
        self.config_path = "test_config.yml"
        with open(self.config_path, "w") as f:
            f.write("""
site_metadata:
  title: "Test Site"
  description: "A test site."
  theme: "minima"
  github_pages_url: "https://example.com"

source_repository: "https://example.com/repo.git"

content_mapping:
  home_page_source: "home.md"
  subpages_folder: "pages"
  destination_folder: "site"
  media_destination_folder: "assets/media"

license: "MIT"
""")

    def tearDown(self):
        os.remove(self.config_path)

    def test_load_config(self):
        config = load_config(self.config_path)
        self.assertIsInstance(config, Config)
        self.assertIsInstance(config.site_metadata, SiteMetadata)
        self.assertIsInstance(config.content_mapping, ContentMapping)
        self.assertEqual(config.site_metadata.title, "Test Site")
        self.assertEqual(config.source_repository, "https://example.com/repo.git")
        self.assertEqual(config.content_mapping.destination_folder, "site")

if __name__ == '__main__':
    unittest.main()
