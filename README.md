# zain api sample

how to use zaim api in python

## Requirements

## Usage

### setup environment
~~~bash
git clone https://github.com/Tatsu015/zaim_api_sample.git
cd zaim_api_sample

python3 -m venv .venv
source .venv/bin/activate
poetry install
~~~

### get access token

~~~bash
python get_token.py
~~~

input `consumer key`, `consumer secret` and access to display URL.  

input datas in web page.  

in `認証が完了` page, probably not redirect eternally. so open `developer tool` and search `oauth_verifier` text in elements lile

> https://www.zaim.net/?oauth_token=...oauth_verifier=xxxxxxxxxxxxxxxxxxxxxxxxxxx

xxxxxxxxxxxxxxxxxxxxxxxxxxx is verifier.

in python execute terminal, input xxxxxxxxxxxxxxxxxxxxxxxxxxx.

after that, display `access token` and `acces token secret`.