import streamlit as st

# ---------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------
st.set_page_config(
    page_title="Data Visualization & Storytelling Academy",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------------------------------------------
# SESSION STATE INITIALIZATION
# ---------------------------------------------------
if "score" not in st.session_state:
    st.session_state.score = 0

if "badges" not in st.session_state:
    st.session_state.badges = []

if "quiz_answers" not in st.session_state:
    st.session_state.quiz_answers = {}

# ---------------------------------------------------
# CUSTOM CSS
# ---------------------------------------------------
st.markdown("""
<style>
.main {
    padding-top: 1rem;
}

.block-container {
    padding-top: 2rem;
}

.stMetric {
    background-color: #111827;
    padding: 10px;
    border-radius: 10px;
}

.hero-title {
    font-size: 3rem;
    font-weight: 800;
    color: #2563EB;
}

.hero-subtitle {
    font-size: 1.2rem;
    color: #6B7280;
    margin-bottom: 2rem;
}

.section-card {
    padding: 1rem;
    border-radius: 15px;
    background-color: #F9FAFB;
    border: 1px solid #E5E7EB;
    margin-bottom: 1rem;
}
</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# SIDEBAR
# ---------------------------------------------------
st.sidebar.title("Navigation")

page = st.sidebar.radio(
    "Go to Module",
    [
        "Home",
        "Cognitive Science of Visualization",
        "Chart Selection Engine",
        "Visualization Crimes",
        "Storytelling with Data",
        "Dashboard Sandbox",
        "Chart Crimes Quiz",
        "Custom Dataset Lab",
        "About the Academy"
    ]
)

# ---------------------------------------------------
# SIDEBAR GAMIFICATION PANEL
# ---------------------------------------------------
st.sidebar.markdown("---")
st.sidebar.subheader("🏆 Gamification")

st.sidebar.metric("Score", st.session_state.score)
st.sidebar.write("Badges Earned:")

if st.session_state.badges:
    for badge in st.session_state.badges:
        st.sidebar.success(badge)
else:
    st.sidebar.info("No badges yet!")


# ---------------------------------------------------
# HOME PAGE
# ---------------------------------------------------
if page == "Home":

    st.markdown(
        """
        <div class="hero-title">
        Kantvisualize Academy: Master Data Visualization & Storytelling
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="hero-subtitle">
        Learn how to think visually, choose the right charts, 
        avoid visualization mistakes, and tell powerful stories with data.
        </div>
        """,
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.info("""
        ### Learn Visual Thinking
        
        Understand:
        - Human perception
        - Cognitive science
        - Data storytelling
        - Design psychology
        """)

    with col2:
        st.success("""
        ### Build Interactive Charts
        
        Practice with:
        - Plotly
        - Altair
        - Dynamic dashboards
        - Real datasets
        """)

    with col3:
        st.warning("""
        ### Gamified Learning
        
        Earn:
        - Points
        - Badges
        - Quiz rewards
        - Storytelling mastery
        """)

    st.markdown("---")

    st.subheader("What You'll Learn")

    tabs = st.tabs([
        "Visualization Science",
        "Chart Selection",
        "Storytelling",
        "Dashboarding",
        "Analytics Careers"
    ])

    with tabs[0]:
        st.write("""
        Learn how the brain processes visuals using:
        - Pre-attentive attributes
        - Data-ink ratio
        - Visual hierarchy
        - Grammar of graphics
        """)

    with tabs[1]:
        st.write("""
        Discover how to choose the right chart for:
        - Comparison
        - Trends
        - Relationships
        - Composition
        - Distribution
        """)

    with tabs[2]:
        st.write("""
        Learn how to transform charts into compelling narratives:
        - Hooks
        - Context
        - Conflict
        - Resolution
        """)

    with tabs[3]:
        st.write("""
        Build interactive dashboards like professionals using:
        - Filters
        - Dynamic visuals
        - KPIs
        - Drilldowns
        """)

    with tabs[4]:
        st.write("""
        Connect your skills to industry tools:
        - Tableau
        - Power BI
        - Looker Studio
        - Business Intelligence roles
        """)

   
# ---------------------------------------------------
# MODULE ROUTING
# ---------------------------------------------------
elif page == "Cognitive Science of Visualization":
    from modules.cognitive_science import run
    run()

elif page == "Chart Selection Engine":
    from modules.chart_selection import run
    run()

elif page == "Visualization Crimes":
    from modules.visualization_crimes import run
    run()

elif page == "Storytelling with Data":
    from modules.storytelling_data import run
    run()

elif page == "Dashboard Sandbox":
    from modules.dashboard_sandbox import run
    run()

elif page == "Chart Crimes Quiz":
    from modules.chart_crimes_quiz import run
    run()

elif page == "Custom Dataset Lab":
    from modules.custom_dataset_lab import run
    run()

elif page == "About the Academy":
    from modules.about import run
    run()