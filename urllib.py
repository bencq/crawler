import urllib3

def main():
    url = "http://sdcs.sysu.edu.cn/"

    headers = {
        
    }
    http = urllib3.PoolManager(num_pools=10, headers=headers)
    resp = http.request('GET', url)
    html = resp.data.decode()


    with open("respContent.html", "w", encoding="utf-8") as f:
        # print(html)
        f.write(html)

if __name__ == '__main__':
    main()
