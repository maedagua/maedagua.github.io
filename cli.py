import os
import click
from divisor.config import load_config
from divisor.source import SourceFetcher
from divisor.jekyll import JekyllSite
from divisor.converter import Converter
from divisor.assets import AssetHandler
from divisor.deploy import Deployer

@click.group()
def main():
    """
    Divisor is a tool for creating Jekyll websites from Git repositories.
    """
    pass

@main.command()
@click.option("--config", default="config.yml", help="Path to the configuration file.")
def generate(config):
    """
    Generates the website.
    """
    # Load the configuration
    cfg = load_config(config)

    # Fetch the source content
    fetcher = SourceFetcher(cfg.source_repository)
    fetcher.fetch()

    # Create the Jekyll site structure
    site = JekyllSite(cfg.content_mapping.destination_folder, cfg)
    site.create_structure()

    # Convert the content
    converter = Converter(cfg)
    # Convert the home page
    converter.convert_file(
        f"source_repo/{cfg.content_mapping.home_page_source}",
        f"{cfg.content_mapping.destination_folder}/index.md",
        "source_repo",
    )

    # Convert the subpages
    subpages_source_dir = f"source_repo/{cfg.content_mapping.subpages_folder}"
    subpages_dest_dir = f"{cfg.content_mapping.destination_folder}"
    if os.path.exists(subpages_source_dir):
        for root, _, files in os.walk(subpages_source_dir):
            for file in files:
                if file.endswith(".md"):
                    source_path = os.path.join(root, file)
                    relative_path = os.path.relpath(source_path, subpages_source_dir)
                    dest_dir = os.path.join(subpages_dest_dir, os.path.splitext(relative_path)[0])
                    os.makedirs(dest_dir, exist_ok=True)
                    dest_path = os.path.join(dest_dir, "index.md")
                    converter.convert_file(source_path, dest_path, "source_repo")

    # Copy the assets
    asset_handler = AssetHandler(cfg)
    asset_handler.copy_assets(
        "source_repo",
        f"{cfg.content_mapping.destination_folder}/{cfg.content_mapping.media_destination_folder}",
    )

    click.echo("Website generated successfully!")

@main.command()
@click.option("--config", default="config.yml", help="Path to the configuration file.")
def deploy(config):
    """
    Deploys the website to GitHub Pages.
    """
    cfg = load_config(config)
    deployer = Deployer(cfg.content_mapping.destination_folder)
    deployer.deploy()
    click.echo("Website deployed successfully!")

if __name__ == "__main__":
    main()
