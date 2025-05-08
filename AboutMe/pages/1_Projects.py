import streamlit as st

st.set_page_config(page_title="Projects | Jingwen Zhang", page_icon="🛠️")

st.title("🛠️ Selected Projects")

st.markdown("### Click to show details :)")

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
    selected = st.button("Performance Analysis Tool")
with col2:
    selected2 = st.button("Trading Records Platform")
with col3:
    selected3 = st.button("Autonomous Driving Data")

# --- Display only one project based on selection
if selected:
    st.header("🚀 Performance Analysis Tool")

    st.markdown("""
#### My role on the team:
**Software Development Engineer** on the Platform Performance team. 

#### Project ideation:  
- Help performance engineers efficiently detect downgrades 
- Automate and improve the analysis of performance test results
- Reduce manual effort and enabling faster, more accurate identification of regressions 
- Addressing key challenges in data analysis, Jira management, and report generation.

#### Business impact:  
- Helps performance engineers quickly validate application performance during daily regression testing. 
- It has greatly reduced manual analysis time, improved visibility of test outcomes, and streamlined Jira ticket generation.
- Faster CI/CD cycle, application maintainence and update.
- Increase customer satisfaction.

#### Project planning:  
Collaboratively planned with engineers on the design and original structure. Designed to be a minimum viable product(MVP).
                
> Streamlit supports both fronted and backend
>
> No large-scale ETL operations
>
> Minimal (not optimal) Infrastructure need
>
> No complex ML model
>
> Automatic jira creation with log
>
> Have its own database for regression and jira tracking

#### Major milestones:  
- Test results Analyzer - Display interactive plots on elapsed time / test result comparison  
- Outlier detection - Use ML model to detect elapsed time outliers  
- Jira Manager - Use ML model to identify downgrade, and enable Jira creation upon detection 
- Automated Reporter - Connecte API into the Jenkins pipeline to achieve automated application downgrade detection
- Inteligent Ticket - Identify correlated tickets and decide whether to comment or create
                
#### Level of responsibility held:  
Design, implement, and maintainence of above modules.
                
#### How was it built:  
Our tool uses a modular design with Flask and Python-based data processing pipelines. Integrated with Jenkins and Jira for ticket management.
Data was stored at AWS S3. All models were deployed to Sagemaker.

#### Outcome:  
TAP is now widely adopted by the Performance team and expanding to other infrastructure teams. 
                It enables scalable, reproducible analysis, and has improved test triage accuracy and efficiency.

#### Key Learnings:  
- Solid backend development of industry level project using python  
- Open-ended task resolution
- From vague problem to exicuable solution
- The value of collaboration and direct user feedback in evolving tool design
                
""")

    # st.subheader("🧱 System Architecture")
    # st.image("assets/perf_tool_arch.png", caption="System Architecture", use_column_width=True)

    st.markdown("### 📚 More Q&As")
    with st.expander("1. What would happen if the outcome did not meet expectations?"):
        st.write("**Prevent bad outcome in advance**: Before implementation, we have formal design document, implementation document, " \
        "and engineers would review these document to make sure we have capability to implement.")
        st.write("**Maintaining after built**: If some functions goes down, user would directly contact my team, and we will identify the error and fix it as quickly as possible " \
        "to maintain the system's avalbility.")
    with st.expander("2. What technical tradeoffs were considered when working on the project?"):
        st.write("Front-end Options: ReactJS vs. Streamlit")
        st.write("Database Options: SQLite vs. MySQL")
        st.write("Model Options: ML vs. DL")
    with st.expander("3. How was the system operated?"):
        st.write("Users could access the web through link, or use the API version that will automatically run in the back every time they runs a test.")
    with st.expander("4. How was it documented?"):
        st.write("We have internal wiki pages that stores all the design documents, implementation documents, and user guide")
    with st.expander("5. If I had to hand this project off to a new team tomorrow, how would I do so?"):
        st.write("I'd provide annotated code, diagrams, runbooks, and host a walkthrough session on CI, API, and components.")
    with st.expander("6. What was cross-functional collaboration like?"):
        st.write("Worked closely with Performance teams. Gathering requirments and feedbacks on product design and model validation.")
    with st.expander("7. If I were to do the same project again, what would you do differently?"):
        st.write("I would take API version into consideration earlier. Since at begining, we only developed an UI version of our tool, which made it become problematic" \
        "when we tired to also have an API verson. The functions inside the UI version contains many frontend code which can not be directly applied " \
        "by the API version. We took about a month to generate the API version and migrate the code.")

elif selected2:
    st.header("📊 Trading Records Platform")
    st.markdown("""
#### My role on the team:  
Backend Developer Intern – designed and migrated data systems

#### Project ideation:  
Built a platform to manage and query trading records with product data entries.

#### Business impact:  
Improved data integrity and query performance; modernized outdated architecture.

#### Project planning:  
Focused on schema design, backend logic, and system migration.

#### Major milestones:  
- Designed MySQL schema with C3P0 connection pooling  
- Migrated platform using Spring MVC and Hibernate  

#### Level of responsibility held:  
Backend ownership, database design, and system performance

#### How was it built:  
Chose Spring stack for Java-based backend, Hibernate for ORM. Focused on efficiency and modularity.

#### Outcome:  
Faster query performance and a scalable backend used by internal product teams.

#### Key Learnings:  
Gained deep understanding of Java Spring ecosystem, and value of modular service architecture.
""")

    # st.markdown("### 📚 More Q&As")
    # with st.expander("1. What would happen if the outcome did not meet expectations?"):
    #     st.write("Manual trading reconciliation would continue to be slow and error-prone.")
    # with st.expander("2. What technical tradeoffs were considered when working on the project?"):
    #     st.write("Relational DB for structure vs. NoSQL for speed; chose MySQL for consistency.")
    # with st.expander("3. How was the system operated and maintained?"):
    #     st.write("Handled via backend service logs and admin dashboard access.")
    # with st.expander("4. How was it documented?"):
    #     st.write("Internal doc for DB schema and API endpoints; Swagger UI planned.")
    # with st.expander("5. If you had to hand this project off to a new team tomorrow, how would you do so?"):
    #     st.write("Provide ER diagram, DB export, and annotated Java services.")
    # with st.expander("6. How does this project affect users upstream and downstream?"):
    #     st.write("Improves finance team's reporting and data team’s ETL quality.")
    # with st.expander("7. What was cross-functional collaboration like?"):
    #     st.write("Collaborated with PM and front-end team for data structure needs.")
    # with st.expander("8. If I were to do the same project again, what would you do differently?"):
    #     st.write("Automate data import pipeline and add caching layer.")

elif selected3:
    st.header("🚗 Autonomous Driving Data Processing")
    st.markdown("""
#### My role on the team:  
Associate Data Scientist Intern – focused on dataset enrichment and quality

#### Project ideation:  
Improve annotation efficiency and fill data gaps in a massive 500K record dataset to support ML engineers.

#### Business impact:  
Increased data quality and model performance; improved annotation efficiency.

#### Level of responsibility held:  
- Annotated data cleaning and migration
- Leading outside data labeling team
- Developed 3D coordinate projection using camera model to project front-view annotations to side-view  
- Enhancing data by appling interpolation for missing values 


#### Outcome:  
Higher quality training data and streamlined annotation workflow.

#### Key Learnings:  
Gained insights into data augmentation and real-world ML data prep. 
Working with diverse teams.
Collaboration and hearing voices from all.
                
""")

    # st.markdown("### 📚 More Q&As")
    # with st.expander("1. What would happen if the outcome did not meet expectations?"):
    #     st.write("Low-quality data would degrade model reliability in autonomous scenarios.")
    # with st.expander("2. What technical tradeoffs were considered when working on the project?"):
    #     st.write("Manual vs. automated annotation; precision vs. throughput.")
    # with st.expander("3. How was the system operated and maintained?"):
    #     st.write("Batch scripts executed regularly and monitored via logs.")
    # with st.expander("4. How was it documented?"):
    #     st.write("Internal wiki page and Python docstrings.")
    # with st.expander("5. If you had to hand this project off to a new team tomorrow, how would you do so?"):
    #     st.write("Provide camera specs, codebase, and a walkthrough of projection/interpolation logic.")
    # with st.expander("6. How does this project affect users upstream and downstream?"):
    #     st.write("Improves model input (upstream) and annotation tools (downstream).")
    # with st.expander("7. What was cross-functional collaboration like?"):
    #     st.write("Worked closely with Data Ops and R&D teams.")
    # with st.expander("8. If I were to do the same project again, what would you do differently?"):
    #     st.write("Include uncertainty estimation in interpolated labels.")
