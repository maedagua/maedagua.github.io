# Divisor

Divisor is a Python-based tool that automates the creation of a Jekyll-powered website from an existing Git repository that keeps a backup of a wiki.js powered website.

The core idea is to provide a simple and flexible way to generate a static website from selected contents, without having to manually set up a Jekyll environment or manage the content conversion process manually. The resulting website will be deployed to GitHub Pages by default.

## How it works

The first basic step is to fetch the contents from the source repository. Then, the tool will generate a Jekyll website based on the configuration file `config.yml`. The generated website will be placed in the `destination_folder` defined in the configuration file.

The `config.yml` file allows you to customize the generated website. You can define the site's title, description, theme, and other options. You can also map specific files and folders from your source repository to the generated website.

## Configuration

The main configuration file is `config.yml`. Here's a breakdown of the available options:

```yaml
site_metadata:
  title: "My Awesome Website"
  description: "Website created with fonte.wiki and Divisor"
  theme: "minima"
  github_repository_url: "git@github.com:your-git-username/your-repository.git" #edit this line
  github_pages_url: "https://your-git-username.github.io/your-repository/" #edit this line
  about_page_title: "About this site"
  about_page_body: "This is a sample description paragraph."

source_repository: "https://github.com/fonte-wiki/Backup-fonte-wiki" #leave this to use fonte.wiki as the source repository

content_mapping:
  home_page_source: "home.md" #edit this line to choose the home page of your website
  subpages_folder: "<none>" #optionally add a folder from the source repository whose contents will be imported as subpages
  destination_folder: "site_contents"
  media_destination_folder: "assets/media"
```

### `site_metadata`

*   `title`: The title of your website.
*   `description`: A short description of your website.
*   `theme`: The Jekyll theme to use. Defaults to "minima".
*   `github_repository_url`: The address of your repository.
*   `github_pages_url`: The URL of your GitHub Pages website.
*   `about_page_title`: The title of the "About" page.
*   `about_page_body`: The content of the "About" page.

### `source_repository`

The URL of the Git repository to use as the source for your website's content.

### `content_mapping`

*   `home_page_source`: The path to the Markdown file to use as the home page.
*   `subpages_folder`: The path to the folder containing the subpages. To disable subpages, set this field to `<none>`.
*   `destination_folder`: The folder where the generated Jekyll site will be created.
*   `media_destination_folder`: The folder where the media files will be copied.

## Getting Started

1. **Clone the repository:**

   ```bash
   git clone https://github.com/fonte-wiki/divisor.git
   cd divisor
   ```

2. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

2. **Configure the website:**

   Edit the `config.yml` file to customize your website.

3. **Generate the website:**

   ```bash
   python cli.py generate
   ```

4. **Preview the website:**

   To preview your site locally, you'll need to have Ruby and Bundler installed. Then, `cd` into your generated site's directory and run:

   ```bash
   bundle install
   bundle exec jekyll serve
   ```

5. **Deploy the website:**

   To deploy the website to GitHub Pages, run:

   ```bash
   python cli.py deploy
   ```

   The destination repository is configured in the `config.yml` file via the `github_repository_url` field.

## Refresh the website contents

To update the website with updated contents from the source repository, run again the `generate` and `deploy` commands:

   ```bash
   python cli.py generate
   ```

   ```bash
   python cli.py deploy
   ```

## GitHub Pages Setup

To deploy your website to GitHub Pages, you need to configure your repository correctly.

1.  **Create a `gh-pages` branch:**

    ```bash
    git checkout --orphan gh-pages
    git rm -rf .
    git commit --allow-empty -m "Initial commit"
    git push origin gh-pages
    ```

2.  **Configure GitHub Pages:**

    In your repository's settings, go to the "Pages" section and select the `gh-pages` branch as the source for your GitHub Pages site.
