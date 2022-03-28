# class TimeDesk:
#     def __init__(self,seconds):
#         self.sec = seconds
#
#
#     def converter_day(self):
#             self.day = self.sec//3600//24
#             self.hours = self.sec//3600-self.day*24
#             self.minutes = self.sec%3600//60
#             self.seconds = self.sec%3600%60
#             return f'{self.day}ДНИ,{self.hours} ЧАСОВ, {self.minutes} МИНУТ, {self.seconds} СЕКУНД'
#
# time = TimeDesk(seconds=60)
# print(time.converter_day())


def fun():
    print('fun')
print(fun())