import re
import json
import unidecode
from pprint import pprint
from bs4 import BeautifulSoup

def slugify(text):
    '''
    return a slugified version of passed in text
    '''
    text = unidecode.unidecode(text).lower()
    return re.sub(r'[\W_]+', '_', text)


def main():
    raw_html = None
    
    with open('zomato.html') as _rh:
        raw_html = _rh.read()
    
    soup = BeautifulSoup(raw_html, 'html.parser')
    
    restaurants = []
    
    for card in soup.select('#orig-search-list > div.search-card'):
        restaurant = {}
        
        establishment_txt = None
        for establishment in card.select('div.content > div > article > div.pos-relative.clearfix > div > div.col-s-16.col-m-12.pl0 > div:nth-child(1) > div.col-s-12 > div.res-snippet-small-establishment.mt5'):
            establishment_txt = establishment.get_text()
        
        restaurant['establishment'] = establishment_txt

        href_txt = None
        for href in card.select('div.content > div > article > div.pos-relative.clearfix > div > div.col-s-16.col-m-12.pl0 > div:nth-child(1) > div.col-s-12 > a.result-title.hover_feedback.zred.bold.ln24.fontsize0'):
            href_txt = href.get('href')
        
        restaurant['url'] = href_txt

        img_url_txt = None
        for img_url in card.select('div.content > div > article > div.pos-relative.clearfix > div > div.col-s-6.col-m-4 > div > a'):
            img_url_txt = img_url.get('data-original')

        restaurant['img_url'] = img_url_txt

        call_txt = None
        for call in card.select('div.ui.two.item.menu.search-result-action.mt0 > a.item.res-snippet-ph-info'):
            call_txt = call.get('data-phone-no-str')

        restaurant['call'] = call_txt

        meta_tag_lst = list(card.select('div.content > div > article > div.search-page-text.clearfix.row'))
        
        for meta_tag in meta_tag_lst:



            meta_tag_name_lst = list(meta_tag.select('span.ttupper'))
            meta_tag_value_lst = list(meta_tag.select('.col-s-11'))
            if len(meta_tag_name_lst) != len(meta_tag_value_lst):
                continue
            
            meta_name_txt = None
            meta_value_txt = None
            for idx in range(len(meta_tag_name_lst)):
                meta_name = meta_tag_name_lst[idx]
                meta_name_txt = meta_name.get_text()
                meta_tag = meta_tag_value_lst[idx]
                meta_value_txt = meta_tag.get_text().strip()
                if meta_name_txt and meta_value_txt:
                    restaurant[slugify(meta_name_txt)] = meta_value_txt
            
            

        restaurants.append(restaurant)
    # pprint(restaurants)
    print(json.dumps(restaurants, indent=2, ensure_ascii=False))

if __name__ == '__main__':
    main()