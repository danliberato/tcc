import unittest

from uuid import uuid4
from src.repository.bucket_repository import save_image


class Bucket(unittest.TestCase):
    def test_upload(self):
        r = save_image('/home/dliberato/Imagens/dummy_image.png', str(uuid4()))
        self.assertEqual(True, r)  # add assertion here


if __name__ == '__main__':
    unittest.main()
