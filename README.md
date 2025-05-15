<h1 align="center">
    🌐 AIOproxytest 🌐
</h1>
<div align="center">
    <a href = "https://opensource.org/licenses/MIT">
    <img  src="https://img.shields.io/badge/License-MIT-yellow.svg">
    </a>
</div>

<div align="center">
    <img src=".github/aiopt.png" align="center">
</div>

<h3 align="center">
    aiopt is a simple asynchronous lib for testing proxy servers
</h3>

---
<h2>
   🖥 Installation 
</h2>

<div>
    To install aiopt you may use pip:
</div>

<br>

<img src=".github/install.png">

<h2>
   💡 Usage
</h2>
Example:

```Python
from aiopt import check_proxies
import asyncio


async def main():
    proxy_list = ['https://190.58.248.86:80',
                  'http://45.12.150.82:8080']

    result = await check_proxies(proxy_list)

    print(result.proxies)         # [https://190.58.248.86:80, http://45.12.150.82:8080]
    print(result.valid_proxies)   # [http://45.12.150.82:8080]
    print(result.invalid_proxies) # [https://190.58.248.86:80]


if __name__ == '__main__':
    asyncio.run(main())
```

<h2>
   🤝 Contribution 
</h2>

<div>
    Contributions are welcome!
    If you have ideas for improving this project, please post them in issues.
    (if I don't answer, you can email me)
</div>

---

<h3 align="center">
    If you have any troubles, please tell about it in issues
</h3>

