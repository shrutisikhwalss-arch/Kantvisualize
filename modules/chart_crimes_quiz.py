import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np


def run():

    st.title("Module 6")
    st.subheader("Chart Crimes Quiz")

    st.markdown("""
    Test your visualization literacy skills.

    Learn to identify:
    - Misleading charts
    - Dashboard mistakes
    - Bad storytelling
    - Manipulative design

    Earn badges and become a visualization expert.
    """)

    st.markdown("---")

    if "practice_mode" not in st.session_state:
        st.session_state.practice_mode = False

    # =========================================================
    # QUIZ QUESTIONS
    # =========================================================

    questions = [

        {
            "question": "What is the main issue with this chart?",
            "options": [
                "Too many categories",
                "Truncated Y-axis",
                "Wrong font",
                "No legend"
            ],
            "answer": "Truncated Y-axis"
        },

        {
            "question": "Why are overloaded pie charts problematic?",
            "options": [
                "Hard to compare angles",
                "Too colorful",
                "Too large",
                "Missing axes"
            ],
            "answer": "Hard to compare angles"
        },

        {
            "question": "Why are 3D charts misleading?",
            "options": [
                "Perspective distortion",
                "No labels",
                "Wrong colors",
                "Missing title"
            ],
            "answer": "Perspective distortion"
        },

        {
            "question": "Which is the best chart for trends over time?",
            "options": [
                "Pie chart",
                "Treemap",
                "Line chart",
                "Donut chart"
            ],
            "answer": "Line chart"
        },

        {
            "question": "What does chartjunk mean?",
            "options": [
                "Useful annotations",
                "Too much unnecessary decoration",
                "Simple charts",
                "Interactive charts"
            ],
            "answer": "Too much unnecessary decoration"
        },

        {
            "question": "Why should bar charts usually start at zero?",
            "options": [
                "To avoid misleading comparisons",
                "To save space",
                "For better colors",
                "To make bars taller"
            ],
            "answer": "To avoid misleading comparisons"
        },

        {
            "question": "Which chart is best for relationships?",
            "options": [
                "Scatter plot",
                "Pie chart",
                "Area chart",
                "Gauge chart"
            ],
            "answer": "Scatter plot"
        },

        {
            "question": "What is the danger of too many colors?",
            "options": [
                "Visual confusion",
                "More insights",
                "Faster charts",
                "More precision"
            ],
            "answer": "Visual confusion"
        },

        {
            "question": "Which chart is best for distributions?",
            "options": [
                "Histogram",
                "Pie chart",
                "Treemap",
                "Stacked donut"
            ],
            "answer": "Histogram"
        },

        {
            "question": "What makes dashboards effective?",
            "options": [
                "Clarity and focus",
                "Many animations",
                "3D effects",
                "Maximum colors"
            ],
            "answer": "Clarity and focus"
        }
    ]

    # =========================================================
    # MAIN QUIZ
    # =========================================================

    st.header("Main Quiz")

    score = 0

    with st.form("main_quiz_form"):

        answers = []

        for i, q in enumerate(questions):

            st.markdown(f"### Question {i+1}")

            # SIMPLE SAMPLE CHARTS
            sample_df = pd.DataFrame({
                "Category": ["A", "B", "C"],
                "Value": np.random.randint(10, 100, 3)
            })

            fig = px.bar(
                sample_df,
                x="Category",
                y="Value",
                color="Category",
                title=f"Visualization Example {i+1}"
            )

            st.plotly_chart(
                fig,
                use_container_width=True,
                key=f"quiz_chart_{i}"
            )

            ans = st.radio(
                q["question"],
                q["options"],
                key=f"quiz_question_{i}"
            )

            answers.append(ans)

            st.markdown("---")

        submitted = st.form_submit_button("Submit Main Quiz")

        if submitted:

            for i, q in enumerate(questions):

                if answers[i] == q["answer"]:
                    score += 1

            percentage = (score / len(questions)) * 100

            st.header("📊 Quiz Results")

            col1, col2 = st.columns(2)

            with col1:
                st.metric("Score", f"{score}/{len(questions)}")

            with col2:
                st.metric("Percentage", f"{percentage:.0f}%")

            # =================================================
            # PERFORMANCE FEEDBACK
            # =================================================

            if percentage >= 90:

                st.success("""
                🏆 Outstanding!
                
                You have strong visualization literacy skills.
                """)

                st.balloons()

                st.session_state.score += 50

                if "Visualization Master 🎖️" not in st.session_state.badges:
                    st.session_state.badges.append(
                        "Visualization Master 🎖️"
                    )

            elif percentage >= 70:

                st.success("""
                🎉 Great job!
                
                You understand most visualization principles.
                """)

                st.session_state.score += 30

            elif percentage >= 50:

                st.warning("""
                👍 Good effort!
                
                Continue practicing chart evaluation.
                """)

                st.session_state.score += 15

            else:

                st.error("""
                📚 Keep practicing.
                
                Visualization literacy improves with repetition.
                """)

            # =================================================
            # ANSWER REVIEW
            # =================================================

            st.markdown("---")
            st.header("🧠 Answer Review")

            for i, q in enumerate(questions):

                with st.expander(f"Question {i+1} Explanation"):

                    st.write(f"""
                    **Correct Answer:** {q['answer']}
                    
                    Understanding this principle helps analysts:
                    - Design ethical visualizations
                    - Communicate clearly
                    - Avoid misleading audiences
                    """)

    # =========================================================
    # PRACTICE MODE
    # =========================================================

    st.markdown("---")
    st.header("Practice More Questions")

    st.write("""
    Want more practice?

    Click below to unlock 10 additional questions.
    """)

    if st.button("Start Practice Mode"):

        st.session_state.practice_mode = True

    # =========================================================
    # EXTRA PRACTICE QUESTIONS
    # =========================================================

    if st.session_state.practice_mode:

        st.markdown("---")
        st.header("Advanced Practice Questions")

        practice_questions = [

            "Which chart is worst for precise comparison?",
            "Why are rainbow color palettes dangerous?",
            "What does pre-attentive processing mean?",
            "Which chart best shows composition?",
            "Why should dashboards avoid clutter?",
            "What is cognitive overload?",
            "Why are labels important?",
            "Which chart is best for ranking?",
            "Why should analysts avoid distortion?",
            "What makes storytelling powerful?"
        ]

        practice_answers = [
            "Pie chart",
            "They confuse interpretation",
            "Instant visual perception",
            "Stacked bar chart",
            "Improves readability",
            "Too much information at once",
            "Improve understanding",
            "Horizontal bar chart",
            "Preserve truth",
            "Creates emotional connection"
        ]

        practice_options = [

            ["Pie chart", "Scatter plot", "Line chart", "Histogram"],

            [
                "They confuse interpretation",
                "They increase precision",
                "They improve speed",
                "They reduce data"
            ],

            [
                "Instant visual perception",
                "Slow reading",
                "Data cleaning",
                "Dashboard exporting"
            ],

            [
                "Stacked bar chart",
                "Scatter plot",
                "Line chart",
                "Histogram"
            ],

            [
                "Improves readability",
                "Makes charts complex",
                "Adds confusion",
                "Increases chartjunk"
            ],

            [
                "Too much information at once",
                "Too few labels",
                "Low resolution",
                "Simple charts"
            ],

            [
                "Improve understanding",
                "Decorate charts",
                "Increase animation",
                "Reduce insight"
            ],

            [
                "Horizontal bar chart",
                "Pie chart",
                "Area chart",
                "Radar chart"
            ],

            [
                "Preserve truth",
                "Increase drama",
                "Improve decoration",
                "Add complexity"
            ],

            [
                "Creates emotional connection",
                "Adds 3D effects",
                "Uses many colors",
                "Removes labels"
            ]
        ]

        practice_score = 0

        with st.form("practice_form"):

            practice_user_answers = []

            for i in range(10):

                st.markdown(f"### Practice Question {i+1}")

                practice_df = pd.DataFrame({
                    "X": ["A", "B", "C", "D"],
                    "Y": np.random.randint(10, 100, 4)
                })

                practice_fig = px.line(
                    practice_df,
                    x="X",
                    y="Y",
                    markers=True,
                    title=f"Practice Visualization {i+1}"
                )

                st.plotly_chart(
                    practice_fig,
                    use_container_width=True,
                    key=f"practice_chart_{i}"
                )

                user_ans = st.radio(
                    practice_questions[i],
                    practice_options[i],
                    key=f"practice_q_{i}"
                )

                practice_user_answers.append(user_ans)

                st.markdown("---")

            practice_submit = st.form_submit_button(
                "Submit Practice Quiz"
            )

            if practice_submit:

                for i in range(10):

                    if practice_user_answers[i] == practice_answers[i]:
                        practice_score += 1

                st.header("Practice Results")

                percentage = (practice_score / 10) * 100

                st.metric(
                    "Practice Score",
                    f"{practice_score}/10"
                )

                st.metric(
                    "Practice Percentage",
                    f"{percentage:.0f}%"
                )

                if percentage >= 80:

                    st.success("""
                    🚀 Excellent Practice Performance!
                    """)

                    st.session_state.score += 25

                    if "Practice Champion 🧠" not in st.session_state.badges:
                        st.session_state.badges.append(
                            "Practice Champion 🧠"
                        )

                elif percentage >= 50:

                    st.warning("""
                    👍 Nice work. Keep improving.
                    """)

                else:

                    st.error("""
                    📚 Continue practicing visualization analysis.
                    """)

    # =========================================================
    # FINAL SECTION
    # =========================================================

    st.markdown("---")

    st.header("Visualization Skill Levels")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.info("""
        ### Beginner
        
        Learning chart fundamentals.
        """)

    with col2:
        st.success("""
        ### Storyteller
        
        Understands effective communication.
        """)

    with col3:
        st.warning("""
        ### Expert
        
        Designs ethical and impactful dashboards.
        """)

    st.markdown("---")

    st.success("""
    Congratulations on completing the academy.

    You now understand:
    - Visualization psychology
    - Ethical chart design
    - Dashboard storytelling
    - Business communication
    - Analytical thinking
    """)
    st.balloons()