import streamlit as st
import pandas as pd

from agriculture_agent import (
    recommend_crop,
    analyze_market,
    weather_risk,
    irrigation_advice,
    fertilizer_advice,
    disease_advice,
    scheme_finder,
    demand_analysis,
    regional_risk,
    officer_priority
)

st.set_page_config(
    page_title="AgriSense AI",
    page_icon="🌾",
    layout="wide"
)

# ==============================
# GREEN COLOR DESIGN
# ==============================

st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #E8F5E9, #FFFFFF, #F1F8E9);
}

.main .block-container {
    padding-top: 2rem;
    padding-bottom: 3rem;
    max-width: 1450px;
}

h1 {
    color: #1B5E20 !important;
    font-size: 42px !important;
    font-weight: 800 !important;
}

h2 {
    color: #2E7D32 !important;
}

h3 {
    color: #388E3C !important;
}

p {
    color: #263238;
}

section[data-testid="stSidebar"] {
    background: linear-gradient(
        180deg,
        #E8F5E9,
        #F1F8E9,
        #FFFFFF
    );
    border-right: 2px solid #A5D6A7;
}

section[data-testid="stSidebar"] label {
    color: #1B5E20 !important;
    font-weight: 700 !important;
}

.stButton > button {
    width: 100%;
    background: linear-gradient(
        90deg,
        #1B5E20,
        #2E7D32,
        #43A047
    );
    color: white !important;
    border: none;
    border-radius: 10px;
    padding: 12px;
    font-weight: 700;
}

.stButton > button:hover {
    background: #1B5E20;
}

div[data-testid="stMetric"] {
    background: white;
    padding: 20px;
    border-radius: 15px;
    border-left: 6px solid #2E7D32;
    box-shadow: 0 5px 15px rgba(0,0,0,0.08);
}

div[data-testid="stMetricLabel"] {
    color: #546E7A !important;
}

div[data-testid="stMetricValue"] {
    color: #1B5E20 !important;
    font-weight: 800 !important;
}

button[data-baseweb="tab"] {
    color: #2E7D32 !important;
    font-weight: 650 !important;
}

button[data-baseweb="tab"][aria-selected="true"] {
    color: #1B5E20 !important;
    font-weight: 800 !important;
    border-bottom: 4px solid #2E7D32 !important;
}

div[data-testid="stAlert"] {
    border-radius: 12px !important;
}

div[data-testid="stExpander"] {
    border: 1px solid #A5D6A7 !important;
    border-radius: 12px !important;
    background: #FAFFFA !important;
}

hr {
    border: none;
    height: 2px;
    background: linear-gradient(
        90deg,
        #1B5E20,
        #66BB6A,
        transparent
    );
}
</style>
""", unsafe_allow_html=True)


# ==============================
# HEADER
# ==============================

st.title("🌾 AgriSense AI")

st.subheader("Intelligent Agriculture Management Agent")

st.write(
    "AI-powered decision support for crop selection, weather, "
    "markets, irrigation, disease risk, crop demand and agricultural support."
)


# ==============================
# SIDEBAR
# ==============================

st.sidebar.header("🌱 Farm Details")

location = st.sidebar.text_input(
    "Location",
    "Peddapuram"
)

soil = st.sidebar.selectbox(
    "Soil Type",
    [
        "Loamy",
        "Clay",
        "Sandy",
        "Black Soil",
        "Red Soil"
    ]
)

ph = st.sidebar.number_input(
    "Soil pH",
    min_value=4.0,
    max_value=9.0,
    value=6.5
)

crop = st.sidebar.selectbox(
    "Current Crop",
    [
        "Paddy",
        "Groundnut",
        "Maize",
        "Cotton",
        "Chilli"
    ]
)

stage = st.sidebar.selectbox(
    "Growth Stage",
    [
        "Seedling",
        "Vegetative",
        "Flowering",
        "Maturity"
    ]
)

water = st.sidebar.selectbox(
    "Water Availability",
    [
        "Low",
        "Medium",
        "High"
    ]
)


# ==============================
# DASHBOARD METRICS
# ==============================

st.markdown("---")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "📍 Location",
        location
    )

with col2:
    st.metric(
        "🌱 Crop",
        crop
    )

with col3:
    st.metric(
        "🧪 Soil pH",
        ph
    )

with col4:
    st.metric(
        "💧 Water",
        water
    )


# ==============================
# FARM OVERVIEW
# ==============================

st.markdown("### 🌿 Farm Overview")

card1, card2, card3 = st.columns(3)

with card1:
    st.success(
        "🌱 Crop Monitoring\n\n"
        "Current crop and soil conditions are analyzed "
        "for better crop decisions."
    )

with card2:
    st.warning(
        "🌦️ Risk Monitoring\n\n"
        "Weather, disease and regional risks are monitored "
        "for timely action."
    )

with card3:
    st.info(
        "🤖 AI Decision Support\n\n"
        "AI recommendations help farmers and officers "
        "take faster decisions."
    )


# ==============================
# TABS
# ==============================

tabs = st.tabs(
    [
        "🌱 Crop Recommendation",
        "💰 Market",
        "🌦️ Weather",
        "🦠 Disease",
        "💧 Water & Fertilizer",
        "🏛️ Schemes",
        "📈 Demand",
        "🚨 Regional Risk",
        "👨‍🌾 Officer"
    ]
)


# ==============================
# CROP RECOMMENDATION
# ==============================

with tabs[0]:

    st.header("🌱 AI Crop Recommendation")

    st.write(
        "Analyze soil, pH and water availability "
        "to identify a suitable crop."
    )

    if st.button("🤖 Recommend Best Crop"):

        result = recommend_crop(
            soil,
            ph,
            water,
            location
        )

        st.success(
            f"🌾 Recommended Crop: {result['crop']}"
        )

        st.info(
            f"⭐ Suitability Score: "
            f"{result['score']}/100"
        )

        st.write("### 💡 Why this crop?")

        for reason in result["reasons"]:
            st.write("✓", reason)


# ==============================
# MARKET
# ==============================

with tabs[1]:

    st.header("💰 Market Price Analysis")

    market_result = analyze_market(crop)

    df = pd.DataFrame(market_result)

    st.dataframe(
        df,
        use_container_width=True
    )

    best = df.loc[
        df["Price"].idxmax()
    ]

    st.success(
        f"⭐ Best Price: {best['Market']} — "
        f"₹{best['Price']}/quintal"
    )

    st.write("### 📊 Market Price Comparison")

    st.bar_chart(
        df.set_index("Market")["Price"]
    )


# ==============================
# WEATHER
# ==============================

with tabs[2]:

    st.header("🌦️ Weather Risk Analysis")

    st.write(
        "Analyze weather conditions and identify "
        "possible agricultural threats."
    )

    if st.button("🌦️ Analyze Weather Risk"):

        result = weather_risk()

        if result["risk"] == "HIGH":
            st.error("🔴 HIGH WEATHER RISK")

        elif result["risk"] == "MEDIUM":
            st.warning("🟠 MEDIUM WEATHER RISK")

        else:
            st.success("🟢 LOW WEATHER RISK")

        st.write(
            f"**Expected Condition:** "
            f"{result['condition']}"
        )

        st.write("### 🛠️ Recommended Actions")

        for action in result["actions"]:
            st.write("→", action)


# ==============================
# DISEASE
# ==============================

with tabs[3]:

    st.header("🦠 Crop Disease Advisory")

    st.write(
        "Upload a crop image for AI-based disease advisory."
    )

    uploaded_file = st.file_uploader(
        "📷 Upload Crop Image",
        type=["jpg", "jpeg", "png"]
    )

    if uploaded_file:

        st.image(
            uploaded_file,
            caption="Uploaded Crop Image",
            width=400
        )

        if st.button("🔍 Analyze Crop Disease"):

            result = disease_advice(crop)

            st.warning(
                f"⚠️ Possible Problem: "
                f"{result['disease']}"
            )

            st.write(
                f"🎯 Confidence: "
                f"{result['confidence']}%"
            )

            st.write("### 🔎 Symptoms")

            for symptom in result["symptoms"]:
                st.write("•", symptom)

            st.write("### 🛠️ Recommended Actions")

            for action in result["actions"]:
                st.write("→", action)

            st.caption(
                "⚠️ This is an AI advisory and "
                "not a confirmed diagnosis."
            )


# ==============================
# WATER & FERTILIZER
# ==============================

with tabs[4]:

    st.header("💧 Irrigation & Fertilizer")

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("💧 Irrigation")

        result = irrigation_advice(
            crop,
            stage,
            water
        )

        st.info(result)

    with col2:

        st.subheader("🌱 Fertilizer")

        result = fertilizer_advice(
            crop,
            stage,
            soil
        )

        st.info(result)


# ==============================
# GOVERNMENT SCHEMES
# ==============================

with tabs[5]:

    st.header("🏛️ Government Scheme Finder")

    st.write(
        "Find agricultural schemes and support "
        "available for farmers."
    )

    if st.button("🏛️ Find Relevant Schemes"):

        schemes = scheme_finder()

        for scheme in schemes:

            with st.expander(
                scheme["name"]
            ):

                st.write(
                    "**Benefit:**",
                    scheme["benefit"]
                )

                st.write(
                    "**Eligibility:**",
                    scheme["eligibility"]
                )

                st.write(
                    "**Support:**",
                    scheme["support"]
                )

                st.write(
                    "**Action:**",
                    scheme["action"]
                )


# ==============================
# DEMAND ANALYSIS
# ==============================

with tabs[6]:

    st.header("📈 Crop Demand Analysis")

    st.write(
        "Identify crops with higher market demand."
    )

    demand = demand_analysis()

    df = pd.DataFrame(demand)

    st.dataframe(
        df,
        use_container_width=True
    )

    st.write("### 📊 Demand Score")

    st.bar_chart(
        df.set_index("Crop")["Demand Score"]
    )

    best_crop = df.loc[
        df["Demand Score"].idxmax()
    ]

    st.success(
        f"🔥 Highest Demand: "
        f"{best_crop['Crop']}"
    )


# ==============================
# REGIONAL RISK
# ==============================

with tabs[7]:

    st.header("🚨 Regional Agriculture Risk")

    st.write(
        "Identify villages requiring immediate "
        "agricultural attention."
    )

    df = regional_risk()

    st.dataframe(
        df,
        use_container_width=True
    )

    urgent = df[
        df["Priority"] == "URGENT"
    ]

    st.error(
        f"🔴 {len(urgent)} villages "
        "require urgent attention."
    )


# ==============================
# AGRICULTURE OFFICER
# ==============================

with tabs[8]:

    st.header(
        "👨‍🌾 Agriculture Officer Decision Support"
    )

    st.write(
        "Prioritize villages and coordinate "
        "field-level agricultural support."
    )

    result = officer_priority()

    st.write("### 🚨 Immediate Support Required")

    for item in result:

        if item["priority"] == "URGENT":

            st.error(
                f"🔴 {item['village']} — "
                f"{item['reason']}"
            )

        else:

            st.warning(
                f"🟠 {item['village']} — "
                f"{item['reason']}"
            )

    st.write("### 🛠️ Recommended Officer Actions")

    st.write("✓ Conduct field inspection")
    st.write("✓ Contact affected farmers")
    st.write("✓ Monitor pest conditions")
    st.write("✓ Check irrigation availability")
    st.write("✓ Issue weather advisory")


# ==============================
# FOOTER
# ==============================

st.markdown("---")

st.caption(
    "🌾 AgriSense AI | Intelligent Agriculture Management Agent"
)