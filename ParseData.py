def ParseInputString(self, inputData):
		# inputStr = "100 documnets"
		price = ""
		priceArray = []
		productArray = []
		dataLength = len(inputData)
		for i in range(dataLength):
			if IsCharNumber(inputData[i]):
				price += input
			else if IsCharCurrensy(inputData):
				price = int(price) * 65
			else:
				priceArray.append(price)
				productArray.append(inputData[i:dataLength])
		return [priceArray, productArray];


	def IsCharNumber(str char):
		numeralArray = "0123456789"
		if char in numeralArray:
			return True;
		return False;

	# С помощью этого метода можно будет получать
	# затраченные деньги в валюте в родной валюте
	def IsCharCurrensy(str char):
		numeralArray = "$"
		if char in numeralArray:
			return True;
		return False;