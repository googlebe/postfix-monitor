# postfix-monitor

## 概要

SMTPサーバのサービス稼働監視プログラム  
cron等から本プログラムをキックし、特定SMTPサーバへメールを送信する  
メールが送信できない場合は別SMTPサーバへメールを送信し、障害通知を行う  

## 動作環境

Language: Python 2.x  
Platform: LinuxOS  

## 実行

```bash
$ python postfix-monitor.py
```
