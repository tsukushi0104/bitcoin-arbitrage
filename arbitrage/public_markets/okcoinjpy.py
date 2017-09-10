from ._okcoin import OKCoin

class OKCoinJPY(OKCoin):
    def __init__(self):
        super().__init__("JPY", "btc_jpy")
