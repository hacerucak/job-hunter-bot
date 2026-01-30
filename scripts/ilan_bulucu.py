import pandas as pd
import os
from dotenv import load_dotenv
from serpapi import GoogleSearch


load_dotenv()
API_KEY = os.getenv("SERPAPI_KEY")

def kullaniciya_sor():
    """Kullanıcıdan arama kriterlerini alır"""
    print("\n" + "="*40)
    print(" İŞ İLANI ANALİZ ROBOTU (V2)")
    print("="*40)
    
    
    print("Hangi pozisyonu arıyorsun? (Varsayılan: Veri Analisti)")
    girilen_pozisyon = input(" Pozisyon: ").strip()
    pozisyon = girilen_pozisyon if girilen_pozisyon else "Veri Analisti"
    
    
    print(f"\n{pozisyon} için hangi şehir? (Varsayılan: İstanbul)")
    girilen_sehir = input(" Şehir: ").strip()
    sehir = girilen_sehir if girilen_sehir else "İstanbul"
    
    
    print("\nMutlaka olması gereken yetenek? (Varsayılan: Python)")
    girilen_yetenek = input(" Yetenek: ").strip()
    yetenek = girilen_yetenek if girilen_yetenek else "Python"
    
    return pozisyon, sehir, yetenek

def analiz_yap(liste):
    """Bulunan ilanlar üzerinde basit istatistikler çıkarır"""
    if not liste:
        return

    df = pd.DataFrame(liste)
    
    toplam = len(df)
    linkedin_sayisi = len(df[df['Site'] == 'LinkedIn'])
    kariyer_sayisi = len(df[df['Site'] == 'Kariyer.net'])
    
    print("\n" + "="*40)
    print("📊 HIZLI PAZAR ANALİZİ")
    print("="*40)
    print(f"• Toplam Aktif İlan: {toplam}")
    print(f"• Kariyer.net Payı:  {kariyer_sayisi} ilan (%{int(kariyer_sayisi/toplam*100)})")
    print(f"• LinkedIn Payı:     {linkedin_sayisi} ilan (%{int(linkedin_sayisi/toplam*100)})")
    print("="*40 + "\n")

def linkleri_getir():
    
    pozisyon, sehir, zorunlu_yetenek = kullaniciya_sor()
    
    
    deneyim_seviyesi = "yeni_mezun" 
    deneyim_sozlugu = {
        "yeni_mezun": '"Junior" OR "Jr" OR "Yeni Mezun" OR "Tecrübesiz" OR "0-2 yıl"'
    }
    deneyim_kodu = deneyim_sozlugu.get(deneyim_seviyesi, "")
    
    
    sorgu = f'(site:kariyer.net OR site:linkedin.com/jobs) "{pozisyon}" {sehir} "{zorunlu_yetenek}"'
    if deneyim_kodu:
        sorgu += f' ({deneyim_kodu})'
    
    print(f"\n🔍 Google'da Aranıyor: {sorgu}...")
    
    params = {
      "engine": "google",
      "q": sorgu,
      "google_domain": "google.com.tr",
      "gl": "tr",
      "hl": "tr",
      "num": 40,
      "tbs": "qdr:m", 
      "api_key": API_KEY
    }

    try:
        search = GoogleSearch(params)
        results = search.get_dict()
    except Exception as e:
        print(f" Hata: {e}")
        return []

    liste = []
    if "organic_results" in results:
        for sonuc in results["organic_results"]:
            link = sonuc.get("link", "")
            baslik = sonuc.get("title", "")
            
            if "is-ilani" in link or "/jobs/" in link:
                site_adi = "Kariyer.net" if "kariyer.net" in link else "LinkedIn"
                liste.append({
                    "Site": site_adi,
                    "Başlık": baslik,
                    "Link": link
                })
    return liste


if __name__ == "__main__":
    veriler = linkleri_getir()
    
    if veriler:
        
        analiz_yap(veriler)
        
        
        df = pd.DataFrame(veriler)
        df.to_csv("Guncel_Linkler.csv", index=False)
        print(f" Tüm linkler 'Guncel_Linkler.csv' dosyasına kaydedildi.")
    else:
        print(" İlan bulunamadı.")