import streamlit as st

st.set_page_config(
    page_title="AI-Driven Medical Intelligence Hub",
    page_icon="🩺",
    layout="wide"
)

# Custom CSS for Styling
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap');

        body {
            font-family: 'Poppins', sans-serif;
            background-color: #f0f4f8;
            color: #333333;
        }

        /* Main Title */
        .title {
            font-size: 50px;
            font-weight: 600;
            color: #1e90ff;
            text-align: center;
            margin-bottom: 10px;
            text-shadow: 0px 0px 10px rgba(30, 144, 255, 0.5);
        }

        /* Subtitle */
        .subtitle {
            font-size: 24px;
            color: #bdbdbd;
            text-align: center;
            font-weight: 300;
            margin-bottom: 40px;
        }

        /* Sections */
        .section {
            background: #ffffff;
            padding: 25px;
            border-radius: 15px;
            box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.1);
            margin-bottom: 20px;
            transition: all 0.3s ease-in-out;
        }

        .section:hover {
            transform: translateY(-5px);
            box-shadow: 0px 6px 16px rgba(0, 0, 0, 0.2);
        }

        /* Sidebar */
        .sidebar-text {
            font-size: 18px;
            color: #333333;
            text-align: center;
            margin-bottom: 20px;
        }

        /* Contact Section */
        .contact {
            text-align: left;
            font-size: 20px;
            color: #333333;
            margin-top: 40px;
        }

        .contact a {
            color: #1e90ff;
            text-decoration: none;
        }

        /* Profile Links */
        .profile-links {
            text-align: center;
            margin-top: 20px;
        }

        .profile-links a {
            font-size: 18px;
            color: #1e40af;
            text-decoration: none;
            margin: 0 15px;
            font-weight: 600;
        }

    </style>
""", unsafe_allow_html=True)

# Sidebar Navigation
st.sidebar.markdown("<h2 style='color: #000000;'>📌 Navigation</h2>", unsafe_allow_html=True)
st.sidebar.markdown("<p class='sidebar-text' style='color: #000000;'>Use the sidebar to explore different features of the AI Healthcare Network.</p>", unsafe_allow_html=True)
st.sidebar.image("utils/ph3.png", use_container_width=True)

# Main Content
st.markdown("<div class='title'>🩺 AI-Driven Medical Intelligence Hub</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Transforming Healthcare with AI-driven Predictions & Insights</div>", unsafe_allow_html=True)

st.image("utils/ph1.jpg", use_container_width=True)

# Features Section
st.markdown("<h2 style='text-align: center; color: #000000;'>✨ Features</h2>", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class='section'>
        <h3 style='color: #000000;'>💡 Disease Prediction</h3>
        <p style='color: #000000;'>Analyze symptoms and predict possible diseases using advanced AI models.</p>
    </div>

    <div class='section'>
        <h3 style='color: #000000;'>💊 Drug Recommendation</h3>
        <p style='color: #000000;'>Get AI-powered medication suggestions based on medical history and diagnosis.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class='section'>
        <h3 style='color: #000000;'>❤️ Heart Disease Risk Assessment</h3>
        <p style='color: #000000;'>Assess your heart health and receive AI-powered risk analysis.</p>
    </div>

    <div class='section'>
        <h3 style='color: #000000;'>🤖 LLM Chatbot</h3>
        <p style='color: #000000;'>Chat with an AI-powered assistant to get health insights and recommendations.</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# Technologies Used
st.markdown("<h2 style='text-align: center; color: #000000;'>⚙️ Technologies Used</h2>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class='section'>
        <h3>🤖 Machine Learning</h3>
        <p>Utilizing RandomForest, XGBoost, and Deep Learning models.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class='section'>
        <h3>🗂 NLP & AI</h3>
        <p>Leveraging Natural Language Processing for chatbot interactions(RAG).</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class='section'>
        <h3>☁️ Cloud Computing</h3>
        <p>Deployed using Streamlit Cloud.</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# Why Use This App? (Separate Block)
st.markdown("""
    <div class='section'>
        <h2 style='text-align: center; color: #000000;'>🔍 Why Use This App?</h2>
        <p>
            ✅ <b>Accurate Predictions:</b> Our AI models are trained on vast healthcare datasets.<br>
            ✅ <b>Real-Time Assistance:</b> Get quick insights and recommendations.<br>
            ✅ <b>User-Friendly Interface:</b> Designed for both professionals and individuals.<br>
            ✅ <b>Secure & Reliable:</b> Your health data is protected with top-tier security.<br>
        </p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# Contact Us (Left Aligned)
st.markdown("""
    <div class='contact'>
        <h2>📬 Contact Us</h2>
        <p>Have questions or need support? Reach out to us at:</p>
        📧 <a href="mailto:sistlasree24@gmail.com">sistlasree24@gmail.com</a>
    </div>
    """, unsafe_allow_html=True)

# Profile Links (Centered)
st.markdown("""
    <div class='profile-links'>
        <h2>🌐 Connect With Me</h2>
        <a href="https://github.com/coolguy-sree" target="_blank">GitHub</a> |
        <a href="https://www.linkedin.com/in/iamsuryasarojsistla24/" target="_blank">LinkedIn</a> |
        <a href="https://tiny-zabaione-53c22a.netlify.app/" target="_blank">Portfolio</a>
    </div>
    """, unsafe_allow_html=True)
