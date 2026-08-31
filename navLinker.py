url  = "https://mrmcfee0.github.io/VideoQuizzes/"
page_nav = "#page-"

nav_links= []


for num in range(1,51):
    nav_links.append(url + page_nav\
                      + str(num))


print(nav_links)