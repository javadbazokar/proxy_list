import http.client
from concurrent.futures import ThreadPoolExecutor, as_completed
from threading import Lock

# Custom headers with ":" in their names
headers = {
    ":authority": "piratewins.io",
    ":method": "POST",
    ":path": "/?pirate=2458836",
    ":scheme": "https",
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-encoding": "gzip, deflate, br, zstd",
    "accept-language": "en-US,en;q=0.9",
    "cache-control": "max-age=0",
    "content-length": "13",
    "content-type": "application/x-www-form-urlencoded",
    "origin": "https://piratewins.io",
    "referer": "https://piratewins.io/?pirate=2458836",
    "sec-fetch-site": "same-origin",
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

# Send a single request using http.client
def send_single_request(proxy, success_counter, total_counter, lock):
    host, port = proxy.split(":")
    try:
        connection = http.client.HTTPSConnection(host, port=int(port), timeout=10)
        connection.request("POST", "/?pirate=2458836", headers=headers)
        response = connection.getresponse()
        with lock:
            total_counter[0] += 1
            if response.status == 302:
                success_counter[0] += 1
        connection.close()
    except Exception as e:
        with lock:
            total_counter[0] += 1
        print(f"Error with proxy {proxy}: {e}")  # Display the error

# Send requests concurrently
def send_requests_concurrently(proxies):
    success_counter = [0]
    total_counter = [0]
    lock = Lock()
    with ThreadPoolExecutor(max_workers=20) as executor:
        futures = [executor.submit(send_single_request, proxy, success_counter, total_counter, lock) for proxy in proxies]
        for future in as_completed(futures):
            with lock:
                print(f"Total: {total_counter[0]} | Successful: {success_counter[0]}", end="\r")
    return success_counter[0]

# Main program execution
if __name__ == "__main__":
    proxies = load_proxies("proxies.txt")  # Proxy file name
    print("Starting to send requests...")
    total_success = send_requests_concurrently(proxies)
    print(f"\n\nTotal successful requests: {total_success}")
