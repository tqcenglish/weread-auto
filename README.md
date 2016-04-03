# 微信读书自动翻页
由于微信读书通过阅读时长送币(可以买书的币). 每周5小时，最多10个币。
如果没有时间阅读，又想攒币。就需要一个自动翻页程序了。

## Android
通过 uiautomator 循环发送翻页指令到手机中。

- [uiautomator](https://github.com/xiaocong/uiautomator)

## 安装

```
sudo apt-get install python-pip python-dev build-essential
sudo pip install uiautomator
```

## 运行
```
python android.py
```

## 注意
- 需要 adb 环境，并通过 pip 安装 uiautomator。
- 手机不能锁屏(需要调节锁屏时间足够长)
