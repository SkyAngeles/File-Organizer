import os
import shutil

#manual input var
action = ["direct_organize", "extract", "full_organize"]
action = action[0]
directory = 'C:\\Users\ica\Downloads'

BASE_PATH = os.path.expanduser('~')
DIRECTORY_PATH = directory
#DIRECTORY_PATH = os.path.join(BASE_PATH, 'Downloads')
print(f"base path: {BASE_PATH}")
print(f"downloads path: {DIRECTORY_PATH}")

def organize():
    for (path,dirs,files) in os.walk(DIRECTORY_PATH):
        for file in files:
            try:
                if os.path.isfile(os.path.join(DIRECTORY_PATH, file)):
                    EXTENSION = os.path.splitext(file)[1]
                    NEW_FOLDER_PATH = os.path.join(DIRECTORY_PATH, EXTENSION)
                    OLD_FILE_PATH = os.path.join(DIRECTORY_PATH, file)
                    NEW_FILE_PATH = os.path.join(NEW_FOLDER_PATH, file)
                    if os.path.exists(NEW_FOLDER_PATH):
                        shutil.move(src=OLD_FILE_PATH, dst=NEW_FILE_PATH)
                        print(f"Moved ({EXTENSION}) {file} to {NEW_FILE_PATH}")
                    else:
                        print("Making new folder...")
                        os.mkdir(NEW_FOLDER_PATH)
                        shutil.move(src=OLD_FILE_PATH, dst=NEW_FILE_PATH)
                        print(f"Moved ({EXTENSION}) {file} to {NEW_FILE_PATH}")
            except Exception as e:
                        print(e)
                        pass
    print("folder organized")

def extract():
    for root, dirs, files in os.walk(DIRECTORY_PATH):
        for file in files:
            try:
                if os.path.isfile(os.path.join(root, file)):
                    shutil.move(os.path.join(root, file), DIRECTORY_PATH)
                    print(f"Extracted {file} to {DIRECTORY_PATH}")
            except Exception as e:
                print(e)
                pass
    print("folder extracted")

if action == "direct_organize":
    organize()
elif action == "full_organize":
    extract()
    organize()
elif action == "extract":
    extract()
else:
    print("action not found")