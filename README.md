linenotify
---
Line へ通知をコマンドラインツールとライブラリ。
Python から import して使用できる。

## usage
### command line
``$ python3 linenotify.py [-h] [--test] [-m MSG] [-f FILE] line_token``

    positional arguments:  
      line_token            LINE access token

    optional arguments:  
      -h, --help            show this help message and exit  
      --test                test mode  
      -m MSG, --msg MSG     notify message  
      -f FILE, --file FILE  image file (jpeg or png)  

### from python
``` python
import linenotify

line_notify = LineNotify(token)
line_notify.msg(msg)
```

## Licence

MIT

## Author

[ryobeam](https://github.com/ryobeam)
