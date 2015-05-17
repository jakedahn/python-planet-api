Planet API Client: The unofficial python client for the public planet labs api
==============================================================================

[![](https://travis-ci.org/jakedahn/python-planet-api.svg)](https://travis-ci.org/jakedahn/python-planet-api)


This is presently a work in progress, please do not use it unless you know what you're doing.

## How to use it

The python stuff below is meant to be an illustration of what the client interface will look like. It does not presently represent what the client is capable of doing:

```python

from planet_api.clients import ApiV0Client

client = ApiV0Client(username='foo', password='bar')  # this can also use api_key, or token
client.authenticate() # this will take the provided credentials, and use them to acquire an access token

# Scenes Resource
client.scenes.get('20150306_022415_0908')
client.scenes.list(count=100, cloud_cover_lte=0)  # 100 cloud-free scenes
# |
# --> [<Scene 20150306_022415_0908>, <Scene 20150306_022415_0131>, ...]

print Scene.camera_bit_depth  # 12
print Scene.cloud_cover  # 0
print Scene.analytic_download_url  # downloads https://api.planet.com/v0/scenes/ortho/20150306_022415_0908/full?product=analytic
# not sure yet what methods will be useful for the Scene object

# Workspaces Resource

workspaces = client.workspaces.list()
# |
# --> [<Workspace rad>, <Workspace murica>, ...]
rad_workspace = workspaces[0]
rad_workspace.name = 'superrad'
rad_workspace.save() # this will call the HTTP API and save with the updated attributes

murica_workspace = workspaces[1]
new_thing = murica_workspace.clone('newthing')
# |
# --> <Workspace newthing>

# Mosaics Resource

mosaic = client.mosaics.get('mosaic_name')
quads = mosaic.quads()
# |
# --> [<Quad L15-1593E-1301N>, <Quad L15-1378E-1310N>, ...]

quads[0].scenes()
# |
# --> [<Scene 20150306_022415_0908>, <Scene 20150306_022415_0131>, ...]



```

## Project Principles

* Community: If a newbie has a bad time, it's a bug.
* Software: Make it work, then make it right, then make it fast.
* Technology: If it doesn't do a thing today, we can make it do it tomorrow.

## License
The contents in this repository are licensed under [Apache 2](https://tldrlegal.com/license/apache-license-2.0-\(apache-2.0\)) License.