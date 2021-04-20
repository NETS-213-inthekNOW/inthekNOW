# inthekNOW

### Data Format

The input data to the quality control module will be a .csv with headers describing the questions in the HIT, and columns with the worker IDs and corresponding responses for each of the questions. For example:
WorkerID     | City          | etc.
------------ | ------------- |----
IOJFOIJIFJWE | Mumbai        | ...
ZXCIGEWQU@!# | Boston        | ...

The input data to the aggregation module will be analogous, since the quality control module only serves to cull workers that are clearly bad actors. 

### Code Design

The quality control module's current design is to simply (????) <- fill in 

The aggregation module's current design is to conglomerate responses that name the same tourist destination, if any. Then, (????) <- fill in 

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
- Write all code needed for the website to present aall information. 
