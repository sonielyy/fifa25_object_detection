from ultralytics import YOLO
import cv2
import numpy as np
import time

# Modeli yükle
model_path = "runs/detect/train/weights/best.pt"
model = YOLO(model_path)

# Video dosyasını aç
video_path = "test_file/fifa_video.mkv"
cap = cv2.VideoCapture(video_path)

# FPS ayarı (15 FPS'e düşürmek için)
target_fps = 15
frame_interval = int(cap.get(cv2.CAP_PROP_FPS) // target_fps)

# Pencereyi aç
cv2.namedWindow("Video Tahmini", cv2.WINDOW_NORMAL)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Kare atlama işlemi (örnekleme)
    current_frame = int(cap.get(cv2.CAP_PROP_POS_FRAMES))
    if current_frame % frame_interval != 0:
        continue

    original_img = frame.copy()

    # Görseli yeniden boyutlandır
    scale_percent = 120
    width = int(original_img.shape[1] * scale_percent / 100)
    height = int(original_img.shape[0] * scale_percent / 100)
    dim = (width, height)
    resized_img = cv2.resize(original_img, dim, interpolation=cv2.INTER_AREA)

    # YOLO tahmini (görüntüyü geçici olarak dosyaya kaydetmeden doğrudan tahmin yapıyoruz)
    results = model.predict(source=original_img, save=False, conf=0.8)
    boxes = results[0].boxes

    # Ölçek faktörlerini hesapla
    x_scale = resized_img.shape[1] / original_img.shape[1]
    y_scale = resized_img.shape[0] / original_img.shape[0]

    for box in boxes:
        xyxy = box.xyxy[0].cpu().numpy()
        x1, y1, x2, y2 = xyxy

        x1 = int(x1 * x_scale)
        y1 = int(y1 * y_scale)
        x2 = int(x2 * x_scale)
        y2 = int(y2 * y_scale)

        conf = float(box.conf.cpu().numpy()[0])
        cls_idx = int(box.cls.cpu().numpy()[0])
        class_label = model.names[cls_idx]
        label_text = f"{class_label} {conf:.2f}"

        cv2.rectangle(resized_img, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.putText(resized_img, label_text, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

    # Sonucu göster
    cv2.imshow("Video Tahmini", resized_img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Temizlik
cap.release()
cv2.destroyAllWindows()
