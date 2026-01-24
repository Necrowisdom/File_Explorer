#author: Engin Can Cicek

import os
import shutil
import time
import datetime
import string
import ctypes

def set_console_signature():
    # 1. Pencere Başlığını (Title Bar) Değiştirir
    # CMD penceresinin en üstündeki mavi/beyaz çubukta bu yazar
    os.system("title Dosya Bulma - Gelistirici: [Engin Can Cicek]")

    # 2. Ekrana Havalı Bir İmza Basar
    print("\n")
    print("X" * 60)
    print(f"X{'':^58}X")
    print(f"X   Dev.: {'[Engin Can Cicek]':<39} X")
    print(f"X{'':^58}X")
    print("X" * 60)
    print("\nSystem initializing...\n")

# Bu fonksiyonu kodun en başında çağırın
set_console_signature()

# ... BURADAN AŞAĞISI SENİN KODLARIN ...
# def get_available_drives(): ...
def get_available_drives():
    """Bilgisayardaki aktif sürücüleri (C:, D: vb.) bulur."""
    drives = []
    bitmask = ctypes.windll.kernel32.GetLogicalDrives()
    for letter in string.ascii_uppercase:
        if bitmask & 1:
            drives.append(f"{letter}:\\")
        bitmask >>= 1
    return drives

def find_newest_netlist():
    x = input("Enter the filename with extension: \n")
    target_file = x
    found_files = []
    
    drives = get_available_drives()
    print(f"📡 Target Drives: {', '.join(drives)}")
    print("🚀 Scanning entire system, this might take a while... Please wait.")

    for drive in drives:
        print(f"--> {drive} Searching...")
        for root, dirs, files in os.walk(drive):
            # Sistem klasörlerinde vakit kaybetmemek için bazılarını atlayalım
            # (İsterseniz bu if bloğunu kaldırabilirsiniz ama süre çok uzar)
            if "Windows" in root or "Program Files" in root or "Recycle" in root:
                continue

            try:
                if target_file in files:
                    full_path = os.path.join(root, target_file)
                    # Dosya zamanını al
                    mod_time = os.path.getmtime(full_path)
                    found_files.append((mod_time, full_path))
                    
                    # Kullanıcıya canlı bilgi ver
                    readable_time = datetime.datetime.fromtimestamp(mod_time).strftime('%Y-%m-%d %H:%M')
                    print(f"   🔎 File was found: {full_path} (Date: {readable_time})")
            except (PermissionError, OSError):
                # Erişim izni olmayan klasörleri sessizce geç
                continue

    if not found_files:
        print(f"\n❌ ERROR: {x} not found anywhere on the system.")
        return

    # Tarihe göre sırala (En yeniden en eskiye)
    found_files.sort(key=lambda x: x[0], reverse=True)
    
    best_file_time, best_file_path = found_files[0]
    readable_best_time = datetime.datetime.fromtimestamp(best_file_time).strftime('%Y-%m-%d %H:%M:%S')

    print("\n" + "="*50)
    print(f"🏆 Latest file selected:")
    print(f"📂 Path: {best_file_path}")
    print(f"⏰ Date: {readable_best_time}")
    print("="*50)

    while False:
        # Kopyalama işlemi
        try:
            shutil.copy(best_file_path, "design_template.net")
            print("\n✅ BAŞARILI! Dosya 'design_template.net' olarak buraya kopyalandı.")
            print("👉 Artık diğer Python scriptini çalıştırıp simülasyonları koşabilirsiniz.")
        except Exception as e:
            print(f"\n❌ Kopyalama Hatası: {e}")

if __name__ == "__main__":
    find_newest_netlist()
    input("\nPress Enter to exit...")
