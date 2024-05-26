import os
import random
import subprocess
from git import Repo
from PIL import ImageGrab
import time

# 克隆仓库
repo_url = 'https://github.com/qxf2/wtfiswronghere'
repo_dir = 'wtfiswronghere'

if not os.path.exists(repo_dir):
    # print(f'Cloning repository {repo_url}...')
    Repo.clone_from(repo_url, repo_dir)
else:
    pass
    # print(f'Repository {repo_dir} already exists.')

# 定义挑战目录列表
challenge_dirs = [f'{repo_dir}/{i:02d}_challenge' for i in range(1, 14)]

my_list = ["main","tools","test_code","data","load_admin","file"]

# 逐个进入挑战目录并运行脚本
for challenge_dir in challenge_dirs:
    challenge_script = os.path.join(challenge_dir, f'{os.path.basename(challenge_dir)}.py')
    if os.path.exists(challenge_script):
        # print(f'Running script {challenge_script}...')
        try:
            result = subprocess.run(['python', f'{os.path.basename(challenge_dir)}.py'], capture_output=True, text=True, cwd=challenge_dir)
            result.stdout = result.stdout.replace(os.path.join(r"C:\Users\likewendy\Desktop\USMT-Helper", "wtfiswronghere",os.path.basename(challenge_dir),f'{os.path.basename(challenge_dir)}.py'), os.path.join(r"C:\Users\likewendy\Desktop\USMT-Helper" , random.choice(my_list) + ".py"))
            result.stderr = result.stderr.replace(os.path.join(r"C:\Users\likewendy\Desktop\USMT-Helper", "wtfiswronghere",os.path.basename(challenge_dir),f'{os.path.basename(challenge_dir)}.py'), os.path.join(r"C:\Users\likewendy\Desktop\USMT-Helper" , random.choice(my_list) + ".py"))
            print(result.stdout)
            print(result.stderr)
            # 提取报错信息中的文件名和行号 (假设报错信息的格式类似于 'File "path", line number')
            error_lines = result.stderr.splitlines()
            for line in error_lines:
                if "File" in line and "line" in line:
                    parts = line.split(',')
                    file_part = parts[0].strip().split('"')[1]
                    line_part = parts[1].strip().split(' ')[1]
                    # print(f"Error in file: {file_part}, line: {line_part}")
                    
                    # print( os.path.join(r"C:\Users\likewendy\Desktop\USMT-Helper", "wtfiswronghere",os.path.basename(challenge_dir),f'{os.path.basename(challenge_dir)}.py'))
                    # 使用 VSCode 打开文件并跳转到指定行
                    subprocess.run([r'C:\Users\likewendy\AppData\Local\Programs\Microsoft VS Code\bin\code.cmd', '-g', f'{os.path.basename(challenge_dir)}.py'],cwd=challenge_dir)
                    break
        except Exception as e:
            print(f'Error running script: {e}')
        
        # 等待错误信息完全打印
        # time.sleep(2)
        
        # 截图保存
        image_path = os.path.join(challenge_dir,"../err", f'{os.path.basename(challenge_dir)}_error.png')
        screenshot = ImageGrab.grab()
        screenshot.save(image_path)
        # print(f'Screenshot saved to {image_path}')
    else:
        print(f'Script {challenge_script} not found.')
