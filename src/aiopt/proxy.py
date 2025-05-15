import asyncio
from aiohttp import ClientSession


class ProxyList:
    """
    Class that represents proxies info.
    """

    def __init__(self, proxies: list):
        self.__proxies = proxies

    @property
    def proxies(self) -> list:
        """Returns a list of proxies"""
        res = [prx[1] for prx in self.__proxies]
        return res

    @property
    def valid_proxies(self) -> list:
        """Returns a list of valid proxies"""
        res = [prx[1] for prx in self.__proxies if prx[0]]
        return res

    @property
    def invalid_proxies(self) -> list:
        """Returns a list of invalid proxies"""
        res = [prx[1] for prx in self.__proxies if not prx[0]]
        return res



async def __is_valid_proxy(proxy:str, url:str, timeout:int, session: ClientSession) -> tuple[bool, str]:
    try:
        async with session.get(url=url,
                               proxy=proxy,
                               timeout=timeout) as response:
            return True, proxy

    except Exception:
        return False, proxy


async def check_proxies(proxy_list:list,
                        url:str = "https://httpbin.org",
                        timeout: int=10) -> ProxyList:
    """
    Returns info about proxies.

    Args:
        proxy_list(list): Proxy to check (must start with http:// | https://)
        url(str): Url to check access with proxy (default = "https://httpbin.org")
        timeout(int): Max testing time for each proxy (default = 10)

    Returns:
        ProxyList object that contains info about proxies.
    """

    async with ClientSession() as session:
        tasks = [__is_valid_proxy(proxy=proxy,
                                  url=url,
                                  timeout=timeout,
                                  session=session) for proxy in proxy_list]

        proxies = await asyncio.gather(*tasks)

        return ProxyList(proxies)

