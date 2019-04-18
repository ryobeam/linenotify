# linenotify

## usage command line
``$ python3 linenotify.py [-h] [--test] [-m MSG] [-f FILE] line_token``

    positional arguments:  
      line_token            LINE access token

    optional arguments:  
      -h, --help            show this help message and exit  
      --test                test mode  
      -m MSG, --msg MSG     notify message  
      -f FILE, --file FILE  image file (jpeg or png)  

## usage from python
``` python
import linenotify

line_notify = LineNotify(token)
line_notify.msg(msg)
```
