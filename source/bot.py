import telebot
import json
from datetime import datetime
import requests
import bot_token

API_TOKEN = bot_token.TOKEN
bot = telebot.TeleBot(API_TOKEN)
# Start

@bot.message_handler(commands=['start'])
def send_welcome(message):
	cid = message.chat.id
	msg = bot.reply_to(message, 'Olá, seja bem-vindo ao Coin Bot! Você pode ver o preço de cada moeda na cotação atual dela.\nDigite /ajuda para abrir a lista de comandos!')
	bot.send_message(cid,'Bot criado por @WillyDev.\nDeixe o seu feedback e veja as atualizaçoes no nosso GitHub: ')

# Ajuda

@bot.message_handler(commands=['ajuda'])
def send_help(message):
	msg_help = bot.reply_to(message, '🤖💱Lista de comandos🤖💱:\n\n*💵💶Moedas*:\n\n/usdbrl - *Preço do Dólar em Real Brasileiro.*\n\n/cadbrl - *Preço do Dolar Canadense em Real Brasileiro.*\n\n/yenbrl - *Preço do Yene Japones em Real Brasileiro.*\n\n/audbrl - *Preço do Dolar Australiano em Real Brasileiro.*\n\n💰*Criptomoedas*:\n\n/eth - *Preço do Etherum em Real Brasileiro.*\n\n/btc - *Preço do Bitcoin em Real Brasileiro.*\n\n📈Taxas:\n\n/cdi - *CDI (Certificado de Depósito Interbancário)*\n\n/selic - *Selic (Sistema Especial de Liquidação de Custódia)*', parse_mode= 'Markdown')
	# 🤖💱Lista de comandos🤖💱:\n\n*💵💶Moedas*:\n\n/usdbrl - *Preço do Dólar em Real Brasileiro.*\n\n/cadbrl - *Preço do Dolar Canadense em Real Brasileiro.*\n\n/yenbrl - *Preço do Yene Japones em Real Brasileiro.*\n\n*/audbrl - Preço do Dolar Australiano em Real Brasileiro.*\n\n💰*Criptomoedas*:\n\n/eth - *Preço do Etherum em Real Brasileiro.*\n\n/btc - *Preço do Bitcoin em Real Brasileiro.*\n\n📈Taxas:\n\n/cdi - *CDI - Certificado de Depósito Interbancário*\n\n/selic - *Selic - Sistema Especial de Liquidação de Custódia*


# Criador

@bot.message_handler(commands=['criador'])
def send_creator(message):
	msg_creator = bot.reply_to(message, 'Oi! Meu nome é Deivid Willy e sou estudante de programação em foco Full-Stack!\nCriei este bot apenas para aprender e continuar à praticar na linguagem de programação Python.\n O bot terá atualizações mais para frente e você pode me ajudar colaborando no *GitHub*, ou apenas dando o seu feedback e me seguindo lá!\nCaso queira falar comigo: @WIllyDev, e entre no canal de atualizações!\nGitHub: https://github.com/DeividWilly/', parse_mode= 'Markdown')

# Dólar - Real

@bot.message_handler(commands=['usdbrl'])
def send_usdbrl(message):
	USDBRL_DICT = requests.get(f"https://api.hgbrasil.com/finance?key={bot_token.FINANCE}").json()
	usdbrl_buy = USDBRL_DICT['results']['currencies']['USD']['buy']
	usdbrl_var = USDBRL_DICT['results']['currencies']['USD']['variation']
	bot.reply_to(message, f'💵*Dólar Americano/Real Brasileiro*\n\n📊*Valor*: {usdbrl_buy}\n\n📈*Variação em percentual referente à última hora útil anterior*: {usdbrl_var}%\n*Fonte*: _HG Brasil Finance_',parse_mode='Markdown')

# Dólar Canadense - Real

@bot.message_handler(commands=['cadbrl'])
def send_cadbrl(message):
	CADBRL_DICT = requests.get(f"https://api.hgbrasil.com/finance?key={bot_token.FINANCE}").json()
	cadbrl_buy = CADBRL_DICT['results']['currencies']['CAD']['buy']
	cadbrl_var = CADBRL_DICT['results']['currencies']['CAD']['variation']
	bot.reply_to(message, f'💵*Dólar Canadense/Real Brasileiro*\n\n📊*Valor*: {cadbrl_buy}\n\n📈*Variação em percentual referente à última hora útil anterior*: {cadbrl_var}%\n*Fonte*: _HG Brasil Finance_', parse_mode='Markdown')

# Dólar Australiano - Real

@bot.message_handler(commands=['audbrl'])
def send_audbrl(message):
	AUDBRL_DICT = requests.get(f"https://api.hgbrasil.com/finance?key={bot_token.FINANCE}").json()
	audbrl_buy = AUDBRL_DICT['results']['currencies']['CAD']['buy']
	audbrl_var = AUDBRL_DICT['results']['currencies']['CAD']['variation']
	bot.reply_to(message, f'💵*Dólar Australiano/Real Brasileiro*\n\n📊*Valor*: {audbrl_buy}\n\n📈*Variação em percentual referente à última hora útil anterior*: {audbrl_var}%\n*Fonte*: _HG Brasil FInance_', parse_mode='Markdown')

# Euro - Real

@bot.message_handler(commands=['eurbrl'])
def send_eurbrl(message):
	EURBRL_DICT = requests.get(f"https://api.hgbrasil.com/finance?key={bot_token.FINANCE}").json()
	eurbrl_buy = EURBRL_DICT['results']['currencies']['EUR']['buy']
	eurbrl_var = EURBRL_DICT['results']['currencies']['EUR']['variation']
	bot.reply_to(message, f'💶*Euro/Real Brasileiro*\n\n📊*Valor*: {eurbrl_buy}\n\n*📈Variação em percentual referente à última hora útil anterior*: {eurbrl_var}%\n*Fonte*: _HG Brasil Finance_',parse_mode='Markdown')

# Libra - Real

@bot.message_handler(commands=['gbpbrl'])
def send_gbpbrl(message):
	GBPBRL_DICT = requests.get(f"https://api.hgbrasil.com/finance?key={bot_token.FINANCE}").json()
	gbpbrl_buy = GBPBRL_DICT['results']['currencies']['GBP']['buy']
	gbpbrl_var = GBPBRL_DICT['results']['currencies']['GBP']['variation']
	bot.reply_to(message, f'💶*Libra/Real Brasileiro*\n\n📊*Valor*: {gbpbrl_buy}\n\n📈*Variação em percentual referente à última hora útil anterior*: {gbpbrl_var}%\n*Fonte*: _HG Brasil Finance_', parse_mode='Markdown')

# Peso Argentino - Real

# @bot.message_handler(commands=['arsbrl'])
# def send_arsbrl(message):
# 	ARSBRL_DICT = requests.get(f"https://api.hgbrasil.com/finance?key={bot_token.FINANCE}").json()
# 	arsbrl_buy = ARSBRL_DICT['results']['currencies']['ARS']['buy']
# 	arsbrl_var = ARSBRL_DICT['results']['currencies']['ARS']['variation']
# 	bot.reply_to(message, f'💵*Peso Argentino/Real Brasileiro*\n\n📊*Valor*: {arsbrl_buy}\n\n📈*Variação em percentual referente à última hora útil: {arsbrl_var}%\n*Fonte*: _HG Brasil Finance_', parse_mode='Markdown')

# Yene Japônes - Real

# @bot.message_handler(commands=['yenbrl'])
# def send_yenbrl(message):
# 	JPYBRL_DICT = requests.get(f"https://api.hgbrasil.com/finance?key={bot_token.FINANCE}").json()
# 	jpybrl_buy = JPYBRL_DICT['results']['currencies']['JPY']['buy']
# 	jpybrl_var = JPYBRL_DICT['results']['currencies']['JPY']['variation']
# 	bot.reply_to(message, f'💵*Yene Japônes/Real Brasileiro*\n\n📊*Valor*: {jpybrl_buy}\n\n📈*Variação em percentual referente à última hora útil: {jpybrl_var}\n*Fonte*: _HG Brasil Finance_', parse_mode='Markdown')

# Bitcoin
@bot.message_handler(commands=['btc'])
def send_btc(message):
	price_btc = requests.get("https://www.mercadobitcoin.net/api/BTC/ticker/").json()
	btc_buy = float(price_btc['ticker']['buy'])
	btc_high = float(price_btc['ticker']['high'])
	btc_low = float(price_btc['ticker']['low'])
	btc_date = datetime.utcfromtimestamp(int(price_btc['ticker']['date'])).strftime('%H:%M:%S %d-%m-%Y')
	bot.reply_to(message, f'💰*Bitcoin/Real Brasileiro*\n\n📊*Valor*: {btc_buy:.2f}\n\n📈*Valor máximo*: {btc_high:.2f}\n\n🔙💲*Valor mínimo*: {btc_low:.2f}\n\n⏱*Última atualização*: {btc_date}\n\n🚨*Preços podem variar de acordo por cada corretora!*🚨\n*Fonte*: _MercadoBitcoin_',parse_mode='Markdown')

# Ethereum
@bot.message_handler(commands=['eth'])
def send_eth(message):
	price_eth = requests.get("https://www.mercadobitcoin.net/api/ETH/ticker/").json()
	eth_buy = float(price_eth['ticker']['buy'])
	eth_high = float(price_eth['ticker']['high'])
	eth_low = float(price_eth['ticker']['low'])
	eth_date = datetime.utcfromtimestamp(int(price_eth['ticker']['date'])).strftime('%H:%M:%S %d/%m/%Y0')
	bot.reply_to(message, f'💰*Ethereum/Real Brasileiro*\n\n📊*Valor*: {eth_buy:.2f}\n\n📈*Valor máximo*: {eth_high:.2f}\n\n🔙💲*Valor mínimo*: {eth_low:.2f}\n\n⏱*Última atualização*: {eth_date}\n\n🚨*Preços podem variar de acordo por cada corretora!*🚨\n*Fonte*: _MercadoBitcoin_',parse_mode='Markdown')

# SELIC

@bot.message_handler(commands=['selic'])
def send_selic(message):
	chat_id = message.chat.id
	SELIC_DICT = requests.get(f"https://api.hgbrasil.com/finance/taxes?key={bot_token.FINANCE}").json()
	selic = SELIC_DICT['results'][0]['selic']
	selic_daily = SELIC_DICT['results'][0]['selic_daily']
	daily_factor = SELIC_DICT['results'][0]['daily_factor']
	selic_date = SELIC_DICT['results'][0]['date']

	bot.send_message(chat_id, f'📈*Selic - Sistema Especial de Liquidação de Custódia*\n\n📊*Taxa Selic:* {selic}%\n\n📊*Taxa Selic diária*: {selic_daily}%\n\n📊*Fator diário*: {daily_factor}%\n\n⏱*Data*: _{selic_date}_', parse_mode='Markdown')


# CDI

@bot.message_handler(commands=['cdi'])
def send_cdi(message):
	chat_id = message.chat.id
	CDI_DICT = requests.get(f"https://api.hgbrasil.com/finance/taxes?key={bot_token.FINANCE}").json()
	cdi = CDI_DICT['results'][0]['cdi']
	cdi_daily = CDI_DICT['results'][0]['cdi_daily']
	daily_factor = CDI_DICT['results'][0]['daily_factor']
	cdi_date = CDI_DICT['results'][0]['date']

	bot.send_message(chat_id, f'📈*CDI - Certificado de Depósito Interbancário*\n\n📊*Taxa CDI*: {cdi}%\n\n📊*Taxa CDI diária*: {cdi_daily}%\n\n📊*Fator diário*: {daily_factor}%\n\n⏱*Data*: _{cdi_date}_', parse_mode='Markdown')

bot.polling()
