import os
import git

class SourceFetcher:
    def __init__(self, repo_url: str, clone_dir: str = "source_repo"):
        self.repo_url = repo_url
        self.clone_dir = clone_dir

    def fetch(self):
        """
        Clones the source repository to the specified directory.
        If the directory already exists, it will be updated.
        """
        if os.path.exists(self.clone_dir):
            repo = git.Repo(self.clone_dir)
            repo.remotes.origin.pull()
        else:
            git.Repo.clone_from(self.repo_url, self.clone_dir)
