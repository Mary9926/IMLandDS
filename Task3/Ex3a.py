import matplotlib.pyplot as plt
from zipfile import ZipFile
import pandas as pd

# Can you observe the trends in the number of births over all years? Are these trends different between girls and boys? Provide relevant charts.

zip_file = ZipFile('names.zip')
dfs = {text_file.filename: pd.read_csv(zip_file.open(text_file.filename), header=None)
       for text_file in zip_file.infolist()
       if text_file.filename.endswith('.txt')}

# for text_file in zip_file.infolist():
#     print("df = pd.read_csv('" + text_file.filename + "', header=None, names=['name','sex','count'])")

# pls don't judge me
years = [1880,1881,1882,1883,1884,1885,1886,1887,1888,1889,1890,1891,1892,
      1893,1894, 1895,1896,1897,1898,1899,1900,1901,1902,1903,1904,1905,1906,1907,1908,1909,1910,1911,
      1912,1913,1914,1915,1916,1917,1918,1919,1920, 1921,1922,1923,1924,1925,1926,1927,1928,1929,1930,
      1931,1932,1933,1934,1935,1936,1937,1938,1939,1940,1941,1942,1943,
      1944,1945,1946,1947,1948, 1949, 1950,1951,1952,1953,1954,1955,1956,
      1957,1958,1959,1960,1961,1962,1963,1964,1965,1966,
      1967,1968,1969,1970,1971,1972,1973,1974,
      1975,1976,1977,1978,1979, 1980,1981,1982,1983,1984,1985,1986,1987,1988,
      1989,1990,1991,1992,1993,1994,1995,1996,1997,1998,1999,2000,2001,2002,2003,2004, 2005,2006,2007, 2008, 2009,2010,2011, 2012,2013,2014, 2015, 2016, 2017, 2018]

df2 = pd.DataFrame(
    columns=['girlsAmount', 'boysAmount'],
    index= years)
for x in range(1880, 2019):
    year = 'yob' + str(x) + '.txt'
    value = dfs[year]
    boys = value[value[1] == 'M']
    girls = value[value[1] == 'F']
    df2.loc[x, :] = [girls[2].sum(), boys[2].sum()]

print(df2)
df2.plot(title = 'Number of births over all years', xlabel="Year", ylabel="Count")
plt.show()
