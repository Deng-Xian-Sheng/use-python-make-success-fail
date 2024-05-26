import os
import requests
from moviepy.editor import VideoFileClip, ImageSequenceClip
from PIL import Image

# 下载视频
# video_url = "https://v3-web.douyinvod.com/1123c9711fa543c5ef35735e216ac657/6652b6fb/video/tos/cn/tos-cn-ve-15-alinc2/9063e39cc6284e06b29193c9ff2dc862/?a=6383&ch=26&cr=3&dr=0&lr=all&cd=0%7C0%7C0%7C3&cv=1&br=1056&bt=1056&cs=0&ds=3&ft=xztusxhhe6BMyq5PJH4JD12Nzj&mime_type=video_mp4&qs=0&rc=OzpmZTk0ZzczNzVnaTpmPEBpamk2Z2g6ZmRmOjMzNGkzM0AxNjEuY2A2Xi8xYTYtNDYvYSNmazMycjRfNmJgLS1kLS9zcw%3D%3D&btag=c0000e00038000&cquery=100B_100D_102u_100a_100L&dy_q=1716692542&l=20240526110221727155952E6C182C51DF"
video_path = "downloaded_video.mp4"

# response = requests.get(video_url)
# with open(video_path, 'wb') as file:
    # file.write(response.content)

# 截取视频片段并转换为音频
start_time = 4 * 60 + 5  # 4:05 in seconds
end_time = 4 * 60 + 42   # 4:42 in seconds
output_audio_path = "extracted_audio.mp3"

video_clip = VideoFileClip(video_path).subclip(start_time, end_time)
video_clip.audio.write_audiofile(output_audio_path)

# 读取图片并制作视频
image_folder = "C:\\Users\\likewendy\\Desktop\\USMT-Helper\\wtfiswronghere\\err"
image_files = [os.path.join(image_folder, f"{i:02d}_challenge_error.png") for i in range(1, 14)]

# 确保所有图片的大小一致
images = [Image.open(img) for img in image_files]
width, height = images[0].size
for img in images:
    img.thumbnail((width, height))

# 使用PIL处理图片并保存临时文件
temp_image_files = []
for i, img in enumerate(images):
    temp_file = f"temp_{i}.png"
    img.save(temp_file)
    temp_image_files.append(temp_file)

# 创建图片序列视频，使得视频时长和音频一致
num_images = len(temp_image_files)
duration = video_clip.duration
fps = num_images / duration
image_clip = ImageSequenceClip(temp_image_files, fps=fps)
image_clip = image_clip.set_audio(video_clip.audio.set_duration(image_clip.duration))

output_video_path = "final_video.mp4"
image_clip.write_videofile(output_video_path, codec='libx264', fps=fps)

# 清理临时文件
for temp_file in temp_image_files:
    os.remove(temp_file)

print("视频处理完成")
