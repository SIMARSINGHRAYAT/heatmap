import os
import random
from datetime import datetime, timedelta

# Customize your pattern
start_date = datetime(2025, 1, 1)
days = 135
min_commits = 0
max_commits = 10  # Max commits per day

for i in range(days):
    date = start_date + timedelta(days=i)
    date_str = date.strftime("%Y-%m-%dT12:00:00")

    # Randomize number of commits for this day
    commits_today = random.randint(min_commits, max_commits)

    for j in range(commits_today):
        with open("file.txt", "a") as f:
            f.write(f"{date} - Commit {j}\n")
        os.system("git add file.txt")
        os.system(f'set GIT_AUTHOR_DATE={date_str} && set GIT_COMMITTER_DATE={date_str} && git commit -m "Commit {i}-{j}"')

print("✅ Done. Now push the repo.")
