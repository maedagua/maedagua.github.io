import yaml
from dataclasses import dataclass

@dataclass
class SiteMetadata:
    title: str
    description: str
    theme: str
    github_pages_url: str
    about_page_title: str = "About this site"
    about_page_body: str = ""

@dataclass
class ContentMapping:
    home_page_source: str
    subpages_folder: str
    destination_folder: str
    media_destination_folder: str

@dataclass
class Config:
    site_metadata: SiteMetadata
    source_repository: str
    content_mapping: ContentMapping

def load_config(path: str = "config.yml") -> Config:
    """Loads the configuration from a YAML file."""
    with open(path, "r") as f:
        data = yaml.safe_load(f)
    return Config(
        site_metadata=SiteMetadata(**data["site_metadata"]),
        source_repository=data["source_repository"],
        content_mapping=ContentMapping(**data["content_mapping"]),
    )
