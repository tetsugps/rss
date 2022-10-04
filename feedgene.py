from feedgen.feed import FeedGenerator

fg = FeedGenerator()
fg.id('http://lernfunk.de/media/654321')
fg.title('テスト')
fg.author({'name': 'John Doe', 'email': 'john@example.de'})
fg.link(href='http://example.com', rel='alternate')
fg.logo('http://ex.com/logo.jpg')
fg.subtitle('This is a cool feed!')
#fg.link(href='http://larskiesow.de/test.atom', rel='self')
fg.language('ja')  # iso639

fg.atom_file("atom.xml")
