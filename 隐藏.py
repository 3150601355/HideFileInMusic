import wave 

# 打开要隐藏的文件，读取数据
with open('三体.txt', 'rb') as f:
    txt_data = f.read()
    file_len = len(txt_data)
    txt_data = file_len.to_bytes(3, byteorder = 'little') + txt_data

# 打开wav格式的歌曲文件，读取数据
with wave.open("音乐.wav", "rb") as f:
    wav_data = bytearray( f.readframes(-1) )

# 隐藏txt_data中的数据到wav_data中
for index in range(len(txt_data)):
    wav_data[index * 4] = txt_data[index]
    
# 生成新的歌曲文件
with wave.open("隐藏后-音乐.wav", "wb") as f:
    f.setnchannels(2)       # 双声道
    f.setsampwidth(2)       # 采样数据为两个字节
    f.setframerate(22050)   # 采样率
    
    f.writeframes(wav_data) # 写入数据


