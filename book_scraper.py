import requests
from bs4 import BeautifulSoup

def scrape_book_data(url):
  """从给定的 Amazon 图书页面 URL 抓取图书数据（标题、作者、价格）。"""

  try:
    response = requests.get(url)
    response.raise_for_status()  # 对于非 200 状态码引发异常

    soup = BeautifulSoup(response.content, "html.parser")
    book_title = soup.find("span", id="productTitle").text.strip()
    book_author = soup.find("a", class_="a-link-normal contributorNameID").text.strip()
    book_price = soup.find("span", class_="a-offscreen").text.strip()

    return {
      "title": book_title,
      "author": book_author,
      "price": book_price
    }

  except requests.exceptions.RequestException as e:
    print("抓取 URL 时出错：", e)
    return None

# 示例用法：
book_url = "https://www.amazon.com/dp/0593480546"  # 替换为实际的图书 URL
book_data = scrape_book_data(book_url)
if book_data:
  print("标题：", book_data["title"])
  print("作者：", book_data["author"])
  print("价格：", book_data["price"])
