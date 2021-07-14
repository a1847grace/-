drive = input('請問你有開過車嗎？')
if drive !='有' and drive != '沒有':
	print('不要亂輸入，只能輸入有或是沒有')
	raise SystemExit
age = input('請問你幾歲？')
age = int(age)
if drive == '有':
	if age >= 18:
		print ('沒錯')
	else:
		print ('為什麼你可以開車')
elif drive == '沒有':
	if age >= 18:	
		print ('你怎麼還沒有開過車')
	else:
		print ('等18歲後，你再來開車')
