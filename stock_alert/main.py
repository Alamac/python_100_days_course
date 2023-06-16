import os
import requests
from twilio.rest import Client

STOCK = "MSFT"
COMPANY_NAME = "Microsoft"

STOCK_API_KEY = os.environ.get("STOCK_API_KEY")
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_API_KEY = os.environ.get("NEWS_API_KEY")
NEWS_ENDPOINT = "https://newsapi.org/v2/top-headlines"
MY_NUMBER = os.environ.get("MY_NUMBER")
TWILIO_SID = os.environ.get("TWILIO_SID")
TWILIO_TOKEN = os.environ.get("TWILIO_TOKEN")
TWILIO_NUMBER = os.environ.get("TWILIO_NUMBER")


class StockApp:
    def __init__(self) -> None:
        self.stock_data = self.get_stock_data()
        self.stock_change = self.get_stock_change()
        self.news = self.get_news()

    def get_stock_data(self) -> dict:
        params = {
            "function": "TIME_SERIES_DAILY_ADJUSTED",
            "symbol": STOCK,
            "apikey": STOCK_API_KEY
        }
        response = requests.get(STOCK_ENDPOINT, params=params)
        response.raise_for_status()
        return response.json()

    def get_stock_change(self) -> float:
        daily_list = list(self.stock_data["Time Series (Daily)"].items())
        self.yesterday_price = float(daily_list[0][1]["4. close"])
        self.day_before_yesterday_price = float(daily_list[1][1]["4. close"])
        return self.yesterday_price / self.day_before_yesterday_price * 100

    def get_stock_message(self) -> str:
        flag = "💹"
        if self.stock_change < 100:
            flag = "🔻"
        diff = round(abs(100 - self.stock_change), 2)
        return f"MSFT: {flag}{diff}% ({round(self.yesterday_price, 2)}$)"

    def get_news(self) -> list[str]:
        params = {
            "q": COMPANY_NAME,
            "apiKey": NEWS_API_KEY,
            "country": "us"
        }
        news_req = requests.get(NEWS_ENDPOINT, params=params)
        news_req.raise_for_status()
        news_data = news_req.json()
        top_headlines = [i["title"] for i in news_data["articles"]]
        top_headlines = top_headlines[:2]
        return top_headlines

    def get_final_message(self) -> str:
        news_string = '\n'.join(self.news)
        return f"\n{self.get_stock_message()}\n{news_string}"

    def send_sms(self) -> None:
        client = Client(TWILIO_SID, TWILIO_TOKEN)
        text = self.get_final_message()
        message = client.messages \
                        .create(
                            body=text,
                            from_=TWILIO_NUMBER,
                            to=MY_NUMBER
                        )

        print(message.sid)


s = StockApp()
s.send_sms()
