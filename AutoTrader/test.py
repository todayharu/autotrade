import pyupbit

access = "eg4u4yoRNrHZEpxtURSCTOeWPYnDaOpoLkjHX3X2"          # 본인 값으로 변경
secret = "BJLWKIKVwUDLVIYnoAFUE0pL23xoXEQaO77XUVeg"          # 본인 값으로 변경
upbit = pyupbit.Upbit(access, secret)

ticker = 'KRW-ETH'

print(pyupbit.get_current_price(ticker))
print(pyupbit.get_ohlcv(ticker=ticker, interval="minute1"))

print(upbit.get_balances())
