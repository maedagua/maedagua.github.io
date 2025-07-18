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

  github_repository_url: "https://github.com/your-git-username/your-repository.git" # Recommended: use HTTPS URL

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

There are two ways to use Divisor to generate and deploy your website:

### Option A: Manual Setup

This option is ideal if you want to generate a one-time static website from the current state of your source repository.

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/fonte-wiki/divisor.git
    cd divisor
    ```
2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
3.  **Configure the website:**
    Edit the `config.yml` file to customize your website.
4.  **Generate the website:**
    ```bash
    python cli.py generate
    ```
    **Note:** This command will always fetch the latest content from the source repository before generating the website.
5.  **Preview the website:**
    To preview your site locally, you'll need to have Ruby and Bundler installed. Then, `cd` into your generated site's directory and run:
    ```bash
    bundle install
    bundle exec jekyll serve
    ```
6.  **Deploy the website:**
    To deploy the website to GitHub Pages, run:
    ```bash
    python cli.py deploy
    ```
    The destination repository is configured in the `config.yml` file via the `github_repository_url` field.
7.  **GitHub Pages Setup:**
    To deploy your website to GitHub Pages, you need to configure your repository correctly.
    *   **Create a `gh-pages` branch:**
        ```bash
        git checkout --orphan gh-pages
        git rm -rf .
        git commit --allow-empty -m "Initial commit"
        git push origin gh-pages
        ```
    *   **Configure GitHub Pages:**
        In your repository's settings, go to the "Pages" section and select the `gh-pages` branch as the source for your GitHub Pages site.

### Option B: Automated Setup with GitHub Actions

This option provides a fully automated way to keep your website in sync with your source repository.

1.  **Fork the repository:**
    Fork this repository to your own GitHub account or organization.
2.  **Enable the workflow:**
    This repository includes a sample workflow file that you can use to automate the website generation and deployment. To enable the workflow, you need to rename the file `.github/workflows/main.yml.sample` to `.github/workflows/main.yml`.
3.  **Enable workflows in your forked repository:**
    By default, GitHub Actions workflows are disabled on forked repositories. To enable them, go to the "Actions" tab in your forked repository and click the "I understand my workflows, go ahead and enable them" button.
4.  **Configure `config.yml`:**
    Edit the `config.yml` file to customize your website. Ensure that the `github_repository_url` points to your forked repository.
5.  **Commit and push:**
    Commit the changes to your `config.yml` and the renamed workflow file. The workflow will then automatically generate and deploy your website.

**Note:** The workflow uses the `GITHUB_TOKEN` to authenticate and push to your repository. You don't need to set up any secrets for this to work.

## Automated Workflow Details

This repository includes a GitHub Actions workflow that automates the process of generating and deploying the website. The workflow is defined in the `.github/workflows/main.yml.sample` file and consists of the following steps:

1.  **Scheduled Trigger:** The workflow is configured to run automatically every hour. It can also be triggered manually from the Actions tab in your GitHub repository.
2.  **Checkout and Setup:** The workflow checks out the repository, sets up the Python environment, and installs the required dependencies.
3.  **Generate Website:** It runs the `python cli.py generate` command to fetch the latest content from the source repository and generate the website.
4.  **Deploy to GitHub Pages:** Finally, it runs the `python cli.py deploy` command to deploy the generated website to the `gh-pages` branch.
