from googlesearch import search
import requests
from bs4 import BeautifulSoup as bs
import webbrowser


check = True
print('For shoutdown search print "quit"\nFor checking example press "Enter"')
while check == True:
    req_link = input('Enter your request link: ')

    if req_link == 'quit':
        check = False
        break

    if len(req_link) < 1:
        req_link = 'loguru'
    try:
        google_list = search(f'{req_link}', num_results=1, lang='ru')
        for link in google_list:
            try:
                r = requests.get(link)
                with open(f'index{req_link}.html', 'a') as index_file:
                    ind = index_file.write(r.text)
                with open(f'index{req_link}.html') as res_file:
                    soup = bs (res_file, 'html.parser')
                    with open('res.txt','a') as res:
                        clear_link = link.split('/')
                        # print(clear_link)
                        clear_link = '/'.join(clear_link[:3])
                        print(clear_link)
                        with open('res.txt') as les:
                            l = les.readlines()
                            print(l)
                            if clear_link in l and soup.title.text in l:
                                print('You already visited this link')
                            else:
                                res.write(f'{clear_link} : \n{soup.title.text}\n')
                        
            except Exception as e:
                print('Error\nFailed\n',e)
    except Exception as e:
        print('Internet connection lost\n',e)
