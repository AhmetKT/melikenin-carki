import streamlit as st
import time
import random

# Sayfa ayarları
st.set_page_config(page_title="Melike'nin Şans Çarkı", page_icon="🎡")

# ÖDÜL HAFIZASI (Session State)
if 'oduller' not in st.session_state:
    st.session_state.oduller = [
        "TEBRİKLER! Büyük ödülü kazandın: İlk buluşmada Ahmet'i 20 kere yanağından öpmek! 😽",
        "İNANILMAZ ŞANS! Büyük ödül: İlk buluşmada Ahmet'in seni 18 kere yanağından öpmesi! 😘",
        "TEBRİKLER! Her tartışmada geçerli 'Sorgusuz Sualsiz Melike Haklıdır' kartı kazandın!\n\n*(Stok: 0 adet. Maalesef stoklarda kalmadı. Şansına küs!)* 📉",
        "SİSTEM HACKLENDİ! 'Evet Hayatım' Modu aktif:\n\nAhmet'in sonraki 2 saat boyunca her dediğine 'Haklısın aşkım, harikasın aşkım' deme zorunluluğu! 🤖",
        "SÜRPRİZ! Buluşunca Ahmet'le 1 dakika boyunca gülmeden göz göze bakışma yarışması.\n\nKaybeden, kazananın kahvesini ısmarlar. 👀☕"
    ]

st.title("🎡 Melike'nin Şanslı Ödül Çarkı")

# Eğer bütün ödüller bittiyse oyun biter
if len(st.session_state.oduller) == 0:
    st.error("Bütün ödülleri sömürdün! Çarkta başka ödül kalmadı. Artık bu kazandıklarını uygulama vakti! 🏃‍♂️💨")
    st.balloons()
else:
    st.write("Aşağıdaki muhteşem ödüllerden birini kazanmak için şansını dene! Ama dikkat et, sürpriz ödülün gelme ihtimali çok düşük! Toplam 5 kere bas ve ödülleri sırayla topla! Ödülleri unutmamak için her çevirmeden sonra ekran görüntüsü almayı unutma!🎯")
    
    # İhtimallerin listelendiği bölüm
    st.markdown("""
    ---
    **📊 Çarktaki İhtimaller (Gerçek Zamanlı Algoritma Verisi):**
    *   Ahmet'e yemek yap 🍲 **(%24.9996)**
    *   Ahmet'e kahve ısmarla ☕ **(%24.9996)**
    *   Ahmet'e sevgi dolu ses kaydı at 🎙️ **(%24.9996)**
    *   Ahmet'e tatlı yap 🍰 **(%24.9996)**
    *   **SÜRPRİZ 🎁 (%0.00153)**
    ---
    """)
    
    # Animasyonlar için ayrılmış alan (Sadece yazı için)
    durum_yazisi = st.empty()

    if st.button("Şansını Dene! 🎯", use_container_width=True):
        
        # 1. Durum Yazılarıyla heyecan katma
        cark_ogeleri = [
            "Ahmet'e yemek yap... 🍲", 
            "Ahmet'e kahve ısmarla... ☕", 
            "Ahmet'e sevgi dolu ses kaydı at... 🎙️", 
            "Ahmet'e tatlı yap... 🍰"
        ]
        
        for i in range(20):
            secilen = random.choice(cark_ogeleri)
            durum_yazisi.markdown(f"<h3 style='text-align: center; color: gray;'>İbre geçiyor: {secilen}</h3>", unsafe_allow_html=True)
            time.sleep(0.12) # Dönüş hızı
            
        # Sonlara doğru yavaşlama hissi
        for i in range(4):
            secilen = random.choice(cark_ogeleri)
            durum_yazisi.markdown(f"<h3 style='text-align: center; color: #ff4b4b;'>Yavaşlıyor: {secilen}</h3>", unsafe_allow_html=True)
            time.sleep(0.4)
        
        # 2. Ekranı temizle
        durum_yazisi.empty() 
        
        # 3. Sürpriz Ekranı ve Balonlar
        st.markdown(f"<h2 style='text-align: center; color: #ff4b4b; margin-top:10px;'>🎁 İNANILMAZ! %0.00153 İHTİMAL GELDİ! 🎁</h2>", unsafe_allow_html=True)
        time.sleep(0.5)
        st.balloons()
        
        # 4. Kalan ödüllerden rastgele birini seç
        kazanilan_odul = random.choice(st.session_state.oduller)
        
        # 5. Kazanılan ödülü listeden tamamen sil
        st.session_state.oduller.remove(kazanilan_odul)
        
        # Ödülü ekranda göster
        st.success(kazanilan_odul, icon="🎉")
        
        # Kalan ödül bilgisini ver
        if len(st.session_state.oduller) > 0:
            st.info(f"Kalan sürpriz sayısı: {len(st.session_state.oduller)}. İstersen imkansızı tekrar deneyebilirsin!")