# Kraken 거래소 API를 사용해서 비트코인(BTC/USD) 현재 가격을 2분마다 파일 bitcoin_price.txt에 추가 저장하는 Python 코드입니다.김상백 11/13/2026 

import requests
import time
from datetime import datetime

OUTPUT_FILE = "bitcoin_price.txt"

def get_btc_price():
    url = "https://api.kraken.com/0/public/Ticker?pair=XBTUSD"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        data = response.json()

        if data["error"]:
            print("Kraken API Error:", data["error"])
            return None

        # 현재 거래 가격
        price = data["result"]["XXBTZUSD"]["c"][0]
        return float(price)

    except Exception as e:
        print("Error:", e)
        return None


while True:
    price = get_btc_price()

    if price:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        line = f"{timestamp},{price}\n"

        with open(OUTPUT_FILE, "a", encoding="utf-8") as f:
            f.write(line)

        print(f"{timestamp} BTC/USD = {price}")

    # 2분(120초) 대기
    time.sleep(120)


# 저장되는 bitcoin_price.txt 예:

# 2026-11-13 17:01:00,91654.3
# 2026-11-13 17:03:00,91672.1
# 2026-11-13 17:05:00,91680.5


# 만약 나중에 Excel에서 쉽게 읽고 그래프를 만들 계획이라면, CSV 형식으로 헤더까지 넣는 버전도 가능합니다.

# import os
# import requests
# import time
# from datetime import datetime

# FILE_NAME = "bitcoin_price.csv"

# if not os.path.exists(FILE_NAME):
    # with open(FILE_NAME, "w") as f:
        # f.write("timestamp,price\n")

# while True:
    # data = requests.get(
        # "https://api.kraken.com/0/public/Ticker?pair=XBTUSD"
    # ).json()

    # price = data["result"]["XXBTZUSD"]["c"][0]

    # with open(FILE_NAME, "a") as f:
        # f.write(f"{datetime.now():%Y-%m-%d %H:%M:%S},{price}\n")

    # time.sleep(120)


# 이 CSV 파일은 Excel에서 바로 열 수 있고, 가격 변동 그래프도 쉽게 만들 수 있습니다.


