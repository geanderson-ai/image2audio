from dotenv import load_dotenv, find_dotenv
from transformers import pipeline
import requests
import requests
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate





load_dotenv(find_dotenv())





def img2text(filename):
    """
    Takes an image file and converts it to text using the Hugging Face image captioning model.

    Args:
        filename (str): The path to the image file.

    Returns:
        dict: The JSON response from the Hugging Face API containing the text caption of the image.
    """
    API_URL = "https://api-inference.huggingface.co/models/Salesforce/blip-image-captioning-large"
    headers = {"Authorization": "Bearer {HUGGINGFACE_API_KEY}"}
    with open(filename, "rb") as f:
        data = f.read()
    response = requests.post(API_URL, headers=headers, data=data)
    return response.json()

def generate_history(scenario):
    """
    Generates a story based on a given scenario.

    Parameters:
        scenario (str): The scenario or context for the story.

    Returns:
        str: The generated story based on the given scenario.
    """

    template = """
    You are a story teller:
    You can generate a story based on simple narrative, the story should be no more than 20 words;

    CONTEXT: {scenario}
    STORY:
    """
    prompt = PromptTemplate(template=template, input_variables=["scenario"])

    story_llm = LLMChain(
        prompt=prompt, 
        llm=ChatOpenAI(temperature=0),
        verbose=True)
    
    story = story_llm.predict(scenario=scenario)


    return story

def text2speech(message):
    """
    Converts a given text message to speech using the Hugging Face text-to-speech API.

    Args:
        message (str): The text message to convert to speech.

    Returns:
        Audio file in .flac format
    """
    API_URL = "https://api-inference.huggingface.co/models/espnet/kan-bayashi_ljspeech_vits"
    headers = {"Authorization": "Bearer {HUGGINGFACE_API_KEY}"}
    payload = {
        "inputs": message
    }
    response = requests.post(API_URL, headers=headers, json=payload)
    with open('audio.flac', 'wb') as file:
        file.write(response.content)
