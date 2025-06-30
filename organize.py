import os
import re
import shutil

def organize_files():
    current_dir = os.getcwd()

    for file in os.listdir(current_dir):
        if file.endswith(".py") and "-" in file:
            match = re.match(r"^(\d+)-", file)
            if match:
                problem_number = int(match.group(1))

                if problem_number < 1000:
                    folder = "Easy"
                elif problem_number < 2000:
                    folder = "Medium"
                else:
                    folder = "Hard"

                
                if not os.path.exists(folder):
                    os.mkdir(folder)

                # انقل الملف للفولدر المناسب
                source = os.path.join(current_dir, file)
                destination = os.path.join(current_dir, folder, file)

                shutil.move(source, destination)
                print(f"✅ Moved {file} → {folder}/")

if __name__ == "__main__":
    organize_files()
