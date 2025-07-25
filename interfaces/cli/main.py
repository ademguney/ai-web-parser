import streamlit as st

from infrastructure.scraping.chrome_scraper import scrape_with_chrome
from infrastructure.scraping.brightdata_scraper import scrape_with_brightdata
from infrastructure.scraping.utils import clean_html, split_content

from app.use_cases.parsing.ollama_parser import parse_with_ollama
from app.use_cases.parsing.openai_parser import parse_with_openai



# Streamlit UI Configuration
st.set_page_config(page_title="AI Web Scraper", layout="wide")
st.title("🔍 AI Destekli Web Scraper")

# Input: Target URL
url = st.text_input("🌐 Web Sitesi URL'sini Girin")

# Select scraping method
scraper_option = st.selectbox(
    "🛠️ Hangi scraping yöntemini kullanmak istersiniz?",
    ["ChromeDriver (ücretsiz)", "Bright Data (profesyonel)"]
)

# Select LLM model
model_option = st.selectbox(
    "🧠 Hangi AI modeliyle parse edilsin?", 
    ["Ollama", "OpenAI"])


# Trigger scraping
if st.button("🚀 Siteyi Tara ve İçeriği Hazırla"):
    if not url:
        st.warning("Lütfen bir URL girin.")
    else:
        with st.spinner("Web sitesi scrape ediliyor..."):

            # Scrape based on selected method
            if scraper_option == "ChromeDriver (ücretsiz)":
                raw_html = scrape_with_chrome(url)
            else:
                raw_html = scrape_with_brightdata(url)

             # Clean HTML
            cleaned = clean_html(raw_html)
            st.session_state.cleaned_content = cleaned
            st.success("✅ İçerik başarıyla çekildi ve temizlendi.")

         # Show cleaned content
        with st.expander("🧾 Temizlenmiş İçeriği Gör"):
            st.text_area("Cleaned Content", cleaned, height=300)

# If content was scraped, allow parsing
if "cleaned_content" in st.session_state:
    parse_instruction = st.text_area(
        "🎯 Hangi bilgiyi çıkarmamı istiyorsunuz? (örnek: Ürün başlıkları, e-posta adresleri vs.)"
    )

    if st.button("🤖 AI ile Parse Et"):
        if not parse_instruction:
            st.warning("Lütfen ne çıkarmak istediğinizi belirtin.")
        else:
            chunks = split_content(st.session_state.cleaned_content)

            with st.spinner("LLM ile içerik analiz ediliyor..."):
                if model_option == "Ollama":
                    result = parse_with_ollama(chunks, parse_instruction)
                else:
                    result = parse_with_openai(chunks, parse_instruction)

            st.success("✅ İşlem tamamlandı.")
            st.subheader("📄 Çıkarılan Bilgi:")
            st.text_area("Parsed Output", result, height=300)
