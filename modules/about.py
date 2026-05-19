import streamlit as st


def run():

    st.title("About Kantvisualize Academy")

    st.markdown("""
    # Data Visualization & Storytelling Academy

    Welcome to **Kantvisualize Academy** — an interactive learning platform
    designed to teach students how to think visually with data.

    This project goes beyond learning chart syntax.

    It focuses on:
    - Visualization psychology
    - Data storytelling
    - Dashboard thinking
    - Analytical communication
    - Ethical visualization design
    """)

    st.markdown("---")

    # =========================================================
    # PROJECT MISSION
    # =========================================================

    st.header("Project Mission")

    st.write("""
    Most people learn visualization tools by memorizing chart types.

    Real analysts do something different.

    They learn:
    - how humans perceive visuals
    - how charts influence decisions
    - how to communicate insights clearly
    - how to avoid misleading dashboards

    This academy was built to teach those real-world skills.
    """)

    # =========================================================
    # WHAT USERS LEARN
    # =========================================================

    st.markdown("---")
    st.header("What You Learn")

    learn_col1, learn_col2 = st.columns(2)

    with learn_col1:

        st.success("""
        ### Visualization Foundations
        
        - Grammar of Graphics
        - Cognitive Science
        - Pre-attentive Processing
        - Data-Ink Ratio
        """)

        st.info("""
        ### Dashboard Design
        
        - KPI Thinking
        - Layout Design
        - Chart Selection
        - Interactive Filtering
        """)

    with learn_col2:

        st.warning("""
        ### Storytelling
        
        - Narrative Building
        - Analytical Framing
        - Business Communication
        - Insight Presentation
        """)

        st.error("""
        ### Visualization Ethics
        
        - Detecting Misleading Charts
        - Avoiding Distortion
        - Reducing Clutter
        - Honest Communication
        """)

    # =========================================================
    # MODULE OVERVIEW
    # =========================================================

    st.markdown("---")
    st.header("Platform Modules")

    modules = [

        (
            "1.Cognitive Science of Visualization",
            "Learn how the brain interprets charts."
        ),

        (
            "2.Chart Selection Engine",
            "Choose the right chart for the right problem."
        ),

        (
            "3.Visualization Crimes",
            "Identify misleading or poor visualizations."
        ),

        (
            "4.Storytelling With Data",
            "Turn raw numbers into meaningful narratives."
        ),

        (
            "5.Dashboard Sandbox",
            "Build interactive dashboards dynamically."
        ),

        (
            "6.Chart Crimes Quiz",
            "Test visualization literacy through gamification."
        ),

        (
            "7.Custom Dataset Lab",
            "Analyze and visualize your own uploaded datasets."
        )
    ]

    for title, desc in modules:

        with st.expander(title):

            st.write(desc)

    # =========================================================
    # TECHNOLOGIES USED
    # =========================================================

    st.markdown("---")
    st.header("Technologies Used")

    tech1, tech2, tech3 = st.columns(3)

    with tech1:

        st.info("""
        ### Frontend
        
        - Streamlit
        - Plotly
        - Altair
        """)

    with tech2:

        st.success("""
        ### Data Handling
        
        - Pandas
        - NumPy
        - OpenPyXL
        """)

    with tech3:

        st.warning("""
        ### Concepts
        
        - Data Storytelling
        - Visualization Psychology
        - Dashboard Design
        """)

    # =========================================================
    # CAREER CONNECTION
    # =========================================================

    st.markdown("---")
    st.header("Career Relevance")

    st.write("""
    These skills are used in real industry roles such as:
    """)

    career_col1, career_col2, career_col3 = st.columns(3)

    with career_col1:

        st.success("""
        ### Data Roles
        
        - Data Analyst
        - BI Analyst
        - Product Analyst
        """)

    with career_col2:

        st.info("""
        ### Visualization Roles
        
        - Tableau Developer
        - Power BI Developer
        - Dashboard Engineer
        """)

    with career_col3:

        st.warning("""
        ### Strategic Roles
        
        - Business Consultant
        - Decision Scientist
        - Data Storyteller
        """)

    # =========================================================
    # LEARNING PHILOSOPHY
    # =========================================================

    st.markdown("---")
    st.header("Learning Philosophy")

    st.write("""
    This platform is designed around:

    ### Learn by Doing

    Instead of only reading theory, users:
    - interact with visualizations
    - manipulate charts
    - detect visualization mistakes
    - build dashboards
    - explore real datasets

    This creates deeper understanding and practical intuition.
    """)

    # =========================================================
    # GAMIFICATION
    # =========================================================

    st.markdown("---")
    st.header("Gamification System")

    st.write("""
    The academy includes:
    - XP scoring
    - Achievement badges
    - Quiz systems
    - Practice challenges
    - Interactive learning

    Gamification improves:
    - engagement
    - retention
    - motivation
    - active learning
    """)

    if "score" in st.session_state:

        st.metric(
            "Your Current XP",
            st.session_state.score
        )

    if "badges" in st.session_state:

        st.write("### Your Badges")

        if len(st.session_state.badges) > 0:

            for badge in st.session_state.badges:
                st.success(f"🏅 {badge}")

        else:

            st.info("No badges earned yet.")

    # =========================================================
    # DEVELOPER NOTE
    # =========================================================

    st.markdown("---")
    st.header("Developer Note")

    st.info("""
    This project demonstrates:
    
    - Full Streamlit application architecture
    - Interactive educational software design
    - Data visualization expertise
    - Dashboard engineering concepts
    - Gamified learning systems
    
    It can be expanded further with:
    - AI chart recommendations
    - NLP storytelling assistants
    - Real-time analytics
    - Database integration
    - User authentication
    - Cloud deployment
    """)

    # =========================================================
    # FINAL MESSAGE
    # =========================================================

    st.markdown("---")

    st.success("""
    Thank you for exploring Kantvisualize Academy.

    Great analysts don't just create charts.

    They create understanding.
    """)

    