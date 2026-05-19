import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np


def run():

    st.title("Module 3")
    st.subheader("Visualization Crimes (Bad vs Good)")

    st.markdown("""
    Even beautiful charts can be dangerously misleading.

    This module teaches the most common **Visualization Crimes** that:
    - Distort perception
    - Mislead audiences
    - Manipulate interpretation
    - Hide truth in data

    Learn to identify bad charts like a professional analyst.
    """)

    st.markdown("---")

    # =========================================================
    # SECTION 1 — TRUNCATED Y AXIS
    # =========================================================

    st.header("1. Truncated Y-Axis")

    st.write("""
    Bar charts should usually start from **zero**.

    When the Y-axis is truncated, small differences can appear massive.
    """)

    sales_df = pd.DataFrame({
        "Company": ["A", "B"],
        "Revenue": [950, 1000]
    })

    y_start = st.slider(
        "Adjust Y-Axis Starting Point",
        0,
        900,
        0,
        step=50
    )

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("❌ Misleading Version")

        fig_bad = px.bar(
            sales_df,
            x="Company",
            y="Revenue",
            color="Company",
            title="Revenue Comparison"
        )

        fig_bad.update_yaxes(range=[y_start, 1050])

        st.plotly_chart(
            fig_bad,
            use_container_width=True,
            key="truncated_bad_chart"
        )

    with col2:

        st.subheader("✅ Honest Version")

        fig_good = px.bar(
            sales_df,
            x="Company",
            y="Revenue",
            color="Company",
            title="Revenue Comparison"
        )

        fig_good.update_yaxes(range=[0, 1050])

        st.plotly_chart(
            fig_good,
            use_container_width=True,
            key="truncated_good_chart"
        )

    if y_start > 0:
        st.error("""
        🚨 Visualization Crime Detected
        
        The chart exaggerates the difference between values.
        
        A small 5% difference now looks enormous.
        """)

    else:
        st.success("""
        ✅ Accurate Interpretation
        
        Starting at zero preserves proportional comparison.
        """)

    # =========================================================
    # SECTION 2 — PIE CHART OVERLOAD
    # =========================================================

    st.markdown("---")
    st.header("2. Pie Chart Overload")

    st.write("""
    Pie charts become unreadable when too many categories exist.

    Humans compare lengths better than angles.
    """)

    categories = [
        "A", "B", "C", "D", "E",
        "F", "G", "H", "I", "J",
        "K", "L", "M", "N", "O"
    ]

    values = [12, 10, 9, 8, 7, 6, 6, 5, 5, 4, 4, 3, 3, 2, 2]

    pie_df = pd.DataFrame({
        "Category": categories,
        "Value": values
    })

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("❌ Cluttered Pie Chart")

        fig_pie = px.pie(
            pie_df,
            names="Category",
            values="Value",
            title="Market Share"
        )

        st.plotly_chart(
            fig_pie,
            use_container_width=True,
            key="pie_overload_chart"
        )

    with col2:

        st.subheader("Better Alternative")

        fig_bar = px.bar(
            pie_df.sort_values("Value"),
            x="Value",
            y="Category",
            orientation="h",
            color="Value",
            title="Market Share"
        )

        st.plotly_chart(
            fig_bar,
            use_container_width=True,
            key="bar_alternative_chart"
        )

    st.info("""
    Why the bar chart is better:
    
    - Easier comparison
    - Clear ranking
    - Better readability
    - Handles many categories
    """)

    # =========================================================
    # SECTION 3 — 3D DISTORTION
    # =========================================================

    st.markdown("---")
    st.header("3. The 3D Distortion Problem")

    st.write("""
    3D charts distort perspective and make accurate comparison difficult.
    
    They add decoration but reduce clarity.
    """)

    product_df = pd.DataFrame({
        "Product": ["Laptop", "Phone", "Tablet", "Monitor"],
        "Sales": [400, 350, 200, 150]
    })

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("❌ Fake 3D Effect")

        fig_3d = go.Figure()

        fig_3d.add_trace(go.Bar(
            x=product_df["Product"],
            y=product_df["Sales"],
            marker=dict(
                color=["#1F77B4", "#FF7F0E", "#2CA02C", "#D62728"],
                line=dict(width=2, color="black")
            )
        ))

        fig_3d.update_layout(
            title="3D Styled Bar Chart",
            template="plotly_dark"
        )

        fig_3d.update_traces(
            opacity=0.85
        )

        st.plotly_chart(
            fig_3d,
            use_container_width=True,
            key="fake_3d_chart"
        )

    with col2:

        st.subheader("✅ Clean 2D Version")

        fig_clean = px.bar(
            product_df,
            x="Product",
            y="Sales",
            color="Product",
            title="Product Sales"
        )

        fig_clean.update_layout(
            plot_bgcolor="white"
        )

        st.plotly_chart(
            fig_clean,
            use_container_width=True,
            key="clean_2d_chart"
        )

    st.warning("""
    Why 3D charts are dangerous:
    
    - Perspective distortion
    - Hidden values
    - Harder comparisons
    - Decorative clutter
    """)

    # =========================================================
    # SECTION 4 — COLOR MISUSE
    # =========================================================

    st.markdown("---")
    st.header("4. Misleading Color Usage")

    st.write("""
    Colors influence emotional interpretation.

    Bad color choices can:
    - Create false urgency
    - Hide important data
    - Confuse viewers
    """)

    color_df = pd.DataFrame({
        "Department": ["HR", "Finance", "IT", "Sales"],
        "Performance": [78, 81, 79, 80]
    })

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("❌ Manipulative Colors")

        fig_bad_color = px.bar(
            color_df,
            x="Department",
            y="Performance",
            color="Performance",
            color_continuous_scale="Reds",
            title="Department Performance"
        )

        fig_bad_color.update_yaxes(range=[70, 82])

        st.plotly_chart(
            fig_bad_color,
            use_container_width=True,
            key="bad_color_chart"
        )

    with col2:

        st.subheader("✅ Neutral Colors")

        fig_good_color = px.bar(
            color_df,
            x="Department",
            y="Performance",
            color="Department",
            title="Department Performance"
        )

        fig_good_color.update_yaxes(range=[0, 100])

        st.plotly_chart(
            fig_good_color,
            use_container_width=True,
            key="good_color_chart"
        )

    st.info("""
    Good color design principles:
    
    - Use color intentionally
    - Avoid emotional manipulation
    - Preserve accessibility
    - Highlight meaning, not decoration
    """)

    # =========================================================
    # SECTION 5 — CHARTJUNK DETECTOR
    # =========================================================

    st.markdown("---")
    st.header("5. Chartjunk Detector")

    st.write("""
    Chartjunk refers to unnecessary visual clutter.
    
    Examples:
    - Heavy shadows
    - Excessive gradients
    - Decorative icons
    - Unnecessary animations
    """)

    junk_level = st.slider(
        "Increase Chartjunk Level",
        0,
        100,
        50
    )

    chartjunk_df = pd.DataFrame({
        "Month": ["Jan", "Feb", "Mar", "Apr", "May"],
        "Profit": [20, 30, 25, 40, 50]
    })

    fig_junk = px.line(
        chartjunk_df,
        x="Month",
        y="Profit",
        markers=True,
        title="Monthly Profit"
    )

    if junk_level < 30:

        fig_junk.update_layout(
            plot_bgcolor="white",
            paper_bgcolor="white"
        )

        st.success("✅ Minimal clutter. Data is easy to read.")

    elif junk_level < 70:

        fig_junk.update_layout(
            plot_bgcolor="#F4F6F7",
            paper_bgcolor="#EBF5FB"
        )

        st.warning("Some unnecessary decoration added.")

    else:

        fig_junk.update_layout(
            plot_bgcolor="#17202A",
            paper_bgcolor="#1B2631",
            font=dict(size=20, color="yellow")
        )

        st.error("""
        🚨 Extreme Chartjunk
        
        The design now competes against the data.
        """)

    st.plotly_chart(
        fig_junk,
        use_container_width=True,
        key="chartjunk_chart"
    )

    # =========================================================
    # MINI QUIZ
    # =========================================================

    st.markdown("---")
    st.header("Spot the Crime Challenge")

    st.write("""
    Which visualization crime is MOST dangerous
    for misleading comparisons?
    """)

    answer = st.radio(
        "Choose your answer:",
        [
            "Using too many colors",
            "Truncated Y-axis",
            "Using line charts",
            "Small font size"
        ],
        key="crime_quiz"
    )

    if st.button("Submit Crime Answer"):

        if answer == "Truncated Y-axis":

            st.success("""
            Correct! 🎯
            
            Truncated axes can drastically distort perception.
            """)

            st.session_state.score += 15

            if "Chart Crime Detective 🕵️" not in st.session_state.badges:
                st.session_state.badges.append(
                    "Chart Crime Detective 🕵️"
                )

        else:

            st.error("""
            Not quite.
            
            Truncated axes are one of the most common
            ways charts manipulate perception.
            """)

    # =========================================================
    # SUMMARY
    # =========================================================

    st.markdown("---")
    st.header("Key Lessons")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.info("""
        ### Avoid Distortion
        
        Start bar charts at zero.
        """)

    with col2:
        st.success("""
        ### Reduce Clutter
        
        Simpler charts communicate better.
        """)

    with col3:
        st.warning("""
        ### Design Ethically
        
        Visualizations influence decisions.
        """)

   