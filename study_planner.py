import pandas as pd
import matplotlib.pyplot as plt

# Read Excel sheets
study = pd.read_excel("Study_Planner.xlsx", sheet_name="Study Log")
attendance = pd.read_excel("Study_Planner.xlsx", sheet_name="Attendance")
progress = pd.read_excel("Study_Planner.xlsx", sheet_name="Exam Progress")

# Total study hours
total_hours = study["Actual Hours"].sum()
print("Total Study Hours:", total_hours)

# Attendance percentage
attendance["Attendance %"] = (
    attendance["Attended"] / attendance["Total Classes"] * 100
)


for i in range(len(attendance)):
    if attendance["Attendance %"][i] < 75:
        print("WARNING:",
              attendance["Subject"][i],
              "attendance below 75%")
        
print("\nAttendance Details")
print(attendance)

# Exam progress percentage
progress["Progress %"] = (
    progress["Completed Topics"] / progress["Total Topics"] * 100
)

print("\nExam Progress")
print(progress)

# Attendance Chart
plt.figure(figsize=(6,4))
plt.bar(attendance["Subject"], attendance["Attendance %"])
plt.title("Attendance Percentage")
plt.ylabel("Percentage")
plt.savefig("attendance_chart.png")
plt.show()

# Exam Progress Chart
plt.figure(figsize=(6,4))
plt.bar(progress["Subject"], progress["Progress %"])
plt.title("Exam Preparation Progress")
plt.ylabel("Percentage")
plt.savefig("progress_chart.png")
plt.show()


subject_hours = study.groupby("Subject")["Actual Hours"].sum()

plt.figure(figsize=(6,4))
subject_hours.plot(kind="pie", autopct="%1.1f%%")
plt.title("Study Hours Distribution")
plt.ylabel("")
plt.savefig("study_hours_chart.png")
plt.show()

print("\n------ DASHBOARD SUMMARY ------")

print("Total Study Hours:", total_hours)

avg_attendance = attendance["Attendance %"].mean()
print("Average Attendance:", round(avg_attendance, 2), "%")

avg_progress = progress["Progress %"].mean()
print("Average Exam Progress:", round(avg_progress, 2), "%")
