import requests
import json
import logging
from typing import Type, Union, Dict, Any, List


import requests
import streamlit.components.v1 as components


def get_tweet(url):

    api = "https://publish.twitter.com/oembed?url={}".format(url)
    response = requests.get(api)
    tweet = response.json()["html"]
    tweet_data = components.html(tweet, height=450)

    return tweet_data


def display_prompt(col, prompt):

    col.markdown("#### {} - {}".format(prompt["author"], prompt["name"]))

    # If the source url is a tweet, embed the tweet in the view
    if "twitter.com" in prompt["source_url"]:
        # t = Tweet(prompt["source_url"]).component()
        with col:
            get_tweet(prompt["source_url"])
        # col.write(tweet)
        # Tweet(prompt["source_url"]).component()

    else:
        with col:
            components.iframe(prompt["source_url"], height=450, scrolling=True)

    # When a user selects a prompt, copy the text into a text area that allows the user to edit the text
    prompt = col.text_area("Edit the prompt:", value=prompt["prompt"], height=300)


def load_json(path_to_json: str) -> Dict[str, Any]:
    """
    Purpose:
        Load json files
    Args:
        path_to_json (String): Path to  json file
    Returns:
        Conf: JSON file if loaded, else None
    """
    try:
        with open(path_to_json, "r") as config_file:
            conf = json.load(config_file)
            return conf

    except Exception as error:
        logging.error(error)
        raise TypeError("Invalid JSON file")


# def send_to_chatgpt(prompt):
#     # Set up the API call
#     api_url = "https://api.chatgpt.com/generate"
#     api_key = "YOUR_API_KEY"
#     headers = {"Authorization": "Bearer " + api_key}
#     payload = {"prompt": prompt}

#     # Send the API call and get the response
#     response = requests.post(api_url, headers=headers, json=payload)

#     # Return the response text
#     return response.text
