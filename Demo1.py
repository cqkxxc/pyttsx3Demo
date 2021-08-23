# -*- coding=UTF-8 -*-
# @Time : 2021/8/23 15:14
# @Author : xuchuan
# @Software : PyCharm

import pyttsx3
import pdfplumber

# 读取PDF文档
pdf = pdfplumber.open("Java加密与解密的艺术 - 梁栋.pdf")

# 获取页数
print("总页数：",len(pdf.pages))
print("-----------------------------------------")

# 读取第4页
first_page = pdf.pages[300]
print("本页：",first_page.page_number+1)
print("-----------------------------------------")

# 导出第4页文本
text = first_page.extract_text()
print(text)

# 初始化来获取语音引擎
engine = pyttsx3.init()

# 去掉文本中的换行符
text = text.replace('\n','')

# 朗读文本
# engine.say(text)
# engine.runAndWait()

# 保存音频到本地，格式为mp3
engine.save_to_file(text, 'test.mp3')
engine.runAndWait()

# 调整人声类型
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

# 调整语速,范围一般在0~500之间
rate = engine.getProperty('rate')
engine.setProperty('rate', 500)

# 调整声量，范围在0~1之间
volume = engine.getProperty('volume')
engine.setProperty('volume',0.8)