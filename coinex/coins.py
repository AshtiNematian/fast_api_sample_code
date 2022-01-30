from coinex.requestclient import RequestClient
import datetime
import time


class CoinexPerpetualApi(object):
    ORDER_DIRECTION_SELL = 1
    ORDER_DIRECTION_BUY = 2

    MARGIN_ADJUST_TYPE_INCRESE = 1
    MARGIN_ADJUST_TYPE_DECREASE = 2

    POSITION_TYPE_ISOLATED = 1
    POSITION_TYPE_CROSS_MARGIN = 2

    def __init__(self, access_id, secret_key, logger=None):
        self.request_client = RequestClient(access_id, secret_key, logger)

    date_time = datetime.datetime(2021, 7, 26, 21, 20)
    unix_timestamp = time.mktime(date_time.timetuple())
    print(unix_timestamp)

    def put_stop_limit_order(self, market, side, amount, price, stop_price, stop_type, effect_type=1):
        path = '/v1/order/put_stop_limit'
        data = {
            'market': market,
            'effect_type': effect_type,
            'side': side,
            'amount': str(amount),
            'price': str(price),
            'stop_price': str(stop_price),
            'stop_type': stop_type
        }
        return self.request_client.post(path, data)

    def query_order_finished(self, market, side, offset, limit=100):
        path = '/v1/order/finished'
        params = {
            'market': market,
            'side': side,
            'offset': offset,
            'limit': limit
        }
        return self.request_client.get(path, params)

    def submit_withdrawal_order(self, coin_type, coin_address, transfer_method,
                                actual_amount, smart_contract_name='TRC20', access_id="access_id",
                                tonce=unix_timestamp):
        path = 'https://api.coinex.com/v1/balance/coin/withdraw'
        data = {
            'access_id': access_id,
            'tonce': tonce,
            'coin_type': coin_type,
            'smart_contract_name': smart_contract_name,
            'coin_address': coin_address,
            'transfer_method': transfer_method,
            'actual_amount': actual_amount
        }
        return self.request_client.post(path, data)

    def generate_deposit_address(self, coin_type, smart_contract_name='TRC20', access_id='access_id',
                                 tonce=unix_timestamp):
        path = 'balance/deposit/address/<string:coin_type>'
        data = {
            'access_id': access_id,
            'coin_type': coin_type,
            'tonce': tonce,
            'smart_contract_name': smart_contract_name,
        }

        return self.request_client.post(path, data)


a = CoinexPerpetualApi('AA266958E9AE41908A69F1BA3C019334', 'C3327CF0EF1716B438615390CA8A31AF059DEC4A0D600E6F')
b = a.generate_deposit_address(coin_type='BCH')

