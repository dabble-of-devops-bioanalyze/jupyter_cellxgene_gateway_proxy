import unittest
from unittest.mock import MagicMock, patch
import os
import jupyter_cellxgene_gateway_proxy

class TestImports(unittest.TestCase):
    def test_imports(self):
        my_env = jupyter_cellxgene_gateway_proxy.setup_jupyter_cellxgene_gateway_proxy()['environment']('5001')
        assert my_env['PROXY_FIX_HOST'] == 1

if __name__ == '__main__':
    unittest.main()