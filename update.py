import git

# Clone the repository to a new directory named 'SaludOcup-Web-Version'
try:
    git.Repo.clone_from('https://github.com/Edu4r0/SaludOcup-Web-Version.git', 'SaludOcup-Web-Version')
except git.exc.GitCommandError:
    pass

# Open the existing repository in the 'SaludOcup-Web-Version' directory
repo = git.Repo('C:\Temp\SaludOcup-Web-Version')

# Pull the latest changes from the remote repository
repo.remotes.origin.pull()
