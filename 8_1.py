class Date:
    def __init__(self, date):
        self.date = date
    def __str__(self):
        return self.date

    @staticmethod
    def check(self):
        a = self.date.splite('-')
        print(a)
        if int(a[0]) > 32:
            print('Не корректная дата')
        elif int(a[1]) > 12:
            print('не корректный месяц')
        print('Дата корректна')

    @classmethod
    def digit(cls, date):
        ndate = []
        for i in date.splite('-'):
            ndate.append(int(i))
        print(ndate)

a = Date('54-13-2020')
#print(a.date)
a.check
a.digit('54-13-2020')


