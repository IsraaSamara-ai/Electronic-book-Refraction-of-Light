# 🔬 انكسار الضوء وتطبيقاته – الصف التاسع (الفصل الرابع)

كتاب تفاعلي لمادة العلوم/الفيزياء للصف التاسع، يشرح **انكسار الضوء وتطبيقاته**، ويتضمن محاكيات تفاعلية (Canvas) لكل من:

- 🌈 انكسار الضوء بين وسطين (قانون سنل)
- 🔄 الانعكاس الداخلي الكلي
- 🔍 العدسات

يتميّز بتصميم عربي (RTL)، ووضع ليلي/نهاري، وتنقّل بين الصفحات أو التمرير المتواصل، وقائمة جانبية للفهرس.

## 📁 هيكل المشروع

```
refraction-of-light-app/
├── app.py                              # تطبيق Streamlit
├── requirements.txt                    # المكتبات المطلوبة
├── README.md                           # هذا الملف
├── .gitignore
├── .streamlit/
│   └── config.toml                     # إعدادات الثيم والخادم
└── assets/
    └── refraction_of_light_ch4.html    # الكتاب التفاعلي (HTML/CSS/JS)
```

## ▶️ التشغيل محلياً

```bash
pip install -r requirements.txt
streamlit run app.py
```

ثم افتحي الرابط الذي يظهر في الطرفية (عادةً `http://localhost:8501`).

## 🚀 الرفع على GitHub

```bash
git init
git add .
git commit -m "Refraction of light interactive book"
git branch -M main
git remote add origin https://github.com/USERNAME/REPO_NAME.git
git push -u origin main
```

> استبدلي `USERNAME` و`REPO_NAME` باسم حسابك واسم المستودع.

## ☁️ النشر على Streamlit Community Cloud

1. ادخلي إلى [share.streamlit.io](https://share.streamlit.io) وسجّلي بحساب GitHub.
2. اضغطي **Create app** ← **Deploy a public app from GitHub**.
3. اختاري المستودع والفرع `main`.
4. في **Main file path** اكتبي: `app.py`
5. اضغطي **Deploy** وانتظري دقيقة تقريباً.

## ⚙️ ملاحظات تقنية

- الكتاب مضمّن عبر `streamlit.components.v1.html`، لذا يعمل بكل وظائفه (JavaScript وCanvas) كما في الملف الأصلي.
- الخط (Tajawal) والأيقونات (Font Awesome) تُحمَّل من الإنترنت، لذا يلزم اتصال بالشبكة.
- لتعديل المحتوى: عدّلي ملف `assets/refraction_of_light_ch4.html` فقط، دون الحاجة لتغيير `app.py`.
- لتغيير ارتفاع العرض عدّلي قيمة `100vh` في تنسيق `iframe` داخل `app.py`.

## 👩‍🏫 إعداد

إسراء يوسف سمارة – معلمة علوم وفيزياء
