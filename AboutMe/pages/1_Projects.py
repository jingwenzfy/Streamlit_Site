import streamlit as st

st.set_page_config(page_title="Projects | Jingwen Zhang", page_icon="🛠️")

st.title("🛠️ Selected Projects")

st.markdown("### Click to show details")

# Apply CSS to enforce equal button width
st.markdown(
    """
    <style>
    div.stButton > button {
        width: 100%;
    }
    </style>
    """,
    unsafe_allow_html=True
)

col1, col2, col3 = st.columns(3)

with col1:
    selected = st.button("Major Project: **Performance Analysis Tool**")
with col2:
    selected2 = st.button("Intern Project: **Trading Records Platform**")
with col3:
    selected3 = st.button("Intern Project: **Autonomous Driving Data Processing**")

# --- Display only one project based on selection
if selected:
    st.header("🚀 Performance Analysis Tool (TAP)")

    st.markdown("""
**My role on the team:**  
**Software Development Engineer** on the Platform Performance team. 
                I contributed to the development of a machine-learning-powered test analysis tool designed to 
                help performance engineers efficiently assess application performance across CI runs.

**Project ideation:**  
Our goal was to automate and improve the analysis of performance test results, 
                reducing manual effort and enabling faster, more accurate identification of regressions. 
                Addressing key challenges in data analysis, Jira management, and report generation.

**Business impact:**  
TAP helps performance engineers quickly validate application performance during daily CI and regression testing. It has reduced manual analysis time by over 80%, improved visibility of test outcomes, and streamlined Jira ticket generation.

**Project planning:**  
Collaboratively planned with senior engineers and co-supervisors. Key milestones included defining core modules, creating reusable components, and integrating the tool into the Jenkins CI pipeline.

**Major milestones:**  
- Designed and implemented modular Python-based TAP backend  
- Built preprocessing pipeline for test artifacts and Metricbeat logs  
- Developed Analyzer, Reporter, and Jira Manager modules  
- Trained ML models for outlier detection and test case recommendation  
- Created automated HTML reports with visual insights (GC plots, throughput, system metrics)

**Level of responsibility held:**  
I held end-to-end ownership of several modules including Analyzer enhancements and Reporter HTML generation, collaborating cross-functionally and receiving co-supervision from a principal data scientist.

**How was it built:**  
TAP uses a modular design with Flask APIs and Python-based data processing pipelines. Key ML components combine statistical analysis and semantic embeddings (e.g., TF-IDF) for log comparison. Integrated with Jenkins and Jira for CI-based execution and ticket management.

**Outcome:**  
TAP is now widely adopted by the Vault Platform Performance team and expanding to Application Performance teams. It enables scalable, reproducible analysis, and has improved test triage accuracy and efficiency.

**Key Learnings:**  
- The importance of modular, maintainable tooling in performance environments  
- How to balance interpretability with automation in ML-driven workflows  
- The value of collaboration and direct user feedback in evolving tool design
""")

    # st.subheader("🧱 System Architecture")
    # st.image("assets/perf_tool_arch.png", caption="TAP System Architecture", use_column_width=True)

    st.markdown("### 📚 More Q&As")
    with st.expander("1. What would happen if the outcome did not meet expectations?"):
        st.write("Without TAP, test analysis would remain manual and error-prone, slowing down the release cycle and increasing risk of regressions reaching production.")
    with st.expander("2. What technical tradeoffs were considered when working on the project?"):
        st.write("We weighed rule-based vs ML-based detection, Flask vs FastAPI, and considered tradeoffs between performance, scalability, and interpretability.")
    with st.expander("3. How was the system operated and maintained?"):
        st.write("The CLI version runs via Jenkins pipelines; logs and reports are archived. HTML output makes triage accessible to both engineers and PMs.")
    with st.expander("4. How was it documented?"):
        st.write("The tool has GitHub markdown docs, onboarding guides, architecture diagrams, and internal wiki pages.")
    with st.expander("5. If you had to hand this project off to a new team tomorrow, how would you do so?"):
        st.write("I'd provide annotated code, diagrams, runbooks, and host a walkthrough session on CI, API, and ML components.")
    with st.expander("6. How does this project affect users upstream and downstream?"):
        st.write("Upstream, it allows QA and Platform teams to validate builds faster. Downstream, it feeds reliable defect reports into engineering workflows via Jira.")
    with st.expander("7. What was cross-functional collaboration like?"):
        st.write("Worked closely with QA, Infrastructure, and Application Performance teams. Also co-supervised by a Principal Data Scientist on product design and model validation.")
    with st.expander("8. If I were to do the same project again, what would you do differently?"):
        st.write("I'd introduce earlier modularization, build structured logging, and design a plug-in framework to make adding new analysis types easier.")

elif selected2:
    st.header("📊 Trading Records Platform")
    st.markdown("""
**My role on the team:**  
Backend Developer Intern – designed and migrated data systems

**Project ideation:**  
Built a platform to manage and query trading records with over 1M product data entries.

**Business impact:**  
Improved data integrity and query performance; modernized outdated architecture.

**Project planning:**  
Focused on schema design, backend logic, and system migration.

**Major milestones:**  
- Designed MySQL schema with C3P0 connection pooling  
- Migrated platform using Spring MVC and Hibernate  
- Built Redis and JWT-powered authentication

**Level of responsibility held:**  
Backend ownership, database design, and system performance

**How was it built:**  
Chose Spring stack for Java-based backend, Hibernate for ORM. Focused on efficiency and modularity.

**Outcome:**  
Faster query performance and a scalable backend used by internal product teams.

**Key Learnings:**  
Gained deep understanding of Java Spring ecosystem, and value of modular service architecture.
""")

    st.markdown("### 📚 More Q&As")
    with st.expander("1. What would happen if the outcome did not meet expectations?"):
        st.write("Manual trading reconciliation would continue to be slow and error-prone.")
    with st.expander("2. What technical tradeoffs were considered when working on the project?"):
        st.write("Relational DB for structure vs. NoSQL for speed; chose MySQL for consistency.")
    with st.expander("3. How was the system operated and maintained?"):
        st.write("Handled via backend service logs and admin dashboard access.")
    with st.expander("4. How was it documented?"):
        st.write("Internal doc for DB schema and API endpoints; Swagger UI planned.")
    with st.expander("5. If you had to hand this project off to a new team tomorrow, how would you do so?"):
        st.write("Provide ER diagram, DB export, and annotated Java services.")
    with st.expander("6. How does this project affect users upstream and downstream?"):
        st.write("Improves finance team's reporting and data team’s ETL quality.")
    with st.expander("7. What was cross-functional collaboration like?"):
        st.write("Collaborated with PM and front-end team for data structure needs.")
    with st.expander("8. If I were to do the same project again, what would you do differently?"):
        st.write("Automate data import pipeline and add caching layer.")

elif selected3:
    st.header("🚗 Autonomous Driving Data Processing")
    st.markdown("""
**My role on the team:**  
Associate Data Scientist Intern – focused on dataset enrichment and quality

**Project ideation:**  
Improve annotation efficiency and fill data gaps in a massive 500K record dataset.

**Business impact:**  
Increased data quality and model performance; improved annotation throughput by 50%.

**Project planning:**  
Targeted 3D-to-2D projection, interpolation, and data quality metrics

**Major milestones:**  
- Developed 3D coordinate projection using camera model  
- Projected front-view annotations to side-view  
- Applied interpolation for missing values  
- Outlier analysis and quality metrics generation

**Level of responsibility held:**  
Led design of interpolation and projection methods

**How was it built:**  
Used camera model math and OpenCV-style transforms for projection. Custom interpolation scripts written in Python.

**Outcome:**  
Higher quality training data and streamlined annotation workflow.

**Key Learnings:**  
Gained insights into data augmentation and real-world ML data prep.
""")

    st.markdown("### 📚 More Q&As")
    with st.expander("1. What would happen if the outcome did not meet expectations?"):
        st.write("Low-quality data would degrade model reliability in autonomous scenarios.")
    with st.expander("2. What technical tradeoffs were considered when working on the project?"):
        st.write("Manual vs. automated annotation; precision vs. throughput.")
    with st.expander("3. How was the system operated and maintained?"):
        st.write("Batch scripts executed regularly and monitored via logs.")
    with st.expander("4. How was it documented?"):
        st.write("Internal wiki page and Python docstrings.")
    with st.expander("5. If you had to hand this project off to a new team tomorrow, how would you do so?"):
        st.write("Provide camera specs, codebase, and a walkthrough of projection/interpolation logic.")
    with st.expander("6. How does this project affect users upstream and downstream?"):
        st.write("Improves model input (upstream) and annotation tools (downstream).")
    with st.expander("7. What was cross-functional collaboration like?"):
        st.write("Worked closely with Data Ops and R&D teams.")
    with st.expander("8. If I were to do the same project again, what would you do differently?"):
        st.write("Include uncertainty estimation in interpolated labels.")
