# 关于这个程序的视频教程：https://www.bilibili.com/video/BV1NF411i7Zh/
# 作者：B站@偶尔有点小迷糊
# 我的口号是：用不正经的风格 讲正经编程知识
#
# 使用本代码请保留以上信息

import wave 

# 打开要隐藏的文件，读取数据
with open('三体.txt', 'rb') as f:
    txt_data = f.read()
    file_len = len(txt_data)
    txt_data = file_len.to_bytes(3, byteorder = 'little') + txt_data

# 打开wav格式的歌曲文件，读取数据
with wave.open("音乐.wav", "rb") as f:
    attrib = f.getparams()    # 获取音频属性 
    wav_data = bytearray( f.readframes(-1) )

# 隐藏txt_data中的数据到wav_data中
for index in range(len(txt_data)):
    wav_data[index * 4] = txt_data[index]
    
# 生成新的歌曲文件
with wave.open("隐藏后-音乐.wav", "wb") as f:
    f.setparams(attrib)     # 设置音频属性    
    f.writeframes(wav_data) # 写入数据


