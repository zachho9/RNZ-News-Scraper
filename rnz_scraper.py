from bs4 import BeautifulSoup
import requests

from_rnz = False
while not from_rnz:
    url = input("Input post link from www.rnz.co.nz >>")
    if "www.rnz.co.nz" in url:
        from_rnz = True
        html_text = requests.get(url).text
        soup = BeautifulSoup(html_text, 'lxml')

        title = soup.find(
            'h1', class_='c-story-header__headline').text.replace(':', '').replace(',', '')
        file_time = soup.find('span', class_='o-kicker__time kicker-item').text
        post_time = soup.find(
            'span', class_='updated').text.replace('  ', '').strip()
        paras = soup.find('div', class_='article__body')

        file_name = f"rnz\[{file_time}] - {title}.txt"
        with open(file_name, 'w', encoding='utf-8') as single_file:
            single_file.write(f"- Title: {title} \n \n")
            single_file.write(f"- Publish time: {post_time} \n \n")
            single_file.write(f"- Main body: \n \n")

        for para in paras.find_all('p', class_=''):
            with open(file_name, 'a', encoding='utf-8') as single_file:
                single_file.write(para.text + '\n')
                single_file.write('\n')

        # from_rnz = False

    else:
        print("The link is not from rnz, try again")
