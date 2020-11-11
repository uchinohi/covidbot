# Covid Bot
A simple information bot made using Rasa to obtain statewise info about covid 19 cases in India.

## Description
This is a very simple project I created to understand the concepts behind the open source Rasa framework. It extracts JSON data about Covid-19 cases in Indian States from a publicly available [API](https://api.covid19india.org/data.json) and extracts the requested data as per the user input.
Users can also obtain basic information about Covid-19 symptoms and safety measures.

## The Requirements
- Python 3.6+
- Rasa 2.0
- Any API that provides Covid-19 related data

## The Approach
I used a linux environment for my project as that made things simplified. I installed Rasa in a virtual environment and created a default project 'moodbot' using the command _rasa init_. This project is tweaked from the default one Rasa creates. I describe the steps undertaken very briefly below:
- I described all the necessary **intents**, **actions**, **entities** and bot **responses** in the **_domain.yml_** file.
- I provided some examples for each of the **intents** and **entities** in the **_nlu.yml_** file. This file contains training data for our NLU model.
- I defined some **rules** and **stories** in the **_rules.yml_** and **_stories.yml_** files respectively. These files hold the training data for the Rasa Core model and link user utterances with bot actions.
- For the pipeline configuration, I have kept everything mostly default, with the exception in the Tokenizer model. I am using **WhiteSpaceTokenizer** with 'intent_tokenization_flag' set to true and the 'intent_split_symbol' parameter to _'+'_, which we use to separate mutliple intents in one user input.
- In the **_endpoints.yml_** file, I uncommented the 'action_endpoint' url to enable the Rasa action server, which handles the custom actions.
- In the **_actions.py_** file, which contains the code for custom actions. I have defined a total of three custom actions. I have used the default template to define two functions which return pre-defined messages to the user once the relevant intent is detected and the action is predicted. These include intents when the user asks about Covid-19 symptoms or about their prevention.
The last custom action basically requests data from the aforementioned API and parses it. The tracker extracts necessary entities from the latest user message and stores the value. I run a loop through the received responses to find data relevant to given user entities and print them as a bot response.

## How to use
To talk with the bot presently, you would need to install Rasa on your system. Clone this repository and change your pwd to this directory. If you're running this for the first time, you need to train the model using a command _rasa train_, which will train the NLU and Core models. Open another terminal window and run the command _rasa run actions_. This command starts the Rasa action server which handles the custom actions. Once done, go back to the previous terminal window and run _rasa shell_. This opens up a simple CLI chat, enabling you to talk to the bot.

## What it can do
Our bot can provide any type of case by numbers as reported by Indian states as and when requested apart from providing information about Covid symptoms and safety measures.
Presently, it cannot do much as I have not been able to provide more data for training the models. Chatbots like this require significant amount of data for training and since this bot is not exposed to real users, we won't get much real world data for our model as well. The best practice is to create a functional bot and deploy it as soon as possible to users to collect real world data to train the model efficiently.


## Authors
Swagnik Banerjee

## Acknowledgements
[The Covid-19 India Project API](https://github.com/covid19india/api) has been a great help, both to develop this bot and in general, to track the pandemic status across my country. Do check their website [here](https://www.covid19india.org/).

Anyone wanting to improve on this project in any way, feel free to do a pull request. Improvements can come in the form of adding more relevant training data, configuring the pipeline for better processing or even adding new related functionality.

Thanks!
