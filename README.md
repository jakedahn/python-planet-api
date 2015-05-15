Planet API Client: The unofficial python client for the public planet labs api
==============================================================================

[![](https://travis-ci.org/jakedahn/python-planet-api.svg)](https://travis-ci.org/jakedahn/python-planet-api)


This is presently a work in progress, please do not use it unless you know what you're doing.

## How to use it

Below is an example of what the interface might look like:

```python

from planet_api.client import ApiV0Client as client

client.scenes.get('20150306_022415_0908')
client.scenes.list(count=100, cloud_cover_lte=0)  # 100 cloud-free scenes
# |
# --> [<Scene 20150306_022415_0908>, <Scene 20150306_022415_0131>, ...]

print Scene.camera_bit_depth  # 12
print Scene.cloud_cover  # 0
print Scene.analytic_download_url  # downloads https://api.planet.com/v0/scenes/ortho/20150306_022415_0908/full?product=analytic
```

## Project Principles

* Community: If a newbie has a bad time, it's a bug.
* Software: Make it work, then make it right, then make it fast.
* Technology: If it doesn't do a thing today, we can make it do it tomorrow.

## License
The contents in this repository are licensed under [Apache 2](https://tldrlegal.com/license/apache-license-2.0-\(apache-2.0\)) License.