#Raw Dataをファイルに出力

import thinkgear
PORT = '/dev/tty.MindWaveMobile-SerialPo' 
buf_file  = open("./buf.csv","a")
buf = []
con = 0
for packets in thinkgear.ThinkGearProtocol(PORT).get_packets():
    for p in packets:
        if isinstance(p, thinkgear.ThinkGearRawWaveData):
            print(p)
            #ファイルの書き込み
            buf_file.write(str(p)+'\n')
            con += 1
    #1000個のrawデータを取得したら終了
    if con == 1000: 
        break
