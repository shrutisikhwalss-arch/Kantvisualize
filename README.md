# Kantvisualize Academy

Kantvisualize Academy is an interactive educational web application built using Streamlit that teaches Data Visualization and Storytelling through hands-on experimentation, gamification, and real-world analytical workflows.

The platform focuses not only on chart creation but also on visualization psychology, ethical dashboard design, storytelling techniques, and analytical thinking.

---

## Features

### Cognitive Science of Visualization
Learn how humans perceive visual information through:
- Grammar of Graphics
- Pre-attentive attributes
- Data-Ink Ratio demonstrations

### Chart Selection Engine
Interactive recommendation system that helps users choose the correct chart based on:
- Data type
- Analytical goal
- Visualization purpose

### Visualization Crimes
Learn common visualization mistakes including:
- Truncated axes
- Pie chart overload
- 3D chart distortion
- Misleading color usage

### Storytelling with Data
Understand how the same dataset can tell multiple stories depending on framing, narrative structure, and chart design.

### Interactive Dashboard Sandbox
Build custom interactive dashboards dynamically using:
- Scatter plots
- Bubble charts
- Filters and dimensions
- Real-time visualization controls

### Chart Crimes Quiz
Gamified visualization literacy module with:
- Interactive quizzes
- Practice mode
- XP scoring
- Achievement badges

### Custom Dataset Visualization Lab
Upload your own CSV or Excel datasets and:
- Build visualizations
- Generate dashboards
- Explore storytelling
- Detect visualization issues
- Export cleaned datasets

### About Page
Provides:
- Project overview
- Learning philosophy
- Career relevance
- Technology stack
- Module descriptions

---

## Technologies Used

### Frontend
- Streamlit
- Plotly Express
- Altair

### Data Processing
- Pandas
- NumPy
- OpenPyXL

---

## Project Structure

```text
project/
│
├── app.py
├── requirements.txt
│
├── modules/
│   ├── cognitive_science.py
│   ├── chart_selection_engine.py
│   ├── visualization_crimes.py
│   ├── storytelling_with_data.py
│   ├── dashboard_sandbox.py
│   ├── chart_crimes_quiz.py
│   ├── custom_dataset_lab.py
│   └── about.py
