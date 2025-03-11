import requests
from bs4 import BeautifulSoup

# URL trang web cần lấy dữ liệu
url = "https://vnexpress.net/kinh-doanh/chung-khoan"

# Gửi yêu cầu HTTP đến trang web
response = requests.get(url)
response.encoding = 'utf-8'

# Kiểm tra xem yêu cầu có thành công không
if response.status_code == 200:
    # Phân tích nội dung HTML
    soup = BeautifulSoup(response.text, "html.parser")
    
    # Lấy tiêu đề các bài báo
    articles = soup.find_all("h2", class_="title-news")
    
    print("📢 DANH SÁCH BÀI VIẾT CHỨNG KHOÁN MỚI NHẤT 📢\n")
    for article in articles:
        title = article.a.get_text(strip=True)
        link = article.a["href"]
        print(f"- {title}\n  Link: {link}\n")
else:
    print("Không thể lấy dữ liệu từ trang web!")
