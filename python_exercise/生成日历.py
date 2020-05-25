# 引入日历模块
import calendar

# 输入指定年月
yy = int(input("输入年份: "))
mm = int(input("输入月份: "))

# 显示日历
print(calendar.month(yy, mm))

print(calendar.monthrange(2019,1))
""""输出的是一个元组，第一个元素是所查月份的第一天对应的是星期几（0-6），
第二个元素是这个月的天数。以上实例输出的意思为 2016 年 9 月份的第一天是星期四，该月总共有 30 天。"""

import datetime
#获取昨天日期
def getYesterday():
    today = datetime.date.today()
    oneday = datetime.timedelta(days=1)
    yesterday = today - oneday
    return yesterday
# 输出
print(getYesterday())