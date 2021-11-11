
class Testchallenges():

    def test_challengeFour(self):
        print('{} - {}'.format(self.getFibonacci(7), self.getStringNumber(self.getFibonacci(7))))
        print('{} - {}'.format(self.getFibonacci(12), self.getStringNumber(self.getFibonacci(12))))
        print('{} - {}'.format(self.getFibonacci(15), self.getStringNumber(self.getFibonacci(15))))
        print('{} - {}'.format(self.getFibonacci(20), self.getStringNumber(self.getFibonacci(20))))

    def getFibonacci(self, n):

        if n < 0:
            print("Incorrect input")
        elif n == 0:
            return 0
        elif n == 1 or n == 2:
            return 1
        else:
            return self.getFibonacci(n - 1) + self.getFibonacci(n - 2)

    def getStringNumber(self, n):
        numberText = {
            1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five',
            6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten',
            11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen',
            15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen',
            19: 'nineteen', 20: 'twenty',
            30: 'thirty', 40: 'forty', 50: 'fifty', 60: 'sixty',
            70: 'seventy', 80: 'eighty', 90: 'ninety',
            100: 'hundred', 1000: 'thousand', 1000000: 'million'
        }
        if n == 0:
            return 'zero'
        if n < 0:
            return 'negative ' + self.getStringNumber(-n)
        result = ''

        for num in sorted(numberText.keys(), reverse=True):
            count = int(n / num)
            if (count < 1):
                continue
            if (num >= 100):
                result += self.getStringNumber(count) + ' '
            result += numberText[num]
            n -= count * num
            if (n > 0):
                result += ' '
        return result
