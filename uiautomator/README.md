# 基于 - [uiautomator](https://github.com/xiaocong/uiautomator) 实现 Android 手机控制

## 安装

``` bash
sudo apt-get install python-pip python-dev build-essential
sudo pip install uiautomator
```

## 微信读书自动翻页

由于微信读书通过阅读时长送币(可以买书的币). 每周5小时，最多10个币。
如果没有时间阅读，又想攒币。就需要一个自动翻页程序了。

### 运行微信读书

``` bash
python android.py
```

## 惠头条

阅读新闻，收获金币, 提现

### 运行惠头条

``` bash
python huitoutiao-read.py
```

## 注意

- 需要 adb 环境，并通过 pip 安装 uiautomator。
- 手机不能锁屏(需要调节锁屏时间足够长)
