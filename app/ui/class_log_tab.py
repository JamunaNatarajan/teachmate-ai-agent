import streamlit as st
import pandas as pd
from datetime import date
import io
import os

# CSV file to store logs
LOG_FILE = "class_logs.csv"

def render():
    st.header("📘 Class Log Entry")

    # Log Entry Form
    with st.form("log_form"):
        class_date = st.date_input("Date", value=date.today())
        subject = st.text_input("Subject")
        topic = st.text_input("Topic / Unit Covered")
        section = st.text_input("Section / Class")
        homework = st.text_area("Homework / Task Given (optional)")
        remarks = st.text_area("Remarks (optional)")
        submit = st.form_submit_button("✅ Save Entry")

    if submit:
        new_entry = {
            "Date": class_date,
            "Subject": subject,
            "Topic": topic,
            "Section": section,
            "Homework": homework,
            "Remarks": remarks
        }

        if os.path.exists(LOG_FILE):
            df = pd.read_csv(LOG_FILE)
            df = pd.concat([df, pd.DataFrame([new_entry])], ignore_index=True)
        else:
            df = pd.DataFrame([new_entry])

        df.to_csv(LOG_FILE, index=False)
        st.success("✅ Class log entry saved!")

    # Show log history
    if os.path.exists(LOG_FILE):
        st.subheader("📋 Log History")
        df = pd.read_csv(LOG_FILE)
        st.dataframe(df)
    buffer = io.BytesIO()

    with pd.ExcelWriter(buffer, engine="xlsxwriter") as writer:
        df.to_excel(writer, sheet_name="Class Logs", index=False, startrow=6)

        workbook = writer.book
        worksheet = writer.sheets["Class Logs"]

        header_format = workbook.add_format({
            "bold": True,
            "align": "center",
            "valign": "vcenter",
            "font_size": 14
        })
        worksheet.merge_range("A1:F1", "Kongunadu College of Engineering and Technology", header_format)

        title_format = workbook.add_format({
            "align": "center",
            "font_size": 12,
            "italic": True
        })
        worksheet.merge_range("A2:F2", "Class Log Report", title_format)

        date_format = workbook.add_format({
            "align": "right",
            "font_size": 10
        })
        today = date.today().strftime("%d-%m-%Y")
        worksheet.write("F3", f"Date: {today}", date_format)

        header_cell_format = workbook.add_format({
            "bold": True,
            "bg_color": "#D9E1F2",
            "border": 1,
            "align": "center"
        })
        for col_num, col_name in enumerate(df.columns.values):
            worksheet.write(6, col_num, col_name, header_cell_format)

        cell_format = workbook.add_format({"border": 1})
        for row in range(7, 7 + len(df)):
            for col in range(len(df.columns)):
                value = df.iloc[row - 7, col]
                if pd.isna(value):
                    value = ""
                worksheet.write(row, col, value, cell_format)

        for i, col in enumerate(df.columns):
            column_width = max(df[col].astype(str).map(len).max(), len(col)) + 2
            worksheet.set_column(i, i, column_width)

    st.download_button(
        label="⬇️ Download Class Log (Excel)",
        data=buffer.getvalue(),
        file_name="class_log_report.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        key="class_log_download"
    )
        