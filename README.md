<hr>

# Proxy Grabber

<a href="https://github.com/Skylier07/proxy-grabber?tab=readme-ov-file"><img alt="GitHub last commit (branch)" src="https://img.shields.io/github/last-commit/skylier07/proxy-grabber/main"></a> <a href="https://github.com/Skylier07/proxy-grabber/blob/main/LICENSE.md"><img alt="GitHub License" src="https://img.shields.io/github/license/skylier07/proxy-grabber"></a>

</p>

Proxy Grabber is a simple Python script utilizing web scraping on Free Proxy List to return a free proxy IP

## Installation

```bash
git clone git@github.com:Skylier07/proxy-grabber.git
```

## Requirements & Dependencies

Python 3.6 or above

Install requests

```bash
pip install requests
```

BeautifulSoup

```bash
pip install beautifulsoup4
```

Lxml phraser

```bash
pip install lxml
```

## Usage

```python
def get_proxy(country: str=None, attempts:int=10):
    """
    Get Proxy located in the same continent
    of your country

    Will return Proxy IPs from random
    avaliable locations if there's
    no avaliable server is avaliable
    in the continent, or no 'country'
    argument is given
    """
    return ip
```

## Disclaimer

Do not use these free proxies in production.

Free Proxies are scraped from [Free Proxy List](https://free-proxy-list.net/)

Proxies grabbed might expose users to security risks, use at your own risks

## License

[MIT](https://choosealicense.com/licenses/mit/)
