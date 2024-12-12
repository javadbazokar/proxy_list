import requests
import time

# هدرهای مورد نیاز
headers = {
    ":authority": "piratewins.io",
    ":method": "POST",
    ":path": "/?pirate=2458836",
    ":scheme": "https",
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-encoding": "gzip, deflate, br, zstd",
    "accept-language": "en-US,en;q=0.9,fa-IR;q=0.8,fa;q=0.7,zh-CN;q=0.6,zh;q=0.5",
    "cache-control": "max-age=0",
    "content-length": "13",
    "content-type": "application/x-www-form-urlencoded",
    "cookie": "_prck=2458836; _ga=GA1.1.517465153.1733256022; _ga_CX7RN8385Z=GS1.1.1733718449.8.0.1733718449.0.0.0; cf_clearance=YwVRrpJNPczFE7MB44anwK7K3p2xLgRLjZKnP_arvTA-1733718450-1.2.1.1-wveeRG2MZIhqSjQxCdlUlYPNJdicCok.jACux671OlfzBPa.K9UoUBWlh6rpRHbka3NwaKl3hmVgD21I6mGPLhg_gl.xUiUhpcSyYXmSfmvBUj7k9y9DpuaV5a1nCneyDWN2XVX7aFKkDclDJe87.eoXPXUsC8tqsghQbWvRtP23cV8oMHFRlmKUxGAPCeN9ag7jidupfdEDkm9DpbqMALYWkvoQmqd8fCgZaTRwayVrWYOHvnmGcvKl8YZQU0orQ1oUOj9.n7T8XOYgY48D1Sc5zLmFo_m71FxAXVtQJI0RIB.eTOFEhpWhmOxyIZBNyKjbrp.i85mKvibAUmaMkgg.78oi.ew7JZZ6AGb2CbZmRiRDG1DnFlUwUaAbrvkjMOcyjEblLnkK8JLpcb4Eag",
    "origin": "https://piratewins.io",
    "priority": "u=0, i",
    "referer": "https://piratewins.io/?pirate=2458836",
    "sec-ch-ua": "\"Google Chrome\";v=\"131\", \"Chromium\";v=\"131\", \"Not_A Brand\";v=\"24\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "same-origin",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
}

# بارگذاری پروکسی‌ها از فایل
def load_proxies(filename):
    proxies = []
    with open(filename, "r") as file:
        for line in file:
            proxy = line.strip()
            if proxy:
                proxies.append(proxy)
    return proxies

# ارسال درخواست
def send_request(url, proxies):
    successful_requests = 0
    for proxy in proxies:
        proxy_dict = {
            "http": f"http://{proxy}",
            "https": f"http://{proxy}",
        }
        try:
            response = requests.post(url, headers=headers, proxies=proxy_dict, timeout=10)
            if response.status_code == 302:
                successful_requests += 1
                # نمایش تعداد درخواست‌های موفق به صورت زنده
                print(f"\rتعداد درخواست‌های موفق: {successful_requests}", end="")
        except requests.RequestException:
            continue
    return successful_requests

# اجرای برنامه
if __name__ == "__main__":
    url = "https://piratewins.io/?pirate=2458836"  # لینک مقصد
    proxies = load_proxies("proxies.txt")  # نام فایل پروکسی‌ها
    print("در حال ارسال درخواست‌ها...")
    success_count = send_request(url, proxies)
    print(f"\nتعداد کل درخواست‌های موفق: {success_count}")
