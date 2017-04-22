from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation
import urllib.request
import json

# basic map setup
globe = Basemap(projection='robin', resolution = 'c', lat_0=0, lon_0=0)
globe.drawcoastlines()
globe.drawcountries()
globe.fillcontinents(color="grey")
globe.drawmapboundary()
globe.drawmeridians(np.arange(0, 360, 30))
globe.drawparallels(np.arange(-90, 90, 30))

x,y = globe(0, 0)
point = globe.plot(x, y, 'ro', markersize=7)[0]

def init():
    point.set_data([], [])
    return point,

# animation function.  This is called sequentially
def animate(i):
    lons, lats =  iss_position()
    x, y = globe(lons, lats)
    point.set_data(x, y)
    return point,

# http://api.open-notify.org/iss-now.json
def iss_position():
    resp = urllib.request.urlopen("http://api.open-notify.org/iss-now.json").read()
    jsn = json.loads(resp.decode('utf-8'))
    pos = jsn["iss_position"]
    lon = pos["longitude"]
    lat = pos["latitude"]
    return (lon, lat)

# call the animator. blit=True means only re-draw the parts that have changed.
anim = animation.FuncAnimation(plt.gcf(), animate, init_func=init,
                               interval=3000, blit=True)
plt.show()
