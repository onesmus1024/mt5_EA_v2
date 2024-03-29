import MetaTrader5 as mt5

account =9159703
password = "E1gRJXt4"
server = "FBS-Demo"
path = "C:\\Program Files\\FBS MetaTrader 5\\terminal64.exe"




def login()->bool:
    if not mt5.initialize(path=path,login=account, password=password, server=server):
        print("initialize() failed, error code =",mt5.last_error())
        quit()
    authorized=mt5.login(account, password=password, server=server)

    if authorized:
        print(mt5.account_info())
        print("Show account_info()._asdict():")
        account_info_dict = mt5.account_info()._asdict()
        for prop in account_info_dict:
            print("  {}={}".format(prop, account_info_dict[prop]))
        return True
    else:
        print("failed to connect at account #{}, error code: {}".format(account, mt5.last_error()))
        return False