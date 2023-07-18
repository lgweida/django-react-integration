from  finvizfinance.news import News
from  finvizfinance.calendar import Calendar
from  finvizfinance.quote import Quote, finvizfinance
news= News().get_news()
calendar= Calendar().calendar()


print(news['news'])
print(news['blogs'])
print(calendar)
ticker = 'nvda'


print (Quote().get_current(ticker))
info = finvizfinance(ticker, 1).ticker_full_info()
print('fundament', 'ratings_outer', 'news', 'inside trader')
print(info['fundament'])
print(info['ratings_outer'])
print(info['news'])
print(info['inside trader'])
