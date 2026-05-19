import streamlit as st
import pandas as pd
import plotly.express as px
import altair as alt
import numpy as np
import time


def run():

    st.title("Module 1")
    st.subheader("The Cognitive Science of Visualization")

    st.markdown("""
    This module teaches **how humans perceive visual information**
    and why some charts instantly communicate while others confuse.

    You will learn:
    - Grammar of Graphics
    - Pre-attentive Attributes
    - Data-Ink Ratio
    """)

    # =========================================================
    # SECTION 1 — GRAMMAR OF GRAPHICS
    # =========================================================

    st.markdown("---")
    st.header("1.Grammar of Graphics")

    st.write("""
    The **Grammar of Graphics** is a framework for building visualizations.

    Every chart is made of:

    - **Data** → The dataset
    - **Aesthetics** → Mapping variables to visuals
    - **Geometry** → The actual visual marks (bars, lines, points)
    """)

    # SAMPLE DATASET
    sales_df = pd.DataFrame({
        "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
        "Sales": [120, 180, 150, 220, 300, 280],
        "Profit": [20, 35, 25, 50, 70, 65]
    })

    st.subheader("Interactive Grammar of Graphics Builder")

    col1, col2 = st.columns(2)

    with col1:

        x_axis = st.selectbox(
            "Select X-axis",
            sales_df.columns,
            key="gog_x"
        )

        y_axis = st.selectbox(
            "Select Y-axis",
            sales_df.columns[1:],
            key="gog_y"
        )

    with col2:

        chart_type = st.selectbox(
            "Select Geometry",
            ["Bar Chart", "Line Chart", "Scatter Plot"],
            key="gog_chart"
        )

        color_option = st.selectbox(
            "Color By",
            ["None"] + list(sales_df.columns),
            key="gog_color"
        )

    # ALTAIR CHART
    if chart_type == "Bar Chart":
        mark = alt.Chart(sales_df).mark_bar(size=40)

    elif chart_type == "Line Chart":
        mark = alt.Chart(sales_df).mark_line(point=True)

    else:
        mark = alt.Chart(sales_df).mark_circle(size=120)

    encoding = {
        "x": alt.X(x_axis),
        "y": alt.Y(y_axis)
    }

    if color_option != "None":
        encoding["color"] = alt.Color(color_option)

    chart = mark.encode(**encoding).properties(
        width=700,
        height=400,
        title="Grammar of Graphics Interactive Demo"
    )

    st.altair_chart(chart, use_container_width=True)

    with st.expander("Learn What's Happening"):

        st.write(f"""
        ### Current Visualization Breakdown

        - **Data:** `sales_df`
        - **X Aesthetic:** `{x_axis}`
        - **Y Aesthetic:** `{y_axis}`
        - **Geometry:** `{chart_type}`
        - **Color Encoding:** `{color_option}`

        This demonstrates how charts are built by combining:

        `data + aesthetics + geometry`
        """)

    # =========================================================
    # SECTION 2 — PRE-ATTENTIVE ATTRIBUTES
    # =========================================================

    st.markdown("---")
    st.header("2.Pre-attentive Attributes")

    st.write("""
    Humans notice certain visual features almost instantly —
    before conscious reading happens.

    Examples:
    - Color
    - Size
    - Position
    - Motion
    - Orientation

    This is called **pre-attentive processing**.
    """)

    st.subheader("200ms Visual Perception Demo")

    st.info("""
    A chart will flash briefly.

    Try to answer:

    ### Which category had the highest value?
    """)

    # SESSION STATE
    if "show_quiz" not in st.session_state:
        st.session_state.show_quiz = False

    if "quiz_answered" not in st.session_state:
        st.session_state.quiz_answered = False

    demo_df = pd.DataFrame({
        "Category": ["A", "B", "C", "D", "E"],
        "Value": [10, 15, 45, 12, 18],
        "Color": ["gray", "gray", "red", "gray", "gray"]
    })

    # START BUTTON
    if st.button("▶ Start Perception Test"):

        st.session_state.show_quiz = True
        st.session_state.quiz_answered = False

        placeholder = st.empty()

        fig = px.bar(
            demo_df,
            x="Category",
            y="Value",
            color="Color",
            color_discrete_map={
                "gray": "lightgray",
                "red": "red"
            },
            title="Quick! Which bar was highest?"
        )

        fig.update_layout(
            showlegend=False,
            height=500
        )

        placeholder.plotly_chart(
            fig,
            use_container_width=True,
            key="perception_test_chart"
        )

        # SHOW CHART LONGER
        time.sleep(1.2)

        placeholder.empty()

    # SHOW QUIZ AFTER FLASH
    if st.session_state.show_quiz:

        st.markdown("### What did you notice?")

        answer = st.radio(
            "Which category had the highest value?",
            ["Select an Answer", "A", "B", "C", "D", "E"],
            index=0,
            key="perception_answer"
        )

        if st.button("Submit Perception Answer"):

            st.session_state.quiz_answered = True

            if answer == "C":

                st.success("""
                Correct! 🎯

                Your brain instantly detected:
                - Height difference
                - Red color emphasis

                This demonstrates pre-attentive processing.
                """)

                st.session_state.score += 10

            elif answer == "Select an Answer":

                st.warning("""
                Please select an answer first.
                """)

            else:

                st.error("""
                Not quite.

                The red highlighted bar was intentionally designed
                to attract immediate visual attention.
                """)

        # RESET BUTTON
        if st.button("Retry Test"):

            st.session_state.show_quiz = False
            st.session_state.quiz_answered = False
            st.rerun()

    # =========================================================
    # SECTION 3 — DATA INK RATIO
    # =========================================================

    st.markdown("---")
    st.header("3.Data-Ink Ratio")

    st.write("""
    Edward Tufte introduced the concept of the
    **Data-Ink Ratio**.

    Good visualizations maximize:
    - Useful information

    And minimize:
    - Decorative clutter
    - Excessive borders
    - Unnecessary gridlines
    - Chartjunk
    """)

    st.subheader("Tufte Slider Demo")

    cleanliness = st.slider(
        "Move toward cleaner visualization",
        0,
        100,
        50
    )

    np.random.seed(42)

    tufte_df = pd.DataFrame({
        "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
        "Revenue": [100, 150, 130, 180, 220, 210]
    })

    fig = px.line(
        tufte_df,
        x="Month",
        y="Revenue",
        markers=True,
        title="Revenue Trend"
    )

    # CLUTTER LEVEL
    if cleanliness < 30:

        fig.update_layout(
            plot_bgcolor="#D6EAF8",
            paper_bgcolor="#FDEDEC",
            font=dict(size=18),
            xaxis=dict(
                showgrid=True,
                gridwidth=2,
                gridcolor="black",
                showline=True,
                linewidth=4,
                linecolor="black"
            ),
            yaxis=dict(
                showgrid=True,
                gridwidth=2,
                gridcolor="black",
                showline=True,
                linewidth=4,
                linecolor="black"
            )
        )

    elif cleanliness < 70:

        fig.update_layout(
            plot_bgcolor="white",
            paper_bgcolor="white",
            xaxis=dict(showgrid=True),
            yaxis=dict(showgrid=True)
        )

    else:

        fig.update_layout(
            plot_bgcolor="white",
            paper_bgcolor="white",
            xaxis=dict(
                showgrid=False,
                zeroline=False
            ),
            yaxis=dict(
                showgrid=False,
                zeroline=False
            )
        )

    st.plotly_chart(
        fig,
        use_container_width=True,
        key="tufte_slider_chart"
    )

    # FEEDBACK
    if cleanliness < 30:

        st.error("""
        ❌ Low Data-Ink Ratio

        Too much decoration competes with the actual data.
        """)

    elif cleanliness < 70:

        st.warning("""
        ⚠ Moderate Data-Ink Ratio

        Better, but still contains some unnecessary visual noise.
        """)

    else:

        st.success("""
        ✅ High Data-Ink Ratio

        The visualization focuses attention on the data itself.
        """)

    # =========================================================
    # SUMMARY
    # =========================================================

    st.markdown("---")
    st.header("Key Takeaways")

    col1, col2, col3 = st.columns(3)

    with col1:

        st.info("""
        ### Grammar of Graphics

        Charts are built from:
        - Data
        - Aesthetics
        - Geometry
        """)

    with col2:

        st.success("""
        ### Pre-attentive Processing

        Visual attributes guide attention instantly.
        """)

    with col3:

        st.warning("""
        ### Data-Ink Ratio

        Remove clutter.
        Highlight meaning.
        """)

   