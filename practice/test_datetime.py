# -*- coding: utf-8 -*-

from datetime import datetime
from datetime import timedelta # 计算时间
from datetime import timezone # 计算时区

# print(datetime.now())
#
# print(datetime(2017, 4, 21, 18,34))
#
# print(datetime.now().timestamp()) # 将时间转换成时间戳，整数表示秒，小数表示毫秒
#
# print(datetime.fromtimestamp(datetime.now().timestamp())) # 本地时间
# print(datetime.utcfromtimestamp(datetime.now().timestamp())) # utc时间

print(datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S')) # 字符串转换成时间

print(datetime.now().strftime('%a %b %d %H:%M:%S'))

print(datetime.now()+timedelta(hours=2, days=3, seconds=20))

tz_utc_8 = timezone(timedelta(hours=8))

now = datetime.now()
print(now.replace(tzinfo=tz_utc_8)) # 系统为tz_utc_8时区时，才正确
utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc) # 获取当前时区并强制转换
print(utc_dt) # 将时区设置为utc
bj_dt =utc_dt.astimezone(timezone(timedelta(hours=8))) # 时区转换
print(bj_dt)

# timestamp与时区无关