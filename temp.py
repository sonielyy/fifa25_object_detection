# Başlangıç ve bitiş numaraları
start = 3133
end = 3182

# Dosya yolu formatı
base_path = "train/images/frame_"

# Satır satır dosya yollarını oluştur ve yazdır
for i in range(start, end + 1):
    filename = f"{base_path}{i:05d}.jpg"
    print(filename)

with open("file_paths.txt", "w") as f:
    for i in range(start, end + 1):
        filename = f"{base_path}{i:05d}.jpg"
        f.write(filename + "\n")
