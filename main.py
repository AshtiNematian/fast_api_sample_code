from fastapi import FastAPI
from coinex.coins import CoinexPerpetualApi
import json

app = FastAPI()
robot = CoinexPerpetualApi('AA266958E9AE41908A69F1BA3C019334',
                           'C3327CF0EF1716B438615390CA8A31AF059DEC4A0D600E6F')


@app.get("/")
async def orders(market: str, side: int, amount: float, price: str, stop_price: str, stop_type: int):
    """

    :param market:Perpetual Market
    :param side: 1: Sell for Short, 2: Buy for Long
    :param amount:Delegation Amount
    :param price:Delegated Price
    :param stop_price:Stop Price
    :param stop_type:Stop Type 1: Trigger at the latest price 2:Trigger at the index price
    3: Trigger at the mark price
    :return:order status
    """
    result = robot.put_stop_limit_order(
        market,
        side,
        amount,
        price,
        stop_price,
        stop_type,

    )
    return json.dumps(result)


@app.get("/finished_order_history")
async def finished_order_history(market: str, side: int, offset: int, limit: int):
    """

    :param market:Perpetual Market
    :param side:0 for no limit, 1 for sell, 2 for buy
    :param offset:means query from a certain record
    :param limit:The number of records acquired at a time, the default is 20 and the maximum is 100.
    :return:
    """
    finished_result = robot.query_order_finished(
        market,
        side,
        offset,
        limit
    )

    return finished_result


@app.get("/submit_withdrawal_order")
async def submit_withdrawal_order(tonce: int, coin_type: str,
                                  coin_address: str,
                                  transfer_method: str,
                                  actual_amount: str):
    """

    :param tonce:intiger timestamp  that represents the number
    of milliseconds from Unix to the current time
    :param coin_type:USDT-ADA-DOT-BNV
    :param coin_address:Withdrawal address, which must be authorized
    :param transfer_method:onchain -- Normal transfer local -- Inter-user transfer
    :param actual_amount:Withdrawal actual amount
    :return:
    """
    withdrawal = robot.submit_withdrawal_order(
        tonce,
        coin_type,
        coin_address,
        transfer_method,
        actual_amount
    )
    return withdrawal


@app.get("/generate_deposit_address")
async def generate_deposit_address(coin_type: str):
    """

    :param tonce:intiger timestamp  that represents the number
    of milliseconds from Unix to the current time
    :param coin_type:USDT-ADA-DOT-BNV
    """
    deposit = robot.generate_deposit_address(
        coin_type,
        print(coin_type)

    )
    print(deposit)
    return json.dumps(deposit)