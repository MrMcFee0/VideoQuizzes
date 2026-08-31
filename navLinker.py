url  = "https://mrmcfee0.github.io/VideoQuizzes/"
page_nav = "#page-"
page_ct = 40


def generate_nav_links(main_url, nav_format, count):
    links = []
    for num in range(1, count + 1):
        links.append(main_url + nav_format + str(num))
    return links

l = generate_nav_links(url, page_nav, page_ct)
print(l)