# SI507F17_finalProject(self-conduct project)
## Stock Info database for S&P 500 stock:
For this project, my purpose is to create a stock infomation database for all the stock in s&p 500. Through
SQL language to retrieve information from the database, I can apply some basic stock price data visulization methods: pricing plot through a certain time window, and correlation table for chosen stocks.


## Final Project Milestones
### Part 1: Get all tickers of all S&P 500
- [ ] Vitual environment setup, create the
- [ ] Analyzing stock tickers info on wiki page: https://en.wikipedia.org/wiki/List_of_S%26P_500_companies.
- [ ] Using BeautifulSoup to extract tickers from the wiki page.
- [ ] Processing the ticker data we get and make sure they are in the right format and store them in the csv file.

### Part 2: Applying googlefinance.client to get stock info
- [ ] Pip install googlefinance.client, play with the api, exploring the valuable infor I might be interested.
- [ ] Start to exact data and do some basic visualization tryout.

### Part 3: Database setup and conduct data query test
- [ ] Design the database structure.
- [ ] Database setup, extract date through googlefinance.client and store them in the database.
- [ ] Query testing, make sure the data is in the right format and take a brief look at the table created through pgadmin interface.

### Part 4: Visualization Method(stock price and correlation table visualization)
- [ ] Make query to the database to get the data we need, and write out the visulization method we need.
- [ ] Do some web programming or use Python to create an HTML document if there is still time left.
- [ ] Make some screen shots to give an example of my result and comments in the readme.md file.
- [ ] Modify the README.md through out the project, and write out the running instructions which the instructor needs to run my program.

### Part 5: Check before submission
- [ ] A README.md, tells instructors exactly what to do to understand and run my code.

- [ ] Main file SI507F17_finalproject.py, all code files included must run, include a description about this document in the README.md.

- [ ] SI507F17_finalproject_tests.py, it should import any code from other files that is being tested.

- [ ] A requirements.txt file from my virtual environment.

- [ ] Any .py or other file templates that we have to fill in. Example sample_secret_data.py, give instructor a version of it, but not contain the actual secret information.

- [ ] Provide an example of the final result of the project, submitted on Canvas, so instructors can see what it should look like when they've run it.