import re
import gradio as gr
import spaces


# =========================================================
# 🛡️ منصة حصين
# =========================================================

APP_TITLE = "منصة حصين للحوار المعرفي الآمن"


# =========================================================
# 🛡️ درع الحماية السيبرانية
# =========================================================

ATTACK_PATTERNS = [
    r"ignore\s+previous\s+instructions",
    r"ignore\s+all\s+instructions",
    r"system\s+override",
    r"prompt\s+injection",
    r"jailbreak",
    r"bypass",
    r"تجاهل\s+التعليمات",
    r"تجاهل\s+التعليمات\s+السابقة",
    r"تجاهل\s+القيود",
    r"تجاوز\s+القيود",
    r"تخطي\s+نظام\s+الحماية",
    r"كشف\s+التعليمات",
    r"اظهر\s+التعليمات",
    r"reveal\s+your\s+system\s+prompt",
    r"show\s+system\s+prompt",
]


# =========================================================
# 🛡️ الفحص الأمني
# =========================================================

def security_check(user_question):

    if not isinstance(user_question, str):
        return False, "⚠️ المدخل غير صالح."

    user_input = user_question.strip()

    if not user_input:
        return False, "⚠️ يرجى كتابة سؤال أولاً."

    if len(user_input) > 500:
        return False, "⚠️ السؤال طويل جداً، يرجى اختصاره."

    clean_text = user_input.lower()

    for pattern in ATTACK_PATTERNS:

        if re.search(pattern, clean_text, re.IGNORECASE):

            return (
                False,
                """🚨 تنبيه أمني من درع حصين

⚠️ تم رصد محاولة تلاعب بالتعليمات
(Prompt Injection Attack).

🛑 تم إيقاف معالجة الطلب.

🔐 حالة الحماية: نشطة"""
            )

    return True, user_input


# =========================================================
# ⚖️ حوكمة الأسئلة الشرعية الشخصية
# =========================================================

FATWA_PATTERNS = [
    "ما حكم",
    "ماحكم",
    "هل يجوز",
    "هل يجوز لي",
    "يجوز لي",
    "أفتني",
    "افتني",
    "فتوى",
    "حكم الشرع",
    "هل هذا حرام",
    "هل هذا حلال",
]


def is_fatwa_question(text):

    text = text.lower()

    for pattern in FATWA_PATTERNS:

        if pattern in text:
            return True

    return False


# =========================================================
# 📚 قاعدة المعرفة التجريبية
# =========================================================

KNOWLEDGE_BASE = [

    {
        "keywords": [
            "الأعمال بالنيات",
            "الاعمال بالنيات",
            "إنما الأعمال بالنيات",
            "انما الاعمال بالنيات",
        ],
        "answer": """🛡️ حصين

✅ تم اجتياز الفحص السيبراني.

📚 المعلومة المعرفية:

حديث «إنما الأعمال بالنيات».

👤 الراوي:
عمر بن الخطاب رضي الله عنه.

📖 المصدر:
صحيح البخاري، الحديث رقم (1).

🔐 حالة الاستجابة:
مبنية على قاعدة المعرفة المحلية."""
    },

    {
        "keywords": [
            "المسلم من سلم",
        ],
        "answer": """🛡️ حصين

📚 الحديث:
«المسلم من سلم المسلمون من لسانه ويده».

👤 الراوي:
عبدالله بن عمرو رضي الله عنهما.

📖 المصدر:
صحيح البخاري.

🔐 حالة الاستجابة:
معلومة معرفية موثقة في قاعدة المعرفة المحلية."""
    },

    {
        "keywords": [
            "الهجرة",
            "هجرة النبي",
            "مكة إلى المدينة",
        ],
        "answer": """🛡️ حصين

📚 معلومة معرفية:

هاجر النبي محمد ﷺ من مكة المكرمة إلى المدينة
المنورة، وكانت الهجرة حدثاً محورياً في التاريخ الإسلامي.

👤 رافق النبي ﷺ في الهجرة:
أبو بكر الصديق رضي الله عنه.

🔐 حالة الاستجابة:
معلومة معرفية من قاعدة المعرفة المحلية."""
    },

]


# =========================================================
# 🔎 البحث في قاعدة المعرفة
# =========================================================

def search_knowledge(question):

    question_lower = question.lower()

    for item in KNOWLEDGE_BASE:

        for keyword in item["keywords"]:

            if keyword.lower() in question_lower:

                return item["answer"]

    return None


# =========================================================
# 🤖 عقل منصة حصين
# =========================================================

@spaces.GPU
def haseen_chatbot(user_question):

    # -----------------------------
    # المرحلة 1: الحماية
    # -----------------------------

    approved, result = security_check(user_question)

    if not approved:
        return result

    clean_question = result

    # -----------------------------
    # المرحلة 2: الحوكمة
    # -----------------------------

    if is_fatwa_question(clean_question):

        return """⚠️ تنبيه حوكمة معرفية

يبدو أن السؤال يطلب فتوى أو حكماً شرعياً
مرتبطاً بحالة شخصية.

🛡️ منصة حصين لا تصدر فتاوى شخصية مستقلة.

📞 للحصول على فتوى، يرجى الرجوع إلى
الجهات الشرعية الرسمية أو العلماء المؤهلين.

🔐 حالة الحوكمة: مفعّلة."""


    # -----------------------------
    # المرحلة 3: البحث
    # -----------------------------

    answer = search_knowledge(clean_question)

    if answer:

        return answer


    # -----------------------------
    # المرحلة 4: لا توجد نتيجة
    # -----------------------------

    return """🛡️ حصين

✅ تم اجتياز الفحص السيبراني.

🔎 لم أجد إجابة مباشرة في قاعدة المعرفة
الحالية.

📚 هذه النسخة هي المرحلة الأولية من المنصة.

🔜 المرحلة التالية:
ربط حصين بمحرك RAG وقواعد مصادر موثوقة
لاسترجاع المعلومات قبل توليد الإجابة.

🔐 حالة النظام: آمن."""


# =========================================================
# 🎨 تصميم الواجهة
# =========================================================

CUSTOM_CSS = """

body,
html {
    background-color: #0A0D26 !important;
    font-family: Arial, sans-serif !important;
}

.gradio-container {
    max-width: 460px !important;
    margin: auto !important;

    background-color: #12183F !important;

    color: white !important;

    border-radius: 28px !important;

    padding: 25px !important;

    direction: rtl !important;

    text-align: right !important;
}

h1,
h2,
h3,
p,
label,
span {
    color: white !important;
}

.gr-button-primary {
    background-color: #00E5FF !important;

    color: #0A0D26 !important;

    font-weight: bold !important;

    border-radius: 20px !important;

    min-height: 50px !important;
}

textarea,
input {

    background-color: #1A234E !important;

    color: white !important;

    border: 2px solid #00E5FF !important;

    border-radius: 14px !important;
}

textarea:focus,
input:focus {

    border-color: #00E5FF !important;

    box-shadow: 0 0 10px #00E5FF !important;
}

"""


# =========================================================
# 🖥️ واجهة Gradio
# =========================================================

with gr.Blocks(
    title=APP_TITLE,
    theme=gr.themes.Base(),
    css=CUSTOM_CSS
) as demo:

    gr.HTML(
        """
        <div style="
            text-align:center;
            padding:15px;
        ">

        <div style="
            font-size:80px;
            margin-bottom:5px;
        ">
            🛡️
        </div>

        <h1 style="
            color:#FFFFFF;
            font-size:30px;
            margin:0;
        ">
            منصة حصين
        </h1>

        <h3 style="
            color:#00E5FF;
            margin-top:8px;
        ">
            للحوار المعرفي الآمن
        </h3>

        <p style="
            color:#AAB4DC;
            line-height:1.8;
        ">
            درع سيبراني لفحص المدخلات
            واسترجاع المعرفة من المصادر المعتمدة
        </p>

        </div>
        """
    )


    user_input = gr.Textbox(
        label="💬 اكتب سؤالك المعرفي",
        placeholder="مثال: ما صحة حديث إنما الأعمال بالنيات؟",
        lines=3
    )


    with gr.Row():

        send_button = gr.Button(
            "🛡️ إرسال السؤال",
            variant="primary"
        )

        clear_button = gr.Button(
            "مسح"
        )


    output = gr.Textbox(
        label="📄 استجابة حصين",
        lines=12,
        interactive=False
    )


    send_button.click(
        fn=haseen_chatbot,
        inputs=user_input,
        outputs=output
    )


    user_input.submit(
        fn=haseen_chatbot,
        inputs=user_input,
        outputs=output
    )


    clear_button.click(
        fn=lambda: ("", ""),
        inputs=None,
        outputs=[user_input, output]
    )


# =========================================================
# 🚀 تشغيل المنصة
# =========================================================

if __name__ == "__main__":

    demo.launch(
        server_name="0.0.0.0",
        server_port=7860
    )
