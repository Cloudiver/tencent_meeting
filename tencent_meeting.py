import requests
import json
import base64

url = 'https://meeting.tencent.com/l/QtJPhKlCxBvj'  # 会议直播地址
resp = requests.get(url)
online_url = resp.url
online_id = online_url[online_url.rfind('/')+1:]

headers = {
    'Content-Type': 'application/json;charset=UTF-8'
}

data = {
    "meeting_id": online_id
}
payload = json.dumps(data)

requ_url = 'https://meeting.tencent.com/wemeet-webapi/v2/wemeet/live/detail'
live_resp = requests.post(requ_url, headers=headers, data=payload)
live_data = json.loads(live_resp.text)

if live_data.get('code') == 0:
    meeting_code = live_data['data']['meeting_code']  # 会议号
    meeting_subject = base64.b64decode(live_data['data']['meeting_subject']).decode('utf-8')  # 直播主题
    live_url = live_data['data']['live_url']  # live直链
    status = live_data['data']['status']  # 直播状态
    print('会议号: ' + meeting_code)
    print('直播主题: ' + meeting_subject)
    print('直播状态: ' + str(status))
    print('live直链: %s\n%s\n%s' % tuple(live_url))