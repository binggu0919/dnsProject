from nslookup import Nslookup
import pandas as pd
import numpy as np
import time

domain = "naver.com"

# set optional Cloudflare public DNS server
dns_query = Nslookup(dns_servers=["8.8.8.8"])
df_whitelist_domain = pd.read_csv("./top-1m.csv", index_col=0, header=None)
df_whitelist_domain.reset_index(inplace=True)
df_whitelist_domain.rename(columns={0: "no", 1: "domain"}, inplace=True)
df_whitelist_domain.set_index('no', inplace=True)
df_whitelist_domain.reset_index(drop=True, inplace=True)
# df_whitelist_domain.set_index('no',append=True)

# for i in range(df_whitelist_domain['domain'].size) :
for i in range(1000) :
    time.sleep(0.1)
    dns_query.dns_lookup(df_whitelist_domain['domain'][i])
    print(i)

