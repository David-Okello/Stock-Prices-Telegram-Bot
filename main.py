import os
import telebot
import yfinance as yf

#acess the api key from the replit secrets
API_KEY = os.environ['API_KEY']
github = os.environ['github']
instagram = os.environ['instagram']
twitter = os.environ['twitter']
replit = os.environ['replit']


#create the bot
bot = telebot.TeleBot(API_KEY)

@bot.message_handler(commands=['start'])
def start(message):

  t = {
    f"\
Hey there\n\
I was created by, David Okello back in 2021\n\
I don't do much yet but you can use the following commands on me:\n\
\n\
############################\n\
  Commands:\n\
\
    /greet : Sends you a greeting response\n\
    /getstocks : Get stock data on 4 hardcoded stocks(tsla, gme, amc and nok)\n\
############################\n\
\n\
############################\n\
  Custom commands:\n\
    price stockname : Get 5 minute periods and 1m intervals stock data on any stock\n\
############################\n\
\n\
Follow me on Social Media:\n\
\n\
############################\n\
  Github: {github}\n\
  Twitter:{twitter}\n\
  Instagram:{instagram}\n\
  Repl:{replit}\n\
#############################\n\
\n\
Stay tuned for more.\
  "}
  bot.send_message(message.chat.id, t)

#a function to reply to greet command sent to the bot 
@bot.message_handler(commands=['greet'])
def greet(message):
  bot.send_message(message.chat.id, "Hey there. How's it going?")

#Get stocks
@bot.message_handler(commands=['getstocks'])
def get_stocks(message):
  response = ""
  stocks = ['tsla','gme', 'amc', 'nok']
  stock_data = []

  #Pull data from yahoo for each stock listed
  for stock in stocks:
    data = yf.download(tickers=stock, period='2d', interval='1d')
    data = data.reset_index()
    response += f"-----{stock}-----\n"
    stock_data.append([stock])
    columns = ['stock']
    for index, row in data.iterrows():
      stock_position = len(stock_data) - 1
      price = round(row['Close'], 2)
      format_date = row['Date'].strftime('%m/%d')
      response += f"{format_date}: {price}\n"
      stock_data[stock_position].append(price)
      columns.append(format_date)
    print()

  response = f"{columns[0] : <10}{columns[1] : ^10}{columns[2] : >10}\n"
  for row in stock_data:
    response += f"{row[0] : <10}{row[1] : ^10}{row[2] : >10}\n"
  response += "\nStock Data"
  print(response)
  bot.send_message(message.chat.id, response)

#create a custom stock request
def stock_request(message):
  request = message.text.split()
  if len(request) < 2 or request[0].lower() not in "price":
    return False
  else:
    return True

'''Split the text entered by user into 2 eg: price tsla and get the 1 index assuming its a stock name
   pass it as a ticker with 5minute periods and 1m intervals...lastly format the data. '''
@bot.message_handler(func=stock_request)
def send_price(message):
  request = message.text.split()[1]
  data = yf.download(tickers=request, period='5m', interval='1m')
  if data.size > 0:
    data = data.reset_index()
    data["format_date"] = data['Datetime'].dt.strftime('%m/%d %I:%M %p')
    data.set_index('format_date', inplace=True)
    print(data.to_string())
    bot.send_message(message.chat.id, data['Close'].to_string(header=False))
  else:
    bot.send_message(message.chat.id, "No data!?")

#set bot to keep looking out for messages 
bot.polling()

