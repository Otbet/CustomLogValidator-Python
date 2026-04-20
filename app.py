import streamlit as st
import pandas as pd
import time
from validator import validate_logs

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Custom Log Validator", 
    page_icon="🔍", 
    layout="wide"
)

# --- HEADER ---
st.title("🔍 Custom Log Validator")
st.markdown("Quickly verify which tests executed by cross-referencing your test list with application logs.")
st.divider()

# --- INPUT SECTION (Side-by-Side Columns) ---
col1, col2 = st.columns(2)

with col1:
    st.subheader("📝 Test List")
    tests_input = st.text_area(
        "Enter tests (one per line):", 
        height=300, 
        placeholder="test_login_module\ntest_database_connection\ntest_checkout_flow"
    )

with col2:
    st.subheader("📄 Log Content")
    log_content = st.text_area(
        "Paste log output here:", 
        height=300, 
        placeholder="[INFO] test_login_module passed successfully..."
    )

# --- ACTION BUTTON ---
# use_container_width makes it a large, prominent button
if st.button("Validate Logs", type="primary", use_container_width=True):
    
    if not tests_input.strip() or not log_content.strip():
        st.warning("⚠️ Please provide both the Test List and the Log Content to proceed.")
    else:
        # Show a loading spinner for a better UX
        with st.spinner("Analyzing logs..."):
            time.sleep(0.5) # Slight delay so the UI doesn't flash too fast
            results = validate_logs(tests_input, log_content)
            
            # --- RESULTS SECTION ---
            st.success("Validation Complete!")
            
            df = pd.DataFrame(results)
            
            passed = len(df[df['Status'] == 'OK'])
            failed = len(df[df['Status'] == 'NOT OK'])
            total = len(df)
            
            # 1. Metrics Dashboard
            st.subheader("📊 Summary")
            m1, m2, m3 = st.columns(3)
            m1.metric(label="Total Tests", value=total)
            m2.metric(label="Passed ✅", value=passed)
            m3.metric(label="Failed ❌", value=failed)
            
            st.divider()
            
            # 2. Styled Data Table
            st.subheader("📋 Detailed Results")
            
            # Function to color-code the pandas dataframe rows/cells
            def color_status(val):
                color = '#00c04b' if val == 'OK' else '#ff4b4b'
                return f'color: {color}; font-weight: bold'
            
            styled_df = df.style.map(color_status, subset=['Status'])
            
            # Render the table in the UI
            st.dataframe(styled_df, use_container_width=True, hide_index=True)