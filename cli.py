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
    site = JekyllSite(cfg.content_mapping.destination_folder)
    site.create_structure()

    # Convert the content
    converter = Converter(cfg)
    # This is a simplified version of the conversion process
    # In a real application, you would iterate over the files and folders
    # in the source repository and convert them accordingly.
    converter.convert_file(
        f"source_repo/{cfg.content_mapping.home_page_source}",
        f"{cfg.content_mapping.destination_folder}/index.md",
    )

    # Copy the assets
    asset_handler = AssetHandler(cfg)
    asset_handler.copy_assets(
        f"source_repo/{cfg.content_mapping.media_destination_folder}",
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
