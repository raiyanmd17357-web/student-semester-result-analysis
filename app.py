

import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Student_ID": [101, 102, 103, 104, 105],
    "Name": ["Aman", "Riya", "Arjun", "Priya", "Rahul"],
    "Semester_1": [65, 72, 60, 68, 55],
    "Semester_2": [70, 74, 58, 72, 60],
    "Semester_3": [75, 76, 62, 74, 63],
    "Semester_4": [80, 78, 65, 79, 67]
}

df = pd.DataFrame(data)
df.to_csv("student_results.csv", index=False)


df = pd.read_csv("student_results.csv")
print("Dataset:\n")
print(df)

semester_cols = ["Semester_1", "Semester_2", "Semester_3", "Semester_4"]
df["Average"] = df[semester_cols].mean(axis=1)

print("\nDataset with Average:\n")
print(df)

plt.figure()

for index, row in df.iterrows():
    plt.plot(
        [1, 2, 3, 4],
        row[semester_cols],
        marker="o",
        label=row["Name"]
    )

plt.title("Student Performance Across Semesters")
plt.xlabel("Semester")
plt.ylabel("Marks")
plt.xticks([1, 2, 3, 4])
plt.legend()
plt.grid(True)
plt.show()
plt.figure()
plt.bar(df["Name"], df["Average"])
plt.title("Overall Student Performance Comparison")
plt.xlabel("Student Name")
plt.ylabel("Average Marks")
plt.grid(axis="y")
plt.show()
print("\nClass Average:", round(df['Average'].mean(), 2))
print("\nTop Performer:", df.loc[df['Average'].idxmax(), 'Name'])
print("Lowest Performer:", df.loc[df['Average'].idxmin(), 'Name'])
