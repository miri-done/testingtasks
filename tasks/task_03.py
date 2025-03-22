import requests

base_url = 'https://www.szse.cn/api/'

def getTimeData():
    url = base_url + 'market/ssjjhq/getTimeData'
    headers = {
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "en-US,en;q=0.9",
        "Connection": "keep-alive",
        "Content-Type": "application/json",
        "Host": "www.szse.cn",
        "Referer": "https://www.szse.cn/English/siteMarketData/siteMarketDatas/lookup/index.html?code=000001",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36 Edg/134.0.0.0",
        "X-Request-Type": "ajax",
        "X-Requested-With": "XMLHttpRequest",
        "sec-ch-ua": '"Chromium";v="134", "Not:A-Brand";v="24", "Microsoft Edge";v="134"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"'
    }

    url = "https://www.szse.cn/api/market/ssjjhq/getTimeData"
    params = {
        "random": "0.1601929636862236",
        "marketId": "1",
        "code": "000001",
        "language": "EN"
    }

    # https://jsonpathfinder.com/ to get json path

    response = requests.get(url, headers=headers, params=params) 

    if response.status_code == 200:
        data = response.json()
        market_data = data.get("data", {}) 
        high_no = float(market_data.get("high"))
        low_no = float(market_data.get("low"))
        
        return {
            "high": high_no,
            "low": low_no,
            "status_code": 200
        }
    else:
        return {"Failed:": response.status_code}
