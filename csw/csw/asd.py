import json

data = {
    'medince_consumption': '<td>\r\n                            <a href="https://ypk.familydoctor.com.cn/factory_226_0_0_0_0_1.html" class="link1">江西盛翔制药有限公司</a>\r\n                        </td>',
    'medince_component': '<td>疏散风热，清热止咳。用于小儿感冒发热，汗出不爽，鼻塞流涕，咳嗽咽痛</td>', 'medince_effect': '<td>国药准字Z20090894</td>',
    's_cate': '小儿感冒', 'b_cate': '\r\n                                [儿科用药]\r\n                        ',
    'medince_name': '小儿感冒宁合剂', 'medince_pic': 'https://ypk.familydoctor.com.cn/202706/',
    'medince_character': '<td>\r\n                                <span class="link1"><a href="https://ypk.familydoctor.com.cn/disease_88_0_0_0_0_1.html" target="_blank">感冒</a></span>\r\n                                <span class="link1"><a href="https://ypk.familydoctor.com.cn/disease_13005_0_0_0_0_1.html" target="_blank">小儿感冒</a></span>\r\n                                <span class="link1"><a href="https://ypk.familydoctor.com.cn/disease_7745_0_0_0_0_1.html" target="_blank">时行感冒</a></span>\r\n                        </td>',
    'medince_enterprise': None}


# scrapy crawl medince -o teachers.json
#
# # json lines格式，默认为Unicode编码
# scrapy crawl medince -o teachers.jsonl
#
# # csv 逗号表达式，可用Excel打开
# scrapy crawl medince -o teachers.csv
#
# # xml格式
# scrapy crawl medince -o teachers.xml



file = open('medince.json', 'wb')



content = json.dumps(dict(data), ensure_ascii=True) + "\n"
content=content.encode()
file.write(content)




file.close()