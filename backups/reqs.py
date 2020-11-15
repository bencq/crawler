import requests
import time
from bs4 import BeautifulSoup






def main():
    headers = {
        'Connection': 'keep-alive',
        'Cache-Control': 'max-age=0',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Referer': 'http://sdcs.sysu.edu.cn/',
        'Accept-Language': 'zh-CN,zh;q=0.9,zh-TW;q=0.8,en-US;q=0.7,en;q=0.6',
        'Cookie': 'ZMRhjlxmTSDe81S=zeFy6uUQxv85noFr2KUYKwbOtb3.fZ8_iSozf49mLZAr9hwV8HnkIS2kz4T9dda9; BIGipServerPool_dpcms-a=3389001738.47138.0000; has_js=1; ZMRhjlxmTSDe81T=53d7HIQZ4Fe42uCx8gw2dTho27d6aNF_ysJ_B56dP17EqWUcbzq0OJ0.Io.UqUn5YpnnsVjo3Nre0OPdGZewA17_OVjo1Nc6tm1F1HPHF9fKKK53LifhN5Z3EJ3tT7xbV.NtLFHXlICkT_VNZ9QCMZgfax0Xdb145OQFtnPCd6peqKUDYeWP1xZFQEAy_YI0p8LC1Aepyu4Ump.uUdfItfqWE1umuoIvDll4hVSSIGgGKcghaP4YShRSzxexmTZBPQ6B83We9d9zvwwMk1emuSKFaAOW05obYy1QsHo9lbCK5LC05sTq9BAw0bf9uYAU13eks55_I1ovnsRbnDjJGbTju',
        # --compressed,
        # --insecure
    }

    # headers={
    #     # 'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    #     'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',
    # }

    url = "http://sdcs.sysu.edu.cn/"
    # url = "http://sdcs.sysu.edu.cn/research/activity"
    # url = "http://www.baidu.com"


    html_doc = requests.get(url, headers=headers)
    print(html_doc)
    print()
    

    # soup = BeautifulSoup(html_doc, 'html.parser')


if __name__ == "__main__":
    main()