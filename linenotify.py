import requests
import sys
import argparse

class LineNotify:
    API = 'https://notify-api.line.me/api/notify'

    def __init__(self, token):
        self.token = token

    def msg(self, msg, filename_image = None):
        payload = {'message': msg}
        headers = {'Authorization': 'Bearer ' + self.token}
 
        if filename_image is None :
            # テキスト
            r = requests.post(LineNotify.API, data=payload, headers=headers)
        else :
            # テキスト+画像 (LINEの仕様で画像のみは不可)
            f = {"imageFile": open(filename_image, "rb")} #jpeg or png
            r = requests.post(LineNotify.API, data=payload, headers=headers, files=f)
        return r

    def sticker(self, msg, package_id, sticker_id):
        payload = {'message': msg, 'stickerPackageId' : package_id, 'stickerId' : sticker_id}
        headers = {'Authorization': 'Bearer ' + self.token}
        
        r = requests.post(LineNotify.API, data=payload, headers=headers)
        return r
  
    def status(self):
        headers = {'Authorization': 'Bearer ' + self.token}
        r = requests.get('https://notify-api.line.me/api/status', headers=headers)
        return r.text

def test_mode(token):
    line_notify = LineNotify(token)

    print(line_notify.msg('line notify class version test'))
    print(line_notify.msg('line notify with image', 'test.jpg'))
    print(line_notify.sticker('sticker test', 2,161))
    print(line_notify.status())

def pipe_mode(token):
    msg = sys.stdin.readlines()
    msg = [line.rstrip() for line in msg]
    msg = '\r\n' + '\r\n'.join(msg)

    line_notify = LineNotify(token)
    print(line_notify.msg(msg))

def main():
    p = argparse.ArgumentParser()
    p.add_argument('line_token', help='LINE access token')
    p.add_argument('--test', action='store_true', help='test mode')
    p.add_argument('-m', '--msg' , help='notify message')
    p.add_argument('-f', '--file' , help='image file (jpeg or png)')

    args = p.parse_args()
    token = args.line_token     
    if  args.test:
        test_mode(token)
    elif args.msg is not None:
        line_notify = LineNotify(token)
        if args.file is not None:
            print(line_notify.msg(args.msg, args.file))
        else:
            print(line_notify.msg(args.msg))
    else:
        pipe_mode(token) 

if __name__ == '__main__':
    main()
