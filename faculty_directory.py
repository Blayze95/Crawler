"""Michael Chung - mjc13b"""

from __future__ import print_function
import requests
import lxml
import re

url = "http://www.cs.fsu.edu/department/faculty/"
main_page = requests.get(url)


def get_faculty_pages():
	link = re.findall(r'<a href="([^"]+)"><strong>(.*?)</strong>', main_page.text, re.S)
	staff = []
	#if link:
	#	print("Name: {}".format(link.group(2)))
	#	print("Webpage: {}{}".format(url, link.group(1)))
	#	staff.append([link.group(1), link.group(2)])

	for staffurl, name in link:
		#print("Name: {}".format(name))
		#("Link: {}{}".format(url, staffurl))
		staff.append([name, staffurl])

	#for x in staff:
		#print(x)

	return staff

def get_info(nurl):
	newpage = requests.get(nurl)
	info = []

	if re.search(url, nurl):
		office = re.search(r'Office:.*?<td>(.*?)</td>', newpage.text, re.S)
		phone = re.search(r'Telephone:.*?<td>(.*?)</td>', newpage.text, re.S)
		contact = re.search(r'E-Mail:.*?<td>(.*?)</', newpage.text, re.S)

	else:
		office = re.search(r'.*?field-office.*?>(.*?)</div>', newpage.text, re.S)
		phone = re.search(r'.*?Phone.*?item">(.*?)</div>', newpage.text, re.S)
		contact = re.search(r'.*?mailto.*?">(.*?)</a>', newpage.text, re.S)


	if office:
		
		if office.group(1) == "":
			print(u"Office: N/A")
			info.append("Office: N/A")

		else:
			print(u"Office: {}".format(office.group(1)))
			info.append(office.group(1))

	if phone:
		if phone.group(1) == "":
			print(u"Telephone: N/A")
			info.append("Telephone: N/A")

		else:
			print(u"Telephone: {}".format(phone.group(1)))
			info.append(phone.group(1))


	if contact:
		if contact.group(1) == "":
			print(u"E-Mail: N/A")
			info.append(u"E-MAil: N/A")

		else:
		
			print(u"E-Mail: {}".format(contact.group(1)))
			info.append(contact.group(1))



if __name__ == "__main__":
	staffinfo = dict()
	staffpages = get_faculty_pages()

	for i in staffpages:
		print("Name: {}".format(i[0]))
		staffinfo[i[0]] = get_info(i[1])
		print("*"*30)
