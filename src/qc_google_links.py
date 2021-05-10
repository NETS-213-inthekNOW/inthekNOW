# -*- coding: utf-8 -*-
"""qc_google_links.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1RQmBrxEdLsn1RFbOpLVzBIS8NJNy76ju
"""

import pandas as pd
import numpy

def findGoogle(locationFinder):
  # we look in column LINK, for each row, see if the string google is in the name 
  # if it is, we keep it, 

  final_list = [] # (attr_id, adj) -> [# of Y, # of N, # of NA]
  for index, row in locationFinder.iterrows():
    loc_id = row['Input.location_link']
    newLoc_id = row['Answer.Q4CorrectLink']
    substring = "google.com"
    corr_substring = "correct"
    res = (row['Input.location'], loc_id)
    res_new = (row['Input.location'], newLoc_id)
    if (substring in loc_id) or (not isinstance(newLoc_id, float) and corr_substring in newLoc_id): 
      final_list.append(res)
    else:
      final_list.append(res_new)
    # final_list = sorted(final_list, key=lambda element: (element[0], -element[1]))
    #final_df = pd.DataFrame(final_list, columns =['Location', 'Link'])
  return final_list 
        
        
import csv
def main():
  locationFinder = pd.read_csv('qc_results.csv')
  # print(locationFinder.dtypes)
  df = findGoogle(locationFinder)
  df_update = pd.DataFrame(df, columns=['Location', 'Link'])
  # remove NaN in 'Link' rows
  no_empty_rows = df_update[df_update['Link'].notna()]
  # remove rows in 'Link' which are not valid links
  only_links = no_empty_rows[no_empty_rows["Link"].str.contains('https')]
  # remove links which are not google links
  only_google = only_links[only_links["Link"].str.contains('google')]
  only_long_links = only_google[only_google['Link'].map(len) > 30]
  # drop duplicates
  prefinal_output = only_long_links.drop_duplicates().reset_index(drop=True).fillna(0)
  final_output = prefinal_output.drop_duplicates(subset='Link', keep="first")
  #print(second_df)
  final_output.to_csv("qc_google_links.csv", index=False)
  
      
if __name__ == '__main__':
    main()