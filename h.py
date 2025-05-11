import os
from datetime import datetime, timedelta

# Customize your pattern
start_date = datetime(2025, 3, 3)
days = 100  # Total number of days to backfill
commits_per_day = 5  # Increase this to make squares darker

for i in range(days):
    date = start_date + timedelta(days=i)
    for j in range(commits_per_day):
        with open("file.txt", "a") as f:
            f.write(f"{date} - Commit {j}\n")
        os.system(f'git add file.txt')
        os.system(f'GIT_AUTHOR_DATE="{date.isoformat()} 12:00:00" GIT_COMMITTER_DATE="{date.isoformat()} 12:00:00" git commit -m "Commit {i}-{j}"')

print("Done. Now push the repo.")
