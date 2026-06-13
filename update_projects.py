import requests
import json
import os

USERNAME = os.getenv("GITHUB_USERNAME", "rose0417m")

url = f"https://api.github.com/users/{USERNAME}/repos?sort=updated"

repos = requests.get(url).json()

projects = []

for repo in repos:

    if repo["fork"]:
        continue

    projects.append({
        "name": repo["name"],
        "description": repo["description"],
        "url": repo["html_url"],
        "stars": repo["stargazers_count"],
        "language": repo["language"]
    })

with open("projects.json", "w", encoding="utf-8") as f:
    json.dump(projects, f, indent=2)

print("Projects updated!")