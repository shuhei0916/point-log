import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime

def get_sbi_points():
    url = "https://hapitas.jp/item/detail/itemid/53979/apn/sf_general_carousel_spot"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
    }
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an error for bad status codes
    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")
        return None
    
    soup = BeautifulSoup(response.text, "html.parser")

    point_element = soup.find(class_="calculated_detail_point") 
    if point_element:
        points = point_element.get_text(strip=True)
        return points
    else:
        print("ポイント情報が見つかりませんでした。")
        return None

def save_points_to_csv(points, site, filename='points.csv'):
    date_today = datetime.now().strftime('%Y-%m-%d')  # 今日の日付を取得
    with open(filename, mode='a', newline='', encoding='cp932') as file:
        writer = csv.writer(file)
        writer.writerow([date_today, points, site])


if __name__ == "__main__":
    points = get_sbi_points()
    if points:
        print(f"SBI証券の獲得ポイント数: {points}")

        # 取得したポイントをSBI証券としてCSVに保存
        save_points_to_csv(points, site="SBI証券")
        print(f"ポイント {points} をCSVに保存しました。")
