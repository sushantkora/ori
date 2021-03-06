import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors.lxmlhtml import LxmlLinkExtractor
from scrapy.http.request import Request
from scrapy.conf import settings
from amazon1.items import Amazon1Item
import bs4 as bs
import lxml


class AmazonProductSpider(CrawlSpider):
    name = "Amazon2"
    allowed_domains = ["amazon.in"]

    # Use working product URL below
    start_urls = ["http://www.amazon.in/s/ref=sr_pg_2?fst=as%3Aoff&rh=n%3A976442031%2Cn%3A!976443031%2Cn%3A1380263031%2Cn%3A3474656031%2Cp_n_feature_thirteen_browse-bin%3A2753048031|2753047031&page={}&bbn=3474656031&ie=UTF8&qid=1485024415".format(x) for  x in list(range(1,48,1))]
    # start_urls = ["http://www.amazon.in/s/ref=sr_pg_2?fst=as%3Aoff&rh=n%3A976442031%2Cn%3A!976443031%2Cn%3A1380263031%2Cn%3A3474656031%2Cp_n_feature_thirteen_browse-bin%3A2753048031|2753047031&page=1&bbn=3474656031&ie=UTF8&qid=1485024415"]

    rules = (
        Rule(LxmlLinkExtractor(allow=(r'(dp)\/([A-Z])([A-Z0-9]{9})'),deny=(r'(.in)\/(dp)\/([A-Z])([A-Z0-9]{9})'), unique=True,), callback="parse_item",),
	)
    

    def parse_item(self,response):
        items = Amazon1Item()
  #       items['Item_name'] = response.xpath('//*[@id="productTitle"]/text()').extract()
        items['Item_href'] = response.url
  #       items['Model'] = response.xpath('//*[@id="prodDetails"]/div/div[1]/div/div[2]/div/div/table/tbody/tr[2]/td[2]/text()').extract()
  #       items['Energy_Efficiency'] = response.xpath('//*[@id="prodDetails"]/div/div[1]/div/div[2]/div/div/table/tbody/tr[3]/td[2]/text()').extract()
  #       items['Capacity'] = response.xpath('//*[@id="prodDetails"]/div/div[1]/div/div[2]/div/div/table/tbody/tr[4]/td[2]/text()').extract()
  #       items['Noise_Level'] = response.xpath('//*[@id="prodDetails"]/div/div[1]/div/div[2]/div/div/table/tbody/tr[5]/td[2]/text()').extract()
  #       items['Installation_Type'] = response.xpath('//*[@id="prodDetails"]/div/div[1]/div/div[2]/div/div/table/tbody/tr[6]/td[2]/text()').extract()
  #       items['Part_Number'] = response.xpath('//*[@id="prodDetails"]/div/div[1]/div/div[2]/div/div/table/tbody/tr[7]/td[2]/text()').extract()
  #       items['Color'] = response.xpath('//*[@id="prodDetails"]/div/div[1]/div/div[2]/div/div/table/tbody/tr[8]/td[2]/text()').extract()
  #       items['Control_Console'] = response.xpath('//*[@id="prodDetails"]/div[2]/div[1]/div/div[2]/div/div/table/tbody/tr[7]/td[2]/text()').extract()
  #       items['Voltage'] = response.xpath('//*[@id="prodDetails"]/div[2]/div[1]/div/div[2]/div/div/table/tbody/tr[8]/td[2]/text()').extract()
  #       items['Wattage'] = response.xpath('//*[@id="prodDetails"]/div[2]/div[1]/div/div[2]/div/div/table/tbody/tr[9]/td[2]/text()').extract()
  #       items['ASIN'] = response.xpath('//*[@id="prodDetails"]/div[2]/div[2]/div[1]/div[2]/div/div/table/tbody/tr[1]/td[2]/text()').extract()
  #       items['Best_Sellers_Rank_Category'] = response.xpath('//*[@id="SalesRank"]/td[2]/text()[1]').extract()
  #       items['Offer_Price'] = response.xpath('//*[@id="priceblock_saleprice"]/text()').extract()
		# # items['MRP']=response.xpath('//*[@id="price"]/table/tbody/tr[1]/td[2]/span/text()').extract()
  #       items['No_of_Reviews'] = response.xpath('//*[@id="acrCustomerReviewText"]/text()').extract()
  #       items['Average_Rating'] = response.xpath('//*[(@id = "averageCustomerReviewRating")]/text()').extract()
        soup=bs.BeautifulSoup(response.text,"lxml")
        items['Item_name']=soup.title.text.encode('ascii')
        try:
            for string in soup.find("span",class_="a-text-strike").stripped_strings:
             items['MRP']=string.encode('ascii')
        except Exception: pass 
        try:
            items['Offer_Price'] = response.xpath('//*[@id="priceblock_saleprice"]/text()').extract()[0].encode("ascii")
            
        except Exception: pass
        try:
            items['Offer_Price'] = response.xpath('//*[@id="priceblock_ourprice"]/text()').extract()[0].encode("ascii")
            
        except Exception: pass
        try:
            items['Offer_Price'] = response.xpath('//*[@id="priceblock_dealprice"]/text()').extract()[0].encode("ascii")
            
        except Exception: pass
        try:
            items['Offer_Price'] = response.xpath('//*[@id="olp_feature_div"]/div/span/span/text()').extract()
            for sting in items['Offer_Price']:items['Offer_Price']=sting.encode('ascii')
        except Exception: pass
        try:table1=soup.find(class_="column col1 ")
        except Exception: pass
        try:items['Brand'] = table1.find("td",text='Brand').next_sibling.text.encode('ascii')
        except Exception: pass
        try:items['Model'] = table1.find("td",text='Model').next_sibling.text.encode('ascii')
        except Exception: pass
        try:items['Energy_Efficiency'] = table1.find("td",text='Energy Efficiency').next_sibling.text.encode('ascii')
        except Exception: pass
        try:items['Capacity'] = table1.find("td",text='Capacity').next_sibling.text.encode('ascii')
        except Exception: pass
        try:items['Noise_Level'] =table1.find("td",text='Noise Level').next_sibling.text.encode('ascii')
        except Exception: pass
        try:items['Installation_Type'] =table1.find("td",text='Installation Type').next_sibling.text.encode('ascii')
        except Exception: pass
        try:items['Part_Number']= table1.find("td",text='Part Number').next_sibling.text.encode('ascii')
        except Exception: pass
        try:items['Color'] = table1.find("td",text='Colour').next_sibling.text.encode('ascii')
        except Exception: pass
        try:items['Control_Console'] = table1.find("td",text='Control Console').next_sibling.text.encode('ascii')
        except Exception: pass
        try:items['Voltage'] = table1.find("td",text='Voltage').next_sibling.text.encode('ascii')
        except Exception: pass
        try:items['Wattage'] = table1.find("td",text='Wattage').next_sibling.text.encode('ascii')
        except Exception: pass
        try:table2=soup.find(class_="column col2 ")
        except Exception: pass
        try:items['ASIN'] = table2.find("td",text='ASIN').next_sibling.text.encode('ascii')
        except Exception: pass
        try:items['No_of_Reviews'] =table2.find(id="averageCustomerReviewCount").text.encode('ascii')
        except Exception: pass
        try:items['Average_Rating'] =table2.find(id="averageCustomerReviewRating").text.encode('ascii')
        except Exception: pass
        try:items['Best_Sellers_Rank_Category_home_kitchen']=table2.find("td",text='Best Sellers Rank').next_sibling.get_text(strip=True).split()[0].encode('ascii')
        except Exception: pass
        try:items['Best_Sellers_Rank_Category_AC']=table2.find("span",class_='zg_hrsr_rank').text.encode('ascii')
        except Exception: pass

        try:
            count=0
            reviews=soup.find('div',id="revMHRL")
            for item in reviews.find_all('div',class_="a-section"):
             if len(item["class"]) != 1:
                 continue;
             count+=1
             items['Review_{}'.format(count)]=item.get_text(strip=True).encode('ascii')
        except Exception: pass
        return items