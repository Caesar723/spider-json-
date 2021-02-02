from urllib import request
import json
def get(n):
    url="https://www.ximalaya.com/revision/category/queryCategoryPageAlbums?category=xiangsheng&subcategory=&meta=&sort=1&page=1&perPage="+str(n)
    header={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36 Edg/88.0.705.56"}
    req=request.Request(url,headers=header)
    response=request.urlopen(req)
    #print(type(response))
    if response.getcode()==200:
        data = response.read()
        da= json.loads(data)

        information=da["data"]["albums"]
        for i in range(0,n):
            data2=information[i]
            print(data2["title"],data2["anchorName"],data2["playCount"])



get(300)