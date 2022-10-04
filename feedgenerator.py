import feedgenerator

feed = feedgenerator.Rss201rev2Feed(
    title="あいうえお",
    link="http://www.poynter.org/column.asp?id=31",
    description=
    "かきくけこ",
    language="ja", )

feed.add_item(
    title="Hello",
    link="http://www.holovaty.com/test/",
    description="さしすせそ")

with open('test.rss', 'w') as fp:
    feed.write(fp, 'utf-8')

print(feed.writeString('utf-8'))