import requests
from requests.api import head
from bs4 import BeautifulSoup
import csv
import smtplib

# TWO PROBLEMS TO TACKLE
# 1. MAKE AN EXCEL SHEET AND SENT THE EMAIL
# 2. FIX THE ISSUE OF THE RETURN VALUE NOT BEING THE SAME AS THE WEBSITE

URL = "https://www.google.com/search?q=apple+software+engineering+internship&rlz=1C5CHFA_enUS883US883&oq=microsoft+software+engineeri&aqs=chrome.1.69i57j0i512l6j0i457i512j0i512l2&sourceid=chrome&ie=UTF-8&ibp=htl;jobs&sa=X&sqi=2&ved=2ahUKEwjTiY3MvMn1AhUz8uAKHRZvCqkQudcGKAJ6BAgcECM#fpstate=tldetail&htivrt=jobs&htidocid=XLaohtg-iRcAAAAAAAAAAA%3D%3D"
#URL = "https://www.google.com/search?q=meta+software+engineering+new+grad+jobs&rlz=1C5CHFA_enUS883US883&oq=meta+jo&aqs=chrome.0.69i59j69i57j0i512j0i457i512j0i131i433i512j69i60l3&sourceid=chrome&ie=UTF-8&ibp=htl;jobs&sa=X&sqi=2&ved=2ahUKEwi3hMfT17n1AhXQAYgKHVnWCkgQudcGKAJ6BAgmEC8#fpstate=tldetail&htivrt=jobs&htidocid=qFjOeqC3oy4AAAAAAAAAAA%3D%3D"
#URL = "https://www.google.com/search?q=facebook+jobs&rlz=1C5CHFA_enUS883US883&ei=He7kYaXKOKilytMPm9yHqAU&uact=5&oq=facebook+jobs&gs_lcp=Cgdnd3Mtd2l6EAMyBQgAEJECMgsIABCABBCxAxDJAzIFCAAQkQIyBQgAEJECMggIABCxAxCRAjIFCAAQgAQyCAgAEIAEELEDMgUIABCABDIFCAAQgAQyBQgAEIAEOgcIABBHELADOgoIABBHELADEMkDOggIABCSAxCwAzoRCC4QgAQQsQMQgwEQxwEQ0QM6CwguEIAEEMcBEKMCOggIABCxAxCDAToOCC4QgAQQsQMQxwEQowI6EAguELEDEIMBEMcBENEDEEM6BAgAEEM6DgguEIAEELEDEMcBENEDOggILhCxAxCDAToHCAAQyQMQQzoFCAAQkgM6CggAELEDEIMBEEM6CwgAEIAEELEDEIMBSgQIQRgASgQIRhgAUL4HWI8YYNQaaARwAngAgAHKAYgBvgqSAQU1LjYuMZgBAKABAcgBB8ABAQ&sclient=gws-wiz&ibp=htl;jobs&sa=X&ved=2ahUKEwiEkfGY97f1AhWmknIEHWHfDOIQudcGKAJ6BAhGEC8#htivrt=jobs&htidocid=ziv84dK0lUAAAAAAAAAAAA%3D%3D&fpstate=tldetail"
#URL = "https://www.google.com/search?q=yobo+jobs&rlz=1C5CHFA_enUS883US883&oq=google+j&aqs=chrome.1.69i57j0i433i512l2j0i512j0i433i512j69i60l3&sourceid=chrome&ie=UTF-8&ibp=htl;jobs&sa=X&sqi=2&ved=2ahUKEwifob-f9Lf1AhWKQ_EDHSBsDosQudcGKAJ6BAgSEC8#htivrt=jobs&fpstate=tldetail&htichips=date_posted:today&htischips=date_posted;today&htidocid=KlPO9gOXvnQAAAAAAAAAAA%3D%3D"
#URL = "https://stackoverflow.com/questions/56302707/how-can-i-extract-just-the-attribute-title-out-of-this-code"
#URL = 'https://www.linkedin.com/jobs/search/?f_TPR=r86400&keywords=google'
#URL = "https://www.amazon.com/Steve-Madden-Fashion-Sneaker-Fabric/dp/B01LVTT9L7/?_encoding=UTF8&pd_rd_w=YKGKc&pf_rd_p=e3507245-c2c1-4f99-8b1e-89193a9e9975&pf_rd_r=VSCVM8AVB11GQF4ZSC9D&pd_rd_r=6d30e48a-cd24-4538-9c4c-ea38fd6accae&pd_rd_wg=Hz9BV&ref_=pd_gw_bmx_gp_h13jyysn"

headers = {"User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'} # Put your user agent here {user agent}

page = requests.get(URL, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')

company = soup.find_all(["div"], text="Apple", class_="vNEEBe", limit=5)
jobs = soup.find_all(["div"], class_="BjJfJf PUpOsf", limit=5)
links = soup.find_all(["a"], class_="pMhGee Co68jc j0vryd", limit=5)



# WRITING TO A FILE
file = open('searched_jobs.csv', 'w', encoding = 'utf-8') # encode it right away so that we don't have to do for every input
writer = csv.writer(file)

# HEADER
writer.writerow(['Job Title', 'Company Name', 'Location', 'Link to Apply'])

for i in range(4):
    job = jobs[i].string.strip()
    companyName = company[i].text
    location = company[0].next_sibling.string.strip()
    link = links[3]['href'].strip()
    #writer.writerow([job.encode('utf-8'), companyName.encode('utf-8'), location.encode('utf-8'), link.encode('utf-8')])
    writer.writerow([job, companyName, location, link])
    

file.close()

if (company[0] != None):
    send_mail()


def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('maungkaungthukhant@gmail.com', 'password')

    subject = 'Jobs found'
    body = 'Check the attachment below'

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'maungkaungthukhant@gmail.com',
        'kaungkhant@go.rmc.edu',
        msg
    )
    print("Email sent")

    server.quit()



'''
print(jobs[0].string)
print(company[0].string)
print(company[0].next_sibling.string)
print(links[0]['href'])
print()

print(jobs[1].string)
print(company[1].string)
print(company[1].next_sibling.string)
print(links[1]['href'])
print()

print(jobs[2].string)
print(company[2].string)
print(company[2].next_sibling.string)
print(links[2]['href'])
print()

print(jobs[3].string)
print(company[3].string)
print(company[3].next_sibling.string)
print(links[3]['href'])
print()



test = soup.find_all("div", {"class": "vNEEBe"})
print(test[0])
print(test)


meta = soup.find_all(text="Meta")
meta_parent = meta[0].parent
print(meta_parent)


title = soup.find("div", {"class": "vNEEBe"})
company = soup.find("div", {"class": "Qk80Jf"})

print(title.get_text())
print(company.get_text())

#next = soup.find_next("div", {"class": "vNEEBe"})
next = soup.find_next("div", {"class", "vNEEBe"})
print(next)

print(next.get_text())




#title = soup.find(id="H+PMWMbYRb3Mmew8jdkBzQ==")
#title = soup.get_text()
#for link in soup.find_all('a'):
#    print(link.get('href'))
#find = soup.find('a', {'data-control-id': 'H+PMWMbYRb3Mmew8jdkBzQ=='})
#find = soup.find_all('a')
#print(find)
#result = soup.find('a', {"id": "ember554"})
#print(result)

'''