from csv_reader import get_resume_list
from resume_reader import get_webpdf, get_personal_info
import pandas as pd
import os

count = len(os.listdir("students"))

eligible_branches = ["Computer Science and Engineering", "Data Science and Artificial Intelligence", "Electronics and Communication Engineering" , "Mathematics and Computing", "Signal Processing and Machine Learning", "Systems, Control and Automation", "Robotics and Artificial Intelligence", "Data Science"]
CSV_FILE = "iit_resume.xlsx"

students = []

student_profiles = get_resume_list(CSV_FILE, eligible_branches)

linkedin_urls = []
i=1
for idx, row in student_profiles.iloc[300:].iterrows():
	print(i, idx)

	name = row["name"]
	resume = row["resume"]
	pdf = get_webpdf(resume)
	linkedin, email, phone = get_personal_info(pdf)
	

	students.append({
	"index": idx,
	"name": name,
	"resume": resume,
	"phone": phone,
	"email": email,
	"linkedin": linkedin,
	"company": ""
	})
	

	if i%50==0:
		df = pd.DataFrame(students)
		df.to_excel(f"students/students7.xlsx", index=False)
		students = []
	
	i+=1
