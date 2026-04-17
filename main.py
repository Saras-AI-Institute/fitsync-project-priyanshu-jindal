import streamlit as st
from modules.processor import load_data, calculate_recovery_score

# Load and process data
df = load_data()
df = calculate_recovery_score(df)

# Set page configuration
st.set_page_config(layout="wide", page_title="FitSync", page_icon="⚡")

# Define a function to get the latest metric data
def get_latest_metrics(df):
    latest_data = df.iloc[-1]
    calories = latest_data.get('Calories_Burned', 0)
    steps = latest_data.get('Steps', 0)
    water_intake = latest_data.get('Water_Intake_Liters', 0)
    sleep = latest_data.get('Sleep_Hours', 0)
    recovery_score = latest_data.get('Recovery_Score', 0)
    return calories, steps, water_intake, sleep, recovery_score

# Extract real data
calories, steps, water_intake, sleep, recovery_score = get_latest_metrics(df)

# Inject enhanced CSS for an appealing UI
st.markdown(
    """
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Syne:wght@600&family=DM+Sans&display=swap');
        body {
            background-color: #0e153a;
            color: #ffffff;
            font-family: 'DM Sans', sans-serif;
        }
        h1, h2, h3, h4 {
            font-family: 'Syne', sans-serif;
            color: #00d4ff;
            margin-bottom: 0;
        }
        .headline-gradient {
            font-size: 3.7rem;
            background: linear-gradient(120deg, #00f5a0, #00d4ff);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin: 25px 0 20px;
            text-align: center;
        }
        .pill-badge {
            display: inline-block;
            padding: 12px 30px;
            border-radius: 25px;
            background-color: #00f5a0;
            color: #0e153a;
            margin: 20px auto;
            font-size: 1.1rem;
            font-weight: bold;
            display: block;
        }
        .metric-card {
            border-radius: 12px;
            padding: 25px;
            background-color: #1f2440;
            color: #ffffff;
            text-align: center;
            box-shadow: 0 6px 18px rgba(0,0,0,0.2);
            margin: 15px 0;
            transition: transform 0.2s, box-shadow 0.2s;
        }
        .metric-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 10px 20px rgba(0,0,0,0.3);
        }
        .metric-card h3 {
            margin: 15px 0 10px;
            color: #29abe2;
        }
        .metric-card .value {
            font-size: 2.7rem;
            font-weight: bold;
        }
        .metric-card .label {
            text-transform: uppercase;
            font-size: 0.9rem;
            color: #cccccc;
        }
        .pro-tip {
            background-color: #1b1b33;
            padding: 15px;
            border-radius: 10px;
            display: flex;
            align-items: center;
            box-shadow: 0 3px 12px rgba(0,0,0,0.25);
            margin-top: 45px;
        }
        .pro-tip-icon {
            margin-right: 12px;
            font-size: 1.8rem;
            color: #00f5a0;
        }
        .css-1v3fvcr { display: none; }
        footer { display: none; }
        header { display: none; }
        .sidebar-arrow {
            animation: bounce 2s infinite;
            margin: 25px 0;
            color: #00f5a0;
            font-size: 2rem;
            text-align: center;
        }
        @keyframes bounce {
            0%, 20%, 50%, 80%, 100% { transform: translateY(0); }
            40% { transform: translateY(-12px); }
            60% { transform: translateY(-6px); }
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Hero Section
st.markdown('<div class="pill-badge">Premium Fitness Tracker</div>', unsafe_allow_html=True)
st.markdown('<h1 class="headline-gradient">Welcome to FitSync</h1>', unsafe_allow_html=True)
st.markdown("""<p style='text-align: center; font-size: 1.1rem;'>Your ultimate personal health analytics dashboard for tracking workouts, nutrition, sleep, and vitals.</p>""", unsafe_allow_html=True)
st.markdown('<div class="sidebar-arrow">⬇️ Open the sidebar to navigate</div>', unsafe_allow_html=True)

st.markdown("<hr style='border-color: #4a4a75; background: linear-gradient(90deg, #00f5a0, #00d4ff);'>", unsafe_allow_html=True)

# Today's Snapshot
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.markdown(f"""
    <div class="metric-card">
        <div class="label">Calories Burned</div>
        <div class="value">{calories}</div>
        <div>🔥 Good job!</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="metric-card">
        <div class="label">Steps Today</div>
        <div class="value">{steps}</div>
        <div>🏃‍♂️ Keep it up!</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
    <div class="metric-card">
        <div class="label">Hydration</div>
        <div class="value">{water_intake}L</div>
        <div>💧 Stay hydrated!</div>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown(f"""
    <div class="metric-card">
        <div class="label">Sleep Last Night</div>
        <div class="value">{sleep}h</div>
        <div>🛌 {recovery_score}% recovery</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<hr style='border-color: #4a4a75; background: linear-gradient(90deg, #00f5a0, #00d4ff);'>", unsafe_allow_html=True)

# Feature Grid
cols = st.columns(3)
features = [
    ("Workouts", "Track your workouts, set goals, and measure progress.", "🏋️‍♂️"),
    ("Nutrition", "Log your meals and plan healthier dietary choices.", "🥗"),
    ("Sleep Quality", "Monitor your sleep patterns for better health.", "🛌"),
    ("Vitals & Health", "Keep tabs on your health with vital signs.", "❤️"),
    ("Progress Charts", "Visualize your progress with dynamic charts.", "📈"),
    ("Goals & Streaks", "Set health goals and build streaks for motivation.", "🎯"),
]

for i, feature in enumerate(features):
    with cols[i % 3]:
        st.markdown(f"""
        <div class="metric-card">
            <div class="label">{feature[0]}</div>
            <div class="value">{feature[2]}</div>
            <div>{feature[1]}</div>
        </div>
        """, unsafe_allow_html=True)

st.markdown("<hr style='border-color: #4a4a75; background: linear-gradient(90deg, #00f5a0, #00d4ff);'>", unsafe_allow_html=True)

# Pro Tip Bar
st.markdown("""
<div class="pro-tip">
    <div class="pro-tip-icon">💡</div>
    <div>Pro Tip: Connect your wearable devices to seamlessly integrate health data into FitSync.</div>
</div>
""", unsafe_allow_html=True)