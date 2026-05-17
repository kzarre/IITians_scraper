from linked_scraper import define_and_scrape
import pandas as pd
import random
import time

s = 7

for n in range(s, 8):
	print(f"CURRENTLY ON FILE: {n}")
	df = pd.read_excel(f"students/students{n}.xlsx")
	urls = list(df["linkedin"])
	companies = define_and_scrape(urls)
	df["company"] = companies
	df.to_excel(f"students/students{n}.xlsx", index=False)
	time.sleep(random.uniform(420 ,600))
