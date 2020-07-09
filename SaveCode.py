from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import Select



driver=webdriver.Firefox(executable_path='./geckodriver')

driver.get("https://leetcode.com/accounts/login/")
wait =WebDriverWait(driver,60);
element=wait.until(EC.presence_of_element_located((By.ID,'home-app')))

driver.get("https://leetcode.com/problemset/all/?status=Solved")

element = driver.find_element_by_xpath('//*[@id="question-app"]/div/div[2]/div[2]/div[2]/table/tbody[2]/tr/td/span/select')
element.click()

rand=driver.find_element_by_xpath('//*[@id="question-app"]/div/div[2]/div[2]/div[2]/table/tbody[2]/tr/td/span/select/option[4]')
rand.click()


problemset=driver.find_elements_by_tag_name('a')
i=1;
j=1
link=[]
name=[]
comment_link=[]
for problem in problemset:
	x=problem.get_attribute("data-slug")
	if x is not None:
		print(i)
		print(x)
		name.append(x)
		i=i+1
		comment_link.append("#"+"https://leetcode.com/problems/"+x+"/")
		url="https://leetcode.com/problems/"+x+"/submissions/"
		link.append(url)

subm=[]
k=0
for url in link:
 	driver.get(url)
 	driver.implicitly_wait(10)
 	ac=driver.find_elements_by_class_name('ac__35gz')
 	subm.append(ac[0].get_attribute('href'))
 	
k=0
for url in subm:
 	driver.get(url)
 	driver.implicitly_wait(30)
 	sol=driver.find_elements_by_class_name('ace_line')
 	filename=name[k]+".cpp" 	
 	file=open(filename,"a")
 	file.write(comment_link[k]+"\n")
 	for line in sol:
 		l=line.text
 		file.write(l+"\n")
 	file.close()
 	k=k+1


# driver.get("https://leetcode.com/submissions/detail/333285062/")
# sol=driver.find_elements_by_class_name('ace_line')
# for line in sol:
# 	l=line.text
# 	print(l)
	
print("Thank You!")
print(driver.title)
