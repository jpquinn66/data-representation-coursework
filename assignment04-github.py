import git

def replace_and_commit(file_path, old_text, new_text):
    # Repository path 
    repo_path = "C:/Users/jpqui/OneDrive/Desktop/Data rep coursework/data-representation-coursework"

    # Open the existing repository
    repo = git.Repo(repo_path)

    # Open the file and replace text
    with open(f"{repo_path}/{file_path}", "r") as file:
        content = file.read()
        content = content.replace(old_text, new_text)

    # Write the modified content back to the file
    with open(f"{repo_path}/{file_path}", "w") as file:
        file.write(content)

    # Stage the changes and commit
    repo.index.add([file_path])
    repo.index.commit(f"Replace '{old_text}' with '{new_text}'")

    # Push the changes to the remote repository
    origin = repo.remote(name='origin')
    origin.push()

if __name__ == "__main__":
    file_path = "Andrew.txt"  # file path
    old_text = "Andrew"
    new_text = "JP"  # Replace with my name

    replace_and_commit(file_path, old_text, new_text)
