# tencent_meeting
腾讯会议直播直链获取，可用于录制直播视频。

输出示例：

```text
会议号: 223943850
直播主题: 清华大学第三届“全球水循环遥感与水利大数据”暨“中国第四届卫星重力与水文学”论坛
直播状态: 2
live直链: https://liveplay.wemeet.tencent.com/trtc_1400115281/stream_7186919883062861502_913650855.flv?txTime=5ff2ccc0&txSecret=B2231A61AB13ADD73B9368F1A413530E
https://liveplay.wemeet.tencent.com/trtc_1400115281/stream_7186919883062861502_913650855.m3u8?txTime=5ff2ccc0&txSecret=B2231A61AB13ADD73B9368F1A413530E
rtmp://liveplay.wemeet.tencent.com/trtc_1400115281/stream_7186919883062861502_913650855?txTime=5ff2ccc0&txSecret=B2231A61AB13ADD73B9368F1A413530E
```

获取到 `live_url` 后就可以用IDM或者其他工具下载(录制)视频。

优点：录制的视频为原画质

缺点：不能中途停止录制，必须要等直播方关闭推流后，才会保存视频。

但是也能解决：取消下载后，可以在 `C:\Users\fan\AppData\Roaming\IDM\DwnlData\fan`下找到一个没有扩展名的文件。在文件名后添加 `.flv` 即可正常播放。

其他录制方式，比如说ffmpeg：

```bash
ffmpeg -i "https://liveplay.wemeet.tencent.com/trtc_1400115281/stream_7186919883062861502_913650855.flv?txTime=5ff2ccc0&txSecret=B2231A61AB13ADD73B9368F1A413530E" -c:v copy -c:a copy -bsf:a aac_adtstoasc 12_05_meeting.mp4
```