import os
from datetime import datetime, timedelta

# Customize your pattern
start_date = datetime(2023, 1, 1)
days = 700
commits_per_day = 1

for i in range(days):
    date = start_date + timedelta(days=i)
    date_str = date.strftime("%Y-%m-%dT12:00:00")

    for j in range(commits_per_day):
        with open("file.txt", "a") as f:
            f.write(f"{date} - Commit {j}\n")
        os.system("git add file.txt")
        os.system(f'set GIT_AUTHOR_DATE={date_str} && set GIT_COMMITTER_DATE={date_str} && git commit -m "Commit {i}-{j}"')

print("Done. Now push the repo.")
