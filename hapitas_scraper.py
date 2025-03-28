import requests
from bs4 import BeautifulSoup
from datetime import datetime
from database import db, PointHistory, app

def get_sbi_points():
    url = "https://hapitas.jp/item/detail/itemid/53979/apn/sf_general_carousel_spot"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
    }
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")
        return None
    
    soup = BeautifulSoup(response.text, "html.parser")
    point_element = soup.find(class_="calculated_detail_point") 
    
    if point_element:
        points = int(point_element.get_text(strip=True).replace(',', ''))
        return points
    else:
        print("ポイント情報が見つかりませんでした。")
        return None

def save_points_to_db(points, site):
    date_today = datetime.now().strftime('%Y-%m-%d')
    
    with app.app_context():
        new_entry = PointHistory(date=date_today, site=site, points=points)
        db.session.add(new_entry)
        db.session.commit()
        print(f"データベースに {points} ポイントを保存しました。")

if __name__ == "__main__":
    points = get_sbi_points()
    if points:
        print(f"SBI証券の獲得ポイント数: {points}")
        save_points_to_db(points, site="SBI証券")
