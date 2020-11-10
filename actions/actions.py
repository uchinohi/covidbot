# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import requests


class ActionCovidSafety(Action):

    def name(self) -> Text:
        return "action_covid_safety"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        message="Wear a mask, wash your hands regularly and maintain social distancing.\nBut I only know so much.\nVisit https://www.who.int/emergencies/diseases/novel-coronavirus-2019/advice-for-public to know more. They know everything!"
        dispatcher.utter_message(message)

        return []

class ActionCovidSymptoms(Action):

    def name(self) -> Text:
        return "action_covid_symptoms"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        message="Most common symptoms may include fever, dry cough and tiredness. You may also experience sore throat, headache and a loss of taste and smell. Severe symptoms may cause difficulties in breathing."
        dispatcher.utter_message(message)

        return []



class ActionCovidSearch(Action):

    def name(self) -> Text:
        return "action_covid_search"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        response = requests.get("https://api.covid19india.org/data.json").json()

        entities = tracker.latest_message['entities']
        state= None
        case= None

        for e in entities:
            if e['entity'] == "state":
                state = e['value']
            if e['entity'] == "type_of_case":
                case = e['value']

        
        message="Sorry you have entered a wrong location! I can only tell you about Indian States."
        for data in response['statewise']:
            if data['state'] == state.title():
                if case == "all":
                    message = "For "+state.title()+":-\nActive: "+data['active']+"\nConfirmed: "+data['confirmed']+"\nRecovered: "+data['recovered']+"\nDeaths: "+data['deaths']
                else:
                    message= "For "+state.title()+", number of "+case+" cases are "+data[case]

        dispatcher.utter_message(message)

        return []