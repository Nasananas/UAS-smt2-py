#!/usr/bin/env python
# coding: utf-8

# In[1]:


#modul yang di perlukan untuk scraping data
import requests
import csv
import os

#kata kunci pengguna
key = input('Masukkan keyword: ') 
directory = 'uas-py' #nama file untuk nantinya digunakan menyimpan file csv
file_path = os.path.join(directory, '{}.csv'.format(key)) #csript untuk menghubungkan direktori dan kata kunci dengan ekstensi

#untuk memeriksa apakah direktori yang ditentukan ada
if not os.path.exists(directory):
    os.makedirs(directory)

#masukkan url untuk titik akhir API
url = 'https://api.bukalapak.com/multistrategy-products'
count = 0

#untuk melacak jumlah produk.
with open(file_path, 'w', newline='') as file:
    write = csv.writer(file)
    header = ['nama', 'harga', 'kategori'] #nama kolom
    write.writerow(header)

    for page in range(1, 2): # untuk mengulang rentang dari 1 hingga 2
        parameters = { #membuat parameter yang dimana terdapat keywords, limit, offset, facet, page, dan access token.
            'keywords': key,
            'limit': 50,
            'offset': (page - 1) * 50,
            'facet': 'True',
            'page': page,
            'access_token': 'eyJhbGciOiJSUzI1NiIsImtpZCI6ImFjY291bnRzLmp3dC5hY2Nlc3MtdG9rZW4iLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJodHRwczovL2FjY291bnRzLmJ1a2FsYXBhay5jb20vIiwic3ViIjoiNjEyMzM0MDk5IiwiYXVkIjpbImh0dHBzOi8vYWNjb3VudHMuYnVrYWxhcGFrLmNvbSIsImh0dHBzOi8vYXBpLmJ1a2FsYXBhay5jb20iLCJodHRwczovL2FwaS5zZXJ2ZXJtaXRyYS5jb20iXSwiZXhwIjoxNjg3MzQ4MjQ1LCJuYmYiOjE2ODczNDAwMjUsImlhdCI6MTY4NzM0MDAyNSwianRpIjoiS2JKQUF0ZTA2X19UUXhfTjlDV1luZyIsImNsaWVudF9pZCI6IjIzMWQ0YTg2OTA1ZjBmMjYyYzVlMDNmYyIsInNjb3BlIjoicHVibGljIHVzZXIgc3RvcmUifQ.jIc_D8GE6qYI8IFJhOJTbpBWytS3SDOl2TOZz9EUajmQIdeZg25Hab4saWatSn7r0OI5IMHEoGJOJ-4e5lZSQZAsRaATwmHToJkF1Hk5f66_UP-dR8gGUTQFBN2IOvcxmR9UEwipdePxm9oFCWCJF0JXOfn7RWehblQcBp4V9kuvJNB8N8eGA3eHJnlRiad6mCHbYguKBIu5zBH0Ki_eSn9hB8Nczrj4ilPcanJPoVgkfN9xcyPi7ybL3q0K7UIuWxpHc0xAd0qVxdaB1rl2ysURuezO_ixpZXHlmvj-iEyV4B2b5lElw7zIk7pt5VHVLbwb2aP1wp7RVVRA8z8u_Q'  # Replace with your actual access token
        }
        
        #Mengirim permintaan GET ke titik akhir API dengan parameter yang ditentukan dan mengambil respons JSON.
        response = requests.get(url, params=parameters).json()
        products = response['data']

        for p in products:
            nama = p['name']
            harga = p['price']
            kategori = p['category']
            count += 1
            print('No:', count, 'Nama:', nama, 'Harga:', harga, 'Kategori:', kategori)

            write.writerow([nama, harga, kategori]) #untuk memproses semua produk


# In[1]:


import pandas as pd
import matplotlib as plt


# In[3]:


df = pd.read_csv("C:/Users/user/uas-py/sabun cuci muka.csv") #link lokasi file sabun cuci muka.csv
df


# In[6]:


import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("C:/Users/user/uas-py/sabun cuci muka.csv")

plt.scatter(data['harga'], data['nama']) #untuk memunculkan grafik scatter gunakan nama atribut 'scatter' dan masukkan data yang ingin di ukur
#berlaku juga untuk diagram lainnya!
plt.title("Scatter Plot")
plt.xlabel('harga') #variabel x
plt.ylabel('nama') #variabel y

plt.show()


# In[7]:


import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("C:/Users/user/uas-py/sabun cuci muka.csv")

plt.plot(data['harga'])
plt.plot(data['nama'])

plt.title("Line Chart")

plt.xlabel('harga')
plt.ylabel('nama')


plt.show()


# In[8]:


import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv("C:/Users/user/uas-py/sabun cuci muka.csv")

plt.bar(data['harga'], data['nama'])

plt.title("Bar Chart")

plt.xlabel('harga')
plt.ylabel('nama')

plt.show()


# In[13]:


import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("C:/Users/user/uas-py/sabun cuci muka.csv")

plt.hist(data['harga'])

plt.title("Histogram")

plt.show()


# In[15]:


import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("C:/Users/user/uas-py/sabun cuci muka.csv")

sabun_muka = ['nama', 'harga', 'kategori']

data = [15, 10, 29]

plt.pie(data, labels=bank)

plt.title("sabun_muka")

plt.show()


# In[19]:


import matplotlib.pyplot as plt

data = pd.read_csv("C:/Users/user/uas-py/sabun cuci muka.csv")

# Generate the plot
plt.plot(data['harga'], data['nama'])

# Set plot title and labels
plt.title("Gambar Diagram")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

# Save the plot to a file
plt.savefig("plot.png")


# In[22]:


import matplotlib.pyplot as plt
data = pd.read_csv("C:/Users/user/uas-py/sabun cuci muka.csv")

sabun_muka = ['nama', 'harga', 'kategori']
data = [15, 10, 29]
plt.pie(data, labels=sabun_muka)

# Save the pie chart as an image file
plt.savefig('pie_chart.png')

