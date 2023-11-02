import requests
from twilio.rest import Client

STOCK = "TSLA"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
STOCK_API_KEY = "P378JIDERII97QRY"

NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_API_KEY = "3c2191879abf4a1ebc7d82c4ff98db27"
COMPANY_NAME = "Tesla Inc"

TWILIO_SID = "AC7f7ede5024d11fe87a5cb51efd48a838"
TWILIO_AUTH_TOKEN = "a6909300e3f809c43ef0a2e84cfd8439"

stock_parameter = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": STOCK_API_KEY
}
response = requests.get(STOCK_ENDPOINT, params=stock_parameter)
data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]

day_before_yesterday_data = data_list[1]
day_before_yesterday_price = day_before_yesterday_data["4. close"]

difference = float(yesterday_closing_price) - float(day_before_yesterday_price)
up_down = None
if difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"
diff_percent = round((difference / float(yesterday_closing_price)) * 100)

news_parameter = {
    "qInTitle": COMPANY_NAME,
    "apiKey": NEWS_API_KEY
}
if diff_percent > 3:
    news_response = requests.get(NEWS_ENDPOINT, params=news_parameter)
    articles = news_response.json()["articles"]
    three_articles = articles[:3]
    formated_articles = [f"{STOCK}, {up_down}{diff_percent}%\n" \
                         f"Headline: {article['title']}. \nBrief: {article['content']}" for article in three_articles]
    print(formated_articles)
    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
    for article in formated_articles:
        message = client.messages.create(
            body=article,
            from_="+12182766209",
            to="+12763127011"
        )
