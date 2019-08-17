#Raw Dataの取得
#from thinkgearPy3 import tk
import thinkgearPy3

#forWin
PORT = "COM5"
#forAny 
#PORT = '/dev/tty.MindWaveMobile-SerialPo' 

thinkgearObj = thinkgearPy3.ThinkGearProtocol(PORT)

while True:
    #ヘッダ部分の読み込み
    headData = thinkgearObj._read(3)
    #print('DEBUG(HEADER)', headData, sep = '')
    
    if ((headData[0] == 170)
    and (headData[1] == 170)):
        # データ本体とチェックサムの取得
        packet = thinkgearObj._read(headData[2])
        checksum = thinkgearObj._read(1)

        print('DEBUG(PACKETS):', packet[0] ,' ', packet[1], sep = '')

        # チェックサムのデータチェック
        if (ord(checksum) == thinkgearObj._chksum(packet)):
            retDecode = thinkgearObj._decode(packet)

            if (type(retDecode) == type(thinkgearPy3.ThinkGearUnknownData)):
                print('Unknown!!')

            print(retDecode)
