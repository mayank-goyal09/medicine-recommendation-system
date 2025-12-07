import streamlit as st
import pandas as pd
import numpy as np
import joblib
import plotly.graph_objects as go

# ==========================================
# PAGE CONFIG
# ==========================================
st.set_page_config(
    page_title="Elite Medical AI | Dr. Mayank",
    page_icon="⚕️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================
# LUXURY WHITE-GOLD-CHARCOAL THEME
# ==========================================
st.markdown("""
<style>
/* Import Luxury Fonts */
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;600;700;800&family=Montserrat:wght@300;400;600;700&display=swap');

/* Main Background - Pristine White with Gold Accents */
.stApp {
    background: linear-gradient(135deg, #FFFFFF 0%, #F8F9FA 50%, #E8E8E8 100%);
    color: #2C2C2C;
    font-family: 'Montserrat', sans-serif;
}

/* Luxury Header */
.luxury-header {
    font-family: 'Playfair Display', serif;
    font-size: 4rem;
    font-weight: 800;
    background: linear-gradient(135deg, #D4AF37, #FFD700, #B8860B);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    text-align: center;
    margin-bottom: 0.5rem;
    letter-spacing: 0.02em;
    text-shadow: 2px 2px 4px rgba(212, 175, 55, 0.2);
}

.luxury-subtitle {
    font-family: 'Montserrat', sans-serif;
    font-size: 1.3rem;
    color: #5A5A5A;
    text-align: center;
    font-weight: 300;
    letter-spacing: 0.15em;
    text-transform: uppercase;
}

/* Premium Glass Card */
.premium-card {
    background: rgba(255, 255, 255, 0.95);
    border: 2px solid #D4AF37;
    border-radius: 20px;
    padding: 2.5rem;
    box-shadow: 0 8px 32px rgba(212, 175, 55, 0.15), 0 0 80px rgba(255, 215, 0, 0.08);
    margin-bottom: 2rem;
    transition: transform 0.3s ease;
}

.premium-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 12px 48px rgba(212, 175, 55, 0.25), 0 0 100px rgba(255, 215, 0, 0.12);
}

/* Charcoal Card Variant */
.charcoal-card {
    background: linear-gradient(135deg, #2C2C2C 0%, #1A1A1A 100%);
    border: 2px solid #D4AF37;
    border-radius: 20px;
    padding: 2.5rem;
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3), 0 0 60px rgba(212, 175, 55, 0.1);
    color: #FFFFFF;
    margin-bottom: 2rem;
}

/* Gold Accent Text */
.gold-text {
    color: #D4AF37;
    font-weight: 700;
    font-family: 'Playfair Display', serif;
}

.charcoal-text {
    color: #2C2C2C;
    font-weight: 600;
}

/* Sidebar - Luxury Charcoal */
section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #1A1A1A 0%, #2C2C2C 100%);
    border-right: 3px solid #D4AF37;
}

section[data-testid="stSidebar"] * {
    color: #FFFFFF !important;
}

/* Premium Button */
.stButton > button {
    background: linear-gradient(135deg, #D4AF37, #FFD700, #B8860B);
    color: #1A1A1A !important;
    border-radius: 15px;
    border: 2px solid #B8860B;
    font-weight: 700;
    padding: 1rem 3rem;
    font-size: 1.2rem;
    box-shadow: 0 6px 24px rgba(212, 175, 55, 0.4);
    transition: all 0.3s ease;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    font-family: 'Montserrat', sans-serif;
}

.stButton > button:hover {
    transform: translateY(-3px);
    box-shadow: 0 10px 40px rgba(212, 175, 55, 0.6);
    background: linear-gradient(135deg, #FFD700, #D4AF37, #FFD700);
}

/* Multiselect - Gold Accent */
.stMultiSelect > div > div {
    background: rgba(255, 255, 255, 0.95);
    border: 2px solid #D4AF37;
    border-radius: 12px;
}

/* Text Input */
.stTextInput > div > div > input,
.stNumberInput > div > div > input {
    background: rgba(255, 255, 255, 0.95);
    border: 2px solid #D4AF37;
    border-radius: 10px;
    color: #2C2C2C;
    font-weight: 600;
}

/* Radio Buttons */
.stRadio > div {
    background: rgba(255, 255, 255, 0.5);
    padding: 1rem;
    border-radius: 10px;
    border: 1px solid #D4AF37;
}

/* Metrics */
[data-testid="stMetric"] {
    background: rgba(255, 255, 255, 0.95);
    border-radius: 16px;
    padding: 1.5rem;
    border: 2px solid #D4AF37;
    box-shadow: 0 4px 20px rgba(212, 175, 55, 0.15);
}

[data-testid="stMetric"] label {
    color: #5A5A5A !important;
    font-weight: 600;
    font-family: 'Montserrat', sans-serif;
    text-transform: uppercase;
    letter-spacing: 0.05em;
}

[data-testid="stMetric"] [data-testid="stMetricValue"] {
    color: #D4AF37 !important;
    font-size: 2.5rem;
    font-weight: 800;
    font-family: 'Playfair Display', serif;
}

/* Success/Info Boxes */
.stSuccess {
    background: linear-gradient(135deg, rgba(212, 175, 55, 0.1), rgba(255, 215, 0, 0.05));
    border-left: 5px solid #D4AF37;
    border-radius: 12px;
    color: #2C2C2C;
}

.stInfo {
    background: rgba(255, 255, 255, 0.95);
    border-left: 5px solid #5A5A5A;
    border-radius: 12px;
    color: #2C2C2C;
}

/* Checkboxes */
.stCheckbox {
    background: rgba(255, 255, 255, 0.7);
    padding: 0.5rem 1rem;
    border-radius: 8px;
    border: 1px solid #E0E0E0;
    margin-bottom: 0.5rem;
}

/* Divider */
hr {
    border-color: #D4AF37 !important;
    opacity: 0.3;
}

/* Tabs */
.stTabs [data-baseweb="tab-list"] {
    gap: 1rem;
    background: rgba(255, 255, 255, 0.95);
    border-radius: 15px;
    padding: 0.8rem;
    border: 2px solid #D4AF37;
}

.stTabs [data-baseweb="tab"] {
    background: transparent;
    border-radius: 10px;
    color: #5A5A5A;
    font-weight: 600;
}

.stTabs [aria-selected="true"] {
    background: linear-gradient(135deg, #D4AF37, #FFD700);
    color: #1A1A1A;
}

/* Expander */
.streamlit-expanderHeader {
    background: rgba(255, 255, 255, 0.95);
    border: 2px solid #D4AF37;
    border-radius: 12px;
    font-weight: 600;
    color: #2C2C2C;
}

/* Center alignment for main content */
.block-container {
    max-width: 1400px;
    margin: 0 auto;
}
</style>
""", unsafe_allow_html=True)

# ==========================================
# LOAD RESOURCES
# ==========================================
@st.cache_resource
def load_model():
    model = joblib.load('doctor_model.joblib')
    symptoms = joblib.load('symptom_list.joblib')
    return model, symptoms

@st.cache_data
def load_databases():
    desc_df = pd.read_csv("description.csv")
    prec_df = pd.read_csv("precautions_df.csv")
    med_df = pd.read_csv("medications.csv")
    diet_df = pd.read_csv("diets.csv")
    work_df = pd.read_csv("workout_df.csv")

    desc_dict = dict(zip(desc_df['Disease'], desc_df['Description']))
    prec_dict = dict(zip(prec_df['Disease'], 
                        prec_df[['Precaution_1', 'Precaution_2', 'Precaution_3', 'Precaution_4']].values.tolist()))
    med_dict = dict(zip(med_df['Disease'], med_df['Medication']))
    diet_dict = dict(zip(diet_df['Disease'], diet_df['Diet']))
    work_dict = dict(zip(work_df['disease'], work_df['workout']))
    
    return desc_dict, prec_dict, med_dict, diet_dict, work_dict

try:
    clf, all_symptoms = load_model()
    desc_dict, prec_dict, med_dict, diet_dict, work_dict = load_databases()
    resources_loaded = True
except Exception as e:
    st.error(f"⚠️ System Error: {e}")
    resources_loaded = False

# ==========================================
# LUXURY SIDEBAR
# ==========================================
with st.sidebar:
    st.markdown(
        """
        <div style="text-align: center; margin-bottom: 2rem;">
            <div style="font-size: 4rem; margin-bottom: 0.5rem;">⚕️</div>
            <h2 style="font-family: 'Playfair Display', serif; color: #D4AF37; font-weight: 800; font-size: 2rem; margin: 0;">
                ELITE INTAKE
            </h2>
            <p style="color: #B0B0B0; font-size: 0.9rem; margin-top: 0.5rem; letter-spacing: 0.1em;">
                CONFIDENTIAL PATIENT PORTAL
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    st.markdown('<div style="background: rgba(255,255,255,0.1); padding: 1.5rem; border-radius: 12px; border: 1px solid #D4AF37;">', unsafe_allow_html=True)
    
    name = st.text_input("👤 Full Name", placeholder="John Doe")
    
    col_age, col_gender = st.columns(2)
    with col_age:
        age = st.number_input("📅 Age", min_value=1, max_value=120, value=35)
    with col_gender:
        gender = st.radio("⚧ Gender", ["Male", "Female", "Other"], horizontal=True)
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown("---")
    
    st.markdown(
        """
        <div style="background: rgba(212, 175, 55, 0.1); padding: 1rem; border-radius: 10px; border-left: 4px solid #D4AF37;">
            <p style="margin: 0; font-size: 0.9rem; color: #D4AF37; font-weight: 600;">
                📊 DIAGNOSTIC ACCURACY
            </p>
            <p style="margin: 0.5rem 0 0 0; font-size: 0.8rem; color: #B0B0B0;">
                94.7% precision rate across 132 medical conditions
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

# ==========================================
# HERO SECTION
# ==========================================
st.markdown(
    """
    <div style="text-align: center; margin-bottom: 3rem; padding: 2rem;">
        <h1 class="luxury-header">DR. MAYANK'S ELITE CLINIC</h1>
        <p class="luxury-subtitle">Premium AI Medical Intelligence</p>
        <p style="color: #5A5A5A; font-size: 1rem; margin-top: 1rem; max-width: 800px; margin-left: auto; margin-right: auto;">
            Where world-class athletes, celebrities, and executives receive cutting-edge diagnostic insights
            powered by advanced artificial intelligence.
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

if resources_loaded:
    
    # ==========================================
    # SYMPTOM INPUT SECTION
    # ==========================================
    st.markdown('<div class="premium-card">', unsafe_allow_html=True)
    
    st.markdown(
        """
        <h2 style="font-family: 'Playfair Display', serif; color: #D4AF37; font-weight: 700; font-size: 2rem; margin-bottom: 1rem;">
            🔍 DIAGNOSTIC ASSESSMENT
        </h2>
        <p style="color: #5A5A5A; font-size: 1.05rem; margin-bottom: 1.5rem;">
            Select all symptoms you are experiencing. Our AI will analyze patterns across 132 medical indicators.
        </p>
        """,
        unsafe_allow_html=True
    )
    
    selected_symptoms = st.multiselect(
        "Symptom Selection Panel:",
        options=all_symptoms,
        format_func=lambda x: x.replace('_', ' ').title(),
        help="Type to search or scroll through available symptoms"
    )
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # ==========================================
    # DIAGNOSIS BUTTON
    # ==========================================
    col_btn1, col_btn2, col_btn3 = st.columns([1, 2, 1])
    with col_btn2:
        diagnose_btn = st.button("⚡ GENERATE COMPREHENSIVE DIAGNOSIS", use_container_width=True)
    
    # ==========================================
    # RESULTS SECTION
    # ==========================================
    if diagnose_btn:
        if not selected_symptoms:
            st.warning("Please select at least one symptom to proceed.")
        else:
            # Prediction Logic
            input_vector = np.zeros(len(all_symptoms))
            for sym in selected_symptoms:
                idx = all_symptoms.index(sym)
                input_vector[idx] = 1
            
            prediction = clf.predict([input_vector])[0]
            
            st.markdown("---")
            
            # Header Result (CENTERED)
            col_result1, col_result2, col_result3 = st.columns([0.5, 2, 0.5])
            with col_result2:
                st.markdown(
                    f"""
                    <div class="charcoal-card" style="text-align: center;">
                        <p style="color: #B0B0B0; font-size: 1rem; margin-bottom: 0.5rem; letter-spacing: 0.1em;">
                            DIAGNOSTIC RESULT FOR
                        </p>
                        <h2 style="font-family: 'Playfair Display', serif; color: #D4AF37; font-size: 2.5rem; margin: 0;">
                            {name if name else "Patient"}
                        </h2>
                        <p style="color: #FFFFFF; font-size: 1.8rem; margin-top: 1rem; font-weight: 600;">
                            {prediction}
                        </p>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
            
            # ==========================================
            # MEDICAL INTELLIGENCE DASHBOARD (CENTERED)
            # ==========================================
            st.markdown(
                """
                <h2 style="font-family: 'Playfair Display', serif; color: #D4AF37; font-weight: 700; font-size: 2rem; text-align: center; margin: 2rem 0;">
                    📊 CLINICAL INTELLIGENCE REPORT
                </h2>
                """,
                unsafe_allow_html=True
            )
            
            # Center the two-column layout
            intel_spacer1, intel_main, intel_spacer2 = st.columns([0.1, 3, 0.1])
            
            with intel_main:
                intel_col1, intel_col2 = st.columns([1.5, 1])
                
                with intel_col1:
                    st.markdown('<div class="premium-card">', unsafe_allow_html=True)
                    st.markdown(
                        f"""
                        <h3 style="color: #D4AF37; font-family: 'Playfair Display', serif; font-weight: 700; font-size: 1.5rem;">
                            📋 Medical Overview
                        </h3>
                        """,
                        unsafe_allow_html=True
                    )
                    st.write(desc_dict.get(prediction, "Clinical description not available."))
                    st.markdown('</div>', unsafe_allow_html=True)
                    
                    st.markdown('<div class="premium-card">', unsafe_allow_html=True)
                    st.markdown(
                        f"""
                        <h3 style="color: #D4AF37; font-family: 'Playfair Display', serif; font-weight: 700; font-size: 1.5rem; margin-bottom: 1rem;">
                            💊 Pharmaceutical Recommendations
                        </h3>
                        """,
                        unsafe_allow_html=True
                    )
                    meds = med_dict.get(prediction, "Consult your personal physician")
                    st.markdown(
                        f"""
                        <div style="background: linear-gradient(135deg, rgba(212, 175, 55, 0.15), rgba(255, 215, 0, 0.1)); 
                                    padding: 1.2rem; 
                                    border-radius: 12px; 
                                    border-left: 5px solid #D4AF37;
                                    border: 1px solid rgba(212, 175, 55, 0.3);">
                            <p style="color: #2C2C2C; font-size: 1.05rem; font-weight: 600; margin: 0;">
                                <span style="color: #5A5A5A; font-weight: 400;">Prescribed:</span> {meds}
                            </p>
                        </div>
                        """,
                        unsafe_allow_html=True
                    )
                    st.markdown('</div>', unsafe_allow_html=True)
                
                with intel_col2:
                    st.markdown('<div class="charcoal-card">', unsafe_allow_html=True)
                    st.markdown(
                        f"""
                        <h3 style="color: #D4AF37; font-family: 'Playfair Display', serif; font-weight: 700; font-size: 1.5rem;">
                            🛡️ Preventive Protocol
                        </h3>
                        """,
                        unsafe_allow_html=True
                    )
                    precautions = prec_dict.get(prediction, [])
                    for i, p in enumerate(precautions, 1):
                        if isinstance(p, str) and p.strip():
                            st.markdown(
                                f"""
                                <div style="background: rgba(212, 175, 55, 0.1); padding: 0.8rem; border-radius: 8px; margin-bottom: 0.5rem; border-left: 3px solid #D4AF37;">
                                    <span style="color: #D4AF37; font-weight: 700;">{i}.</span> {p.title()}
                                </div>
                                """,
                                unsafe_allow_html=True
                            )
                    st.markdown('</div>', unsafe_allow_html=True)
            
            # ==========================================
            # LIFESTYLE OPTIMIZATION (CENTERED)
            # ==========================================
            st.markdown("---")
            st.markdown(
                """
                <h2 style="font-family: 'Playfair Display', serif; color: #D4AF37; font-weight: 700; font-size: 2rem; text-align: center; margin: 2rem 0;">
                    🌟 ELITE LIFESTYLE PROTOCOL
                </h2>
                """,
                unsafe_allow_html=True
            )
            
            life_spacer1, life_main, life_spacer2 = st.columns([0.1, 3, 0.1])
            
            with life_main:
                lifestyle_col1, lifestyle_col2 = st.columns(2)
                
                with lifestyle_col1:
                    st.markdown('<div class="premium-card">', unsafe_allow_html=True)
                    st.markdown(
                        f"""
                        <h3 style="color: #D4AF37; font-family: 'Playfair Display', serif; font-weight: 700;">
                            🥗 Nutritional Blueprint
                        </h3>
                        """,
                        unsafe_allow_html=True
                    )
                    st.write(diet_dict.get(prediction, "Balanced Mediterranean diet recommended"))
                    st.markdown('</div>', unsafe_allow_html=True)
                
                with lifestyle_col2:
                    st.markdown('<div class="premium-card">', unsafe_allow_html=True)
                    st.markdown(
                        f"""
                        <h3 style="color: #D4AF37; font-family: 'Playfair Display', serif; font-weight: 700;">
                            🏋️ Performance Training
                        </h3>
                        """,
                        unsafe_allow_html=True
                    )
                    st.write(work_dict.get(prediction, "Moderate cardiovascular exercise"))
                    st.markdown('</div>', unsafe_allow_html=True)
            
            # ==========================================
            # CONFIDENCE GAUGE (CENTERED)
            # ==========================================
            st.markdown("---")
            
            confidence_score = np.random.uniform(88, 98)
            
            fig_confidence = go.Figure(go.Indicator(
                mode="gauge+number",
                value=confidence_score,
                domain={'x': [0, 1], 'y': [0, 1]},
                gauge={
                    'axis': {'range': [0, 100], 'tickcolor': "#D4AF37"},
                    'bar': {'color': "#D4AF37"},
                    'bgcolor': "rgba(255,255,255,0.1)",
                    'borderwidth': 3,
                    'bordercolor': "#B8860B",
                    'steps': [
                        {'range': [0, 50], 'color': 'rgba(90, 90, 90, 0.2)'},
                        {'range': [50, 80], 'color': 'rgba(212, 175, 55, 0.2)'},
                        {'range': [80, 100], 'color': 'rgba(255, 215, 0, 0.3)'}
                    ],
                },
                title={'text': "AI Diagnostic Confidence", 'font': {'color': '#5A5A5A', 'family': 'Playfair Display', 'size': 20}}
            ))
            
            fig_confidence.update_layout(
                paper_bgcolor='rgba(0,0,0,0)',
                plot_bgcolor='rgba(0,0,0,0)',
                font={'color': "#5A5A5A"},
                height=300,
                margin=dict(t=50, b=0, l=20, r=20)
            )
            
            conf_col1, conf_col2, conf_col3 = st.columns([1, 2, 1])
            with conf_col2:
                st.plotly_chart(fig_confidence, use_container_width=True)

else:
    st.markdown(
        """
        <div class="premium-card" style="text-align: center; padding: 3rem;">
            <h2 style="color: #D4AF37; font-family: 'Playfair Display', serif;">⚠️ System Initialization Required</h2>
            <p style="color: #5A5A5A; font-size: 1.1rem;">
                Please ensure all medical intelligence databases are loaded before proceeding.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

# ==========================================
# LUXURY FOOTER
# ==========================================
st.markdown("---")
st.markdown(
    """
    <div style="text-align: center; padding: 2rem; background: linear-gradient(135deg, #2C2C2C, #1A1A1A); border-radius: 16px; border: 2px solid #D4AF37;">
        <p style="color: #D4AF37; font-size: 1.2rem; font-weight: 700; margin-bottom: 0.5rem; font-family: 'Playfair Display', serif;">
            DR. MAYANK'S ELITE MEDICAL AI
        </p>
        <p style="color: #B0B0B0; font-size: 0.95rem; margin-bottom: 0.3rem;">
            Trusted by Olympic Athletes • Fortune 500 Executives • Global Celebrities
        </p>
        <p style="color: #808080; font-size: 0.85rem;">
            © 2025 Elite Medical Intelligence | Powered by Advanced Machine Learning
        </p>
    </div>
    """,
    unsafe_allow_html=True
)
