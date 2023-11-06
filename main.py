import random
import os
import time
import shutil
from config import config


def get_file_from_list(path):
    time.sleep(0.02)
    files = os.listdir(path)
    index = random.randint(0, len(files) - 1)
    return files[index]


def overwrite_file(src_path, dest_path):
    try:
        shutil.copy(src_path, dest_path)
        print(f"파일을 성공적으로 복사하여 {dest_path}에 붙여넣었습니다.")
    except Exception as e:
        print(f"파일 복사 및 붙여넣기 중 오류가 발생했습니다: {str(e)}")


picked_up_file_path = config["list_path"] + get_file_from_list(config["list_path"])
goal_file_path = config["goal_path"] + config["file_name"] + config["extension"]
print(picked_up_file_path)
print(goal_file_path)
overwrite_file(picked_up_file_path, goal_file_path)
