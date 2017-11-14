import requests, webbrowser, bs4

print("## input google keyword? ")
keyword = input()

# Get방식으로 검색 요청 
res = requests.get("http://www.google.co.kr/search?q="+keyword)
res.raise_for_status()

# 모든 결과 찾기
soup = bs4.BeautifulSoup(res.text, "lxml")
"""
    <h3 class="r">
        <a href="http://korean.visitseoul.net/eat" onmousedown="return rwt(this,'','','','4','AOvVaw1QxHWP5Hu1Qi812ycJD9V3','','0ahUKEwiAmsvviL7XAhVDk5QKHeiRCNQQFghlMAM','','',event)" target="_blank">
            맛집 - 서울특별시 - 음식점 : Visit Seoul - 서울시 공식 관광정보 웹사이트
        </a>
    </h3>

"""
# r CSS 클래스안에 있는 모든 <a> 엘리먼트를 찾아라 (.<CSS class> <tag>)
linkElements = soup.select('.r a')

# 검색결과 출력
for element in linkElements[:5] :
    print("\t", element.text)
    print("\t>> ", element.get('href'))
    