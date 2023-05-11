def get_veg_data():
    try:
        import pandas as pd
        import requests
        from bs4 import BeautifulSoup
        url = "https://vegetablemarketprice.com/market/andhraPradesh/today"
        df = pd.read_html(url)


        df = df[0]
        df.drop("Unnamed: 0",axis=1,inplace=True)
        d = []
        for i in range(len(df)):
            d.append(df.iloc[i].to_dict())
        D = {}
        D["Vegetables"] = d


        req = requests.get(url)
        soup = BeautifulSoup(req.content,"html.parser")
        img = []
        for i in soup.findAll("div",{"class":"vegetableImageDiv"}):
            img.append("https://vegetablemarketprice.com"+i.get("image-src-file"))
        imgs = []
        for i in range(len(img)):
            imgs.append(img[i].split("-")[0]+"-"+img[i].split("-")[-1].replace("64","256"))
        for i,j in zip(D["Vegetables"],imgs):
            i["Image"] = j
        return D

    except Exception as e:
        raise e
