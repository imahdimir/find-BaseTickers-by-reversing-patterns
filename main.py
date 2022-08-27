##


import pandas as pd

from githubdata import GithubData
from mirutil import funcs as mf
from mirutil.funcs import read_data_according_to_type as rdata


id2t_rpo_url = 'https://github.com/imahdimir/d-TSETMC-ID-2-Ticker-map'
bt_rpo_url = 'https://github.com/imahdimir/d-BaseTicker'

tic = 'Ticker'
btic = 'BaseTicker'
name = 'Name'

def srch_tsetmc_check_eq(istr):
  df = mf.search_tsetmc(istr)
  return df[tic].eq(istr).any()


def main() :
  pass

  ##
  id2t_rpo = GithubData(id2t_rpo_url)
  id2t_rpo.clone()

  ##
  dfip = id2t_rpo.data_filepath
  dfi = rdata(dfip)
  dfi = dfi.reset_index()
  dfi = dfi[[tic]]
  dfi = dfi.drop_duplicates()

  ##
  bt_rpo = GithubData(bt_rpo_url)
  bt_rpo.clone()

  ##
  dfbp = bt_rpo.data_filepath
  dfb = rdata(dfbp)

  ##
  not_base_tic = {
      'رپارسح1' : None,
      'آرينح1' : None
      }

  ##
  ptr = '\D+1'
  msk0 = dfi[tic].str.fullmatch(ptr)
  msk1 = ~ dfi[tic].str[:-1].isin(dfb[btic])
  msk2 = ~ dfi[tic].isin(not_base_tic.keys())

  msk3 = dfi[tic].str[-2].eq('ح')
  msk4 = dfi[tic].str[:-2].isin(dfi.loc[msk0, tic].str[:-1])

  ms0 = msk0 & msk1 & msk2
  ms1 = msk0 & msk3 & msk4

  ms = ms0 & ~ms1

  ##
  df1 = dfi[ms]

  ##
  df1['-1'] = df1[tic].str[:-1]
  df1['s'] = df1['-1'].apply(srch_tsetmc_check_eq)

  ##
  df11 = df1[['-1']]
  df11 = df11.rename(columns = {'-1' : btic})

  ##
  dfb = pd.concat([dfb, df11])
  dfb = dfb.drop_duplicates()

  ##
  dfb = dfb.set_index(btic)

  ##
  fp = bt_rpo.local_path / 'data.prq'
  ##
  dfb.to_parquet(fp)

  ##
  msg = '128 new , fmt changed to .prq'

  bt_rpo.commit_push(msg)

  ##
  bt_rpo.rmdir()
  id2t_rpo.rmdir()


  ##


##

##