import os
import git

class Deployer:
    def __init__(self, site_path: str):
        self.site_path = site_path

    def deploy(self, remote_url="origin"):
        """
        Deploys the generated website to GitHub Pages.
        """
        repo = git.Repo.init(self.site_path)
        repo.git.add(A=True)
        repo.index.commit("Deploy to GitHub Pages")

        # Create a gh-pages branch if it doesn't exist
        if "gh-pages" not in repo.branches:
            repo.git.branch("gh-pages")

        # Push to the gh-pages branch
        repo.git.push("origin", "gh-pages", "--force")
