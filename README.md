# Native Spawner

1. Clone and install
```
git clone https://github.com/KamalGalrani/jupyterhub-nativespawner
cd jupyterhub-nativespawner
pip install -e .
```

2. Configure Jupyterhub
```
...
c.JupyterHub.spawner_class = 'nativespawner.NativeSpawner'
# user notebooks are stored in separate directories within this directory
c.Spawner.storage = '/opt/jupyterhub/users'
...
```
