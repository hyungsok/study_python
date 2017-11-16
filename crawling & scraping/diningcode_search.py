from selenium import webdriver
 
print("## 검색어를 입력하시오. ")
keyword = input()

# 드라이버 추출하기
driver = webdriver.Chrome()

# 검색 페이지 로딩 ( 3초 기다림 )
path = "https://www.diningcode.com/isearch.php?query=" + keyword
driver.get(path)
print("## 페이지 로딩", path, sep=' : ')
driver.implicitly_wait(3)

# 추천 카테고리로 가져오기
# //*[@id="main_area"]/div[1]/div[3]/div/div/div[1]/a[4]
tags = driver.find_elements_by_xpath("//*[@id='main_area']/div/div/div/div/div/a")
print("## '", keyword, "' 추천 카테고리")
for tag in tags :
    if tag.text :
        print("\t - ", tag.text)

print("## 추천 레스토랑 ")
# //*[@id="main_area"]/div[3]/div[3]/div[1]/div[3]/div[2]/div[1]/a
resturant_names = driver.find_elements_by_xpath("//*[@id='main_area']/div/div/div/div/div/div/a")
for name in resturant_names :
    print("\t - ", name.text)