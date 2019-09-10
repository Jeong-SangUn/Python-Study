import csv, sqlite3

con = sqlite3.connect("./memory.db")
cur = con.cursor()
cur.execute('''
create table if not exists stocks(
    no text,
    score text,      
    movie text,
    content text,
    author text,
    date text
    )
''') # use your column names here

with open('crawling/review.csv','rt',encoding='utf-8') as csvfile: # `with` statement available in 2.5+
    # csv.DictReader uses first line in file for column headings by default
    read = csv.reader(csvfile, delimiter=',') # comma is default delimiter
    to_db = [(i[0], i[1], i[2], i[3], i[4], i[5]) for i in read]

cur.executemany("INSERT INTO stocks (no, score, movie, content, author, date) VALUES (?, ?, ?, ?, ?, ?);", to_db)
con.commit()
con.close()