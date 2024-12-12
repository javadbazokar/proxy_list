import requests

# Required headers
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

# Load proxies from file
def load_proxies(filename):
    proxies = []
    with open(filename, "r") as file:
        for line in file:
            proxy = line.strip()
            if proxy:
                proxies.append(proxy)
    return proxies

# Send requests
def send_request(url, proxies):
    successful_requests = 0
    for index, proxy in enumerate(proxies, start=1):
        proxy_dict = {
            "http": f"http://{proxy}",
            "https": f"http://{proxy}",
        }
        try:
            response = requests.post(url, headers=headers, proxies=proxy_dict, timeout=10)
            if response.status_code == 302:
                successful_requests += 1
                print(f"[{index}/{len(proxies)}] Proxy {proxy} succeeded (302 response).")
            else:
                print(f"[{index}/{len(proxies)}] Proxy {proxy} failed (Status: {response.status_code}).")
        except requests.RequestException as e:
            print(f"[{index}/{len(proxies)}] Proxy {proxy} error: {e}")
    return successful_requests

# Main program execution
if __name__ == "__main__":
    url = "https://piratewins.io/?pirate=2458836"  # Destination URL
    proxies = load_proxies("proxies.txt")  # Proxy file name
    print("Starting to send requests...")
    success_count = send_request(url, proxies)
    print(f"\nTotal successful requests: {success_count}")
