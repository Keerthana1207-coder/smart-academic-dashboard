import pandas as pd
import matplotlib.pyplot as plt
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from reportlab.pdfgen import canvas


def open_dashboard():

    # Excel Read
    study = pd.read_excel(
        "Study_Planner.xlsx",
        sheet_name="Study Log"
    )

    attendance = pd.read_excel(
        "Study_Planner.xlsx",
        sheet_name="Attendance"
    )

    progress = pd.read_excel(
        "Study_Planner.xlsx",
        sheet_name="Exam Progress"
    )

    goals = pd.read_excel(
        "Study_Planner.xlsx",
        sheet_name="Goals"
    )

    streak = pd.read_excel(
        "Study_Planner.xlsx",
        sheet_name="Streak"
    )

    # Calculations

    total_hours = study["Actual Hours"].sum()

    attendance["Attendance %"] = (
        attendance["Attended"] /
        attendance["Total Classes"] * 100
    )

    avg_attendance = attendance["Attendance %"].mean()

    progress["Progress %"] = (
        progress["Completed Topics"] /
        progress["Total Topics"] * 100
    )

    avg_progress = progress["Progress %"].mean()

    actual_hours = study.groupby(
        "Subject"
    )["Actual Hours"].sum()

    current_streak = streak[
        "Current Streak"
    ][0]

    # Alert

    if avg_attendance < 75:

        messagebox.showwarning(
            "Attendance Alert",
            "Attendance is below 75%"
        )

    # Charts

    def show_attendance_chart():

        plt.figure(figsize=(6,4))

        plt.bar(
            attendance["Subject"],
            attendance["Attendance %"]
        )

        plt.title(
            "Attendance Percentage"
        )

        plt.ylabel("Percentage")

        plt.show()

    def show_progress_chart():

        plt.figure(figsize=(6,4))

        plt.bar(
            progress["Subject"],
            progress["Progress %"]
        )

        plt.title(
            "Exam Progress"
        )

        plt.ylabel("Percentage")

        plt.show()

    def weekly_report():

        weekly_hours = study.groupby(
            "Date"
        )["Actual Hours"].sum()

        plt.figure(figsize=(7,4))

        weekly_hours.plot(
            kind="line",
            marker="o"
        )

        plt.title(
            "Weekly Study Report"
        )

        plt.ylabel("Hours")

        plt.show()

    # PDF

    def generate_pdf():

        pdf = canvas.Canvas(
            "Study_Report.pdf"
        )

        pdf.setFont(
            "Helvetica-Bold",
            16
        )

        pdf.drawString(
            150,
            800,
            "Study Planner Report"
        )

        pdf.setFont(
            "Helvetica",
            12
        )

        pdf.drawString(
            100,
            760,
            f"Total Study Hours: {total_hours}"
        )

        pdf.drawString(
            100,
            730,
            f"Average Attendance: {avg_attendance:.2f}%"
        )

        pdf.drawString(
            100,
            700,
            f"Exam Progress: {avg_progress:.2f}%"
        )

        pdf.save()

        print(
            "PDF Generated Successfully"
        )

    # Excel Export

    def export_excel():

        summary = pd.DataFrame({

            "Metric": [

                "Total Hours",

                "Attendance %",

                "Exam Progress %"

            ],

            "Value": [

                total_hours,

                avg_attendance,

                avg_progress

            ]

        })

        summary.to_excel(

            "Dashboard_Summary.xlsx",

            index=False

        )

        print(
            "Excel Report Saved"
        )

    # GUI

    root = Tk()

    root.title(
        "Smart Academic Dashboard"
    )

    root.geometry(
        "800x800"
    )

    root.configure(
        bg="#1E1E1E"
    )

    Label(

        root,

        text="📚 Smart Academic Dashboard",

        font=("Arial",16,"bold"),

        bg="#1E1E1E",

        fg="white"

    ).pack(pady=10)

    Label(

        root,

        text=f"🔥 Study Streak: {current_streak} Days",

        bg="#1E1E1E",

        fg="orange",

        font=("Arial",12,"bold")

    ).pack(pady=5)

    Label(

        root,

        text=f"Total Study Hours : {total_hours}",

        bg="#1E1E1E",

        fg="white"

    ).pack()

    Label(

        root,

        text=f"Average Attendance : {avg_attendance:.2f}%",

        bg="#1E1E1E",

        fg="white"

    ).pack()

    attendance_bar = ttk.Progressbar(

        root,

        length=300,

        mode="determinate"

    )

    attendance_bar["value"] = avg_attendance

    attendance_bar.pack(
        pady=5
    )

    Label(

        root,

        text=f"Exam Progress : {avg_progress:.2f}%",

        bg="#1E1E1E",

        fg="white"

    ).pack()

    progress_bar = ttk.Progressbar(

        root,

        length=300,

        mode="determinate"

    )

    progress_bar["value"] = avg_progress

    progress_bar.pack(
        pady=5
    )

    # Goal Tracking

    Label(

        root,

        text="🎯 Goal Progress",

        bg="#1E1E1E",

        fg="yellow",

        font=("Arial",13,"bold")

    ).pack(pady=10)

    for i in range(len(goals)):

        subject = goals["Subject"][i]

        target = goals["Goal Hours"][i]

        actual = actual_hours.get(
            subject,
            0
        )

        percentage = (
            actual / target
        ) * 100

        Label(

            root,

            text=f"{subject}: {percentage:.1f}% Goal Completed",

            bg="#1E1E1E",

            fg="yellow"

        ).pack()

    Button(

        root,

        text="Show Attendance Chart",

        command=show_attendance_chart,

        width=25

    ).pack(pady=5)

    Button(

        root,

        text="Show Progress Chart",

        command=show_progress_chart,

        width=25

    ).pack(pady=5)

    Button(

        root,

        text="Weekly Report",

        command=weekly_report,

        width=25

    ).pack(pady=5)

    Button(

        root,

        text="Generate PDF Report",

        command=generate_pdf,

        width=25

    ).pack(pady=5)

    Button(

        root,

        text="Export Excel Report",

        command=export_excel,

        width=25

    ).pack(pady=5)

    root.mainloop()
