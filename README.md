# Araç ve İnsan Sayma Sistemi

Bu proje, YOLOv8 ve ByteTrack kullanılarak geliştirilmiş görüntü işleme tabanlı araç ve insan sayma sistemidir.

## Proje Özellikleri

- İnsan tespiti
- Araç tespiti
- Çoklu nesne takibi (Multi Object Tracking)
- ROI (Region Of Interest) tabanlı sayım sistemi
- CPU optimize edilmiş çalışma yapısı
- Gerçek zamanlı video işleme
- Tkinter tabanlı grafik arayüz
- Farklı algılama modları

## Kullanılan Teknolojiler

- Python
- OpenCV
- YOLOv8
- ByteTrack
- Tkinter
- Supervision

## Proje Yapısı

```bash
vehicle_human_counter/
│
├── app/
│   ├── gui.py
│   ├── detector.py
│   ├── tracker.py
│   ├── counter.py
│   └── video_processor.py
│
├── models/
├── videos/
├── screenshots/
├── reports/
│
├── main.py
├── requirements.txt
└── README.md
Kurulum

1-Gerekli kütüphaneleri yüklemek için:

pip install -r requirements.txt

2-Projeyi Çalıştırma
python main.py

3-Sistem Çalışma Mantığı
Kullanıcı video seçer
YOLOv8 nesneleri tespit eder
ByteTrack nesnelere ID atar
ROI alanına giren nesneler kontrol edilir
Aynı ID yalnızca bir kez sayılır
Sonuç ekranda gösterilir

4-Algılama Modları
İnsan
Araç
Tümü

Performans
-CPU dostu yapı
-Düşük çözünürlük optimizasyonu
-Gerçek zamanlı işleme
-Ortalama 10-15 FPS performansı

Gelecekte Yapılabilecek Geliştirmeler
-Mouse ile ROI seçme
-GPU desteği
-Web kamera desteği
-Veri analizi paneli
-Çoklu kamera desteği
-Raporlama sistemi

Geliştirici:
Muharrem Tarayan