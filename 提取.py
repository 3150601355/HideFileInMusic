# 关于这个程序的视频教程：https://www.bilibili.com/video/BV1NF411i7Zh/
# 作者：B站@偶尔有点小迷糊
# 我的口号是：用不正经的风格 讲正经编程知识
#
# 使用本代码请保留以上信息

import wave 

# 打开藏有其它文件的歌曲文件，读取数据
with wave.open('隐藏后-音乐.wav', 'rb') as f:
    wav_data = f.readframes(-1)

# 提取wav_data中的特殊位置数据
extract_data = bytearray()
for index in range(0, len(wav_data), 4):
    extract_data += (wav_data[index]).to_bytes(1, byteorder = 'little')

# 得到被隐藏的文件的大小
file_len = int.from_bytes(extract_data[0:3], 'little')

# 重新生成被隐藏的文件
with open('提取结果-三体.txt', 'wb') as f:
    f.write(extract_data[3 : file_len+3])

