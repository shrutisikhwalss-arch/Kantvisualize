import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np


def run():

    st.title("Module 2")
    st.subheader("The Chart Selection Engine")

    st.markdown("""
    One of the most important skills in Data Visualization is choosing the **right chart**.

    Different charts answer different questions.

    This interactive engine helps you decide:
    - Which chart to use
    - Why it works
    - When to avoid it
    """)

    st.markdown("---")

    # =========================================================
    # SAMPLE DATASETS
    # =========================================================

    sales_df = pd.DataFrame({
        "Category": ["Electronics", "Furniture", "Clothing", "Sports", "Books"],
        "Sales": [450, 300, 500, 280, 150]
    })

    trend_df = pd.DataFrame({
        "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
        "Revenue": [120, 150, 170, 210, 260, 300]
    })

    distribution_df = pd.DataFrame({
        "Scores": np.random.normal(70, 12, 500)
    })

    relationship_df = pd.DataFrame({
        "Hours_Studied": np.random.randint(1, 10, 100),
        "Exam_Score": np.random.randint(40, 100, 100)
    })

    composition_df = pd.DataFrame({
        "Department": ["HR", "Sales", "IT", "Finance"],
        "Employees": [20, 45, 25, 10]
    })

    # =========================================================
    # USER INPUTS
    # =========================================================

    st.header("Interactive Decision Tree")

    col1, col2 = st.columns(2)

    with col1:
        data_type = st.selectbox(
            "1️⃣ What type of data are you working with?",
            [
                "Categorical",
                "Continuous",
                "Time Series",
                "Geographical"
            ]
        )

    with col2:
        goal = st.selectbox(
            "2️⃣ What is your analytical goal?",
            [
                "Comparison",
                "Distribution",
                "Relationship",
                "Composition",
                "Trend"
            ]
        )

    st.markdown("---")

    # =========================================================
    # DECISION ENGINE
    # =========================================================

    recommended_chart = ""
    why = ""
    avoid = ""

    # =========================================================
    # COMPARISON
    # =========================================================

    if goal == "Comparison":

        recommended_chart = "Bar Chart"

        why = """
        Bar charts are excellent for comparing values across categories.
        
        Human eyes compare lengths very accurately, making bar charts highly readable.
        """

        avoid = """
        Avoid:
        - Pie charts with many categories
        - 3D bars
        - Truncated baselines
        """

        fig = px.bar(
            sales_df,
            x="Category",
            y="Sales",
            color="Category",
            title="Sales Comparison Across Categories"
        )

    # =========================================================
    # DISTRIBUTION
    # =========================================================

    elif goal == "Distribution":

        recommended_chart = "Histogram"

        why = """
        Histograms reveal:
        - Spread
        - Shape
        - Skewness
        - Outliers
        
        They help understand how values are distributed.
        """

        avoid = """
        Avoid:
        - Pie charts
        - Line charts for distributions
        """

        fig = px.histogram(
            distribution_df,
            x="Scores",
            nbins=25,
            title="Distribution of Student Scores"
        )

    # =========================================================
    # RELATIONSHIP
    # =========================================================

    elif goal == "Relationship":

        recommended_chart = "Scatter Plot"

        why = """
        Scatter plots reveal relationships between variables.
        
        Useful for:
        - Correlation
        - Clusters
        - Trends
        - Outliers
        """

        avoid = """
        Avoid:
        - Pie charts
        - Stacked bars
        """

        fig = px.scatter(
            relationship_df,
            x="Hours_Studied",
            y="Exam_Score",
            trendline="ols",
            title="Relationship Between Study Time and Scores"
        )

    # =========================================================
    # COMPOSITION
    # =========================================================

    elif goal == "Composition":

        recommended_chart = "Stacked Bar Chart / Donut Chart"

        why = """
        Composition charts show how parts contribute to a whole.
        
        Use them carefully and keep categories limited.
        """

        avoid = """
        Avoid:
        - Too many pie slices
        - 3D pies
        """

        fig = px.pie(
            composition_df,
            names="Department",
            values="Employees",
            hole=0.5,
            title="Employee Composition by Department"
        )

    # =========================================================
    # TREND
    # =========================================================

    elif goal == "Trend":

        recommended_chart = "Line Chart"

        why = """
        Line charts are ideal for showing change over time.
        
        They emphasize:
        - Direction
        - Growth
        - Seasonality
        - Trends
        """

        avoid = """
        Avoid:
        - Bar overload for long timelines
        - Unnecessary markers
        """

        fig = px.line(
            trend_df,
            x="Month",
            y="Revenue",
            markers=True,
            title="Revenue Trend Over Time"
        )

    # =========================================================
    # OUTPUT SECTION
    # =========================================================

    st.header("Recommended Visualization")

    metric_col1, metric_col2 = st.columns(2)

    with metric_col1:
        st.metric(
            "Recommended Chart",
            recommended_chart
        )

    with metric_col2:
        st.metric(
            "Analytical Goal",
            goal
        )

    st.plotly_chart(fig, use_container_width=True)

    # =========================================================
    # WHY THIS CHART?
    # =========================================================

    tabs = st.tabs([
        "✅ Why This Works",
        "❌ What to Avoid",
        "Visualization Thinking"
    ])

    with tabs[0]:
        st.success(why)

    with tabs[1]:
        st.error(avoid)

    with tabs[2]:
        st.info(f"""
        ### Think Like a Data Storyteller
        
        You selected:
        - **Data Type:** {data_type}
        - **Goal:** {goal}
        
        Good visualizations are chosen based on:
        
        1. Audience
        2. Business question
        3. Data structure
        4. Cognitive load
        5. Storytelling clarity
        """)

    # =========================================================
    # CHART MATCHING GRID
    # =========================================================

    st.markdown("---")
    st.header("Quick Chart Selection Cheat Sheet")

    cheat_sheet = pd.DataFrame({
        "Goal": [
            "Comparison",
            "Trend",
            "Distribution",
            "Relationship",
            "Composition"
        ],
        "Best Chart": [
            "Bar Chart",
            "Line Chart",
            "Histogram",
            "Scatter Plot",
            "Stacked Bar / Pie"
        ],
        "Why": [
            "Compare category values",
            "Show change over time",
            "Reveal spread & shape",
            "Find correlations",
            "Show parts of a whole"
        ]
    })

    st.dataframe(
        cheat_sheet,
        use_container_width=True
    )

    # =========================================================
    # INTERACTIVE CHALLENGE
    # =========================================================

    st.markdown("---")
    st.header("Mini Challenge")

    st.write("""
    Choose the best chart for this scenario:
    
    **Scenario:**  
    A company wants to show website traffic growth over 24 months.
    """)

    answer = st.radio(
        "Pick the best visualization:",
        [
            "Pie Chart",
            "Scatter Plot",
            "Line Chart",
            "Treemap"
        ],
        key="chart_quiz"
    )

    if st.button("Submit Answer"):

        if answer == "Line Chart":

            st.success("""
            Correct! 🎉

            Line charts are best for:
            - Time series
            - Trends
            - Growth analysis
            """)

            if "Chart Selection Explorer 🧭" not in st.session_state.badges:
                st.session_state.badges.append(
                    "Chart Selection Explorer 🧭"
                )

            st.session_state.score += 10

        else:

            st.error("""
            Not quite.

            Since the data changes over time,
            a line chart is the clearest option.
            """)

    # =========================================================
    # PROFESSIONAL INSIGHT
    # =========================================================

    st.markdown("---")

    with st.expander("Real-World Industry Insight"):

        st.write("""
        Professional Data Analysts and BI Developers spend more time
        selecting the *right visualization* than building the chart itself.

        In tools like:
        - Tableau
        - Power BI
        - Looker
        - Qlik
        
        choosing the wrong chart can:
        - Mislead executives
        - Hide insights
        - Distort business decisions
        
        Great analysts think visually before they build.
        """)

    # =========================================================
    # SUMMARY
    # =========================================================

    st.markdown("---")
    st.header("Key Takeaways")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.info("""
        ### Comparison
        
        Use Bar Charts
        """)

    with col2:
        st.success("""
        ### Trends
        
        Use Line Charts
        """)

    with col3:
        st.warning("""
        ### Relationships
        
        Use Scatter Plots
        """)

    