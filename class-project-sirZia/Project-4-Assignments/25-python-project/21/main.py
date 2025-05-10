#pip install types-beautifulsoup4
import requests
from bs4 import BeautifulSoup as bs


github_user_id = input("Enter Github Id : ")

if github_user_id == "":
    print("\nPlease enter github id")

else:
    url = "https://github.com/"+github_user_id
    send_request = requests.get(url)
    soup = bs(send_request.content, "html.parser") ## html.parser ek built-in Python parser hai jo HTML code ko read aur samajhne ke liye use hota hai.


    # is ky andar image 
    avatar_tag = soup.find('img', {'alt': 'Avatar'}) or \
                soup.find('img', {'class': 'avatar'}) or \
                soup.find('img', {'alt': f'{github_user_id}'})

    if avatar_tag and avatar_tag.get('src'):
       
        image_url = avatar_tag['src']

        image_data = requests.get(image_url) ## image url ka response check karry ga

        with open(f"{github_user_id}_image.png", "wb") as file:
            file.write(image_data.content)
            print("\nsave successfully")

        print(f"\nImage Url : {image_url}")


    else:
        print("\nError: Could not find profile image. GitHub may have updated their page structure.")