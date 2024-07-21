import json


def save_df_as_json(df , metadesc , path):
    metadata = {
        'description': metadesc,
    }
    data_dict = df.to_dict(orient='records')
    combined = {
        'metadata': metadata,
        'data': data_dict
    }

    with open(path, 'w') as f:
        json.dump(combined, f, indent=4)



import git

def get_current_branch(repo_path='.'):
    try:
        repo = git.Repo(repo_path)
        branch = repo.active_branch.name
        return branch
    except Exception as e:
        print(f"Error: {e}")
        return None

def get_current_commit_id(repo_path='.'):
    try:
        repo = git.Repo(repo_path)
        commit_id = repo.head.commit.hexsha
        return commit_id
    except Exception as e:
        print(f"Error: {e}")
        return None

# if __name__ == "__main__":
#     branch = get_current_branch()
#     commit_id = get_current_commit_id()

#     if branch:
#         print(f"Current branch: {branch}")
#     else:
#         print("Could not determine the current branch.")

#     if commit_id:
#         print(f"Current commit ID: {commit_id}")
#     else:
#         print("Could not determine the current commit ID.")
