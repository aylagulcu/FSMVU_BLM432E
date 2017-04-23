
# coding: utf-8

# In[1]:

import cartopy.crs as ccrs
import numpy as np
import pandas as pd
import cartopy as cartopy
import cartopy.io.shapereader as shpreader
import matplotlib.pyplot as plt
import matplotlib as mpl
import pysal as pysal
from matplotlib.colors import Normalize


# In[2]:

df= pd.read_csv('C:/Users/SAMSUNG/Desktop/Deaths.csv')
df


# In[27]:

ax = plt.axes(projection=ccrs.PlateCarree())
fig= plt.gcf()
fig.set_size_inches(17,10)

ax.stock_img()

#ax.add_feature(cartopy.feature.LAND)
ax.add_feature(cartopy.feature.OCEAN)
#ax.add_feature(cartopy.feature.COASTLINE)
#ax.add_feature(cartopy.feature.BORDERS, linestyle='-', alpha=1)
#ax.add_feature(cartopy.feature.LAKES, alpha=0.95)
#ax.add_feature(cartopy.feature.RIVERS)
ax.set_extent([-28, 50,30, 63])
ax.set_aspect('auto', adjustable=None)

#Natural Earth Datasını okudum
shpfilename = shpreader.natural_earth(resolution='50m',category='cultural',name='admin_0_countries')
reader = shpreader.Reader(shpfilename)
#Bütün ülkeleri countries adındaki bir generator objesine aktardım
countries = reader.records()

cmap = plt.get_cmap('Reds')   
norm = Normalize()

color_codes=cmap(norm(df['% of all deaths'].fillna(0).values))

for country in countries:
    ax.add_geometries(country.geometry, ccrs.PlateCarree(),facecolor='gray',label=country.attributes['adm0_a3'])

countries = reader.records()
    for country in countries:
        for i in range(len(df)):
            if(country.attributes['adm0_a3']==df.loc[i]['Country']):
                ax.add_geometries(country.geometry, 
                                  ccrs.PlateCarree(),
                                  facecolor=(color_codes[i][0], color_codes[i][1], color_codes[i][2]),
                                  label=country.attributes['adm0_a3'])
                break;
            
mapper = mpl.cm.ScalarMappable(norm=norm, cmap=cmap) 
mapper.set_array(df['% of all deaths'])

plt.colorbar(mapper, shrink=1)
fig.suptitle('Mental Diseases Based Deaths Percent in All Deaths in European Countries', fontsize=20)
        
plt.show()


# In[29]:

ax = plt.axes(projection=ccrs.PlateCarree())
fig= plt.gcf()
fig.set_size_inches(17,10)

ax.stock_img()

#ax.add_feature(cartopy.feature.LAND)
ax.add_feature(cartopy.feature.OCEAN)
#ax.add_feature(cartopy.feature.COASTLINE)
#ax.add_feature(cartopy.feature.BORDERS, linestyle='-', alpha=1)
#ax.add_feature(cartopy.feature.LAKES, alpha=0.95)
#ax.add_feature(cartopy.feature.RIVERS)
ax.set_extent([-28, 50,30, 63])
ax.set_aspect('auto', adjustable=None)

#Natural Earth Datasını okudum
shpfilename = shpreader.natural_earth(resolution='50m',category='cultural',name='admin_0_countries')
reader = shpreader.Reader(shpfilename)
countries = reader.records()

cmap = plt.get_cmap('Blues')  
norm = Normalize()

color_codes=cmap(norm(df['Population'].fillna(0).values))

for country in countries:
    ax.add_geometries(country.geometry, ccrs.PlateCarree(),facecolor='gray',label=country.attributes['adm0_a3'])

countries = reader.records()
for country in countries:
    for i in range(len(df)):
        if(country.attributes['adm0_a3']==df.loc[i]['Country']):
            ax.add_geometries(country.geometry, 
                              ccrs.PlateCarree(),
                              facecolor=(color_codes[i][0], color_codes[i][1], color_codes[i][2]),
                              label=country.attributes['adm0_a3'])
            break;
            
mapper = mpl.cm.ScalarMappable(norm=norm, cmap=cmap)
 
mapper.set_array(df['Population'])
plt.colorbar(mapper, shrink=1)
fig.suptitle('Population by Countries in Europe', fontsize=20)
        
plt.show()


# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:



