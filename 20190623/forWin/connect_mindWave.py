# 環境
# macOs Mojave
# python 2.7.13

# 手順
# 1. python に thinkgear,pyserial(シリアル通信を行うためのライブラリ)をインストール
#  $pip install thinker
#  $pip install pyserial
# 2. ThinkGear ConnectorをPCにインストール
#  http://developer.neurosky.com/docs/doku.php?id=thinkgear_connector_tgc
# 3. ThinkGear Connectorを起動
# 4. ターミナルで　$ls /dev/tty.* で /dev/tty.MindWaveMobile-SerialPo　 が表示されていることを確認
# 5. サンプルコードで脳波を取得できる

#mindwaveの接続
import thinkgear
PORT = '/dev/tty.MindWaveMobile-SerialPo' 
for packets in thinkgear.ThinkGearProtocol(PORT).get_packets():
    for p in packets:
        if isinstance(p, thinkgear.ThinkGearRawWaveData):
            continue
        print (p)