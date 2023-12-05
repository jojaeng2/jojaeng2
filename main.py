import feedparser, time

URL="http://rss.blog.naver.com/ds4ouj" 
RSS_FEED = feedparser.parse(URL)

markdown_text = '![image](./image/231205.png){: width="100%" height="40%"}'
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
