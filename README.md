# FC25 Object Detection with YOLOv8

![image](https://github.com/user-attachments/assets/ef0a46ea-1bf3-4495-8151-ff0f59c7b8a8)

## Summary

This project applies real-time object detection on gameplay footage from **FC25 (FIFA 2025)** using a fine-tuned YOLOv8 model. The goal is to detect key elements on the field during live matches.

Bu projede, **FC25 (FIFA 2025)** oyun görüntüsü üzerinden gerçek zamanlı nesne tespiti gerçekleştirilmektedir. Amaç, sahadaki temel nesneleri canlı maç esnasında tespit etmektir.

---

## Detected Objects

### 🇬🇧 English
Using a fine-tuned `yolov8n.pt` model, the following objects are detected:
- Players in red jerseys
- Players in blue jerseys
- Goalkeepers (both teams)
- Penalty areas (both sides)
- Top and bottom touch lines
- Football (ball)

### 🇹🇷 Türkçe
Fine-tune edilmiş YOLOv8 modeli ile aşağıdaki nesneler etiketlenmiştir:
- Kırmızı forma giyen oyuncular  
- Mavi forma giyen oyuncular  
- Her iki takımın kalecileri  
- Ceza sahaları  
- Üst ve alt dış çizgiler (taç çizgileri)  
- Futbol topu

---

## Technical Details

- Base model: [`yolov8n.pt`](https://github.com/ultralytics/ultralytics)
- Trained on: FC25 game footage
- Live inference support: Yes

Model was trained to make real-time predictions directly from video feed. It distinguishes players by team colors and identifies static areas like the penalty box effectively.

Model, canlı video akışı üzerinden tahmin yapacak şekilde eğitildi. Oyuncuların forma renkleri ile takım ayrımı yapabiliyor ve ceza sahası gibi sabit alanları başarıyla tanıyor.

---

## Performance / Başarılar

| Object               | Performance (🇬🇧)     | Performans (🇹🇷)       |
|----------------------|------------------------|-------------------------|
| Team Players         | Accurate             | Doğru tahminler       |
| Goalkeepers          | Accurate             | Doğru tahminler       |
| Penalty Areas        | Good                 | Başarılı              |
| Touch Lines (Top/Bottom) | ⚠️ Struggles       | ⚠️ Zorlanıyor           |
| Football (Ball)      | ⚠️ Struggles           | ⚠️ Zorlanıyor           |

---

## 📜 License / Lisans

This project is licensed under the **MIT License**.  
You are free to use, modify, and distribute the project **with attribution**.

Bu proje **MIT Lisansı** ile lisanslanmıştır.  
Kullanmakta özgürsünüz ancak **yazar bilgilerini belirtmeniz ve lisans metnini korumanız gerekir.**

---

## Demo

![image](https://github.com/user-attachments/assets/d214a583-5fe1-46a3-907d-1d0d1666731b)

![image](https://github.com/user-attachments/assets/07c9b2d3-de94-4921-9cf2-73d03e339c24)

![image](https://github.com/user-attachments/assets/d18ab1b1-0b3c-435d-8741-550997379cdb)
