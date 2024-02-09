import numpy as np
import pandas as pd

ne_url = 'https://raw.githubusercontent.com/mclainbrown/kpop_project/main/2ne1.csv'
ne_df = pd.read_csv(ne_url)

bigbang_url = 'https://raw.githubusercontent.com/mclainbrown/kpop_project/main/bigbang.csv'
bigbang_df = pd.read_csv(bigbang_url)

blackpink_url = 'https://raw.githubusercontent.com/mclainbrown/kpop_project/main/blackpink.csv'
blackpink_df = pd.read_csv(blackpink_url)

treasure_url = 'https://raw.githubusercontent.com/mclainbrown/kpop_project/main/treasure.csv'
treasure_df = pd.read_csv(treasure_url)

ikon_url = 'https://raw.githubusercontent.com/mclainbrown/kpop_project/main/ikon.csv'
ikon_df = pd.read_csv(ikon_url)

#bigbang_df = pd.concat([bigbang1_df, bigbang2_df])

#bigbang_df.to_csv('bigbang.csv')

YG_df = pd.concat([treasure_df, blackpink_df, ikon_df, ne_df, bigbang_df])

YG_df.to_csv('YG.csv')