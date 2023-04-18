import asyncio
import hashlib
import logging
import os
from tempfile import gettempdir

import aiohttp
from bs4 import BeautifulSoup

logging.basicConfig(level='INFO')

URL = 'https://gitea.radium.group/radium/project-configuration'
TASKS_AMOUNT: int = 3
HASHFILE: str = 'hash'
TMPDIR: str = '{tmpdir}/heads'.format(tmpdir=gettempdir())


async def head_reciever(namefile: str, url: str):
    """Get HEAD content and write it to temporary file.

    Parameters
    ----------
    namefile : str
        Name that will be assigned to file.
    url : str
        Getting URL.
    """
    if not os.path.exists(TMPDIR):
        os.mkdir(TMPDIR)
    temp_file = '{tdir}/{nmfile}'.format(tdir=TMPDIR, nmfile=namefile)
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            cont = BeautifulSoup(await response.read(), 'html.parser')
            with open(temp_file, 'w') as tmp_file:
                tmp_file.write(str(cont.find_all('head')))


async def main():
    """Create task-list for async loop."""
    tasks = []
    for task in range(TASKS_AMOUNT):
        tasks.append(asyncio.create_task(head_reciever(task, URL)))
    await asyncio.gather(*tasks)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    with open(HASHFILE, 'w', encoding='UTF-8') as hashfile:
        for HEAD_file in os.listdir(TMPDIR):
            filename = '{tmpd}/{headf}'.format(tmpd=TMPDIR, headf=HEAD_file)
            with open(filename, 'rb') as headfile:
                hashstr = hashlib.sha256(headfile.read()).hexdigest()
                out = '{headf}: {hash}\n'.format(headf=HEAD_file, hash=hashstr)
                logging.info(out)
                hashfile.write(out)
