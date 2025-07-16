# Divisor

Divisor is a Python-based tool that automates the creation of a Jekyll-powered website from an existing Git repository that keeps a backup of a wiki.js powered website.

The core idea is to provide a simple and flexible way to generate a static website from selected contents, without having to manually set up a Jekyll environment or manage the content conversion process manually. The resulting website will be deployed to GitHub Pages by default.

## Features

- **Configuration-driven:** A central `config.yml` file allows you to define all aspects of the generated website.
- **Content Mapping:** Map specific files and folders from your source repository to the generated website.
- **Automatic Conversion:** Divisor handles the conversion of Markdown files, including front matter adaptation and link rewriting.
- **GitHub Pages Deployment:** Easily deploy your generated website to GitHub Pages.

## Getting Started

1. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

2. **Generate the website:**

   ```bash
   python cli.py generate
   ```

3. **Run the Jekyll server:**

   To preview your site locally, you'll need to have Ruby and Bundler installed. Then, run the following commands from your generated site's directory:

   ```bash
   bundle install
   bundle exec jekyll serve
   ```

4. **Deploy the website:**

   To deploy the website to GitHub Pages, run:

   ```bash
   python cli.py deploy
   ```
