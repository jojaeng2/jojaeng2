import feedparser, time

URL="https://jojaeng2.tistory.com/rss" 
RSS_FEED = feedparser.parse(URL)


markdown_text = '![image](https://user-images.githubusercontent.com/76645095/162124599-f9d701d6-e523-49c4-a6ce-193dc38f1026.png)'
markdown_text += """

## ✅ Latest Blog Post

"""  # list of blog posts will be appended here

MAX_POST = 5
for idx, feed in enumerate(RSS_FEED['entries']):
    if idx > MAX_POST:
        break
    else:
        feed_date = feed['published_parsed']
        markdown_text += f"[{time.strftime('%Y/%m/%d', feed_date)} - {feed['title']}]({feed['link']}) <br/>\n"
        
f = open("README.md", mode="w", encoding="utf-8")
f.write(markdown_text)
f.close()
