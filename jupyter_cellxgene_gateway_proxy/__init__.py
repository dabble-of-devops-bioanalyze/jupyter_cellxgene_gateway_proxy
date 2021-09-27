"""
Return config on servers to start for jupyter_cellxgene_gateway_proxy

See https://jupyter-server-proxy.readthedocs.io/en/latest/server-process.html
for more information.
"""
import os


def setup_jupyter_cellxgene_gateway_proxy():
    def _get_env(port):
        my_env = os.environ.copy()

        my_env["PROXY_FIX_FOR"] = 1
        my_env["PROXY_FIX_PROTO"] = 1
        my_env["PROXY_FIX_HOST"] = 1
        my_env["PROXY_FIX_PORT"] = 1
        my_env["PROXY_FIX_PREFIX"] = 1
        my_env["GATEWAY_IP"] = "0.0.0.0"
        my_env["GATEWAY_PORT"] = port
        CELLXGENE_DATA = os.environ.get("CELLXGENE_DATA", False)
        if not CELLXGENE_DATA:
            my_env["CELLXGENE_DATA"] = "{home}/cellxgene_data".format(
                home=os.environ.get("HOME")
            )
        return my_env

    def _get_cmd(port):
        cmd = ["cellxgene-gateway"]

        return cmd

    return {
        "command": _get_cmd,
        "environment": _get_env,
        "launcher_entry": {
            "title": "jupyter_cellxgene_gateway_proxy",
            "icon_path": os.path.join(
                os.path.dirname(os.path.abspath(__file__)),
                "icons",
                "cellxgene-logo.svg",
            ),
        },
    }


def setup_jupyter_cellxgene_proxy():
    def _get_env(port):
        my_env = os.environ.copy()

        return my_env

    def _get_cmd(port):
        CELLXGENE_DATA = os.environ.get("CELLXGENE_DATASET", False)
        if not CELLXGENE_DATA:
            os.environ["CELLXGENE_DATA"] = "https://cellxgene-example-data.czi.technology/pbmc3k.h5ad "

        # cellxgene launch https://cellxgene-example-data.czi.technology/pbmc3k.h5ad --host 0.0.0.0 -d --port 5001
        cmd = ["cellxgene",
            "launch",
            "{dataset}".format(dataset=os.environ.get('CELLXGENE_DATA')),
            "--host",
            "0.0.0.0",
            "--port",
            "{port}"
        ]

        return cmd

    return {
        "command": _get_cmd,
        "environment": _get_env,
        "launcher_entry": {
            "title": "jupyter_cellxgene_proxy",
            "icon_path": os.path.join(
                os.path.dirname(os.path.abspath(__file__)),
                "icons",
                "cellxgene-logo.svg",
            ),
        },
    }

from . import _version
__version__ = _version.get_versions()['version']
