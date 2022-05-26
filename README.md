# FastApi-Selenium-MongoDB-Dockerization


A Scraping Service for a public Facebook Page .
Open and view the Project using the `.zip` file provided or at my [GitHub Repository]



## Table of Contents
- [Getting Started](#getting-started)
	- [Tools Required](#tools-required)
	- [Installation](#installation)
- [Development](#development)
	  - [Part 1: Scraping](#part-1-heading)
	  - [Part 2: Storing](#part-2-heading)
	  - [Part 3: Dockerization ](#part-2-heading)


- [Running the App](#running-the-app)


## Getting Started

```
	scraping-service 
	├── README.md
	├── docker-compose.yaml
	├── dockerfile
  ├── requirements.txt
	├── app
	│   ├── main.py
	│   ├── model.py
	│   └── scraping.py
	└── drivers
		├── chromedriver
		
``` 
### Tools Used

All tools required go here. You would require the following tools to develop and run the project:

* A text editor or an IDE (like IntelliJ)
* FastApi
* Selenium
* MongoBD
* Docker

### Installation

No Installation needed - Docker controlled
version

## Development


1. Facebook has a very strong anti-bot system in place, which goes much more than just IP tracking
2. Scraping Facebook is not an easy task
3. Selenium will help you render JavaScript, it can be counterproductive. This is because Facebook uses JavaScript for browser fingerprinting and behavioral analysis, and with this, they can tell if requests are originating from a bot, and your access will be blocked after a few requests.
4. The old mobile web version of Facebook (https://mobile.facebook.com) does not require JavaScript, and as such, you can scrape from this site instead of the web version of Facebook . And this is the strategie followed by this project

### Part 1: Scraping

#### Step 1: FastApi

* Call the scraping service 
  
#### Step 2: Selenium

* scrap the text data using Css_Selectors.
 

For details now how everything has been implemented, refer the source code

### Part 2: Storing

* MongoBD stores the data that have been caption using an FastApi service


### Part 3 :Dockerization

* 3 containers needed Api | DB | Selenium 

check docker-compose for more details 

## Running the App



  ```
sudo docker-compose build
sudo docker-compose up

```


