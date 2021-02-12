from django import forms

class CalculatorForm(forms.Form):
    dog_krname_list=[('siberian-husky', '시베리아 허스키'),
                    ('poodle-standard', '푸들'),
                    ('german-shepherd-dog', '저먼 셰퍼드'),
                    ('alaskan-malamute', '알래스칸맬러뮤트'),
                    ('doberman-pinscher', '도베르만_핀셔'),
                    ('golden-retriever', '골든 리트리버'),
                    ('labrador-retriever', '레브라도 레트리버'),
                    ('bedlington-terrier', '베들링턴 테리어'),
                    ('italian-greyhound', '이탈리안 그레이 하운드'),
                    ('cardigan-welsh-corgi', '웰시코기'),
                    ('samoyed', '사모예드'),
                    ('shiba-inu', '시바 이누'),
                    ('japanese-spitz', '제페니스 스피츠'),
                    ('miniature-schnauzer', '미니어처 슈나우저'),
                    ('bichon-frise', '비숑프리제'),
                    ('shih-tzu', '시츄'),
                    ('russell-terrier', '잭 러셀 테리어'),
                    ('pomeranian', '포메라니안'),
                    ('miniature-pinscher', '미니어처 핀셔'),
                    ('papillon', '파피용'),
                    ('yorkshire-terrier', '요크셔 테리어'),
                    ('maltese', '말티즈'),
                    ('dachshund', '닥스훈트'),
                    ('chihuahua', '치와와'),
                    ('pug', '퍼그'),
                    ('French-Bulldog', '프렌치 불독'),
                    ('shetland-sheepdog', '셔틀랜드 쉽독'),
                    ('old-english-sheepdog', '올드 잉글리시 쉽독'),
                    ('collie', '러프콜리'),
                    ('jindo', '진돗개'),
                    ('border-collie', '보더콜리'),
                    ('bulldog', '불독'),
                    ('dalmatian', '달마시안'),
                    ('chow-chow', '차우차우'),
                    ('Miniature-Schnauzer', '미니어쳐 슈나우저'),
                    ('Airedale-Terrier', '에어데일 테리어'),
                    ('Scottish-Terrier', '스코티시 테리어'),
                    ('Beagle', '비글'),
                    ('Afghan-Hound', '아프간하운드'),
                    ('Basset-Hound', '바셋하운드'),
                    ('Cocker-Spaniel', '코커스패니얼'),
                    ('Pointer', '포인터'),
                    ('Vizsla', '비즐라'),
                    ('Rottweiler', '로트 와일러'),
                    ('Bernese-Mountain-Dog', '버니즈 마운틴독')] # db, form_display
    levels = [('5', 'level 1'),
         ('10', 'level 2'),
         ('20', 'level 3'),
         ('30', 'level 4'),
         ('40', 'level 5')]

    bcs = forms.ChoiceField(choices=levels, widget=forms.RadioSelect)
    breeds = forms.ChoiceField(required = True, choices = dog_krname_list, label = '견종')
    current_weight = forms.IntegerField(required = True, label='현재 체중', widget=forms.TextInput(attrs={'placeholder':'현재 체중을 입력하세요'}))





    