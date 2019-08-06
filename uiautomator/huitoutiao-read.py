# coding:utf-8
from uiautomator import device as d
import random
import time
import datetime

# 加关注，容易出现在文章列表
news = ["光明网", "新华社", "中国青年网", "看看新闻", "娱小白", "环球网", "花影故事"]
# news = ["小时前", "评"]


# 点亮屏幕
def light_screen():
    d.screen.on()


# 自动阅读
def auto_read():
    print("自动阅读")
    # 随机滚动距离
    d.swipe(500, 100 * random.uniform(3, 10), 500, 100)

    if d(text='展开全文').exists:
        d(text='展开全文').click()

    # 随机停止 0-4 秒
    time.sleep(random.uniform(0, 4))


# 寻找新文章
def click_new():
    while 1:
        # 滑动寻找指定文章
        d.swipe(500, 1000, 500, 400)
        random.shuffle(news)
        for new in news:
            print('寻找' + new)
            if d(text=new).exists:
                d(text=new).click()
                return
        print('寻找失败, 继续')
        time.sleep(1000)


# 开始阅读
def start_read():
    print("寻找新文章")
    click_new()
    # 开始阅读
    print("开始自动阅读阅读")
    while True:
        auto_read()
        if d(text='没有更多了').exists:
            d.press("back")
            # 滚动一次，否则一次阅读到同一文章
            d.swipe(500, 1000, 500, 100)
            break
        else:
            auto_read()
    # 重新阅读
    start_read()

# 执行5小时
if __name__ == '__main__':

    print("点亮屏幕")
    # light_screen()

    # 获取当前时间
    startTime = datetime.datetime.now()
    while 1:
        now_time = datetime.datetime.now()
        mkt_last = time.mktime(startTime.timetuple())
        mkt_now = time.mktime(now_time.timetuple())
        post_time = (mkt_now - mkt_last) / 60  # 转成分钟
        # 1小时 ＝＝＝ 60分钟
        left_time = 60 - post_time
        if left_time > 0:
            print("剩余" + str(int(left_time)) + '分钟')
            start_read()
        else:
            print("自动读书完毕")
            break
