import unittest

from main import head_reciever, URL, TMPDIR


class TestHeadReciever(unittest.IsolatedAsyncioTestCase):

    async def test_head_reciever(self):
        await head_reciever('testfile', URL)
        with open(f'{TMPDIR}/testfile', encoding='UTF-8') as testfile:
            cont = testfile.read()
        self.assertRegex(cont, '<head>\w|\W<\/head>')

if __name__ == '__main__':
    unittest.main()
