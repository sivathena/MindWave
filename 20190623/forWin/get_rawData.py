#Raw Dataの取得
import thinkgear


PORT = 'COM5' #'/dev/tty.MindWaveMobile-SerialPo' 
for packets in thinkgear.ThinkGearProtocol(PORT)._read(100):
    #print (packets)
    for p in packets:
        if isinstance(p, thinkgear.ThinkGearRawWaveData):
            print('true')
        print (p)
