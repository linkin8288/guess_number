# 產生一個隨機整數1-100(不要印出來)
# 讓使用者重複輸入數字去猜
# 猜對的話 印出'出於猜對了'
# 猜錯的話 印出'比答案大/小'
# 開始計數
# 讓使用者決定數字範圍

import random # 載入隨機模組
start = input('請決定隨機數字開始值: ')
end = input('請決定隨機數字結束值: ')
start = int(start)
end = int(end)

r = random.randint(start, end) #用函式產生隨機數
count = 0 # 不能寫在迴圈裡面，不然會一直歸零
while True:
	count += 1 # count = count = count + 1
	num = input('請猜數字: ') #input都會把東西存成字串
	num = int(num) #將字串轉換成整數
	if num == r:
		print('你猜中了!')
		print('這是你猜的', count, '次')
		break
	elif num > r:
		print('比答案大')
	elif num < r:
		print('比答案小')	
	print('這是你猜的', count, '次') # 若寫在if裡面，就要寫三次，這樣只要寫一次就好