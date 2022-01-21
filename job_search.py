import requests
from requests.api import head
from bs4 import BeautifulSoup



print()
print()
print()
print()

URL = "https://www.google.com/search?q=netflix+jobs&rlz=1C5CHFA_enUS883US883&oq=netflix+j&aqs=chrome.1.69i57j0i433i457i512j0i433i512j0i131i433i512j46i175i199i433i512j0i512j46i433i512j0i512j0i131i433i512j46i512&sourceid=chrome&ie=UTF-8&ibp=htl;jobs&sa=X&sqi=2&ved=2ahUKEwjZlt-r78H1AhU7QfEDHYmHBpcQudcGKAJ6BAgmEC8#htivrt=jobs&fpstate=tldetail&htichips=date_posted:today&htischips=date_posted;today&htidocid=IcSMkAJ36sQAAAAAAAAAAA%3D%3D"
#URL = "https://www.google.com/search?q=meta+software+engineering+new+grad+jobs&rlz=1C5CHFA_enUS883US883&oq=meta+jo&aqs=chrome.0.69i59j69i57j0i512j0i457i512j0i131i433i512j69i60l3&sourceid=chrome&ie=UTF-8&ibp=htl;jobs&sa=X&sqi=2&ved=2ahUKEwi3hMfT17n1AhXQAYgKHVnWCkgQudcGKAJ6BAgmEC8#fpstate=tldetail&htivrt=jobs&htidocid=qFjOeqC3oy4AAAAAAAAAAA%3D%3D"
#URL = "https://www.google.com/search?q=facebook+jobs&rlz=1C5CHFA_enUS883US883&ei=He7kYaXKOKilytMPm9yHqAU&uact=5&oq=facebook+jobs&gs_lcp=Cgdnd3Mtd2l6EAMyBQgAEJECMgsIABCABBCxAxDJAzIFCAAQkQIyBQgAEJECMggIABCxAxCRAjIFCAAQgAQyCAgAEIAEELEDMgUIABCABDIFCAAQgAQyBQgAEIAEOgcIABBHELADOgoIABBHELADEMkDOggIABCSAxCwAzoRCC4QgAQQsQMQgwEQxwEQ0QM6CwguEIAEEMcBEKMCOggIABCxAxCDAToOCC4QgAQQsQMQxwEQowI6EAguELEDEIMBEMcBENEDEEM6BAgAEEM6DgguEIAEELEDEMcBENEDOggILhCxAxCDAToHCAAQyQMQQzoFCAAQkgM6CggAELEDEIMBEEM6CwgAEIAEELEDEIMBSgQIQRgASgQIRhgAUL4HWI8YYNQaaARwAngAgAHKAYgBvgqSAQU1LjYuMZgBAKABAcgBB8ABAQ&sclient=gws-wiz&ibp=htl;jobs&sa=X&ved=2ahUKEwiEkfGY97f1AhWmknIEHWHfDOIQudcGKAJ6BAhGEC8#htivrt=jobs&htidocid=ziv84dK0lUAAAAAAAAAAAA%3D%3D&fpstate=tldetail"
#URL = "https://www.google.com/search?q=yobo+jobs&rlz=1C5CHFA_enUS883US883&oq=google+j&aqs=chrome.1.69i57j0i433i512l2j0i512j0i433i512j69i60l3&sourceid=chrome&ie=UTF-8&ibp=htl;jobs&sa=X&sqi=2&ved=2ahUKEwifob-f9Lf1AhWKQ_EDHSBsDosQudcGKAJ6BAgSEC8#htivrt=jobs&fpstate=tldetail&htichips=date_posted:today&htischips=date_posted;today&htidocid=KlPO9gOXvnQAAAAAAAAAAA%3D%3D"
#URL = "https://stackoverflow.com/questions/56302707/how-can-i-extract-just-the-attribute-title-out-of-this-code"
#URL = 'https://www.linkedin.com/jobs/search/?f_TPR=r86400&keywords=google'
#URL = "https://www.amazon.com/Steve-Madden-Fashion-Sneaker-Fabric/dp/B01LVTT9L7/?_encoding=UTF8&pd_rd_w=YKGKc&pf_rd_p=e3507245-c2c1-4f99-8b1e-89193a9e9975&pf_rd_r=VSCVM8AVB11GQF4ZSC9D&pd_rd_r=6d30e48a-cd24-4538-9c4c-ea38fd6accae&pd_rd_wg=Hz9BV&ref_=pd_gw_bmx_gp_h13jyysn"

headers = {"User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'}

page = requests.get(URL, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')

location = soup.find_all(["div"], text="Netflix", class_="vNEEBe", limit=5)
jobs = soup.find_all(["div"], class_="BjJfJf PUpOsf", limit=5)
links = soup.find_all(["a"], class_="pMhGee Co68jc j0vryd", limit=5)

print(jobs[0].string)
print(location[0].string)
print(location[0].next_sibling.string)
print(links[0]['href'])
print()

print(jobs[1].string)
print(location[1].string)
print(location[1].next_sibling.string)
print(links[1]['href'])
print()

print(jobs[2].string)
print(location[2].string)
print(location[2].next_sibling.string)
print(links[2]['href'])
print()

print(jobs[3].string)
print(location[3].string)
print(location[3].next_sibling.string)
print(links[3]['href'])
print()


'''
test = soup.find_all("div", {"class": "vNEEBe"})
print(test[0])
print(test)


meta = soup.find_all(text="Meta")
meta_parent = meta[0].parent
print(meta_parent)


title = soup.find("div", {"class": "vNEEBe"})
location = soup.find("div", {"class": "Qk80Jf"})

print(title.get_text())
print(location.get_text())

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