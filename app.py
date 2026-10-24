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

# ---------- مسار ملف الكتاب التفاعلي ----------
HTML_FILE = Path(__file__).parent / "assets" / "refraction_of_light_ch4.html"


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
if HTML_FILE.exists():
    components.html(load_html(HTML_FILE), height=900, scrolling=False)
else:
    st.error(f"لم يتم العثور على الملف: {HTML_FILE}")
