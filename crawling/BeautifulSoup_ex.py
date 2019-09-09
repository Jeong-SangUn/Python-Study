from bs4 import BeautifulSoup

html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b id="boldest">The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""
soup = BeautifulSoup(html,'html.parser')

# print(soup.title)

# print(soup.title.name)

# print(soup.title.string)

print(soup.title.parent)

# print(soup.p)

# print(soup.find_all('p'))
# for className in soup.find_all('p'):
#     print(className.get('class'))

# print(soup.a)

# print(soup.find_all('a'))

# print(soup.find(id="link3"))

# for link in soup.find_all('a'):
#     print(link.get('href'))

# print(soup.get_text())

tag = soup.b
# print(type(tag))
# print(tag.name)
# tag.name = "blockquote"
# print(tag)
# print(soup)

# print(tag['id'])
# print(tag.attrs)


# tag['id'] = 'verybold'
# tag['another-attribute'] = 1
# print(tag)

# del tag['id']
# del tag['another-attribute']
# print(tag)

# #print(tag['id'])
# # KeyError: 'id'

# print(tag.get('id'))
# # None

# css_soup = BeautifulSoup('<p class="body"></p>','html.parser')
# print(css_soup.p['class'])
# # ["body"]

# css_soup = BeautifulSoup('<p class="body strikeout"></p>','html.parser')
# print(css_soup.p['class'])
# # ["body", "strikeout"]

# id_soup = BeautifulSoup('<p id="my id"></p>','html.parser')
# print(id_soup.p['id'])
# # 'my id'

# rel_soup = BeautifulSoup('<p>Back to the <a rel="index">homepage</a></p>','html.parser')
# print(rel_soup.a['rel'])
# # ['index']
# rel_soup.a['rel'] = ['index', 'contents']
# print(rel_soup.p)
# # <p>Back to the <a rel="index contents">homepage</a></p>

# xml_soup = BeautifulSoup('<p class="body strikeout"></p>', 'xml')
# print(xml_soup.p['class'])
# # u'body strikeout'

# head_tag = soup.head
# print(head_tag)
# # <head><title>The Dormouse's story</title></head>

# print(head_tag.contents)

# #[<title>The Dormouse's story</title>]

# title_tag = head_tag.contents[0]
# print(title_tag)
# # <title>The Dormouse's story</title>

# print(title_tag.contents)
# # [u'The Dormouse's story']

# print(len(soup.contents))
# # 1
# print(soup.contents[0].name)
# # u'html'

# for string in soup.strings:
#     print(repr(string))

# for string in soup.stripped_strings:
#     print(repr(string))

# title_tag = soup.title
# print(title_tag)
# # <title>The Dormouse's story</title>

# print(title_tag.parent)
# # <head><title>The Dormouse's story</title></head>    

# print(title_tag.string.parent)
# # <title>The Dormouse's story</title>

# html_tag = soup.html
# print(type(html_tag.parent))
# # <class 'bs4.BeautifulSoup'>

# print(soup.parent)
# # None

# link = soup.a
# print(link)
# # <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>
# for parent in link.parents:
#     if parent is None:
#         print(parent)
#     else:
#         print(parent.name)
# # p
# # body
# # html
# # [document]
# # None

# sibling_soup = BeautifulSoup("<a><b>text1</b><c>text2</c></b></a>")
# print(sibling_soup.prettify())
# # <html>
# #  <body>
# #   <a>
# #    <b>
# #     text1
# #    </b>
# #    <c>
# #     text2
# #    </c>
# #   </a>
# #  </body>
# # </html>

# print(sibling_soup.b.next_sibling)
# # <c>text2</c>

# print(sibling_soup.c.previous_sibling)
# # <b>text1</b>

# print(sibling_soup.b.string)
# # u'text1'

# print(sibling_soup.b.string.next_sibling)
# # None

# for sibling in soup.a.next_siblings:
#     print(repr(sibling))
# # u',\n'
# # <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>
# # u' and\n'
# # <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>
# # u'; and they lived at the bottom of a well.'
# # None

# for sibling in soup.find(id="link3").previous_siblings:
#     print(repr(sibling))
# # ' and\n'
# # <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>
# # u',\n'
# # <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>
# # u'Once upon a time there were three little sisters; and their names were\n'
# # None

# last_a_tag = soup.find("a", id="link3")
# print(last_a_tag)
# # <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>

# print(last_a_tag.next_sibling)
# # '; and they lived at the bottom of a well.'

# print(last_a_tag.next_element)
# # u'Tillie'

# print(last_a_tag.previous_element)
# # u' and\n'
# print(last_a_tag.previous_element.next_element)
# # <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>

# for element in last_a_tag.next_elements:
#     print(repr(element))
# # u'Tillie'
# # u';\nand they lived at the bottom of a well.'
# # u'\n\n'
# # <p class="story">...</p>
# # u'...'
# # u'\n'
# # None