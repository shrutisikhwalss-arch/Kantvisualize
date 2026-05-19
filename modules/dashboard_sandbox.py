import streamlit as st
import pandas as pd
import plotly.express as px


def run():

    st.title("Module 5")
    st.subheader("Interactive Dashboard Sandbox")

    st.markdown("""
    Welcome to your hands-on analytics lab.

    In this module, you will build your own interactive dashboard
    using real-world data just like professional analysts do in:
    
    - Tableau
    - Power BI
    - Looker Studio
    - Qlik Sense

    Experiment with:
    - Dimensions
    - Measures
    - Colors
    - Bubble sizes
    - Filters
    """)

    st.markdown("---")

    # =========================================================
    # LOAD DATASET
    # =========================================================

    st.header("Dataset: Gapminder Global Development Data")

    st.write("""
    The Gapminder dataset contains information about:
    
    - Countries
    - Population
    - GDP per capita
    - Life expectancy
    - Continents
    - Year
    
    This dataset is widely used for storytelling and dashboarding.
    """)

    df = px.data.gapminder()

    st.success(f"Dataset Loaded Successfully ✅ ({len(df):,} rows)")

    # =========================================================
    # SIDEBAR CONTROLS
    # =========================================================

    st.sidebar.subheader("🎛 Dashboard Controls")

    years = sorted(df["year"].unique())

    selected_year = st.sidebar.select_slider(
        "Select Year",
        options=years,
        value=2007
    )

    filtered_df = df[df["year"] == selected_year]

    numeric_cols = filtered_df.select_dtypes(include="number").columns.tolist()

    categorical_cols = filtered_df.select_dtypes(
        exclude="number"
    ).columns.tolist()

    # =========================================================
    # MAIN CONTROLS
    # =========================================================

    st.header("Build Your Visualization")

    col1, col2 = st.columns(2)

    with col1:

        x_axis = st.selectbox(
            "Select X-Axis",
            numeric_cols,
            index=numeric_cols.index("gdpPercap")
        )

        color_col = st.selectbox(
            "Color By",
            categorical_cols,
            index=categorical_cols.index("continent")
        )

    with col2:

        y_axis = st.selectbox(
            "Select Y-Axis",
            numeric_cols,
            index=numeric_cols.index("lifeExp")
        )

        size_col = st.selectbox(
            "Bubble Size",
            numeric_cols,
            index=numeric_cols.index("pop")
        )

    # =========================================================
    # ADVANCED FILTERS
    # =========================================================

    st.markdown("---")
    st.subheader("Advanced Filters")

    filter_col1, filter_col2 = st.columns(2)

    with filter_col1:

        selected_continents = st.multiselect(
            "Filter by Continent",
            options=sorted(filtered_df["continent"].unique()),
            default=sorted(filtered_df["continent"].unique())
        )

    with filter_col2:

        life_exp_range = st.slider(
            "Life Expectancy Range",
            int(filtered_df["lifeExp"].min()),
            int(filtered_df["lifeExp"].max()),
            (
                int(filtered_df["lifeExp"].min()),
                int(filtered_df["lifeExp"].max())
            )
        )

    # Apply filters
    filtered_df = filtered_df[
        filtered_df["continent"].isin(selected_continents)
    ]

    filtered_df = filtered_df[
        (filtered_df["lifeExp"] >= life_exp_range[0]) &
        (filtered_df["lifeExp"] <= life_exp_range[1])
    ]

    # =========================================================
    # KPI CARDS
    # =========================================================

    st.markdown("---")
    st.header("Dashboard KPIs")

    kpi1, kpi2, kpi3, kpi4 = st.columns(4)

    with kpi1:
        st.metric(
            "Countries",
            filtered_df["country"].nunique()
        )

    with kpi2:
        st.metric(
            "Avg Life Expectancy",
            f"{filtered_df['lifeExp'].mean():.1f}"
        )

    with kpi3:
        st.metric(
            "Avg GDP Per Capita",
            f"${filtered_df['gdpPercap'].mean():,.0f}"
        )

    with kpi4:
        st.metric(
            "Total Population",
            f"{filtered_df['pop'].sum():,.0f}"
        )

    # =========================================================
    # MAIN VISUALIZATION
    # =========================================================

    st.markdown("---")
    st.header("Interactive Bubble Chart")

    fig = px.scatter(
        filtered_df,
        x=x_axis,
        y=y_axis,
        size=size_col,
        color=color_col,
        hover_name="country",
        size_max=60,
        title=f"{y_axis} vs {x_axis} ({selected_year})",
        log_x=True
    )

    fig.update_layout(
        height=650
    )

    st.plotly_chart(fig, use_container_width=True)

    # =========================================================
    # INSIGHT PANEL
    # =========================================================

    st.markdown("---")
    st.header("Insight Generator")

    highest_life = filtered_df.loc[
        filtered_df["lifeExp"].idxmax()
    ]

    highest_gdp = filtered_df.loc[
        filtered_df["gdpPercap"].idxmax()
    ]

    insight_col1, insight_col2 = st.columns(2)

    with insight_col1:

        st.info(f"""
        ### 🌟 Highest Life Expectancy
        
        **Country:** {highest_life['country']}
        
        **Life Expectancy:** {highest_life['lifeExp']:.1f} years
        """)

    with insight_col2:

        st.success(f"""
        ### 💰 Highest GDP Per Capita
        
        **Country:** {highest_gdp['country']}
        
        **GDP Per Capita:** ${highest_gdp['gdpPercap']:,.0f}
        """)

    # =========================================================
    # DASHBOARD DESIGN PRINCIPLES
    # =========================================================

    st.markdown("---")
    st.header("Dashboard Design Principles")

    tabs = st.tabs([
        "Clarity",
        "Interactivity",
        "Visual Hierarchy",
        "Business Focus"
    ])

    with tabs[0]:

        st.write("""
        ### Clarity
        
        Great dashboards:
        - Remove clutter
        - Use readable labels
        - Highlight key insights
        - Simplify complexity
        """)

    with tabs[1]:

        st.write("""
        ### Interactivity
        
        Interactive dashboards allow users to:
        - Filter data
        - Explore trends
        - Drill into insights
        - Personalize analysis
        """)

    with tabs[2]:

        st.write("""
        ### Visual Hierarchy
        
        Arrange visuals by importance:
        
        1. KPIs first
        2. Main chart second
        3. Supporting visuals last
        """)

    with tabs[3]:

        st.write("""
        ### Business Focus
        
        Every dashboard should answer:
        
        - What happened?
        - Why did it happen?
        - What should we do next?
        """)

    # =========================================================
    # SECONDARY VISUALS
    # =========================================================

    st.markdown("---")
    st.header("Supporting Visualizations")

    chart_col1, chart_col2 = st.columns(2)

    with chart_col1:

        continent_avg = (
            filtered_df.groupby("continent")["lifeExp"]
            .mean()
            .reset_index()
        )

        fig_bar = px.bar(
            continent_avg,
            x="continent",
            y="lifeExp",
            color="continent",
            title="Average Life Expectancy by Continent"
        )

        st.plotly_chart(fig_bar, use_container_width=True)

    with chart_col2:

        fig_hist = px.histogram(
            filtered_df,
            x="lifeExp",
            nbins=20,
            title="Distribution of Life Expectancy"
        )

        st.plotly_chart(fig_hist, use_container_width=True)

    # =========================================================
    # DATA TABLE
    # =========================================================

    st.markdown("---")
    st.header("Explore the Data")

    with st.expander("View Dataset Table"):

        st.dataframe(
            filtered_df,
            use_container_width=True
        )

    # =========================================================
    # CAREER BRIDGE
    # =========================================================

    st.markdown("---")
    st.header("Career Bridge")

    st.success("""
    The skills you practiced here directly map to industry tools:
    
    ### Tableau
    - Drag-and-drop visual analytics
    - Dashboard storytelling
    - Interactive filters
    
    ### Power BI
    - Business dashboards
    - KPI reporting
    - Executive analytics
    
    ### Data Analyst Roles
    You are practicing:
    - Exploratory Data Analysis (EDA)
    - Dashboard Development
    - Interactive BI Design
    - Insight Communication
    """)

    # =========================================================
    # MINI CHALLENGE
    # =========================================================

    st.markdown("---")
    st.header("Dashboard Challenge")

    st.write("""
    Which variable appears most strongly related
    to life expectancy?
    """)

    answer = st.radio(
        "Choose your answer:",
        [
            "GDP Per Capita",
            "Country Name",
            "Population Rank",
            "Year Label"
        ]
    )

    if st.button("Submit Dashboard Answer"):

        if answer == "GDP Per Capita":

            st.success("""
            Correct! 🎉
            
            Wealthier countries generally show
            higher life expectancy.
            """)

            st.session_state.score += 20

            if "Dashboard Architect 📊" not in st.session_state.badges:
                st.session_state.badges.append(
                    "Dashboard Architect 📊"
                )

        else:

            st.error("""
            Not quite.
            
            GDP per capita often correlates strongly
            with healthcare quality and life expectancy.
            """)

    # =========================================================
    # SUMMARY
    # =========================================================

    st.markdown("---")
    st.header("Key Takeaways")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.info("""
        ### Dashboards
        
        Combine visuals into one analytical experience.
        """)

    with col2:
        st.success("""
        ### Interactivity
        
        Users should explore data dynamically.
        """)

    with col3:
        st.warning("""
        ### Business Intelligence
        
        Dashboards support decision-making.
        """)

