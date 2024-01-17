import requests

url = 'https://wisgoon.com/pin-like/'

headers = {
    'authority': 'wisgoon.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'fa,en;q=0.9',
    'content-type': 'application/json',
    'cookie': 'analytics_token=0049523c-07ad-5a58-42a6-198a9d6191b6; _yngt=e2a42ee3-3191f-f2997-754fb-bb0b04138249f; g_state={"i_l":0}; _gid=GA1.2.1762382625.1703421526; analytics_session_token=87b11b87-1d12-2e51-2f3a-00de30f16a91; yektanet_session_last_activity=12/25/2023; _yngt_iframe=1; _ga_ZS72RVQS0Y=GS1.1.1703490139.286.1.1703490514.59.0.0; _ga=GA1.2.1520522488.1697262423; _gat_UA-108679439-2=1; wisgoon_website_session=MTcwMzQ5MDUxN3xEdi1CQkFFQ180SUFBUkFCRUFBQV9nRUlfNElBQlFaemRISnBibWNNQ1FBSFgyWnNZWE5vWHdkYlhYVnBiblE0Q2dRQUFudDlCbk4wY21sdVp3d01BQXAxYzJWeVgzUnZhMlZ1Qm5OMGNtbHVad3dxQUNneU16Tm1NVGMzWWpZMlptRXlaRGhrTURVeFlXRTVZVEZqTkRRMll6TmhZVEl6TkRZNE9EUmpCbk4wY21sdVp3d0pBQWQxYzJWeVgybGtBMmx1ZEFRRkFQMXdiRmdHYzNSeWFXNW5EQTRBREhKbGNYVmxjM1J2Y2w5cFpBWnpkSEpwYm1jTUZnQVVNelF6WkRrek1XUTBaR1JqTkRNd09ERmxZbUVHYzNSeWFXNW5EQlFBRW1GMWRHaGxiblJwWTJsMGVWOTBiMnRsYmdkYlhYVnBiblE0Q2lJQUlPdnk3NlRYUHRqTnBTSkh1OUM1Mnd5YVFCQjcxa0RwQlpYUVNTaVVlYUNGfH9fCoHSkUyhsGm4qB8k9eIOEarEEsO9lQhkQFMBYZ9h',
    'origin': 'https://wisgoon.com',
    'referer': 'https://wisgoon.com/pin/59977780/',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

data = {"item_id": 60244125}
num_iterations = 1000000
for i in range(num_iterations):
    response = requests.post(url, headers=headers, json=data)
    print(f"id: {data['item_id']}")
    data["item_id"] += 1