import base64
import io
import os
import json
from dotenv import load_dotenv
from PIL import Image
import pdf2image
import streamlit as st
from google import genai
from google.genai import types

# ---------------------------------------------------------
# INITIALIZATION & ENVIRONMENT SETUP
# ---------------------------------------------------------
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

# Initialize Gemini Client (Using official google-genai SDK)
client = genai.Client(api_key=api_key) if api_key else None

# Page Setup - Ultra Wide Desktop Studio Mode
st.set_page_config(
    page_title="Enterprise AI Resume Intelligence Suite",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ---------------------------------------------------------
# CORE ENGINE & AI PROMPT ARCHITECTURE
# ---------------------------------------------------------
def get_gemini_analysis(pdf_content, job_description):
    """
    Sends multi-page vision rendering of PDF alongside Job Description to Gemini 3.6 Flash.
    Requests structured JSON output for strict client-side rendering.
    """
    if not client:
        st.error("API Key not found. Please set `GOOGLE_API_KEY` in your `.env` file.")
        return None

    prompt = """
    You are an elite Fortune 500 Executive Recruiter, Principal Talent Architect, and ATS Engineer.
    Perform an exhaustive multi-dimensional analysis of the candidate's uploaded resume image against the provided job description.

    STRICT REQUIREMENT: Respond ONLY with a valid, raw JSON object matching this schema EXACTLY. Do not wrap in markdown code blocks.

    {
      "ats_score": 87,
      "keyword_density": 92,
      "format_precision": 85,
      "action_verbs_impact": 78,
      "readability_score": 94,
      "bullet_optimizations": [
        {
          "id": 1,
          "original": "Original text from user resume",
          "flag": "Flag Reason",
          "optimized": "Optimized bullet point"
        }
      ],
      "skills_matrix": {
        "validated_skills": ["Skill1", "Skill2"],
        "missing_critical_gaps": ["MissingSkill1", "MissingSkill2"],
        "radar_data": {
          "categories": ["Category 1", "Category 2"],
          "candidate_levels": [80, 70],
          "market_demands": [90, 85]
        }
      },
      "salary_analytics": {
        "estimated_min": 100000,
        "estimated_target": 120000,
        "estimated_max": 150000,
        "location_adjustment": "Location / Remote",
        "value_multiplier_skills": [
          "Skill 1",
          "Skill 2"
        ]
      },
      "interview_questions": [
        {
          "id": 1,
          "type": "Category",
          "question": "Question text",
          "blueprint": "Answer guidance"
        }
      ]
    }

    Job Description:
    """ + job_description

    contents = [prompt]
    for page in pdf_content:
        image_part = types.Part.from_bytes(
            data=base64.b64decode(page["data"]),
            mime_type=page["mime_type"]
        )
        contents.append(image_part)

    try:
        response = client.models.generate_content(
            model="gemini-3.6-flash",
            contents=contents,
            config=types.GenerateContentConfig(
                response_mime_type="application/json"
            )
        )
        return json.loads(response.text)
    except Exception as e:
        st.error(f"AI API Response Parse Error: {str(e)}")
        return None

def input_pdf_setup(uploaded_file):
    """Converts PDF pages into base64 visual representations for Gemini Vision."""
    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()
        images = pdf2image.convert_from_bytes(bytes_data)

        pdf_parts = []
        for page in images:
            img_byte_arr = io.BytesIO()
            page.save(img_byte_arr, format="JPEG", quality=85)
            img_byte_arr = img_byte_arr.getvalue()

            pdf_parts.append({
                "mime_type": "image/jpeg",
                "data": base64.b64encode(img_byte_arr).decode()
            })
        return pdf_parts, images
    else:
        raise FileNotFoundError("No resume PDF provided")

# ---------------------------------------------------------
# CYBER-ONYX EMBEDDED CSS DESIGN SYSTEM
# ---------------------------------------------------------
cyber_onyx_css = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&display=swap');

/* GLOBAL CANVAS RESET */
html, body, [data-testid="stAppViewContainer"] {
    background-color: #030712 !important;
    color: #F9FAFB !important;
    font-family: 'Plus Jakarta Sans', sans-serif !important;
}

[data-testid="stHeader"] {
    background: transparent !important;
}

/* HIDE STREAMLIT BRANDING CONSTRAINTS */
#MainMenu, footer, header {visibility: hidden;}
.block-container {
    padding-top: 1rem !important;
    padding-bottom: 2rem !important;
    max-width: 98% !important;
}

/* TOP STICKY NAVIGATION BAR */
.navbar-container {
    position: sticky;
    top: 0;
    z-index: 999;
    background: rgba(17, 24, 39, 0.7);
    backdrop-filter: blur(16px);
    -webkit-backdrop-filter: blur(16px);
    border-bottom: 1px solid #374151;
    padding: 0.75rem 1.5rem;
    display: flex;
    align-items: center;
    justify-content: space-between;
    border-radius: 12px;
    margin-bottom: 1.25rem;
}

.nav-logo-group {
    display: flex;
    align-items: center;
    gap: 0.75rem;
}

.nav-brand-title {
    font-weight: 800;
    font-size: 1.15rem;
    letter-spacing: -0.02em;
    background: linear-gradient(135deg, #FFFFFF 0%, #94A3B8 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.nav-badge {
    background: rgba(79, 70, 229, 0.15);
    border: 1px solid rgba(79, 70, 229, 0.4);
    color: #818CF8;
    font-size: 0.7rem;
    font-weight: 700;
    padding: 0.2rem 0.6rem;
    border-radius: 99px;
    letter-spacing: 0.05em;
    text-transform: uppercase;
}

.nav-center-nodes {
    display: flex;
    gap: 1.5rem;
    font-size: 0.85rem;
    font-weight: 500;
    color: #9CA3AF;
}

.nav-node-active {
    color: #38BDF8;
    font-weight: 600;
    display: flex;
    align-items: center;
    gap: 0.4rem;
}

.nav-right-workspace {
    display: flex;
    align-items: center;
    gap: 1rem;
}

.cmd-k-trigger {
    background: rgba(31, 41, 55, 0.8);
    border: 1px solid #374151;
    color: #9CA3AF;
    font-size: 0.75rem;
    padding: 0.35rem 0.75rem;
    border-radius: 6px;
    display: flex;
    align-items: center;
    gap: 0.5rem;
    cursor: pointer;
}

/* BENTO GRID CARD CONTAINERS */
.bento-card {
    background: rgba(17, 24, 39, 0.6);
    border: 1px solid #374151;
    border-radius: 14px;
    padding: 1.25rem;
    backdrop-filter: blur(12px);
    box-shadow: 0 10px 30px -10px rgba(0, 0, 0, 0.5);
    margin-bottom: 1rem;
    transition: all 0.2s ease-in-out;
}

.bento-card:hover {
    border-color: rgba(79, 70, 229, 0.5);
    box-shadow: 0 12px 35px -10px rgba(79, 70, 229, 0.15);
}

.bento-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 1rem;
    border-bottom: 1px solid rgba(55, 65, 81, 0.5);
    padding-bottom: 0.6rem;
}

.bento-title {
    font-size: 0.95rem;
    font-weight: 700;
    color: #F3F4F6;
    display: flex;
    align-items: center;
    gap: 0.5rem;
    letter-spacing: -0.01em;
}

.bento-tag {
    font-size: 0.7rem;
    font-weight: 600;
    color: #06B6D4;
    background: rgba(6, 182, 212, 0.1);
    padding: 0.2rem 0.5rem;
    border-radius: 4px;
    border: 1px solid rgba(6, 182, 212, 0.25);
}

/* MODULE 1: RADIAL GAUGE & METRIC BARS */
.radial-container {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    position: relative;
}

.radial-score-value {
    position: absolute;
    font-weight: 800;
    font-size: 2.2rem;
    color: #FFFFFF;
    text-shadow: 0 0 20px rgba(79, 70, 229, 0.6);
}

.radial-score-label {
    position: absolute;
    top: 62%;
    font-size: 0.7rem;
    color: #9CA3AF;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.08em;
}

.metric-bar-wrapper {
    margin-bottom: 0.85rem;
}

.metric-bar-meta {
    display: flex;
    justify-content: space-between;
    font-size: 0.8rem;
    font-weight: 600;
    margin-bottom: 0.3rem;
}

.metric-bar-bg {
    height: 7px;
    width: 100%;
    background: #1F2937;
    border-radius: 99px;
    overflow: hidden;
}

.metric-bar-fill {
    height: 100%;
    border-radius: 99px;
    transition: width 1s ease-in-out;
}

/* MODULE 2: BULLET OPTIMIZER CARDS */
.bullet-card {
    background: rgba(31, 41, 55, 0.4);
    border: 1px solid #374151;
    border-radius: 10px;
    padding: 1rem;
    margin-bottom: 0.75rem;
}

.bullet-flag {
    display: inline-flex;
    align-items: center;
    gap: 0.3rem;
    font-size: 0.7rem;
    font-weight: 700;
    color: #EF4444;
    background: rgba(239, 68, 68, 0.1);
    border: 1px solid rgba(239, 68, 68, 0.25);
    padding: 0.15rem 0.5rem;
    border-radius: 4px;
    margin-bottom: 0.5rem;
}

.bullet-original {
    font-size: 0.85rem;
    color: #9CA3AF;
    text-decoration: line-through;
    margin-bottom: 0.6rem;
}

.bullet-optimized {
    font-size: 0.88rem;
    color: #F3F4F6;
    font-weight: 500;
    line-height: 1.4;
    border-left: 2px solid #10B981;
    padding-left: 0.75rem;
    background: rgba(16, 185, 129, 0.03);
    padding-top: 0.3rem;
    padding-bottom: 0.3rem;
}

/* MODULE 3: SKILL CHIPS */
.chip-container {
    display: flex;
    flex-wrap: wrap;
    gap: 0.5rem;
    margin-top: 0.5rem;
}

.skill-chip-emerald {
    background: rgba(16, 185, 129, 0.1);
    border: 1px solid rgba(16, 185, 129, 0.3);
    color: #34D399;
    font-size: 0.78rem;
    font-weight: 600;
    padding: 0.3rem 0.65rem;
    border-radius: 6px;
    display: flex;
    align-items: center;
    gap: 0.35rem;
}

.skill-chip-crimson {
    background: rgba(239, 68, 68, 0.1);
    border: 1px solid rgba(239, 68, 68, 0.3);
    color: #F87171;
    font-size: 0.78rem;
    font-weight: 600;
    padding: 0.3rem 0.65rem;
    border-radius: 6px;
    display: flex;
    align-items: center;
    gap: 0.35rem;
}

/* MODULE 4: SALARY RANGE SLIDER COMPONENT */
.salary-hero-box {
    text-align: center;
    background: linear-gradient(180deg, rgba(79, 70, 229, 0.12) 0%, rgba(17, 24, 39, 0) 100%);
    border: 1px solid rgba(79, 70, 229, 0.3);
    border-radius: 12px;
    padding: 1rem;
    margin-bottom: 1rem;
}

.salary-figure {
    font-size: 2.2rem;
    font-weight: 800;
    color: #10B981;
    letter-spacing: -0.02em;
}

.salary-subtext {
    font-size: 0.75rem;
    color: #9CA3AF;
}

/* SHIMMER DYNAMIC LOADING SCANNER */
.scan-container {
    position: relative;
    width: 100%;
    height: 180px;
    background: #111827;
    border: 1px dashed #374151;
    border-radius: 12px;
    overflow: hidden;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
}

.scan-bar {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 4px;
    background: linear-gradient(90deg, #06B6D4, #4F46E5, #10B981);
    box-shadow: 0 0 15px #4F46E5;
    animation: scanMove 2s infinite ease-in-out;
}

@keyframes scanMove {
    0% { top: 0%; }
    50% { top: 95%; }
    100% { top: 0%; }
}

/* COMMAND PALETTE OVERLAY */
.cmd-modal-backdrop {
    background: rgba(3, 7, 18, 0.85);
    backdrop-filter: blur(8px);
    padding: 1rem;
    border-radius: 12px;
    border: 1px solid #374151;
    margin-bottom: 1rem;
}

/* PLACEHOLDER SKELETON STATE STYLE */
.placeholder-text {
    color: #4B5563;
    font-style: italic;
    font-size: 0.85rem;
}

/* BUTTON OVERRIDES */
.stButton>button {
    background: linear-gradient(180deg, #4F46E5 0%, #4338CA 100%) !important;
    color: #FFFFFF !important;
    font-weight: 600 !important;
    border: 1px solid rgba(255, 255, 255, 0.15) !important;
    border-radius: 8px !important;
    padding: 0.5rem 1rem !important;
    box-shadow: 0 4px 12px rgba(79, 70, 229, 0.3) !important;
    transition: all 0.2s ease !important;
}

.stButton>button:hover {
    transform: translateY(-1px) !important;
    box-shadow: 0 6px 18px rgba(79, 70, 229, 0.5) !important;
}
</style>
"""

st.markdown(cyber_onyx_css, unsafe_allow_html=True)

# ---------------------------------------------------------
# SECTION 1: GLOBAL FIXED NAVIGATION HEADER
# ---------------------------------------------------------
st.markdown("""
<div class="navbar-container">
    <div class="nav-logo-group">
        <svg width="28" height="28" viewBox="0 0 32 32" fill="none" xmlns="http://www.w3.org/2000/svg">
            <rect width="32" height="32" rx="8" fill="#4F46E5"/>
            <path d="M9 12L16 7L23 12V20L16 25L9 20V12Z" stroke="white" stroke-width="2" stroke-linejoin="round"/>
            <path d="M16 7V25" stroke="white" stroke-width="1.5" stroke-dasharray="2 2"/>
        </svg>
        <span class="nav-brand-title">CYBER-ONYX ATS SUITE</span>
        <span class="nav-badge">v4.0 Enterprise</span>
    </div>
    <div class="nav-center-nodes">
        <span class="nav-node-active">
            <svg width="6" height="6" viewBox="0 0 6 6" fill="none"><circle cx="3" cy="3" r="3" fill="#38BDF8"/></svg>
            Live Engine View
        </span>
        <span>•</span>
        <span>Candidate Optimization</span>
        <span>•</span>
        <span>Market Analytics</span>
    </div>
    <div class="nav-right-workspace">
        <div class="cmd-k-trigger">
            <span>⌘K</span>
            <span style="color:#6B7280;">Command Hub</span>
        </div>
        <div style="width:32px; height:32px; border-radius:99px; background:linear-gradient(135deg, #4F46E5, #06B6D4); display:flex; align-items:center; justify-content:center; font-weight:700; font-size:0.8rem; border:1px solid #374151;">
            VL
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# COMMAND PALETTE UTILITY HUB (TOGGLEABLE)
# ---------------------------------------------------------
with st.expander("⌨️ Command Palette Utilities (Ctrl+K / Cmd+K Quick Menu)", expanded=False):
    st.markdown("""
    <div class="cmd-modal-backdrop">
        <span style="font-size:0.75rem; color:#9CA3AF; font-weight:600;">ENTERPRISE SHORTCUTS & NAVIGATION</span>
    </div>
    """, unsafe_allow_html=True)
    cmd_col1, cmd_col2, cmd_col3 = st.columns(3)
    with cmd_col1:
        if st.button("🚀 Switch to Senior Architect Profile", use_container_width=True):
            st.toast("Profile switched: Senior Architect Tier")
    with cmd_col2:
        if st.button("📥 Trigger Full Audit Export", use_container_width=True):
            st.toast("Generating PDF Audit Payload...")
    with cmd_col3:
        if st.button("🔄 Reset Environment Canvas", use_container_width=True):
            st.session_state.clear()
            st.rerun()

# ---------------------------------------------------------
# DUAL-CANVAS VIEWPORT LAYOUT ARCHITECTURE
# ---------------------------------------------------------
left_split, right_split = st.columns([45, 55], gap="large")

# ---------------------------------------------------------
# LEFT SPLIT: INPUT & PDF VISUALIZER CANVAS
# ---------------------------------------------------------
with left_split:
    st.markdown("""
    <div class="bento-card">
        <div class="bento-header">
            <span class="bento-title">📄 Document & Job Spec Inputs</span>
            <span class="bento-tag">STEP 1 & 2</span>
        </div>
    """, unsafe_allow_html=True)

    input_text = st.text_area(
        label="Target Job Description Requirements",
        height=180,
        placeholder="Paste target job specification, core qualifications, and technical stack requirements...",
        key="jd_input"
    )

    uploaded_file = st.file_uploader(
        label="Upload Candidate Resume (PDF)",
        type=["pdf"],
        help="Upload multi-page PDF document for vision rendering.",
        key="pdf_uploader"
    )

    st.markdown("</div>", unsafe_allow_html=True)

    # PDF RENDERER SUB-SYSTEM
    if uploaded_file is not None:
        try:
            pdf_payload, page_images = input_pdf_setup(uploaded_file)
            st.session_state['pdf_payload'] = pdf_payload
            st.session_state['pdf_images'] = page_images

            st.markdown("""
            <div class="bento-card">
                <div class="bento-header">
                    <span class="bento-title">🔍 High-Fidelity PDF Viewer</span>
                    <span class="bento-tag">VISION ENGINE READY</span>
                </div>
            """, unsafe_allow_html=True)

            # Sub-bar Controls
            pdf_ctrl1, pdf_ctrl2, pdf_ctrl3 = st.columns([2, 1, 1])
            with pdf_ctrl1:
                st.caption(f"File: **{uploaded_file.name}** ({len(page_images)} Page(s))")
            with pdf_ctrl2:
                zoom_level = st.selectbox("Zoom", ["100%", "125%", "75%"], index=0, key="zoom")
            with pdf_ctrl3:
                page_select = st.number_input("Page", min_value=1, max_value=len(page_images), value=1)

            # Render selected image page
            target_img = page_images[page_select - 1]
            st.image(target_img, use_container_width=True, caption=f"Page {page_select} of {len(page_images)}")

            st.markdown("</div>", unsafe_allow_html=True)

        except Exception as e:
            st.error(f"Error reading PDF file: {str(e)}")

    else:
        st.markdown("""
        <div class="scan-container">
            <div class="scan-bar"></div>
            <span style="font-size:2rem; margin-bottom:0.5rem;">📥</span>
            <span style="font-size:0.9rem; font-weight:600; color:#F3F4F6;">Upload Resume PDF to Initiate Vision Processing</span>
            <span style="font-size:0.75rem; color:#9CA3AF; margin-top:0.25rem;">Multi-page documents rendered dynamically</span>
        </div>
        """, unsafe_allow_html=True)

    # Trigger Execution Action
    st.markdown("<br>", unsafe_allow_html=True)
    analyze_btn = st.button("⚡ EXECUTE COMPLETE AI SUITE AUDIT", use_container_width=True)

# ---------------------------------------------------------
# RIGHT SPLIT: BENTO GRID DASHBOARD
# ---------------------------------------------------------
with right_split:

    # Trigger API Call
    if analyze_btn:
        if uploaded_file is not None and input_text.strip() != "":
            with st.spinner("🤖 Gemini Vision Engine Analyzing PDF Layout & Text Matrix..."):
                analysis_results = get_gemini_analysis(st.session_state['pdf_payload'], input_text)
                if analysis_results:
                    st.session_state['data'] = analysis_results
        else:
            st.warning("⚠️ Please provide a Job Description and upload a Resume (PDF).")

    # Fetch data if exists
    data = st.session_state.get('data', None)

    # =========================================================
    # MODULE 1: THE MATRIX ATS SCORING HUB
    # =========================================================
    st.markdown("""
    <div class="bento-card">
        <div class="bento-header">
            <span class="bento-title">🎯 Module 1: The Matrix ATS Scoring Hub</span>
            <span class="bento-tag">360° EVALUATION</span>
        </div>
    """, unsafe_allow_html=True)

    m1_col1, m1_col2 = st.columns([1, 1], gap="medium")

    with m1_col1:
        score = data.get("ats_score", 0) if data else 0
        dash_offset = 283 - (283 * score / 100)

        svg_radial = f"""
        <div class="radial-container">
            <svg width="150" height="150" viewBox="0 0 100 100">
                <circle cx="50" cy="50" r="45" fill="none" stroke="#1F2937" stroke-width="8"/>
                <circle cx="50" cy="50" r="45" fill="none" stroke="{ '#4F46E5' if data else '#374151' }" stroke-width="8"
                        stroke-dasharray="283" stroke-dashoffset="{dash_offset}"
                        stroke-linecap="round" transform="rotate(-90 50 50)"/>
            </svg>
            <div class="radial-score-value">{f"{score}%" if data else "0%"}</div>
            <div class="radial-score-label">MATCH INDEX</div>
        </div>
        """
        st.markdown(svg_radial, unsafe_allow_html=True)

    with m1_col2:
        metrics = [
            ("Keyword Density", data.get("keyword_density", 0) if data else 0, "#06B6D4"),
            ("Format Precision", data.get("format_precision", 0) if data else 0, "#4F46E5"),
            ("Action Verbs Impact", data.get("action_verbs_impact", 0) if data else 0, "#F59E0B"),
            ("Readability Rating", data.get("readability_score", 0) if data else 0, "#10B981"),
        ]

        for label, val, color in metrics:
            bar_color = color if data else "#374151"
            st.markdown(f"""
            <div class="metric-bar-wrapper">
                <div class="metric-bar-meta">
                    <span style="color:#9CA3AF;">{label}</span>
                    <span style="color:{bar_color};">{val}%</span>
                </div>
                <div class="metric-bar-bg">
                    <div class="metric-bar-fill" style="width: {val}%; background: {bar_color};"></div>
                </div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

    # =========================================================
    # MODULE 2: INLINE AI BULLET POINT OPTIMIZER
    # =========================================================
    st.markdown("""
    <div class="bento-card">
        <div class="bento-header">
            <span class="bento-title">✨ Module 2: Inline AI Bullet Point Optimizer</span>
            <span class="bento-tag">METRIC-DRIVEN REWRITE</span>
        </div>
    """, unsafe_allow_html=True)

    if data and "bullet_optimizations" in data:
        bullets = data.get("bullet_optimizations", [])
        for b in bullets:
            st.markdown(f"""
            <div class="bullet-card">
                <div class="bullet-flag">
                    <span>⚠️</span>
                    <span>{b.get('flag', 'Optimization Required')}</span>
                </div>
                <div class="bullet-original">{b.get('original', '')}</div>
                <div class="bullet-optimized">{b.get('optimized', '')}</div>
            </div>
            """, unsafe_allow_html=True)
    else:
        st.markdown("""
        <div class="bullet-card" style="border-style: dashed; text-align: center;">
            <p class="placeholder-text">Awaiting resume analysis. Bullet point optimizations will appear here.</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

    # =========================================================
    # MODULE 3: 3D SKILL GAP VECTOR MATRIX
    # =========================================================
    st.markdown("""
    <div class="bento-card">
        <div class="bento-header">
            <span class="bento-title">📊 Module 3: 3D Skill Gap Vector Matrix</span>
            <span class="bento-tag">GAP ANALYSIS</span>
        </div>
    """, unsafe_allow_html=True)

    if data and "skills_matrix" in data:
        skills_data = data.get("skills_matrix", {})
        validated = skills_data.get("validated_skills", [])
        missing = skills_data.get("missing_critical_gaps", [])

        st.markdown("<span style='font-size:0.8rem; font-weight:700; color:#34D399;'>VALIDATED SKILLS DETECTED</span>", unsafe_allow_html=True)
        val_chips = "".join([f'<div class="skill-chip-emerald"><span>🛡️</span>{s}</div>' for s in validated])
        st.markdown(f'<div class="chip-container">{val_chips}</div>', unsafe_allow_html=True)

        st.markdown("<br><span style='font-size:0.8rem; font-weight:700; color:#F87171;'>MISSING CRITICAL MARKET GAPS</span>", unsafe_allow_html=True)
        miss_chips = "".join([f'<div class="skill-chip-crimson"><span>⚠️</span>{s}</div>' for s in missing])
        st.markdown(f'<div class="chip-container">{miss_chips}</div>', unsafe_allow_html=True)
    else:
        st.markdown("""
        <div style="padding: 1rem 0; text-align: center;">
            <p class="placeholder-text">Upload a resume to render matched skills and missing critical gap metrics.</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

    # =========================================================
    # MODULE 4: PREDICTIVE SALARY ANALYTICS & MARKET INSIGHT
    # =========================================================
    st.markdown("""
    <div class="bento-card">
        <div class="bento-header">
            <span class="bento-title">💰 Module 4: Predictive Salary Analytics</span>
            <span class="bento-tag">MARKET INSIGHT</span>
        </div>
    """, unsafe_allow_html=True)

    if data and "salary_analytics" in data:
        salary = data.get("salary_analytics", {})
        target_val = salary.get("estimated_target", 0)
        min_val = salary.get("estimated_min", 0)
        max_val = salary.get("estimated_max", 0)

        st.markdown(f"""
        <div class="salary-hero-box">
            <span class="salary-subtext">PROJECTED BASE TARGET COMPENSATION</span>
            <div class="salary-figure">${target_val:,} / yr</div>
            <span class="salary-subtext">Location Index: {salary.get('location_adjustment', 'Market Standards')}</span>
        </div>
        """, unsafe_allow_html=True)

        st.markdown(f"**Industry Range Band:** ${min_val:,} — ${max_val:,}")
        if max_val > min_val:
            st.progress(float((target_val - min_val) / (max_val - min_val)))

        st.markdown("<br>**Top Value-Multiplier Skills to Bridge Gap:**", unsafe_allow_html=True)
        for mult in salary.get("value_multiplier_skills", []):
            st.markdown(f"- 📈 **{mult}**")
    else:
        st.markdown("""
        <div class="salary-hero-box" style="border-style: dashed;">
            <span class="salary-subtext">PROJECTED BASE TARGET COMPENSATION</span>
            <div class="salary-figure" style="color: #4B5563;">$0 / yr</div>
            <span class="salary-subtext">Awaiting target job spec & resume data...</span>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

    # =========================================================
    # MODULE 5: CONTEXTUAL INTERVIEW SIMULATOR & PREP
    # =========================================================
    st.markdown("""
    <div class="bento-card">
        <div class="bento-header">
            <span class="bento-title">🎯 Module 5: Contextual Interview Simulator</span>
            <span class="bento-tag">AI PREP CANVAS</span>
        </div>
    """, unsafe_allow_html=True)

    if data and "interview_questions" in data:
        questions = data.get("interview_questions", [])
        for q in questions:
            with st.expander(f"❓ [{q.get('type', 'General')}] {q.get('question', '')}"):
                st.markdown(f"**Suggested Strategy / Answer Blueprint:**\n\n{q.get('blueprint', '')}")
    else:
        st.markdown("""
        <div style="padding: 1rem 0; text-align: center;">
            <p class="placeholder-text">Interview questions and strategy blueprints will generate automatically after analysis.</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)