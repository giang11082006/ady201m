import json
import requests
import pandas as pd
import os
import time
import random

# 1. Cấu hình Oxylabs API
API_ENDPOINT = 'https://realtime.oxylabs.io/v1/queries'
API_AUTH = ('letuan272823_WwsaN', 'Letuan12345_')

target_zipcodes = [
    # Los Angeles / Malibu
    "90210", "90265", "90024", "90025", "90046",

    # San Diego
    "92101", "92103", "92109", "92130", "92037",

    # San Francisco
    "94102", "94103", "94109", "94110", "94114",

    # Bakersfield
    "93301", "93306", "93309", "93311", "93312",

    # Một số khu khác trong dataset
    "92315",  # Big Bear Lake
    "92262",  # Palm Springs
    "95969",  # Paradise
    "96161",  # Truckee
    "96150"   # South Lake Tahoe
]
MAX_PAGES_PER_ZIP = 5 

all_listings = []
seen_zpids = set() 

print("BẮT ĐẦU CHIẾN DỊCH QUÉT DỮ LIỆU TOÀN QUỐC THEO ZIP CODE...\n" + "="*60)

# 3. Vòng lặp quét Zip Code
for zipcode in target_zipcodes:
    print(f"\n>>> ĐANG QUÉT ZIP CODE: {zipcode} <<<")
    
    for page in range(1, MAX_PAGES_PER_ZIP + 1):
        page_slug = f"{page}_p/" if page > 1 else ""
        target_url = f"https://www.zillow.com/homes/{zipcode}_rb/{page_slug}"
        
        print(f"[*] Tiến trình: Trang {page}/{MAX_PAGES_PER_ZIP} - {target_url}")
        
        payload = {
            "source": "universal",
            "url": target_url,
            "user_agent_type": "desktop",
            "render": "html",
            "browser_instructions": [
                {
                    "type": "fetch_resource",
                    "filter": "https://www.zillow.com/async-create-search-page-state"
                }
            ]
        }
        
        try:
            response = requests.post(API_ENDPOINT, json=payload, auth=API_AUTH)
            response.raise_for_status()
            
            data = response.json()
            zillow_json_str = data["results"][0]["content"]
            zillow_data = json.loads(zillow_json_str)
            
            search_results = zillow_data.get("cat1", {}).get("searchResults", {})
            raw_listings = search_results.get("listResults", [])
            
            if not raw_listings:
                raw_listings = search_results.get("mapResults", [])
                
            # XỬ LÝ LỌC TRÙNG NGAY LẬP TỨC
            if raw_listings:
                new_houses_count = 0
                for listing in raw_listings:
                    zpid = listing.get("zpid")
                    
                    # Nếu có ZPID và ZPID này CHƯA TỪNG xuất hiện
                    if zpid and zpid not in seen_zpids:
                        seen_zpids.add(zpid)
                        all_listings.append(listing)
                        new_houses_count += 1
                
                print(f"    -> Nhận {len(raw_listings)} nhà. Trong đó có {new_houses_count} nhà mới.")
                
                # Nếu trang này trả về toàn bộ là nhà đã cào (Zillow bị kẹt ở trang 1)
                # -> NGẮT vòng lặp phân trang luôn để đỡ tốn tiền API
                if new_houses_count == 0:
                    print("    [!] Zillow trả về dữ liệu trùng lặp. Ngừng lật trang tại Zip code này!")
                    break 
            else:
                print("    -> Khu vực này hết nhà. Chuyển sang Zip Code tiếp theo!")
                break 
                
        except Exception as e:
            print(f"    -> [LỖI] Zillow chặn hoặc mạng lag: {e}")
            break # Lỗi nặng thì bỏ qua Zip code này luôn
            
        time.sleep(random.uniform(1.0, 3.0))

print("\n" + "="*60)
print(f"[HOÀN TẤT] Tổng cộng đã gom được thực tế: {len(all_listings)} căn nhà DUY NHẤT.")

# 4. Lưu file (Không cần Pandas drop_duplicates nữa vì đã sạch 100% từ trên)
if all_listings:
    print("Đang xuất file CSV...")
    df_final = pd.json_normalize(all_listings)
    
    output_dir = os.path.expanduser("~/workspace/project_ml/")
    os.makedirs(output_dir, exist_ok=True)
    output_file = os.path.join(output_dir, "zillow_national_dataset.csv")
    
    try:
        df_final.to_csv(output_file, index=False, encoding="utf-8-sig")
        print(f"\n[THÀNH CÔNG] Đã lưu {len(df_final)} dòng vào:")
        print(f"-> {output_file}")
    except OSError:
        fallback = "/tmp/zillow_national_dataset.csv"
        df_final.to_csv(fallback, index=False, encoding="utf-8-sig")
        print(f"\n[THÀNH CÔNG] Đã lưu tạm thời tại: {fallback}")
else:
    print("\n[THẤT BẠI] Quá trình cào thất bại, không có dữ liệu.")