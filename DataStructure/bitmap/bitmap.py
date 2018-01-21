class Bitmap(object):
    def __init__(self,max):
        self.size=self.calcElemIndex(max,True)
        self.array=[0 for i in range(self.size)]

    def calcElemIndex(self, num, up=False):
        '''up为True则为向上取整, 否则为向下取整'''
        if up:
            return int((num + 31 - 1) // 31)  # 向上取整
        return num // 31

    def calcBitIndex(self,num):
        return num % 31

    def set(self,num):
        '''

        :param num:num从0开始
        :return:
        '''
        elemIndex=self.calcElemIndex(num)
        bitIndex=self.calcBitIndex(num)
        elem=self.array[elemIndex]
        self.array[elemIndex]=elem|(1<<bitIndex)

    def clean(self, i):
        elemIndex = self.calcElemIndex(i)
        bitIndex = self.calcBitIndex(i)
        elem = self.array[elemIndex]
        self.array[elemIndex] = elem & (~(1 << bitIndex))

    def test(self, i):
        elemIndex = self.calcElemIndex(i)
        byteIndex = self.calcBitIndex(i)
        if self.array[elemIndex] & (1 << byteIndex):
            return True
        return False


if __name__=='__main__':
    MAX = 879
    suffle_array = [45, 2, 78, 35, 67, 90, 879, 0, 340, 123, 46]
    result = []
    bitmap = Bitmap(MAX)
    for num in suffle_array:
        bitmap.set(num)
    for i in range(MAX + 1):
        if bitmap.test(i):
            result.append(i)
    print(result)


