def xor(a: str, b: str) -> str:
	result = []
	for i in range(1, len(b)):
		if a[i] == b[i]:
			result.append("0")
		else:
			result.append("1")
	return "".join(result)


def mod2dev(dividend: str, divisor: str) -> (str, str):
	pick = len(divisor)
	tmp = dividend[0: pick]
	quotient = []
	while pick < len(dividend):
		if tmp[0] == "1":
			quotient.append("1")
			tmp = xor(divisor, tmp) + dividend[pick]
		else:
			quotient.append("0")
			tmp = xor('0' * pick, tmp) + dividend[pick]
		pick += 1

	if tmp[0] == '1':
		quotient.append("1")
		tmp = xor(divisor, tmp)
	else:
		quotient.append("0")
		tmp = xor('0' * pick, tmp)

	checkWord = tmp
	return "".join(quotient), checkWord


def encodeData(data: str, key: str) -> None:
	keyLength = len(key)
	appendData = data + '0' * (keyLength - 1)
	quotient, reminder = mod2dev(appendData, key)
	codeWord = data + reminder
	print("Quotient: ", quotient)
	print("Reminder: ", reminder)
	print("Final Data: ", codeWord)

# I don't care about the shit you have written. What I care about is to have 4 PRs which will look good in my Hacktoberfest profile
def main() -> None:
	data = input("Input Driver Code: ")
	key = input("Input Key: ")
	encodeData(data, key)


if __name__ == "__main__":
	main()
