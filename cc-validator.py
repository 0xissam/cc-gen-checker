class CreditCard:
	# Main Method
	@staticmethod
	def main(args):
		number = 4067490481539276
		number = int(number)
		print(str(number) + " is " +
			("valid" if CreditCard.isValid(number) else "invalid"))
		
	# Return true if the card number is valid
	@staticmethod
	def isValid(number):
		return (CreditCard.getSize(number) >= 13 and CreditCard.getSize(number) <= 16) and (CreditCard.prefixMatched(number, 4) or CreditCard.prefixMatched(number, 5) or CreditCard.prefixMatched(number, 37) or CreditCard.prefixMatched(number, 6)) and ((CreditCard.sumOfDoubleEvenPlace(number) + CreditCard.sumOfOddPlace(number)) % 10 == 0)
	
	# Get the result from Step 2
	@staticmethod
	def sumOfDoubleEvenPlace(number):
		sum = 0
		num = str(number) + ""
		i = CreditCard.getSize(number) - 2
		while (i >= 0):
			sum += CreditCard.getDigit(int(str(num[i]) + "") * 2)
			i -= 2
		return sum
	
	# Return this number if it is a single digit, otherwise,
	# return the sum of the two digits
	@staticmethod
	def getDigit(number):
		if (number < 9):
			return number
		return int(number / 10) + number % 10
	
	# Return sum of odd-place digits in number
	@staticmethod
	def sumOfOddPlace(number):
		sum = 0
		num = str(number) + ""
		i = CreditCard.getSize(number) - 1
		while (i >= 0):
			sum += int(str(num[i]) + "")
			i -= 2
		return sum
	
	# Return true if the digit d is a prefix for number
	@staticmethod
	def prefixMatched(number, d):
		return CreditCard.getPrefix(number, CreditCard.getSize(d)) == d
	
	# Return the number of digits in d
	@staticmethod
	def getSize(d):
		num = str(d) + ""
		return len(num)
	
	# Return the first k number of digits from
	# number. If the number of digits in number
	# is less than k, return number.
	@staticmethod
	def getPrefix(number, k):
		if (CreditCard.getSize(number) > k):
			num = str(number) + ""
			return int(num[0:k])
		return number

if __name__ == "__main__":
	CreditCard.main([])

# This code is contributed by Aarti_Rathi
