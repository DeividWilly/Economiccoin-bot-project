<h1 align="center">
    :moneybag:<br>:robot:CoinBot
    <br><a href="https://t.me/economiccoin_bot" target="_blank"><img src="https://img.shields.io/badge/Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white"></a>
</h1>

Bot para o Telegram. Retorna e manda cotações das moedas desejadas como Dólar para Real Brasileiro.
Projeto _open-source_ que você pode colaborar aqui no GitHub ou apenas deixando o seu feedback.

<img align="center" src="imgs-readme/effigy_crying-3.jpg"/>

# Menu #

- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [Comandos](#comandos-v01)
- [Changelog](#changelog)

# Tecnologias utilizadas #
- [Python](https://www.python.org)
    - [pyTelegrambotAPI](https://pypi.org/project/pyTelegramBotAPI/)
    - [JSON](https://docs.python.org/3/library/json.html)
    - [requests](https://docs.python-requests.org/en/latest/)
    - APIS
        - [HG Brasil Finance](https://www.mercadobitcoin.com.br/api-doc/)
        - [Mercado Bitcoin](https://console.hgbrasil.com/documentation/finance)
- Heroku
- Visual Studio Code
- Linux Mint

# Comandos (v0.3) #

| Comando | Descrição | Comando | Descrição |
| ------- | --------- | ------- | --------- |
| `/start` | Inicia o bot | `/cadbrl` | Retorna valor da conversão do Dólar Canadense para Real Brasileiro |
| `/ajuda` | Mostra a lista de comandos disponíveis | `/audbrl` | Retorna valor da conversão do Dólar Australiano para Real Brasileiro |
| `/criador` | Lhe mostra um pouco sobre mim e o projeto | `/yenbrl` | Retorna valor da conversão do Yene Japonês para Real Brasileiro |
| `/usdbrl` | Retorna valor da conversão do Dólar para Real Brasileiro |
| `/eurbrl` | Retorna o valor da conversão do Euro para Real Brasileiro |
| `/btc` | Retorna o valor do Bitcoin |
| `/eth` | Retorna o valor do Ethereum |

# Changelog #
### 0.1 (BETA) ###
- - -
**02/04/2022** - Bot finalmente colocado ao ar.
**Hospedado no Heroku**

### 0.2 (BETA) ###
- - -
**04/04/2022**
**-Adicionado Novos comandos:**
- `/cadbrl`, `/audbrl`, `/yenbrl`

**-Comandos Removidos:**
- `brleur`, `brlusd`

**Nova API:**
- HG Brasil Finance
- Mercado Bitcoin
Sai API: _AwesomeAPI_

### 0.3 (BETA ) ##
- - -
**05/04/2022**

**Corrigido: Erros ortográficos**
`/ajuda` **atualizada**
Melhoria: **Valores retornados mostram suas fontes**