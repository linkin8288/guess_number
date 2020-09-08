# 產生一個隨機整數1-100(不要印出來)
# 讓使用者重複輸入數字去猜
# 猜對的話 印出'出於猜對了'
# 猜錯的話 印出'比答案大/小'

import random # 載入隨機模組

r = random.randint(1, 100) #用函式產生隨機數
while True:
	num = input('請猜數字: ') #input都會把東西存成字串
	num = int(num) #將字串轉換成整數
	if num == r:
		print('你猜中了!')
		break
	elif num > r:
		print('比答案大')
	elif num < r:
		print('比答案小')	