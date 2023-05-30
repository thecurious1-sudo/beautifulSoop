from bs4 import BeautifulSoup

with open('E:/Python/Learning/beautifulSoop/webpage.html','r', encoding="utf8") as html_file:
    content=html_file.read()

    soup=BeautifulSoup(content,'lxml')
    #Approach-2
    courses=soup.find_all('h3',{"data-purpose":"course-title-url"})
    for course in courses:
        print(course.prettify())
        course_a=course.find('a')
        course_title=course_a.contents[0]
        _=course_a.find('div')
        course_rating=_.find('span',{"data-purpose":"seo-rating"}).text
        course_current_price=_.find('span',{"data-purpose":"seo-current-price"}).text
        print(course_title)
        print(course_rating)
        print(course_current_price)
        # break
    #Approach -1
    # all_courses=soup.find_all('div',class_='popper-module--popper--2BpLn')
    # print(all_courses[7].find('div').find_all('div')[1].find('h3').find('a').contents[0])
    # print(all_courses[27].prettify())
    # for i in range(7,len(all_courses)):
    #     print(str(i)+"->"+all_courses[i].find('div').find_all('div')[1].find('h3').find('a').contents[0])