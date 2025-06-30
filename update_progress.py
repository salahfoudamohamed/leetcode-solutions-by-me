import os
import re

README_FILE = "README.md"

def count_problems_by_folder():
    difficulties = ["Easy", "Medium", "Hard"]
    counts = {}

    for diff in difficulties:
        folder = os.path.join(".", diff)
        if os.path.exists(folder):
            count = len([f for f in os.listdir(folder) if f.endswith(".py")])
        else:
            count = 0
        counts[diff] = count
    return counts

def update_readme(counts):
    with open(README_FILE, "r", encoding="utf-8") as f:
        content = f.read()

   
    new_table = "\n".join([
        "## 📊 Progress Tracker",
        "",
        "| Difficulty | Solved |",
        "|------------|--------|",
        f"| Easy       | {counts['Easy']} ✅    |",
        f"| Medium     | {counts['Medium']} ⏳    |",
        f"| Hard       | {counts['Hard']} ⏳    |",
        ""
    ])

   
    updated_content = re.sub(r"## 📊 Progress Tracker.*?(?=##|$)", new_table, content, flags=re.DOTALL)

    with open(README_FILE, "w", encoding="utf-8") as f:
        f.write(updated_content)

    print("✅ README.md updated with current progress.")

if __name__ == "__main__":
    counts = count_problems_by_folder()
    update_readme(counts)
