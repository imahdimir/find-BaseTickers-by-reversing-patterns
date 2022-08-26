##


import pandas as pd
from pathlib import Path

from githubdata import GithubData
from mirutil import funcs as mf
from mirutil.funcs import save_df_as_a_nice_xl as sxl


id2t_rpo_url = 'https://github.com/imahdimir/d-TSETMC-ID-2-Ticker-map'
bt_rpo_url = 'https://github.com/imahdimir/d-uniq-BaseTickers'



def main() :
  pass

  ##
  id2t_rpo = GithubData(id2t_rpo_url)
  id2t_rpo.clone()

  ##
  dfip = id2t_rpo.data_filepath


  ##
##
##