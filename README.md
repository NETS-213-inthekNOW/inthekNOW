# inthekNOW

Repo format: data/ directory contains .csv that acts as sample i/o for the modules/code, which are listed in the src/ directory. The .pdfs generally elaborate on the details of the HIT that will generate corresponding .csvs.

### Data Format

The input data to the quality control module will be multifold.

The first will be a .csv with headers describing the questions in the "upvote" HIT, and columns with the worker IDs and corresponding responses for each of the questions. The upvote HIT will essentially present the worker with a submitted tourist location and ask the worker to judge the location as good or bad. If they've never heard of it they are asked to research it.
For example:
WorkerID     | Destination | Which best represents your relation to the destination| Do you recommend visiting? | Why?          |
------------ | ---------------- | ----------------------------------------------------- |----------------------------| ------------- |
IOJFOIJIFJWE | Porta-potty on 1st street near Boston   | Never been there                                      | No                         | It smells bad.        |
ZXCIGEWQU@!# | Porta-potty on 1st street near Boston | I haven't been there, but have heard of it            | Yes                        | Smells good.          |

The second input data to the quality control module will be a .csv with headers describing the questions in the HIT, and columns with the worker IDs and corresponding responses for each of the questions. For example:
WorkerID     | City          |What destination in your area do you recommend?|
------------ | ------------- |-----------------------------------------------|
IOJFOIJIFJWE | Mumbai        |Elephanta caves|
ZXCIGEWQU@!# | Boston        |Porta-potty on 1st street|

The quality control module then appends columns to the .csv, one column describing number of workers who recommended, and the other describing the number of workers that recommended against it, and outputs that .csv.

The aggregation module input then takes in that .csv and uses the EM algorithm until convergence to assign final decisions for each of the destinations. Then it appends these decisions as a new column to the input .csv and returns it as output.

### Code Design

The quality control module's current design is to simply take in the input .csv, and using pandas, count the number of affirmative and negative answers, forming a weighted majority vote/decision. In upvoting, since responses specified if the worker actually went to the destination or not, we separated vote counts based on these factors. Our output has four columns: one for users who went to the destination and recommended it, one for users who did not go to the destination and recommended it, one for users who did not recommend the destination and did go there, and one for users who did not go to the destination and also did not recomment it. 'qc_sample_input.csv' is an example csv file we ran through our code, and 'new_destinations.csv' is our output.

The aggregation module's current design is to  (????) <- fill in 

### Project Components Breakdown

Phase 1: Gather Raw Data/Forming the Experiment (2 points)
- Forming github repo/organization, creating HIT design/questions, finalizing project details such as the name

Phase 2: 1st MTurk Task (2 points)
- Set up the HIT html/css/AWS/relevant items so the crowd can give their recommendations.
- Quality control through Python to remove results with response length shorter than required / other misc. bad responses.

Phase 3: 2nd MTurk Task (4 points)
- Aggregating all the results of the previous step. This involves spreadsheet management with Excel or Google Sheets to get relevant locations and their descriptions, pictures, and all other relevant information. 
- Writing HIT html/css/AWS/relevant items so the crowd can choose the best set of recommendations by majority vote.

Phase 4: Refining (4 points)
- Write HIT html/css/AWS/relevant items so that the crowd can iteratively improve the set of information it has been given.

Phase 5: Form the website (4 points)
- Write all code needed for the website to present all information. 
