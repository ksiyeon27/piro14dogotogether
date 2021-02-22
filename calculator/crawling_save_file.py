from bs4 import BeautifulSoup
import requests
dognames_list=['siberian-husky',
            'poodle-standard','german-shepherd-dog','alaskan-malamute',
            'doberman-pinscher','golden-retriever','labrador-retriever','bedlington-terrier',
            'italian-greyhound','cardigan-welsh-corgi','samoyed','shiba-inu',
            'japanese-spitz','miniature-schnauzer','bichon-frise','shih-tzu',
            'russell-terrier','pomeranian','miniature-pinscher','papillon',
            'yorkshire-terrier','maltese','dachshund','chihuahua',
            'pug','French-Bulldog','shetland-sheepdog','old-english-sheepdog',
            'collie','jindo','border-collie','bulldog',
            'dalmatian','chow-chow','Miniature-Schnauzer','Airedale-Terrier',
            'Scottish-Terrier','Beagle','Afghan-Hound','Basset-Hound',
            'Cocker-Spaniel','Pointer','Vizsla','Rottweiler',
            'Bernese-Mountain-Dog',         
            ]

print(len(dognames_list))
for i in range(len(dognames_list)):
    response = requests.get(f'https://www.akc.org/dog-breeds/{dognames_list[i]}/')
    # print(response.encoding)
    # print(response.status_code)
    # print(type(response.status_code))
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        press_text = soup.select("#panel-EXERCISE p")[0].text
        press_graph = soup.select('#panel-EXERCISE div.graph-section .bar-graph__section')[0].get('style')
        press_image = soup.select('#puppy-finder div.side-by-side__poster img')[0].get('data-src') 
        
        with open(f'.\calculator\crawl_text\{dognames_list[i]}.txt', 'w', -1, 'utf-8') as f:
            f.write(press_text)
            f.write('\n')
            f.write(press_graph)
            f.write('\n')
            f.write(press_image)
    else:
        print("url not found. please check the dog breed\'s url")

    i += 1