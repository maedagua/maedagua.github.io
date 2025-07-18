# Divisor

Divisor is a Python-based tool that automates the creation of a Jekyll-powered website from an existing Git repository that keeps a backup of a wiki.js powered website.

The core idea is to provide a simple and flexible way to generate a static website from selected contents, without having to manually set up a Jekyll environment or manage the content conversion process manually. The resulting website will be deployed to GitHub Pages by default.

## How it works

The first basic step is to fetch the contents from the source repository. Then, the tool will generate a Jekyll website based on the configuration file `config.yml`. The generated website will be placed in the `destination_folder` defined in the configuration file.

The `config.yml` file allows you to customize the generated website. You can define the site's title, description, theme, and other options. You can also map specific files and folders from your source repository to the generated website.

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

   If you want to push to a remote other than `origin`, you can use the `--remote` option:

   ```bash
   python cli.py deploy --remote <your-remote-name>
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
