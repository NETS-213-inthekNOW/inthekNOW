# -*- coding: utf-8 -*-
"""NETS 213 Final Project QC.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1DnKRwcU_jflvhvC8qmf2dPHjrgVU_4S7
"""

import pandas as pd

def weighted_majority_vote(data):
  data = data.drop(data[data['Answer.Q3Answer'] != 'Validate_No'].index)
  data = data.sort_values(by=['Input.location_label'], ignore_index = True)
  # results will only include locations that were upvoted sufficiently
  results = []
  hit = 0
  while hit in range(len(data['Answer.Q4Answer'])):
    # the data is categorized with the format "recommend_visited_preferred_count"
    yes_been_match_count = 0
    yes_been_not_count = 0
    yes_heard_match_count = 0
    yes_heard_not_count = 0
    yes_not_match_count = 0
    yes_not_not_count = 0
    no_been_match_count = 0
    no_been_not_count = 0
    no_heard_match_count = 0
    no_heard_not_count = 0
    no_not_match_count = 0
    no_not_not_count = 0
    location = data['Input.location_label'][hit]
    while data['Input.location_label'][hit] == location:
      if (data['Answer.Q4Answer'][hit] == 'Reccomend'):
        if (data['Answer.Q1Answer'][hit] == 'Yes_Visited'):
          if (data['Answer.Q2Answer'][hit] == 'Yes_Like'):
            yes_been_match_count = yes_been_match_count + 1
          else:
            yes_been_not_count = yes_been_not_count + 1
        elif (data['Answer.Q1Answer'][hit] == 'No_Not_Visited'):
          if (data['Answer.Q2Answer'][hit] == 'Yes_Like'):
            yes_heard_match_count = yes_heard_match_count + 1
          else:
            yes_heard_not_count = yes_heard_not_count + 1
        else:
          if (data['Answer.Q2Answer'][hit] == 'Yes_Like'):
            yes_not_match_count = yes_not_match_count + 1
          else:
            yes_not_not_count = yes_not_not_count + 1
      #Did not recommend the area
      else:
        if (data['Answer.Q1Answer'][hit] == 'Yes_Visited'):
          if (data['Answer.Q2Answer'][hit] == 'Yes_Like'):
            no_been_match_count = no_been_match_count + 1
          else:
            no_been_not_count = no_been_not_count + 1
        elif (data['Answer.Q1Answer'][hit] == 'No_Not_Visited'):
          if (data['Answer.Q2Answer'][hit] == 'Yes_Like'):
            no_heard_match_count = no_heard_match_count + 1
          else:
            no_heard_not_count = no_heard_not_count + 1
        else:
          if (data['Answer.Q2Answer'][hit] == 'Yes_Like'):
            no_not_match_count = no_not_match_count + 1
          else:
            no_not_not_count = no_not_not_count + 1
      hit = hit + 1
      if (hit >= len(data['Answer.Q4Answer'])):
        break
    total_vote = (5 * yes_been_match_count + 4 * yes_been_not_count + 2 * yes_heard_match_count +
      1.5 * yes_heard_not_count + 2 * yes_not_match_count + 1 * yes_not_not_count +
      (5 * no_been_match_count + 4 * no_been_not_count + 2 * no_heard_match_count
      + 1.5 * no_heard_not_count + 2 * no_not_match_count + 1 * no_not_not_count))
    tally = (5 * yes_been_match_count + 4 * yes_been_not_count + 2 * yes_heard_match_count +
      1.5 * yes_heard_not_count + 2 * yes_not_match_count + 1 * yes_not_not_count)
    five_star = round(tally * 5 / (total_vote), 3)
    hundred_star = round(tally * 100 / (total_vote), 3)
    results.append((location, yes_been_match_count, yes_been_not_count, yes_heard_match_count,
                    yes_heard_not_count, yes_not_match_count, yes_not_not_count,
                    no_been_match_count, no_been_not_count, no_heard_match_count,
                    no_heard_not_count, no_not_match_count, no_not_not_count,
                    five_star))
  return results

def create_csv(state):
  data = pd.read_csv(str(state) + ' Upvote Results.csv')
  updated_destinations = weighted_majority_vote(data)
  #Format of columns is recommend/been there/prefer
  updated_df = pd.DataFrame(updated_destinations, columns = ['Location', 'Yes/Yes/Prefer', 'Yes/Yes/Not Prefer', 'Yes/Heard/Prefer',
                                                             'Yes/Heard/Not Prefer', 'Yes/No/Prefer', 'Yes/No/Not Prefer',
                                                             'No/Yes/Prefer', 'No/Yes/Not Prefer', 'No/Heard/Prefer', 'No/Heard/Not Prefer',
                                                             'No/No/Prefer', 'No/No/Not Prefer', 'Five Star'])
  updated_df = updated_df.sort_values(by=['Five Star'], ignore_index = True)
  updated_df.to_csv(str(state) + '_upvote_output.csv')

def main():
  create_csv('CA')
  create_csv('FL')
  create_csv('NY')
  create_csv('TX')

if __name__ == '__main__':
    main()
  # With the new csv, we have a new (smaller) dataset for either further upvoting or refining