students = {
    1: {
        "name": "harshal gholap",
        "age": 16,
        "attendance": [],
        "marks": {}
    }
}

def mark_attendance(student_id):
    status = input("Enter attendance (P/A): ").upper()
    if status in ["P", "A"]:
        students[student_id]["attendance"].append(status)
        print("✅ ATTENDANCE MARKED")
    else:
        print("❌ INVALID INPUT")

def add_marks(student_id):
    subject = input("Enter subject name: ")
    score = float(input("Enter marks: "))

    if subject not in students[student_id]["marks"]:
        students[student_id]["marks"][subject] = []

    students[student_id]["marks"][subject].append(score)
    print("✅ MARKS ADDED")

def attendance_percentage(student_id):
    records = students[student_id]["attendance"]
    if len(records) == 0:
        return 0.0
    present = records.count("P")
    return round((present / len(records)) * 100, 2)

def progress_analysis(student_id):
    marks_data = students[student_id]["marks"]

    print("\n--- PROGRESS & RISK ANALYSIS ---")

    if len(marks_data) == 0:
        print("No marks data available.")
        return

    for subject, scores in marks_data.items():
        if len(scores) < 2:
            print(f"{subject}: Not enough data")
            continue

        trend = scores[-1] - scores[0]
        avg = sum(scores) / len(scores)

        if trend > 5:
            status = "📈 Improving"
        elif trend < -5:
            status = "📉 Declining"
        else:
            status = "➖ Stable"

        risk = "⚠️ At Risk" if avg < 35 else "✅ Safe"
        print(f"{subject}: {status} | Avg: {round(avg,1)} | {risk}")

def student_report(student_id):
    student = students[student_id]

    print("\n==============================")
    print("        STUDENT REPORT        ")
    print("==============================")
    print("Name:", student["name"])
    att = attendance_percentage(student_id)
    print("Attendance:", att, "%")

    if att < 75:
        print("⚠️ Attendance Warning!")

    if len(student["marks"]) == 0:
        print("Marks: No tests yet!")
    else:
        print("\nMarks:")
        for subject, scores in student["marks"].items():
            print(f"{subject}: {scores}")

    progress_analysis(student_id)
    print("==============================")

def main():
    student_id = 1

    while True:
        print("\n1. MARK ATTENDANCE")
        print("2. ADD TEST MARKS")
        print("3. VIEW STUDENT REPORT")
        print("4. EXIT")

        choice = input("Choose option: ")

        if choice == "1":
            mark_attendance(student_id)

        elif choice == "2":
            add_marks(student_id)

        elif choice == "3":
            student_report(student_id)

        elif choice == "4":
            print("System closed.")
            break
        
        else:
            print("Invalid choice!")

main()

