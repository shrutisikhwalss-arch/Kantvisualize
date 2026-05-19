import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import altair as alt
import numpy as np


def run():

    st.title("Custom Dataset Visualization Lab")

    st.markdown("""
    Upload your own dataset and explore:

    - Interactive visualizations
    - Chart selection
    - Dashboard building
    - Storytelling with data
    - Visualization quality analysis

    Supports:
    - CSV
    - Excel (.xlsx)
    """)

    st.markdown("---")

    # =========================================================
    # FILE UPLOAD
    # =========================================================

    st.header("Upload Dataset")

    uploaded_file = st.file_uploader(
        "Upload CSV or Excel File",
        type=["csv", "xlsx"]
    )

    if uploaded_file is None:

        st.info("Upload a dataset to begin.")
        return

    # =========================================================
    # LOAD DATA
    # =========================================================

    try:

        if uploaded_file.name.endswith(".csv"):
            df = pd.read_csv(uploaded_file)

        else:
            df = pd.read_excel(uploaded_file)

    except Exception as e:

        st.error(f"Error loading file: {e}")
        return

    st.success("✅ Dataset Loaded Successfully")

    st.markdown("---")

    # =========================================================
    # DATA OVERVIEW
    # =========================================================

    st.header("Dataset Overview")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Rows", df.shape[0])

    with col2:
        st.metric("Columns", df.shape[1])

    with col3:
        st.metric(
            "Numeric Columns",
            len(df.select_dtypes(include=np.number).columns)
        )

    with col4:
        st.metric(
            "Missing Values",
            int(df.isnull().sum().sum())
        )

    with st.expander("Preview Dataset"):

        st.dataframe(df, use_container_width=True)

    # =========================================================
    # COLUMN TYPES
    # =========================================================

    numeric_cols = df.select_dtypes(include=np.number).columns.tolist()

    categorical_cols = df.select_dtypes(
        exclude=np.number
    ).columns.tolist()

    all_cols = df.columns.tolist()

    # =========================================================
    # VISUALIZATION BUILDER
    # =========================================================

    st.markdown("---")
    st.header("Interactive Visualization Builder")

    chart_type = st.selectbox(
        "Choose Chart Type",
        [
            "Scatter Plot",
            "Bar Chart",
            "Line Chart",
            "Histogram",
            "Box Plot",
            "Pie Chart",
            "Heatmap"
        ]
    )

    col1, col2 = st.columns(2)

    with col1:

        x_axis = st.selectbox(
            "Select X-axis",
            all_cols,
            key="custom_x"
        )

        color_col = st.selectbox(
            "Color By",
            ["None"] + all_cols,
            key="custom_color"
        )

    with col2:

        y_axis = st.selectbox(
            "Select Y-axis",
            all_cols,
            key="custom_y"
        )

        size_col = st.selectbox(
            "Bubble Size",
            ["None"] + numeric_cols,
            key="custom_size"
        )

    # =========================================================
    # CHART GENERATION
    # =========================================================

    st.markdown("---")
    st.subheader("Generated Visualization")

    color_arg = None if color_col == "None" else color_col
    size_arg = None if size_col == "None" else size_col

    try:

        if chart_type == "Scatter Plot":

            fig = px.scatter(
                df,
                x=x_axis,
                y=y_axis,
                color=color_arg,
                size=size_arg,
                hover_data=df.columns,
                title=f"{y_axis} vs {x_axis}"
            )

        elif chart_type == "Bar Chart":

            fig = px.bar(
                df,
                x=x_axis,
                y=y_axis,
                color=color_arg,
                title=f"{y_axis} by {x_axis}"
            )

        elif chart_type == "Line Chart":

            fig = px.line(
                df,
                x=x_axis,
                y=y_axis,
                color=color_arg,
                markers=True,
                title=f"{y_axis} Trend"
            )

        elif chart_type == "Histogram":

            fig = px.histogram(
                df,
                x=x_axis,
                color=color_arg,
                title=f"Distribution of {x_axis}"
            )

        elif chart_type == "Box Plot":

            fig = px.box(
                df,
                x=x_axis,
                y=y_axis,
                color=color_arg,
                title=f"Box Plot of {y_axis}"
            )

        elif chart_type == "Pie Chart":

            fig = px.pie(
                df,
                names=x_axis,
                values=y_axis,
                title=f"{y_axis} Composition"
            )

        elif chart_type == "Heatmap":

            corr = df[numeric_cols].corr()

            fig = px.imshow(
                corr,
                text_auto=True,
                aspect="auto",
                title="Correlation Heatmap"
            )

        st.plotly_chart(
            fig,
            use_container_width=True,
            key="custom_dataset_chart"
        )

    except Exception as e:

        st.error(f"Visualization Error: {e}")

    # =========================================================
    # SMART CHART RECOMMENDATION
    # =========================================================

    st.markdown("---")
    st.header("Smart Chart Recommendation")

    goal = st.selectbox(
        "What is your analytical goal?",
        [
            "Comparison",
            "Trend",
            "Relationship",
            "Distribution",
            "Composition"
        ]
    )

    recommendations = {

        "Comparison": {
            "chart": "Bar Chart",
            "why": "Best for comparing categories."
        },

        "Trend": {
            "chart": "Line Chart",
            "why": "Best for time-series and trend analysis."
        },

        "Relationship": {
            "chart": "Scatter Plot",
            "why": "Best for correlation and relationships."
        },

        "Distribution": {
            "chart": "Histogram",
            "why": "Best for understanding spread and frequency."
        },

        "Composition": {
            "chart": "Pie Chart or Stacked Bar",
            "why": "Best for part-to-whole analysis."
        }
    }

    st.success(f"Recommended Chart: {recommendations[goal]['chart']}")

    st.info(recommendations[goal]["why"])

    # =========================================================
    # DATA STORYTELLING
    # =========================================================

    st.markdown("---")
    st.header("Storytelling With Your Data")

    st.write("""
    Great analysts do more than create charts.

    They tell stories.
    """)

    story_type = st.selectbox(
        "Choose Story Angle",
        [
            "Growth Story",
            "Problem Detection",
            "Performance Comparison",
            "Outlier Discovery"
        ]
    )

    if story_type == "Growth Story":

        st.success("""
        Focus on trends increasing over time.

        Recommended:
        - Line charts
        - Area charts
        - KPI cards
        """)

    elif story_type == "Problem Detection":

        st.warning("""
        Focus on anomalies and declines.

        Recommended:
        - Heatmaps
        - Box plots
        - Conditional formatting
        """)

    elif story_type == "Performance Comparison":

        st.info("""
        Compare groups, products, or departments.

        Recommended:
        - Bar charts
        - Grouped bars
        - Ranked visuals
        """)

    else:

        st.error("""
        Highlight unusual values and anomalies.

        Recommended:
        - Scatter plots
        - Box plots
        - Distribution charts
        """)

    # =========================================================
    # VISUALIZATION CRIME DETECTOR
    # =========================================================

    st.markdown("---")
    st.header("Visualization Crime Detector")

    st.write("Analyze your visualization for common mistakes.")

    crime_checks = []

    if chart_type == "Pie Chart" and len(df[x_axis].unique()) > 8:
        crime_checks.append(
            "Too many pie slices reduce readability."
        )

    if chart_type == "3D Chart":
        crime_checks.append(
            "3D charts distort perception."
        )

    if len(df.columns) > 15:
        crime_checks.append(
            "Large datasets may create cluttered dashboards."
        )

    if crime_checks:

        for crime in crime_checks:
            st.warning(f"⚠ {crime}")

    else:

        st.success("✅ No major visualization crimes detected.")

    # =========================================================
    # DASHBOARD BUILDER
    # =========================================================

    st.markdown("---")
    st.header("Mini Dashboard")

    kpi1, kpi2, kpi3 = st.columns(3)

    if numeric_cols:

        metric_col = st.selectbox(
            "Select KPI Metric",
            numeric_cols
        )

        with kpi1:
            st.metric(
                "Average",
                f"{df[metric_col].mean():.2f}"
            )

        with kpi2:
            st.metric(
                "Maximum",
                f"{df[metric_col].max():.2f}"
            )

        with kpi3:
            st.metric(
                "Minimum",
                f"{df[metric_col].min():.2f}"
            )

    # =========================================================
    # DOWNLOAD CLEANED DATA
    # =========================================================

    st.markdown("---")
    st.header("⬇ Export Dataset")

    csv = df.to_csv(index=False).encode("utf-8")

    st.download_button(
        label="Download Dataset as CSV",
        data=csv,
        file_name="cleaned_dataset.csv",
        mime="text/csv"
    )

    # =========================================================
    # FINAL SECTION
    # =========================================================

    st.markdown("---")

    st.success("""
    🎉 You are now working like a real Data Analyst.

    You practiced:
    - Exploratory Data Analysis
    - Dashboard Building
    - Storytelling
    - Visualization Design
    - Analytical Thinking
    """)





