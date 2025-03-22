import requests

# Replace with your actual API credentials
base_url = 'https://www.szse.cn/api/'

def suggest():
    url = base_url + 'search/suggest'
    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Origin': 'https://www.szse.cn',
        'Referer': 'https://www.szse.cn/English/siteMarketData/siteMarketDatas/lookup/index.html?code=000001',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36',
        'X-Request-Type': 'ajax',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua': '"Chromium";v="134", "Not:A-Brand";v="24", "Google Chrome";v="134"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
    }
    data = {
        'keyword': '000001'
    }
    
    response = requests.post(url, headers=headers, data=data)  # Use data parameter for form data
    if response.status_code == 200:
        print("Success:", response.status_code, response.text)
        return response.json()  # Return the response as JSON
    else:
        print("Error:", response.status_code, response.text)
 
        return response.json()


def getTimeData():
    url = base_url + 'market/ssjjhq/getTimeData'
    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'zh-TW,zh;q=0.9',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json',  # This is fine for a GET request
        'Referer': 'https://www.szse.cn/English/siteMarketData/siteMarketDatas/lookup/index.html?code=000001',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36',
        'X-Request-Type': 'ajax',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua': '"Chromium";v="134", "Not:A-Brand";v="24", "Google Chrome";v="134"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
    }
    params = {
        'random': '0.5330422193112323',  # Ensure this matches your random value
        'marketId': '1',
        'code': '000001',
        'language': 'EN',
    }
    
    response = requests.get(url, headers=headers, params=params)  # Use params for GET requests
    if response.status_code == 200:
        print("Success:", response.status_code)
        # To get json path: https://jsonpathfinder.com/ (or ask AI)
        print('Value of High: ', response.json().get('data', {}).get('high'))
        print('Value of Low: ', response.json().get('data', {}).get('low'))
        return response.json()  # Return the response as JSON
    else:
        print("Error:", response.status_code)
        return response.json()

# Main function
def main():
    getTimeDataAPI = getTimeData();
    # print(getTimeDataAPI)
    # Suggestapi = suggest()
    # print(Suggestapi)
   


if __name__ == "__main__":
    main()