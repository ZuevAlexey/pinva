from models.assetinfo import AssetInfo


def get_asset_info(ticker):
    return AssetInfo(f'new{ticker}', ticker, 123)