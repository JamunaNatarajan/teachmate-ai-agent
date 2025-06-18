import streamlit as st
import pandas as pd
import io

def render():
    st.header("📊 Attendance Report Generator")

    uploaded_file = st.file_uploader("Upload attendance CSV", type="csv")

    if uploaded_file:
        df = pd.read_csv(uploaded_file)

        # Validate required columns
        required_columns = {"Name", "Reg.No", "Present Days", "Total Days"}
        if not required_columns.issubset(df.columns):
            st.error("❌ Invalid file format. Make sure your CSV contains: Name, Reg.No, Present Days, Total Days.")
            return

        # Calculate % Attendance
        df["% Attendance"] = (df["Present Days"] / df["Total Days"]) * 100

        # Add status column
        df["Status"] = df["% Attendance"].apply(
            lambda x: "✅ OK" if x >= 75 else ("⚠️ Borderline" if x >= 65 else "❌ Low")
        )

        # Show Report
        st.success("✅ Attendance Report Generated")
        st.dataframe(df.style.highlight_max(axis=0, color='lightgreen'))
        # Excel Export Code
        excel_buffer = io.BytesIO()
        with pd.ExcelWriter(excel_buffer, engine="xlsxwriter") as writer:
            df.to_excel(writer, index=False, sheet_name="Attendance Report")

        st.download_button(
            label="⬇️ Download Report as Excel",
            data=excel_buffer.getvalue(),
            file_name="attendance_report.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )
        # Show metrics
        st.metric("📈 Class Average", f"{df['% Attendance'].mean():.2f}%")
        st.metric("🧑‍🎓 Total Students", len(df))
        st.metric("🚨 Students <75%", sum(df["% Attendance"] < 75))
