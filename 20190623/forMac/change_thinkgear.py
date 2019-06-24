# RawData 数値のみの表示
# ターミナルで　$pip show thinkgear　コマンドを実行してインストールされている箇所を探す
# thinkgear.py内の以下の箇所を書き直す

class ThinkGearRawWaveData(ThinkGearData):
    '''RAW Wave Value (-32768 to 32767)'''
    code = 0x80
    _strfmt = '%(value)s' #この箇所
    _decode = staticmethod(lambda v: struct.unpack('>h', v)[0])
    # There are lots of these, don't log them by default
    _log = False