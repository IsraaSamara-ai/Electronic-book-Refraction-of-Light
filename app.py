# -*- coding: utf-8 -*-
"""
انكسار الضوء وتطبيقاته - الصف التاسع (الفصل الرابع)
كتاب تفاعلي مبني بـ HTML/CSS/JS ومعروض داخل Streamlit.
"""
from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

# ---------- إعداد الصفحة ----------
st.set_page_config(
    page_title="انكسار الضوء وتطبيقاته - الصف التاسع",
    page_icon="🔬",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ---------- البحث عن ملف الكتاب التفاعلي ----------
BASE_DIR = Path(__file__).parent


def find_html_file():
    """يبحث عن ملف HTML في assets ثم في المجلد الرئيسي (بأي اسم)."""
    preferred = BASE_DIR / "assets" / "refraction_of_light_ch4.html"
    if preferred.exists():
        return preferred
    for folder in (BASE_DIR / "assets", BASE_DIR):
        if folder.exists():
            files = sorted(folder.glob("*.html"))
            if files:
                return files[0]
    return None


HTML_FILE = find_html_file()


@st.cache_data(show_spinner=False)
def load_html(path: Path) -> str:
    """قراءة ملف HTML مرة واحدة وتخزينه مؤقتاً."""
    return path.read_text(encoding="utf-8")


# ---------- تنسيق Streamlit: إخفاء العناصر الزائدة لعرض كامل الشاشة ----------
st.markdown(
    """
    <style>
      #MainMenu, header, footer {visibility: hidden; height: 0;}
      [data-testid="stToolbar"], [data-testid="stDecoration"] {display: none;}
      .block-container {padding: 0 !important; max-width: 100% !important;}
      iframe {height: 100vh !important; width: 100% !important; border: 0;}
    </style>
    """,
    unsafe_allow_html=True,
)

# ---------- عرض الكتاب التفاعلي ----------
if HTML_FILE is not None:
    components.html(load_html(HTML_FILE), height=900, scrolling=False)
else:
    st.error(
        "لم يتم العثور على ملف HTML في المستودع. "
        "ارفعي الملف داخل مجلد assets أو في المجلد الرئيسي بجانب app.py."
    )
    st.write("الملفات الموجودة في المجلد الرئيسي:", [p.name for p in BASE_DIR.iterdir()])
