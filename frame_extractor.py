import cv2
import os

# Video dosyasının adı
video_path = "fifa_video.mkv"

# Çıktı klasörü (karelerin kaydedileceği yer)
output_dir = "frames"
os.makedirs(output_dir, exist_ok=True)

# Video dosyasını aç
video = cv2.VideoCapture(video_path)

# Kare hızı: saniyede kaç kare alınacak
desired_fps = 15
fps = video.get(cv2.CAP_PROP_FPS)
frame_interval = int(fps / desired_fps)

count = 0
saved_count = 0

while True:
    success, frame = video.read()
    if not success:
        break
    if count % frame_interval == 0:
        filename = os.path.join(output_dir, f"frame_{saved_count:05d}.jpg")
        cv2.imwrite(filename, frame)
        saved_count += 1
    count += 1

video.release()
print(f"{saved_count} frame kaydedildi.")
