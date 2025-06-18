import streamlit as st
import pandas as pd
import io

def render():
    st.header("📊 Marks Analyzer")

    uploaded_file = st.file_uploader("Upload Marks CSV", type="csv")

    if uploaded_file:
        df = pd.read_csv(uploaded_file)

        required_cols = {"Name", "Reg.No", "Marks"}
        if not required_cols.issubset(df.columns):
            st.error("❌ CSV must have: Name, Reg.No, Marks columns")
            return

        # Stats
        avg = df["Marks"].mean()
        topper_row = df.loc[df["Marks"].idxmax()]
        failed_df = df[df["Marks"] < 50]

        st.success("✅ Marks Analysis Completed")

        st.metric("🧑‍🎓 Total Students", len(df))
        st.metric("📈 Class Average", f"{avg:.2f}")
        st.metric("🥇 Topper", f"{topper_row['Name']} ({topper_row['Marks']})")
        st.metric("❌ Students Below 50", len(failed_df))

        st.subheader("📋 Full Report")
        df["Status"] = df["Marks"].apply(lambda x: "✅ Pass" if x >= 50 else "❌ Fail")
        st.dataframe(df)

        # Excel Download
        excel_buf = io.BytesIO()
        with pd.ExcelWriter(excel_buf, engine="xlsxwriter") as writer:
            df.to_excel(writer, index=False, sheet_name="Marks Report")

        st.download_button(
            label="⬇️ Download Report as Excel",
            data=excel_buf.getvalue(),
            file_name="marks_report.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )
