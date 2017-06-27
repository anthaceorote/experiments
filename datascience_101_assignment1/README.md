# Helping Students in Choosing Colleges
### Data Science 101 - Demo Assignment

[Source](https://data.world/nrippner/datascience-101-assignment-1): data.world demo assignment

#### Problem Statement
* Supporting the decision making process of students and families in choosing which college to go to, based on factors such as - 
	* Field of Education
	* Location (Urban, Metropolitan, University Town)
	* Neighbourhood (Low crime rate)
	* Job Market/ Startup Activity
* Use relevant data sets to find the top 20 colleges that satisfy the given criteria

#### Data
| Data | Description | Source |
| :--- | :---------- | :----- |
|[College Scorecard](/data/CollegeScorecard.csv) | [CollegeScorecardDocumentation.pdf](/data/CollegeScorecardDocumentation.pdf) | [US Dept of Edu](https://collegescorecard.ed.gov/data/)|
| [Crime Trends](/data/Crime_2015.csv) | [LocalCrimeTrends.pdf](/data/LocalCrimeTrends.pdf) | [UCRS](https://www.ucrdatatool.gov/Search/Crime/Local/TrendsInOneVarLarge.cfm) |
| [Entrepreneurialism - Kaufmann Index](/data/kieadata15.csv) | [kieacodebook_v7.xlsx](/data/kieacodebook_v7.xlsx) | [Kaufmann Index](http://www.kauffman.org/kauffman-index/about/kiea-microdata) |

#### Use Case
Maria is a 25-year-old US Army veteran, newly returned to the civilian workforce. She has recently completed a six-year commitment with the Army. During her time in the Army, she worked in supply management and logistics. She has decided to pursue a degree in Management Systems and Information Technology.

Maria has asked you to use your skill with data to help her search for the best school for her. She is willing to relocate anywhere in the continental United States, but she has a few criteria that her ideal schools must satisfy: 1) safety (low crime), 2) urban -- Maria wants to live the big city life, and 3) start-ups -- the school should be in a metropolitan area that ranks highly in entrepreneurialism (she plans to find an internship at a startup while she studies).

Maria would like you to help her narrow down her search to a list of schools that she can investigate more closely before making her decision.

**TASK**:  
1. Produce a dataset of schools which satisfy all of Maria's criteria
2. Rank them from best to worst according to the same criteria  

Maria's schools must:
* be in an urban/metropolitan area
* be in a city that ranks 75th percentile or higher on Kauffman's start-up rankings
* be below 50th percentile in overall crime
* offer a 2-year or 4-year degree in Information Technology/Science

#### Methodology

1. Read the data dictionaries or codebooks to figure out what the variables mean and which ones you will need to use
2. Eliminate unneeded columns
3. Look for suitable columns to join the tables on
4. Perform any cleaning and standardization needed to facilitate the joins
5. Engineer a summary variable for school crime so that we can compare schools by levels of crime overall
6. Eliminate from the data all the data points that fail to satisfy Maria's criteria
7. Engineer a method for ranking the schools in consideration of all of Maria's criteria taken together

#### Results


