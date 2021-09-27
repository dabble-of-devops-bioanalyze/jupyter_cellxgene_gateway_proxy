import setuptools
import versioneer

setuptools.setup(
    name="jupyter_cellxgene_gateway_proxy",
    url="https://github.com/jupyterhub/jupyter-server-proxy/tree/master/contrib/jupyter_cellxgene_gateway_proxy",
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    author="Jillian Rowe",
    description="jillian@dabbleofdevops.com",
    packages=setuptools.find_packages(),
    keywords=["Jupyter"],
    classifiers=["Framework :: Jupyter"],
    install_requires=[
        "jupyter-server-proxy",
        "cellxgene>=0.18.0",
        "cellxgene-gateway>=0.3.7",
    ],
    entry_points={
        "jupyter_serverproxy_servers": [
            "cellxgene_gateway = jupyter_cellxgene_gateway_proxy:setup_jupyter_cellxgene_gateway_proxy",
            "cellxgene = jupyter_cellxgene_gateway_proxy:setup_jupyter_cellxgene_proxy",
        ]
    },
    package_data={"jupyter_cellxgene_gateway_proxy": ["icons/*"],},
)
