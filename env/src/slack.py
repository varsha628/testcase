import json
import logging
import requests

# Configure logging
logging.basicConfig(level=logging.INFO,filename="result.log",filemode="w" )

class SlackAPI:
    def __init__(self,token):
        """Initialize the SlackAPI class with the Slack bot token."""
        self.base_url = "https://slack.com/api"
        self.token ="token"
        self.headers = {
            'Authorization': f'Bearer {self.token}'
        }

    # def get_conversations_list(self):
    #     """function to get conversations list"""
    #     endpoint = f"{self.base_url}/conversations.list"
    #     try:
    #         response = requests.get(endpoint, headers=self.headers)
    #         response.raise_for_status() #raises an exception if response indictaes error
    #         data = response.json()
    #         if not data.get("ok"):
    #             logging.error(f"Error fetching conversations list: {data.get('error')}")
    #         logging.info("Successfully fetched conversations list.")
    #         #logging.info(data.get("channels", []))
    #         pretty_data=json.dumps(data,indent=4)
    #         logging.info(f'Json data = {pretty_data}')
    #     except requests.exceptions.RequestException as e:
    #         logging.error(f"Request failed: {e}")
    #         return None

    def get_conversations_list(self,url:str):
        endpoint = f"{self.base_url}/conversations.list"
        try:
            response = requests.get(endpoint, headers=self.headers)
            response.raise_for_status()  # Raises an exception if response indicates error
            data = response.json()
            if not data.get("ok"):
                logging.error(f"Error fetching conversations list: {data.get('error')}")
                return None
            logging.info("Successfully fetched conversations list.")
            # Log formatted JSON data for debugging
            pretty_data = json.dumps(data, indent=4)
            logging.info(f"Json data = {pretty_data}")
            #return data  # Return the parsed data
            return response
        except requests.exceptions.RequestException as e:
            logging.error(f"Request failed: {e}")
            return None



    def get_users_list(self):
        """ function to get users list

        """
        endpoint = f"{self.base_url}/users.list"
        try:
            response = requests.get(endpoint, headers=self.headers)
            response.raise_for_status()
            data = response.json()
            if not data.get("ok"):
                logging.error(f"Error fetching users list: {data.get('error')}")
                return None
            logging.info("Successfully fetched users list.")
            #logging.info(data.get("members", []))
            pretty_data=json.dumps(data,indent=4)
            logging.info(f'Json data = {pretty_data}')
        except requests.exceptions.RequestException as e:
            logging.error(f"Request failed: {e}")
            return None

a=SlackAPI(1)
a.get_conversations_list(1)
a.get_users_list()