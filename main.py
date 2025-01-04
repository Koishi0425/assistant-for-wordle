import json
import os
import re

cwd = os.getcwd()
json_file = os.path.join(cwd, 'wordlist.json')

# 读取wordlist.json文件，编码utf-8
with open(json_file, 'r', encoding='utf-8') as f:
    wordlist = json.load(f)

# 用户输入单词长度
try:
    word_length = int(input('请输入单词长度: '))
except ValueError:
    print('请输入一个整数')
    word_length = int(input('请输入单词长度: '))

# 用户输入已知字母位置信息，未知字母位置用0代替，单词长度必须符合word_length
hint = input('请输入已知字母位置信息（未知字母位置用0代替）: ')
while len(hint) != word_length:
    hint = input('已知字母位置信息与单词长度不符，请重新输入: ')

# 生成已知字母位置信息的正则表达式
pattern = '^' + ''.join(['.' if i == '0' else re.escape(i) for i in hint]) + '$'

# 除去已知字母位置外，还有已知存在字母不知道位置的信息
word_exist = input('请输入已知存在字母不知道位置的信息，字母之间用逗号隔开: ')

# 在wordlist中查找符合条件的单词，剔除不包含word_exist中的字母的单词
result = []
word_secected = [word for word in wordlist if word['length'] == word_length]

for word in word_secected:
    if all(letter in word['word'] for letter in word_exist.split(',')):
        if re.match(pattern, word['word']):
            result.append(word['word'])
            
print(result)
        