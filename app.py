import streamlit as st
import base64
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Hiba ❤️",
    page_icon="💖",
    layout="centered"
)

# Load image
with open("hiba.jpeg", "rb") as f:
    img_b64 = base64.b64encode(f.read()).decode()

html_code = f"""
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<style>
body {{
    margin: 0;
    padding: 0;
    background: radial-gradient(circle at top, #ff758c, #ff7eb3, #b24592);
    font-family: 'Segoe UI', sans-serif;
    overflow-x: hidden;
    color: white;
}}

.container {{
    padding: 18px;
    text-align: center;
}}

.glow {{
    width: 100%;
    max-width: 420px;
    border-radius: 24px;
    animation: glow 3s ease-in-out infinite alternate;
    box-shadow: 0 0 25px rgba(255,182,193,0.7);
}}

@keyframes glow {{
    from {{ box-shadow: 0 0 25px rgba(255,182,193,0.5); }}
    to {{ box-shadow: 0 0 45px rgba(255,105,180,0.9); }}
}}

.title {{
    font-size: 42px;
    font-weight: bold;
    margin-top: 16px;
    text-shadow: 0 0 12px rgba(255,255,255,0.5);
}}

.subtitle {{
    font-size: 18px;
    font-style: italic;
    color: #ffe4ec;
    margin-bottom: 18px;
}}

.poetry {{
    font-size: 17px;
    line-height: 1.9;
    margin-top: 18px;
    padding: 12px;
    min-height: 220px;
}}

.footer {{
    margin-top: 30px;
    font-size: 16px;
    color: #ffe4ec;
}}

.floating {{
    position: fixed;
    top: -10%;
    font-size: 26px;
    animation: float linear;
    pointer-events: none;
    z-index: 9999;
}}

@keyframes float {{
    to {{ transform: translateY(120vh) rotate(360deg); }}
}}
</style>
</head>

<body>

<div class="container">
    <img class="glow" src="data:image/jpeg;base64,{img_b64}" alt="Hiba">

    <div class="title">For you Rooh-e-qainat</div>
    <div class="subtitle">✨</div>

    <div id="poetry" class="poetry"></div>

    <div class="footer">
        ❤️❤️
    </div>
</div>

<script>
// ---------------- FLOATING HEARTS & ROSES ----------------
const symbols = ["🌹", "💖", "❤️"];

function createFloating() {{
    const el = document.createElement("div");
    el.className = "floating";
    el.innerHTML = symbols[Math.floor(Math.random() * symbols.length)];
    el.style.left = Math.random() * 100 + "vw";
    el.style.animationDuration = (Math.random() * 4 + 6) + "s";
    document.body.appendChild(el);
    setTimeout(() => el.remove(), 12000);
}}
setInterval(createFloating, 300);

// ---------------- TYPING ANIMATION ----------------
const text = `
Dear Hiba,

Your eyes feel like verses destiny whispered gently,
one glance — and the world forgets how to breathe.

Your face is a prayer answered in silence,
cheeks brushed by grace,
lips holding a softness words can’t reach.

You are not just beautiful,
you are Afreen —
a miracle wrapped in elegance and light.

If love ever searched for beauty,
it would stop…
smile quietly…
and call your name — Hiba.
`;

let index = 0;
const speed = 35;
const poetryDiv = document.getElementById("poetry");

function typeText() {{
    if (index < text.length) {{
        poetryDiv.innerHTML += text.charAt(index) === "\\n" ? "<br>" : text.charAt(index);
        index++;
        setTimeout(typeText, speed);
    }}
}}

typeText();
</script>

</body>
</html>
"""

components.html(html_code, height=1050, scrolling=True)
