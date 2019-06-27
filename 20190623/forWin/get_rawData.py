#Raw Dataの取得
import thinkgear
PORT = '/dev/tty.MindWaveMobile-SerialPo' 
for packets in thinkgear.ThinkGearProtocol(PORT).get_packets():
    for p in packets:
        if isinstance(p, thinkgear.ThinkGearRawWaveData):
            print (p)