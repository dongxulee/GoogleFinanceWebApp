# SI507F17_finalProject(self-conduct project)
## Stock Info database for S&P 500 stock:
For this project, my purpose is to create a stock infomation database for all the stock in s&p 500. Through
SQL language to retrieve information from the database, I can apply some basic stock price data visulization methods: pricing plot through a certain time window, and correlation table for chosen stocks. And I also developed a web running on the local server. User can select the stock they are interested in and get more infomation from the stock open high low close price for most recent 3 month.


## Run the application
### Step 1: Created a virtual environment
- Download or clone the repo into a local pc.
- Open Terminal (OSX or Unix), set the current folder to be the final project folder.
- If you are a anaconda user you can type ```conda create --name myenv```, if not you can use pip to create the environment.
- Activate the environment by typing ```source active myenv```.
- Install all the required package by typing ```pip install -r requirements.txt```.

### Step 2: Database table creating and first visualization
- Assume you are a PostgreSQL user, Edit __config.py__ by including the database name and user/password required to connect to the database. An example is as follow:
```
db_name = 'finalProject'
db_user = 'lee'
db_password = ' '
```
- Start the database server, for example: ```pg_ctl -D /usr/local/var/postgres start```, check if the server is running.
- Start running the __SI507F17_finalproject.py__ file: ```python SI507F17_finalproject.py```, this program will construct the database on the caching data(using all the csv file under the __stock_dfs__ folder). 
- If you want to update the caching data, you can open __SI507F17_finalproject.py__ file and follow the instruction for __dataBaseConstuct()__ function. If you want to cache the new data from the web, please be patient, because this may take up to 4 minutes, since there are 3 month data for 505 stocks. You can keep track of the process in the command window output.
- After successfully ran the program, you can get an __correlation_table.html__ file, you can use the web browser to open the file and you get something like this:
<img width="957" alt="screen shot 2017-12-14 at 21 19 49" src="https://user-images.githubusercontent.com/26841080/34023815-ec7ed51c-e114-11e7-97cd-97a10aeafea0.png">
- The image above is a correlation table visualization of the stocks specified in the __SI507F17_finalproject.py__ file, you can select the stock you like by make change in this file. The default stock list: 
``` 
stocks = ['GOOG','MSFT','IBM','AAPL','FB','ORCL','AMZN']
```.

### Step 3: Runing the Web App using flask framework
- In the terminal, typing ```python webApp.py runserver``` to start the web application.
- Once the web server is runing, go the browser and go to the default local server address http://localhost:5000/, you should see something like this:
<img width="719" alt="screen shot 2017-12-14 at 21 30 23" src="https://user-images.githubusercontent.com/26841080/34024024-0cbd37dc-e116-11e7-807c-500da232649c.png">
- This the web which list all the stocks in the S&P 500, and you can see, at the left corner of the page, there is a selecting menu, you can type the stock ticker you are interested or you can also scrow down to selet one. Then hit the submit bottom, and you will see some thing like this: here we select __BRK.B(Berkshire Hathaway Inc)__
<img width="1105" alt="screen shot 2017-12-14 at 21 35 06" src="https://user-images.githubusercontent.com/26841080/34024155-b381f990-e116-11e7-9b38-6f7144b99cb1.png">
- This is the daily stock price visualization for __BRK.B(Berkshire Hathaway Inc)__, the data traces back to three month, and when you move you cursor on the graph, the nicely plotly feature will show the open high low close price at a specific day. 
