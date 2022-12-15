import os
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import urllib.request


def PageUrl(itemName, pageNum):
    url = "https://search.musinsa.com/search/musinsa/goods?q=" + itemName + "&list_kind=small&sortCode=pop&sub_sort=&page=" + \
        str(pageNum) + "&display_cnt=0&saleGoods=false&includeSoldOut=false&popular=false&category1DepthCode=&category2DepthCodes=&category3DepthCodes=&selectedFilters=&category1DepthName=&category2DepthName=&brandIds=&price=&colorCodes=&contentType=&styleTypes=&includeKeywords=&excludeKeywords=&originalYn=N&tags=&saleCampaign=false&serviceType=&eventType=&type=&season=&measure=&openFilterLayout=N&selectedOrderMeasure=&d_cat_cd="
    return url


FindingItemName = "신발"

driver = webdriver.Chrome(os.getcwd() + "/chromedriver")

pageUrl = PageUrl(FindingItemName, 1)
driver.get(pageUrl)

totalPageNum = driver.find_element_by_css_selector(".totalPagingNum").text
items = driver.find_elements_by_css_selector(".lazyload.lazy")
print("Total Page of ", FindingItemName, " : ", str(totalPageNum))

cnt = 1
for i in range(int(totalPageNum)):
    pageUrl = PageUrl(FindingItemName, i+1)
    driver.get(pageUrl)
    time.sleep(0.5)
    items = driver.find_elements_by_css_selector(".lazyload.lazy")
    print("Finding: ", FindingItemName, " - Page ", i+1, "/",
          totalPageNum, " start - ", len(items), " items exist")

    for item in items:
        try:
            time.sleep(0.5)
            imgUrl = item.get_attribute("data-original")
            urllib.request.urlretrieve(
                imgUrl, "../images/musinsa/m" + str(cnt) + ".jpg")
            cnt += 1
        except Exception as e:
            print(e)
            pass

driver.close()
