import pandas as pd

df_mars_clima = pd.read_csv("mars-weather.csv")

print(df_mars_clima['terrestrial_date'].unique())

# temperaturas maximas: media, mediana e moda
df_mars_temp_max = df_mars_clima['max_temp']

media_max_temp =  df_mars_temp_max.mean()
print(f'a media de temperaturas maximas foi de: {media_max_temp}')

mediana_max_tempo = df_mars_temp_max .median()
print(f'a mediana da temepeatura maxima foi de: {mediana_max_tempo}')

moda_max_temp = df_mars_temp_max.mode()
print(f'a moda da temepeatura maxima foi de: {moda_max_temp}')


# temperaturas minimas: media, mediana e moda
df_mars_temp_min = df_mars_clima['min_temp']

media_min_temp = df_mars_temp_min.mean()
print(f'a media de temperatira minima foi de: {media_min_temp}')

mediana_min_temp = df_mars_temp_min.median()
print(f'a mediana de temperatira minima foi de: {mediana_min_temp}')

moda_min_temp = df_mars_temp_min.mode()
print(f'a moda de temperatira minima foi de: {moda_min_temp}')

# medidas condicionadas
# criar um frame so com a condicao que eu preciso

dados_mes_6 = df_mars_clima[df_mars_clima['month'] == 'Month 6']

# temperatura minina mes 6: moda media e mediana 
df_min_temp_6 = dados_mes_6["min_temp"]
media_min_temp_m6 = df_min_temp_6.mean()
print(f'a media da menor temperatura do mes 6 foi de: {media_min_temp_m6}')