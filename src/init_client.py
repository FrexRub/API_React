from src.config import setting
from src.http_client import CMCHTTPClient

cmc_client = CMCHTTPClient(
    base_url="https://pro-api.coinmarketcap.com",
    api_key=setting.CMC_API_KEY,
)
