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
            'Bernese-Mountain-Dog'          
            ]

# POST 값으로 받아온 후, calculate_result.html 로 render하는 변수 return
def to_calculate_result(dog_breed):
    with open(f'./calculator/crawl_text/{dog_breed}.txt', 'r', -1, 'utf-8') as f:
        press_text = f.readline()
        press_graph = f.readline()
    return press_text, press_graph

def return_dognames_list():
    return dognames_list

if __name__=='__main__':
    to_calculate_result('poodle-standard')