import requests
from twilio.rest import Client


STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
ALPHAVANTAGE_API_KEY = "P378JIDERII97QRY"
NEWS_API_KEY = "3c2191879abf4a1ebc7d82c4ff98db27"
TWILIO_ACCOUNT_SID = "AC7f7ede5024d11fe87a5cb51efd48a838"
TWILIO_AUTH_TOKEN = "a6909300e3f809c43ef0a2e84cfd8439"


def send_text(flag: bool):
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    for item in news[1:]:
        emoji = "🔺"
        if not flag:
            emoji = "🔻"
        message = client.messages.create(
            body=f"TSLA: {emoji}{percentage_increase}%\n"
                 f"Headline:{item['headline']}\n"
                 f"Brief:{item['brief']}",
            from_="+12182766209",
            to="+12763127011"
        )


# STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
alphavantage_parameter = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": ALPHAVANTAGE_API_KEY
}
alphavantage_url = 'https://www.alphavantage.co/query'
alphavantage_response = requests.get(alphavantage_url, params=alphavantage_parameter)
data = alphavantage_response.json()

list_data = list(data["Time Series (Daily)"].items())
yesterday_price = float(list_data[0][1]["4. close"])
day_before_price = float(list_data[1][1]["4. close"])
percentage_increase = int(((yesterday_price - day_before_price)/yesterday_price)*100)

# STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
news_parameter = {
    # "q": COMPANY_NAME,
    "qInTitle": COMPANY_NAME,
    # "sortBy": "popularity",
    "apiKey": NEWS_API_KEY
}
news_url = "https://newsapi.org/v2/everything"
news_response = requests.get(news_url, news_parameter)
news_response.raise_for_status()
news_data = news_response.json()["articles"][:3]
headlines = [item["title"] for item in news_data]
briefs = [item["content"] for item in news_data]
news = [{}]
for i in range(len(headlines)):
    news.append({"headline": headlines[i], "brief": briefs[i]})

# STEP 3: Use https://www.twilio.com
# Send a separate message with the percentage change and each article's title and description to your phone number.
# Percentage Increase
if percentage_increase >= 1:
    print(news)
    send_text(flag=True)
# Percentage Decrease
else:
    percentage_increase *= -1
    print(news)
    send_text(flag=False)


