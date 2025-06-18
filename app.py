import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import joblib
import warnings
warnings.filterwarnings('ignore')

# Page configuration
st.set_page_config(
    page_title="Jaya Jaya Institut - Dropout Prediction",
    page_icon="🎓",
    layout="wide"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
    }
    .prediction-high {
        background: linear-gradient(135deg, #ff6b6b 0%, #ee5a24 100%);
        padding: 1rem;
        border-radius: 10px;
        color: white;
        text-align: center;
    }
    .prediction-medium {
        background: linear-gradient(135deg, #feca57 0%, #ff9ff3 100%);
        padding: 1rem;
        border-radius: 10px;
        color: white;
        text-align: center;
    }
    .prediction-low {
        background: linear-gradient(135deg, #48dbfb 0%, #0abde3 100%);
        padding: 1rem;
        border-radius: 10px;
        color: white;
        text-align: center;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown('<h1 class="main-header">🎓 Jaya Jaya Institut<br>Student Dropout Prediction System</h1>', unsafe_allow_html=True)

# Load model function
@st.cache_resource
def load_trained_model():
    """Load the trained model from notebook"""
    try:
        # Try to load complete artifacts first
        artifacts = joblib.load('model_artifacts_complete.pkl')
        model = artifacts['model']
        scaler = artifacts.get('scaler', None)
        feature_names = artifacts['feature_names']
        performance_metrics = artifacts['performance_metrics']
        
        return {
            'model': model,
            'scaler': scaler,
            'feature_names': feature_names,
            'performance_metrics': performance_metrics,
            'artifacts': artifacts,
            'status': 'complete'
        }
        
    except FileNotFoundError:
        try:
            # Fallback to individual files
            model = joblib.load('dropout_prediction_model.pkl')
            try:
                scaler = joblib.load('feature_scaler.pkl')
            except:
                scaler = None
            
            return {
                'model': model,
                'scaler': scaler,
                'feature_names': None,
                'performance_metrics': None,
                'artifacts': None,
                'status': 'basic'
            }
            
        except FileNotFoundError:
            return {
                'model': None,
                'scaler': None,
                'feature_names': None,
                'performance_metrics': None,
                'artifacts': None,
                'status': 'not_found'
            }
    
    except Exception as e:
        return {
            'model': None,
            'scaler': None,
            'feature_names': None,
            'performance_metrics': None,
            'artifacts': None,
            'status': f'error: {e}'
        }

# Load model data
model_data = load_trained_model()

# Navigation
st.sidebar.title("🎯 Navigation")
page = st.sidebar.radio(
    "Choose a page:",
    ["🏠 Home", "📊 Prediction", "📈 Analytics", "ℹ️ About"],
    key="navigation_radio"
)

# Model status in sidebar
st.sidebar.markdown("---")
st.sidebar.markdown("### 🤖 Model Status")
if model_data['status'] == 'complete':
    st.sidebar.success("✅ Complete Model Loaded")
elif model_data['status'] == 'basic':
    st.sidebar.warning("⚠️ Basic Model Loaded")
elif model_data['status'] == 'not_found':
    st.sidebar.error("❌ Model Not Found")
else:
    st.sidebar.error(f"❌ Error: {model_data['status']}")

if page == "🏠 Home":
    st.markdown("## Welcome to the Student Dropout Prediction System")
    
    # Model status
    if model_data['model'] is not None:
        st.success("🤖 Machine Learning Model: Ready")
        
        if model_data['performance_metrics']:
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Model Accuracy", f"{model_data['performance_metrics']['accuracy']:.1%}")
            with col2:
                st.metric("F1-Score", f"{model_data['performance_metrics']['f1_score']:.3f}")
            with col3:
                cv_mean = model_data['performance_metrics'].get('cross_val_mean', 0)
                if cv_mean > 0:
                    st.metric("CV Score", f"{cv_mean:.3f}")
    else:
        st.error("🚫 Model not loaded. Please run the notebook first.")
        st.info("Required files: model_artifacts_complete.pkl or dropout_prediction_model.pkl")
    
    # Key Statistics
    st.markdown("## 📊 System Overview")
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Total Students", "4,424")
    with col2:
        st.metric("Dropout Rate", "32.1%")
    with col3:
        st.metric("At-Risk Students", "15%")
    with col4:
        if model_data['performance_metrics']:
            st.metric("Model Accuracy", f"{model_data['performance_metrics']['accuracy']:.1%}")
        else:
            st.metric("Model Status", "Ready" if model_data['model'] else "Not Ready")

elif page == "📊 Prediction":
    st.markdown("## 🔮 Student Dropout Risk Prediction")
    
    if model_data['model'] is None:
        st.error("❌ Model not loaded! Please run the notebook first.")
        st.stop()
    
    # Create prediction form
    with st.form("prediction_form", clear_on_submit=False):
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("### 👤 Personal Information")
            age_at_enrollment = st.slider("Age at Enrollment", 17, 35, 20, key="age_slider")
            gender = st.selectbox("Gender", ["Female", "Male"], key="gender_select")
            marital_status = st.selectbox(
                "Marital Status", 
                [1, 2, 3, 4, 5, 6], 
                format_func=lambda x: ["Single", "Married", "Divorced", "Widowed", "Other", "Unknown"][x-1],
                key="marital_select"
            )
            
            st.markdown("### 💰 Financial Information")
            tuition_fees = st.selectbox("Tuition Fees Up to Date", ["No", "Yes"], key="tuition_select")
            scholarship = st.selectbox("Scholarship Holder", ["No", "Yes"], key="scholarship_select")
        
        with col2:
            st.markdown("### 📚 Academic Performance")
            prev_grade = st.slider("Previous Qualification Grade", 50.0, 200.0, 120.0, key="prev_grade_slider")
            admission_grade = st.slider("Admission Grade", 50.0, 200.0, 130.0, key="admission_slider")
            
            st.markdown("### 📈 Semester Performance")
            sem1_grade = st.slider("1st Semester Grade", 0.0, 20.0, 12.0, key="sem1_slider")
            sem2_grade = st.slider("2nd Semester Grade", 0.0, 20.0, 12.0, key="sem2_slider")
        
        submitted = st.form_submit_button("🔮 Predict Dropout Risk", use_container_width=True)
        
        if submitted:
            try:
                # Prepare input data
                input_data = {
                    'Age_at_enrollment': age_at_enrollment,
                    'Gender': 1 if gender == "Male" else 0,
                    'Marital_status': marital_status,
                    'Tuition_fees_up_to_date': 1 if tuition_fees == "Yes" else 0,
                    'Scholarship_holder': 1 if scholarship == "Yes" else 0,
                    'Previous_qualification_grade': prev_grade,
                    'Admission_grade': admission_grade,
                    'Curricular_units_1st_sem_grade': sem1_grade,
                    'Curricular_units_2nd_sem_grade': sem2_grade,
                }
                
                # Create input DataFrame
                if model_data['feature_names']:
                    # Use exact feature names from training
                    input_df = pd.DataFrame(0, index=[0], columns=model_data['feature_names'])
                    for key, value in input_data.items():
                        if key in model_data['feature_names']:
                            input_df[key] = value
                else:
                    # Fallback: create with available features
                    input_df = pd.DataFrame([list(input_data.values())[:10]])
                
                # Apply scaling if available
                if model_data['scaler'] is not None:
                    numerical_cols = input_df.select_dtypes(include=[np.number]).columns
                    input_df[numerical_cols] = model_data['scaler'].transform(input_df[numerical_cols])
                
                # Make prediction
                prediction = model_data['model'].predict(input_df)[0]
                prediction_proba = model_data['model'].predict_proba(input_df)[0]
                dropout_risk = prediction_proba[1] if len(prediction_proba) > 1 else prediction_proba[0]
                
                # Display results
                st.markdown("---")
                st.markdown("## 🎯 Prediction Results")
                
                col1, col2, col3 = st.columns(3)
                
                with col1:
                    if dropout_risk > 0.7:
                        st.markdown(f"""
                        <div class="prediction-high">
                            <h3>⚠️ HIGH RISK</h3>
                            <h2>{dropout_risk:.1%}</h2>
                            <p>Immediate intervention needed</p>
                        </div>
                        """, unsafe_allow_html=True)
                    elif dropout_risk > 0.3:
                        st.markdown(f"""
                        <div class="prediction-medium">
                            <h3>⚡ MEDIUM RISK</h3>
                            <h2>{dropout_risk:.1%}</h2>
                            <p>Monitor and support</p>
                        </div>
                        """, unsafe_allow_html=True)
                    else:
                        st.markdown(f"""
                        <div class="prediction-low">
                            <h3>✅ LOW RISK</h3>
                            <h2>{dropout_risk:.1%}</h2>
                            <p>Continue monitoring</p>
                        </div>
                        """, unsafe_allow_html=True)
                
                with col2:
                    # Risk gauge
                    fig = go.Figure(go.Indicator(
                        mode = "gauge+number",
                        value = dropout_risk * 100,
                        title = {'text': "Dropout Risk %"},
                        gauge = {
                            'axis': {'range': [None, 100]},
                            'bar': {'color': "darkblue"},
                            'steps': [
                                {'range': [0, 30], 'color': "lightgreen"},
                                {'range': [30, 70], 'color': "yellow"},
                                {'range': [70, 100], 'color': "red"}
                            ]
                        }
                    ))
                    fig.update_layout(height=300)
                    st.plotly_chart(fig, use_container_width=True)
                
                with col3:
                    st.markdown("### 📋 Risk Factors")
                    risk_factors = []
                    
                    if sem1_grade < 10:
                        risk_factors.append("Low 1st semester grade")
                    if sem2_grade < 10:
                        risk_factors.append("Low 2nd semester grade")
                    if tuition_fees == "No":
                        risk_factors.append("Tuition payment issues")
                    if age_at_enrollment > 25:
                        risk_factors.append("Older enrollment age")
                    
                    if risk_factors:
                        for factor in risk_factors:
                            st.markdown(f"⚠️ {factor}")
                    else:
                        st.markdown("✅ No major risk factors")
                
                # Recommendations
                st.markdown("### 🎯 Recommendations")
                if dropout_risk > 0.7:
                    st.error("**Immediate Action Required:**")
                    st.markdown("- Contact student within 24 hours\n- Assign academic advisor\n- Review financial aid")
                elif dropout_risk > 0.3:
                    st.warning("**Proactive Support:**")
                    st.markdown("- Schedule check-in meeting\n- Monitor progress closely\n- Offer tutoring")
                else:
                    st.success("**Continue Monitoring:**")
                    st.markdown("- Regular progress reviews\n- Maintain support systems")
                
            except Exception as e:
                st.error(f"Error making prediction: {e}")

elif page == "📈 Analytics":
    st.markdown("## 📈 Model Performance Analytics")
    
    if model_data['performance_metrics']:
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("Accuracy", f"{model_data['performance_metrics']['accuracy']:.1%}")
        with col2:
            st.metric("F1-Score", f"{model_data['performance_metrics']['f1_score']:.3f}")
        with col3:
            cv_mean = model_data['performance_metrics'].get('cross_val_mean', 0)
            if cv_mean > 0:
                st.metric("CV Score", f"{cv_mean:.3f}")
        with col4:
            cv_std = model_data['performance_metrics'].get('cross_val_std', 0)
            if cv_std > 0:
                st.metric("CV Std", f"{cv_std:.3f}")
    
    # Sample charts
    col1, col2 = st.columns(2)
    
    with col1:
        # Risk distribution
        risk_data = pd.DataFrame({
            'Risk_Level': ['Low Risk', 'Medium Risk', 'High Risk'],
            'Count': [2650, 1110, 664]
        })
        
        fig = px.pie(risk_data, values='Count', names='Risk_Level', 
                     title="Student Risk Distribution")
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        # Performance trend
        months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
        rates = [34.5, 33.8, 32.2, 31.9, 30.7, 32.1]
        
        fig = px.line(x=months, y=rates, title="Dropout Rate Trend")
        st.plotly_chart(fig, use_container_width=True)

elif page == "ℹ️ About":
    st.markdown("## ℹ️ About This System")
    
    st.markdown("""
    ### 🎓 Jaya Jaya Institut Student Dropout Prediction System
    
    Developed by: **Andre Gregori Sangari**  
    Email: andresangari12@gmail.com  
    Dicoding ID: andregregs12
    
    This system uses machine learning to predict student dropout risk
    and provide early intervention recommendations.
    """)
    
    if model_data['artifacts'] and 'training_info' in model_data['artifacts']:
        training_info = model_data['artifacts']['training_info']
        
        st.markdown("### 🔬 Model Information")
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown(f"""
            - **Algorithm**: {model_data['artifacts'].get('model_name', 'Unknown')}
            - **Training Samples**: {training_info.get('training_samples', 'N/A')}
            - **Features**: {training_info.get('features_count', 'N/A')}
            """)
        
        with col2:
            if model_data['performance_metrics']:
                st.markdown(f"""
                - **Accuracy**: {model_data['performance_metrics']['accuracy']:.1%}
                - **F1-Score**: {model_data['performance_metrics']['f1_score']:.3f}
                - **Training Date**: {training_info.get('training_date', 'Unknown')}
                """)

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666; font-size: 0.8em;'>
    <p>© 2024 Jaya Jaya Institut - Student Dropout Prediction System</p>
    <p>Developed by Andre Gregori Sangari | Dicoding ID: andregregs12</p>
</div>
""", unsafe_allow_html=True)