import requests
import re
class Data():
    def __init__(self,iter,position):
        self.iter = iter
        self.position = position
    def opgg(self):

        url = 'https://www.op.gg/champions?region=kr&tier={}&patch=13.24&position={}'.format(self.iter,self.position)
        header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
        }

        request = requests.get(url, headers=header, params={'zh_CN': 'zh_CN'})

        new_text = request.text.split('<main>')[1].split('</main>')[0].split('<tbody>')[1].split('</tbody>')[0] #缩短数据范围

        request.close() #关闭requests
        res_id = re.compile('<td class="css-ijscnw e1lge34e4"><span>(?P<id>.*?)</span>.*?<strong>(?P<name>.*?)'
                            '</strong>.*?<td .*?<span.*?</span>(?P<tier>.*?)</td>.*?<td class="css-9aydzo e1tupkk21">'
                            '.*?(?P<win>.*?)<!.*?</td><td class="css-9aydzo e1tupkk21">(?P<pick>.*?)<!.*?</td><td class="css-9aydzo e1tupkk21">'
                            '(?P<ban>.*?)<!.*?</td>')
        #正则表达式
        opgg_data = re.finditer(res_id,new_text)
        return opgg_data





