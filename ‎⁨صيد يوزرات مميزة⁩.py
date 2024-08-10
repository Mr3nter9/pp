import requests, random
Z = '\033[1;31m' #احمر
X = '\033[1;33m' #اصفر
F = '\033[2;32m' #اخضر
B="\033[1;30m" # Black
L = "\033[1;95m"  #ارجواني
R="\033[1;31m" # Red
G="\033[1;32m" # Green
Y="\033[1;33m" # Yellow
Bl="\033[1;34m" # Blue
P="\033[1;35m" # Purple
C="\033[1;36m" # Cyan
W="\033[1;37m" # White
E = "\033[0;90m" #رمادي
z = 0
l = 'qwertyuiopasdfghjklzxcvbnm1234567890'
#------------------colors---------------#
B="\033[1;30m" # Black
R="\033[1;31m" # Red
G="\033[1;32m" # Green
Y="\033[1;33m" # Yellow
Bl="\033[1;34m" # Blue
P="\033[1;35m" # Purple
C="\033[1;36m" # Cyan
W="\033[1;37m" # White
E = "\033[0;90m" #رمادي
#------------------logo---------------------#
def logo():
    print(f'{G}-{R}-'*29)
    print(f"""
    𓆩𝗩𝗜𝗣𓆪 
⠀⠀⠀⠀⠀⢀⣤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⢤⣤⣀⣀⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⡼⠋⠀⣀⠄⡃⠍⣀⣒⣒⠂⠀⠬⠤⠤⠬⠍⠉⠝⠲⣄⡀⠀⠀
⠀⠀⠀⢀⡾⠁⠀⠊⢔⠕⠈⣀⣀⡀⠈⠆⠀⠀⠀⡍⠁⠀⠁⢂⠠⠈⣷⠀⠀
⠀⠀⣠⣾⠥⠀⠀⣠⢠⣞⣿⣿⣿⣉⠳⣄⠀⠀⣠⣤⣶⣶⣶⡄⠀⠀⣘⢦⡀
⢀⡞⡍⣠⠞⢋⡛⠶⠤⣤⠴⠚⠀⠈⠙⠁⠀⠀⢹⡏⠁⠀⣀⣠⠤⢤⡕⠱⣷
⠘⡇⠇⣯⠤⢾⡙⠲⢤⣀⡀⠤⠀⢲⡖⣂⣀⠀⠀⢙⣶⣄⠈⠉⣸⡄⠠⣠⡿
⠀⠹⣜⡪⠀⠈⢷⣦⣬⣏⠉⠛⠲⣮⣧⣁⣀⣀⠶⠞⢡⣂⣨⢶⢿⣧⠉⡼⠁
⠀⠀⠈⢷⡀⠀⠀⠳⣌⡟⠻⠷⣶⣧⣀⣀⣹⣉⣉⣿⣉⣉⣇⣼⣾⣿⠀⡇⠀
⠀⠀⠀⠈⢳⡄⠀⠀⠘⠳⣄⡀⡼⠈⠉⠛⡿⠿⠿⡿⠿⣿⢿⣿⣿⡇⠀⡇⠀
⠀⠀⠀⠀⠀⠙⢦⣕⠠⣒⠌⡙⠓⠶⠤⣤⣧⣀⣸⣇⣴⣧⠾⠾⠋⠀⠀⡇⠀
⠀⠀⠀⠀⠀⠀⠀⠈⠙⠶⣭⣒⠩⠖⢠⣤⠄⠀⠀⠀⠀⠀⠠⠔⠁⡰⠀⣧⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠲⢤⣀⣀⠉⠉⠀⠀⠀⠀⠀⠁⠀⣠⠏⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠛⠒⠲⠶⠤⠴⠒⠚⠁⠀⠀
    """)
    print(f'{G}-{R}-'*29)
    print ('  '+Y+'['+P+'*'+Y+']'+C+'𝗖𝗢𝗗𝗘 𝗕𝗬 :'+W+' 𓆩@M02MM𓆪™✓🇮🇶')
    print ('  '+Y+'['+P+'*'+Y+']'+C+'𝗖𝗛𝗔𝗡𝗡𝗘𝗟 :'+W+' @uiujq')
    print(f'{G}-{R}-'*29)
logo()
dead = (C+"""▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬~𓆩𝗩𝗜𝗣𓆪~▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬""")
print(dead)
#-------------------------start code---------------------------#
id = input(f'{X} 𝗘𝗡𝗧𝗘𝗥 𝗜𝗗 : ')

token = input(f'{X} 𝗘𝗡𝗧𝗘𝗥 𝗧𝗢𝗞𝗘𝗡 : ')
while True:
    u = "".join(random.choice(l)for i in range(1))
    us = "".join(random.choice(l)for i in range(1))
    use = "".join(random.choice(l)for i in range(1))
    user = "".join(random.choice(l)for i in range(1))
    user = f'{u}_{us}_{use}'
    url = 'https://www.instagram.com/api/v1/web/accounts/web_create_ajax/attempt/'
    headers = {
    'accept': '*/*',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.9,ar;q=0.8',
    'content-length': '56',
    'content-type': 'application/x-www-form-urlencoded',
    'cookie': 'mid=WzoscQAEAAF_6GtVX1t5dOYWEp8t; ig_did=46CAAE8B-316F-4CAC-8FC3-17F9B8A1ABBF; ig_nrcb=1; datr=WUqAZNpT7esRe8Zvmlyg6e9w; csrftoken=yEqvi73A3qJCryIWsy5kYhEy0A2wMrol; ds_user_id=2167209024',
    'dnt': '1',
    'dpr': '1',
    'origin': 'https://www.instagram.com',
    'referer': 'https://www.instagram.com/accounts/emailsignup/',
    'sec-ch-prefers-color-scheme': 'light',
    'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
    'sec-ch-ua-full-version-list': '"Not_A Brand";v="99.0.0.0", "Google Chrome";v="109.0.5414.120", "Chromium";v="109.0.5414.120"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-model': '',
    'sec-ch-ua-platform': '"Windows"',
    'sec-ch-ua-platform-version': '"0.1.0"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
    'viewport-width': '478',
    'x-asbd-id': '129477',
    'x-csrftoken': 'yEqvi73A3qJCryIWsy5kYhEy0A2wMrol',
    'x-ig-app-id': '936619743392459',
    'x-ig-www-claim': '0',
    'x-instagram-ajax': '1009679609',
    'x-requested-with': 'XMLHttpRequest'
    }
    data = {
    'email': '',
    'first_name': '',
    'username': user,
    'opt_into_one_tap': 'false'
    }
    res = requests.post(url, headers=headers, data=data).text
    if "You can't start your username with a period." in res or "This username isn't available. Please try another." in res or "You can't end your username with a period." in res or "A user with that username already exists." in res:
        z+=1
        print(f'{Z}{z} | Bad UserName: {user}')
    else:
        email=0
        print(W+f" [+] {F} Good  ➯ {C}{user} ")
        email+=1
        god=f"""
←•━━━━━━━━━━━━•→
 𝗨𝗦𝗘𝗥 ➠ {user}
←•━━━━━━━━━━━━•→
 𝗕𝗬 » @uiujq - @M02MM """
        requests.get("https://api.telegram.org/bot"+str(token)+"/sendMessage?chat_id="+str(id)+"&text="+str(user))