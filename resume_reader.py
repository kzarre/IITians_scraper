import requests
from io import BytesIO
from pypdf  import PdfReader
import re

url = "https://iitg.ac.in/placements/api/uploads/cv/file-1725515475465-6649737365c1ed6e2-275f-407b-b683-b3d4ae0b9027.pdf"

def get_webpdf(url):
	response = requests.get(url)
	pdf = PdfReader(BytesIO(response.content))
	return pdf

def get_embedded(page):
	links = []
	if "/Annots" in page:
		for annot in page['/Annots']:
			obj = annot.get_object()
			if "/A" in obj and "/URI" in obj["/A"]:
				
				links.append(obj["/A"]["/URI"])
	return links

def get_phone(page):
	text = page.extract_text().split("\n")
	for line in text:
		phone = re.findall(r"(?:\+91[-\s]?)?[6-9]\d{9}", line)
		if phone:
			return phone[0]

def get_personal_info(pdf):
	pages = pdf.pages
	embedded = get_embedded(pages[0])

	linkedin = ""
	email = ""
	phone = ""

	for uri in embedded:
		if re.match(r".*linkedin.com/.*", uri):
			linkedin = uri
		elif re.match(r"mailto:[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.com", uri):
			email = uri[7:]

	phone = get_phone(pages[0])

	return linkedin or "", email or "", phone or ""

if __name__=="__main__":

	pdf = get_webpdf(url)
	print(get_personal_info(pdf))