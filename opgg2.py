import requests
import re
def opgg2():
    url = "https://www.op.gg/spectate/live/pro-gamer"

    header = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
    }
    cookies = {
    'Cookie':'_gcl_au=1.1.2099108692.1700660106; _pbjs_userid_consent_data=3524755945110770; __qca=P0-1840519177-1700660117994; _lr_env_src_ats=false; _cc_id=17c98f1a0b83691dc9b8d33b9521f3f4; _au_1d=AU1D-0100-001701164358-KOGAP2XT-0FGJ; _oee=2023-08-08T12%3A29%3A58.000Z; _gid=GA1.2.1661309783.1702047331; panoramaId_expiry=1702652138263; panoramaId=6fd172fd974fe865a63414b7b1df16d5393836e69bfae309f34af3fa3fb81079; _pubcid=272c6aee-fd4c-41fe-90c0-b5ac64dd43a9; _pubcid_cst=zix7LPQsHA%3D%3D; __$rs=%22kr%22; _ga_G1664XX595=GS1.1.1702059565.1.0.1702059568.57.0.0; _ga_LY7N9NQLGT=GS1.1.1702059565.1.0.1702059568.0.0.0; cto_bidid=piG1Ul9xU1hOUk9KMUxXbG5TUWZYM2ZFV1hLQkVZbndkUE04TnRlTEtnWEl2ZnJUQU9QTE1QNGxoSFpjSjRUWmFEY1glMkYzTWdQclpnQnZGTkFvdnpBRG9rTHZrUTgwY2tBVWZhOUJ5bExYM0RVd1c4JTNE; _rs=%5B%7B%22key%22%3A%22CHAMPION%22%2C%22value%22%3A%22kr%22%7D%2C%7B%22key%22%3A%22SUMMONER%22%2C%22value%22%3A%22kr%22%7D%5D; pbjs-unifiedid=%7B%22TDID%22%3A%225fde3cb1-7029-4fb7-978b-9dcb5e18993b%22%2C%22TDID_LOOKUP%22%3A%22TRUE%22%2C%22TDID_CREATED_AT%22%3A%222023-11-09T09%3A12%3A20%22%7D; pbjs-unifiedid_last=Sat%2C%2009%20Dec%202023%2009%3A12%3A21%20GMT; bounceClientVisit6439v=N4IgNgDiBcIBYBcEQM4FIDMBBNAmAYnvgO6kB0A9hGQOY1EDGcAhgLYQCWFAduhvgCcApjS7dMAEQDWAvADYEHIbIwSaFMABN5ECig6KekhFRAAaEAJghSxStTrmQHFAH11rlEJT6eMAGbMYF4WLu4Qnt6+3AFBISBeNDAA2gC6AL5AA; _au_last_seen_pixels=eyJhcG4iOjE3MDIxMTI2MDksInR0ZCI6MTcwMjExMjYwOSwicHViIjoxNzAyMTEyNjA5LCJydWIiOjE3MDIxMTI2MDksInRhcGFkIjoxNzAyMTEyNjA5LCJhZHgiOjE3MDIxMTI2MDksImdvbyI6MTcwMjExMjYwOSwiY29sb3NzdXMiOjE3MDIwNTgyOTEsImJlZXMiOjE3MDIxMTI2MDksInBwbnQiOjE3MDIwNTgyOTEsInRhYm9vbGEiOjE3MDIxMTUxOTEsImluZGV4IjoxNzAyMTEyNjA5LCJhZG8iOjE3MDIwNTgyOTEsImltcHIiOjE3MDIwNTgyOTEsImFtbyI6MTcwMjA1ODI5MSwic29uIjoxNzAyMDU4MjkxLCJzbWFydCI6MTcwMjA1ODI5MSwidW5ydWx5IjoxNzAyMDU4MjkxLCJvcGVueCI6MTcwMjA1ODI5MX0%3D; cto_bundle=4LIdiV80Tmlkb0FyaURVbkFLaGc3VFlrYllyMlpEWnNYNlV1NE1mR09MamI1cTZqWHBobTgxc240ZWJ6S1JGcWhjZFg4WkliQllkZHNKSEJMb3FaJTJGN3IwamxGVnNIb09JUDhrb3dnVmFJVnNnSkFoV2hYa3V1bTAxN2tXV1FqcyUyRmt5WkE1eEc4SDN6ZXJyeG5GSkdPRWRtamJ4aE5HUHJEdjRaNE9Ec2s1Y2xBVWpqNU9VR1VqS0J3QUZ1Z3l1TTRsd09mZ3ZLTGVxSnE5JTJGdkdKaDNSQnd5azdnJTNEJTNE; _ol=zh_CN; _ovfr=ap; _ga_Y5593E5J0V=GS1.1.1702115775.1.1.1702115782.0.0.0; _ga_6G6B5VPJ90=GS1.1.1702115775.1.1.1702115782.0.0.0; _ga_HG9DB5ECL8=GS1.1.1702112603.17.1.1702116067.0.0.0; _ga=GA1.2.764994145.1700660106; _awl=2.1702116067.5-bfe3cd42d8146146698abf39915e89d1-6763652d75732d7765737431-0; _ga_37HQ1LKWBE=GS1.1.1702112603.17.1.1702116067.0.0.0; __gads=ID=5da29e1a82499612:T=1700660116:RT=1702116067:S=ALNI_Mbfb40RjfJvemiY2dnP7fiUI1_TVQ; __gpi=UID=00000c942a371503:T=1700660116:RT=1702116067:S=ALNI_MaXESJ-yUTJXSelpOAuCwoFkPXcsg; FCNEC=%5B%5B%22AKsRol_52p7k2_UD6JIoO13uHVZEDxCVHur9_VqCDlN29jmmoOIg90OXWBKxiV-mmaYutw9_Ju7NLRvqN6JL-tEBBsN-1egeob93I7y6kSrMuRqZ0HFtwGk4jHrS1qJB5fJBXLIqxX5OpeiZtnh6ETDsCzxSKZ7Mfw%3D%3D%22%5D%2Cnull%2C%5B%5B5%2C%22838%22%5D%5D%5D; _ga_HKZFKE5JEL=GS1.1.1702112602.17.1.1702116076.50.0.0'
    }
    res = requests.get(url,headers=header, params={'zh_CN': 'zh_CN'},cookies=cookies)
    res.close()
    new_res = res.text.split('<div id="content-container" class="css-1mw8x2 esk32cx0">')[1].split('<div id="div-gpt-ad-1643855213073-0"')[0]

    comp = re.compile('<li class="css-1r8dkjm e857g990">.*?alt=(?P<champion_name>.*?)class="champion".*?class="css-ao94tw e1swkqyq1">'
                      '(?P<id>.*?)</span>.*?class="tier">(?P<iter>.*?)<!.*?<div class="timer".*?<strong></strong>.*?class="team-name">'
                      '(?P<team_name>.*?)</div>.*?class="extra">(?P<id_name>.*?)</div>')
    opgg2_data = re.finditer(comp,new_res)

    return opgg2_data
