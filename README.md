# 🕵️‍♂️ İş İlanı Takip ve Analiz Botu (Job Hunter Bot)

Bu proje, Python kullanarak Google arama sonuçları üzerinden **güncel (son 30 gün)** iş ilanlarını tarayan, verileri toplayan ve basit bir pazar analizi sunan bir otomasyon aracıdır.

Özellikle veri analizi ve yazılım alanındaki iş arama sürecini optimize etmek, manuel arama yükünü kaldırmak ve piyasa trendlerini görmek için geliştirilmiştir.

## 🚀 Özellikler

* **🔍 İnteraktif Arama:** Kullanıcıdan pozisyon, şehir ve zorunlu yetenek bilgisini (örn: Python, SQL) alarak kişiselleştirilmiş arama yapar.
* **🕒 Güncellik Filtresi:** Eski tarihli veya süresi dolmuş ilanları eler; sadece Google'ın **son 30 gün** içinde indekslediği aktif ilanları getirir.
* **📊 Pazar Analizi:** Bulunan ilanların hangi platformlardan (LinkedIn vs Kariyer.net) geldiğini analiz eder ve terminalde istatistiksel rapor sunar.
* **💾 Otomatik Raporlama:** Sonuçları düzenli bir formatta `Guncel_Linkler.csv` dosyasına kaydeder.
* **🛡️ Güvenlik:** Hassas API anahtarlarını kod içinde barındırmaz, `.env` dosyası kullanarak güvenliği sağlar.

## 🛠️ Kullanılan Teknolojiler

* **Python 3.11**
* **SerpApi** (Google Arama Motoru Sonuçları için)
* **Pandas** (Veri İşleme ve CSV Kaydı için)
* **Python-Dotenv** (Çevre Değişkeni ve Güvenlik Yönetimi için)

## 💻 Kurulum ve Çalıştırma

Projeyi kendi bilgisayarınızda çalıştırmak için aşağıdaki adımları izleyin:

### 1. Gerekli Kütüphaneleri Yükleyin
Proje klasöründe terminali açın ve şu komutu yazın:

    pip install -r requirements.txt

2. API Anahtarını Ayarlayın
Projenin çalışması için SerpApi anahtarına ihtiyacınız vardır.

Proje ana dizininde .env adında yeni bir dosya oluşturun.

İçine şu satırı ekleyin (Kendi API anahtarınızı eşittirden sonra yapıştırın):

    SERPAPI_KEY=buraya_api_anahtarinizi_yapisitirin

3. Botu Başlatın
Terminalde şu komutu çalıştırın:
    python scripts/ilan_bulucu.py

Kullanım Örneği
Program çalıştığında terminalde size 3 soru soracaktır:
    
İŞ İLANI ANALİZ ROBOTU (V2)
========================================
Hangi pozisyonu arıyorsun? (Varsayılan: Veri Analisti)
Pozisyon: İş Analisti

İş Analisti için hangi şehir? (Varsayılan: İstanbul)
Şehir: Ankara

Mutlaka olması gereken yetenek? (Varsayılan: Python)
Yetenek: SQL

Sonuçlar analiz edildikten sonra Guncel_Linkler.csv dosyasında hazır olacaktır.

Bu proje, Veri Analizi yetkinliklerini ve Python otomasyon becerilerini sergilemek amacıyla açık kaynak olarak geliştirilmiştir.