import pandas as pd 

eligible_branches = ["Computer Science and Engineering", "Data Science and Artificial Intelligence", "Electronics and Communication Engineering" , "Mathematics and Computing", "Signal Processing and Machine Learning", "Systems, Control and Automation", "Robotics and Artificial Intelligence", "Data Science"]
CSV_FILE = "iit_resume.xlsx"


def get_resume_list(CSV_FILE, eligible_branches):
    df = pd.read_excel(CSV_FILE, header=None, names=["name", "cg", "branch", "course", "resume", "resume2", "drive"])
    df_cleaned = df[df["branch"].isin(eligible_branches)]

    df_cleaned = df_cleaned.dropna(subset=["resume"])
    df_cleaned = df_cleaned[df_cleaned["resume"].str.endswith(".pdf", na=False)]

    return df_cleaned[["name", "resume"]]

f = get_resume_list(CSV_FILE, eligible_branches)