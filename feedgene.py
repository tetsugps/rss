from feedgen.feed import FeedGenerator
import datetime
import pytz

unaware = datetime.datetime(2011, 8, 15, 8, 15, 12, 0)
aware = datetime.datetime(2011, 8, 15, 8, 15, 12, 0, pytz.UTC)
now = datetime.datetime.now()

logo = "https://prtimes.jp/data/corp/40420/tmp-9c9afdfe87f255d43762faf051399838-4146237a3477a4f2e775a05b4fa06df7.jpg"
url = "https://t-i.jp"

fg = FeedGenerator()
fg.id("0")
fg.title('テスト')
fg.author({'name': 'TI Inc.', 'email': 'info@t-i.jp'})
fg.link(href=url, rel='alternate')
fg.logo(logo)
fg.subtitle('フィードのタイトルです')
fg.link(href=url, rel='self')
fg.language('ja')  # iso639
fg.image(url)

fe = fg.add_entry()
fe.id("1")
fe.title('エントリー１')
fe.link(href=url)
fe.pubDate(now)
fe.content("content")
fe.description("description")

fg.atom_file("atom.xml")
