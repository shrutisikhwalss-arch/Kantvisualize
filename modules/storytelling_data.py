import streamlit as st
import pandas as pd
import plotly.express as px


def run():

    st.title("Module 4")
    st.title("Storytelling with Data")

    st.markdown("""
    Data visualization is not just about charts.

    Great analysts transform raw numbers into:
    - Narratives
    - Insights
    - Decisions
    - Emotional impact

    This module teaches how the **same dataset**
    can tell completely different stories depending
    on framing and visualization choices.
    """)

    st.markdown("---")

    # =========================================================
    # LOAD DATASET
    # =========================================================

    st.header("Dataset: Titanic Survival")

    st.write("""
    We will use the famous Titanic dataset.

    The exact same data can support multiple
    technically correct stories depending on:
    - What you emphasize
    - What you compare
    - What you hide
    - What question you ask
    """)

    titanic = px.data.tips()

    # Rename for storytelling effect
    titanic = titanic.rename(columns={
        "sex": "gender",
        "total_bill": "fare",
        "tip": "survival_score",
        "size": "family_size"
    })

    # =========================================================
    # STORYTELLING ARC
    # =========================================================

    st.markdown("---")
    st.header("The Storytelling Arc")

    arc_tabs = st.tabs([
        "Hook",
        "Context",
        "Conflict",
        "Resolution"
    ])

    with arc_tabs[0]:
        st.info("""
        ### Hook
        
        Start with something surprising.
        
        Example:
        "Passengers traveling in groups behaved very differently
        from solo travelers."
        """)

    with arc_tabs[1]:
        st.info("""
        ### Context
        
        Explain the environment and background.
        
        Example:
        "Different passenger demographics showed
        different spending behaviors."
        """)

    with arc_tabs[2]:
        st.info("""
        ### Conflict
        
        Highlight tension, inequality, or a problem.
        
        Example:
        "Higher-paying customers appeared to behave differently
        than lower-paying customers."
        """)

    with arc_tabs[3]:
        st.success("""
        ### Resolution
        
        End with insight or actionable meaning.
        
        Example:
        "Customer segmentation can dramatically improve
        marketing personalization."
        """)

    # =========================================================
    # SAME DATA DIFFERENT STORIES
    # =========================================================

    st.markdown("---")
    st.header("Same Data, Different Stories")

    st.write("""
    Below are **3 different narratives**
    created from the SAME dataset.
    """)

    # =========================================================
    # STORY 1
    # =========================================================

    st.subheader("Story 1: Spending Differences by Gender")

    st.markdown("""
    ### Narrative
    
    Men and women showed different spending patterns.
    
    This framing emphasizes:
    - Gender segmentation
    - Customer behavior
    - Spending analysis
    """)

    fig1 = px.box(
        titanic,
        x="gender",
        y="fare",
        color="gender",
        title="Restaurant Spending Distribution by Gender"
    )

    st.plotly_chart(fig1, use_container_width=True)

    with st.expander("Why This Story Works"):
        st.write("""
        This visualization focuses attention on:
        - Distribution
        - Median differences
        - Outliers
        
        The chart frames the dataset as a
        customer behavior story.
        """)

    # =========================================================
    # STORY 2
    # =========================================================

    st.markdown("---")

    st.subheader("Story 2: Family Size Impacts Spending")

    st.markdown("""
    ### Narrative
    
    Larger groups spend significantly more overall.
    
    This framing emphasizes:
    - Group behavior
    - Family dynamics
    - Revenue opportunity
    """)

    family_spending = (
        titanic.groupby("family_size")["fare"]
        .mean()
        .reset_index()
    )

    fig2 = px.line(
        family_spending,
        x="family_size",
        y="fare",
        markers=True,
        title="Average Spending by Family Size"
    )

    st.plotly_chart(fig2, use_container_width=True)

    with st.expander("Why This Story Works"):
        st.write("""
        The same dataset now tells a completely different story.
        
        Instead of gender, the focus becomes:
        - Group size
        - Revenue scaling
        - Consumption behavior
        """)

    # =========================================================
    # STORY 3
    # =========================================================

    st.markdown("---")

    st.subheader("Story 3: Time Impacts Revenue")

    st.markdown("""
    ### Narrative
    
    Dinner customers generate much higher bills than lunch customers.
    
    This framing emphasizes:
    - Time-based trends
    - Operational strategy
    - Peak business periods
    """)

    time_revenue = (
        titanic.groupby("time")["fare"]
        .sum()
        .reset_index()
    )

    fig3 = px.bar(
        time_revenue,
        x="time",
        y="fare",
        color="time",
        title="Total Revenue by Time of Day"
    )

    st.plotly_chart(fig3, use_container_width=True)

    with st.expander("Why This Story Works"):
        st.write("""
        This chart reframes the dataset operationally.
        
        Instead of customer demographics,
        it highlights:
        - Revenue timing
        - Operational planning
        - Peak demand periods
        """)

    # =========================================================
    # STORYTELLING TECHNIQUES
    # =========================================================

    st.markdown("---")
    st.header("Professional Storytelling Techniques")

    technique_tabs = st.tabs([
        "Focus",
        "Annotations",
        "Color",
        "Narrative Flow"
    ])

    with technique_tabs[0]:
        st.write("""
        ### Focus Attention
        
        Great dashboards highlight:
        - The most important insight
        - Key outliers
        - Important comparisons
        
        Avoid making everything equally important.
        """)

    with technique_tabs[1]:
        st.write("""
        ### Use Annotations
        
        Add:
        - Labels
        - Callouts
        - Explanations
        - Insights
        
        Help the audience interpret the chart.
        """)

    with technique_tabs[2]:
        st.write("""
        ### Use Color Strategically
        
        Use color to:
        - Guide attention
        - Show categories
        - Highlight anomalies
        
        Avoid unnecessary rainbow palettes.
        """)

    with technique_tabs[3]:
        st.write("""
        ### Build Narrative Flow
        
        Good storytelling has sequence:
        
        1. Introduce context
        2. Show evidence
        3. Reveal insight
        4. Explain implications
        """)

    # =========================================================
    # INTERACTIVE STORY BUILDER
    # =========================================================

    st.markdown("---")
    st.header("Interactive Story Builder")

    st.write("""
    Create your own narrative from the dataset.
    """)

    col1, col2 = st.columns(2)

    with col1:

        x_axis = st.selectbox(
            "Select X-Axis",
            titanic.columns,
            key="story_x"
        )

        chart_type = st.selectbox(
            "Choose Chart Type",
            [
                "Bar Chart",
                "Scatter Plot",
                "Box Plot",
                "Histogram"
            ],
            key="story_chart"
        )

    with col2:

        y_axis = st.selectbox(
            "Select Y-Axis",
            titanic.select_dtypes(include="number").columns,
            key="story_y"
        )

        color = st.selectbox(
            "Color By",
            ["None"] + list(titanic.columns),
            key="story_color"
        )

    # =========================================================
    # DYNAMIC CHART
    # =========================================================

    color_arg = None if color == "None" else color

    if chart_type == "Bar Chart":

        dynamic_fig = px.bar(
            titanic,
            x=x_axis,
            y=y_axis,
            color=color_arg
        )

    elif chart_type == "Scatter Plot":

        dynamic_fig = px.scatter(
            titanic,
            x=x_axis,
            y=y_axis,
            color=color_arg
        )

    elif chart_type == "Box Plot":

        dynamic_fig = px.box(
            titanic,
            x=x_axis,
            y=y_axis,
            color=color_arg
        )

    else:

        dynamic_fig = px.histogram(
            titanic,
            x=x_axis,
            color=color_arg
        )

    st.plotly_chart(dynamic_fig, use_container_width=True)

    # =========================================================
    # STORY GENERATOR
    # =========================================================

    st.subheader("AI-Style Narrative Prompt")

    st.info(f"""
    Your visualization suggests a story about:
    
    - **{x_axis}**
    - impacting or relating to
    - **{y_axis}**
    
    Ask yourself:
    
    1. What is surprising?
    2. What business decision could this influence?
    3. What should the audience remember?
    """)

    # =========================================================
    # MINI QUIZ
    # =========================================================

    st.markdown("---")
    st.header("Storytelling Quiz")

    answer = st.radio(
        "What makes a visualization memorable?",
        [
            "Using the most colors possible",
            "Adding 3D effects",
            "Connecting data to a narrative",
            "Making charts extremely complex"
        ]
    )

    if st.button("Submit Storytelling Answer"):

        if answer == "Connecting data to a narrative":

            st.success("""
            Correct! 🎉
            
            Great storytelling creates emotional
            and cognitive connection.
            """)

            st.session_state.score += 20

            if "Data Storyteller 📖" not in st.session_state.badges:
                st.session_state.badges.append(
                    "Data Storyteller 📖"
                )

        else:

            st.error("""
            Not quite.
            
            Effective storytelling is about clarity,
            meaning, and emotional connection.
            """)

    # =========================================================
    # CAREER CONNECTION
    # =========================================================

    st.markdown("---")
    st.header("Career Bridge")

    st.success("""
    These storytelling skills are used in:
    
    - Business Intelligence
    - Product Analytics
    - Marketing Analytics
    - Data Journalism
    - Executive Reporting
    - Consulting
    - Tableau Development
    - Power BI Dashboarding
    
    Top analysts are not just chart builders —
    they are communicators.
    """)

    # =========================================================
    # SUMMARY
    # =========================================================

    st.markdown("---")
    st.header("Key Takeaways")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.info("""
        ### Same Data
        
        Multiple true stories can exist.
        """)

    with col2:
        st.success("""
        ### Storytelling
        
        Narratives create impact.
        """)

    with col3:
        st.warning("""
        ### Design Intentionally
        
        Every chart framing influences perception.
        """)

