from bitcoinrpc.authproxy import AuthServiceProxy

def connect_to_btccore(network, rpc_user, rpc_pwd):
    if network == 'mainnet':
        rpc_connection = AuthServiceProxy(
            'http://%s:%s@localhost:8332' % (rpc_user, rpc_pwd)
        )
    elif network == 'signet':
        rpc_connection = AuthServiceProxy(
            'http://%s:%s@localhost:38332' % (rpc_user, rpc_pwd)
        )
    elif network == 'regtest':
        rpc_connection = AuthServiceProxy(
            'http://%s:%s@localhost:18332' % (rpc_user, rpc_pwd)
        )
    return rpc_connection

def get_transaction_fees():
    rpc_connect = connect_to_btccore('signet', 'rpc_username', 'rpc_password')
    mempool_list = rpc_connect.getrawmempool(True)
    transaction_fees = [{i: str(mempool_list[i]['fees']['base'])} for i in mempool_list]
    return transaction_fees


def get_lowest_and_highest():
    rpc_connect = connect_to_btccore('signet', 'rpc_username', 'rpc_password')
    mempool_list = rpc_connect.getrawmempool(True)
    fees = [mempool_list[i]['fees']['base'] for i in mempool_list]
    lowest = min(fees)
    highest = max(fees)
    return {'lowest_fee': lowest, 'highest fee': highest}


if __name__ == '__main__':
    print(get_transaction_fees())
    print(get_lowest_and_highest())
