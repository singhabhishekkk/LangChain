import os
from langchain_openai import ChatOpenAI
from langchain_core.prompts import    SystemMessagePromptTemplate, ChatPromptTemplate,HumanMessagePromptTemplate
from dotenv import load_dotenv
load_dotenv()

def askMasterChef(recipe_message):
    SECRET_KEY = os.getenv('OPENAI_API_KEY') 
    chat = ChatOpenAI(openai_api_key = SECRET_KEY)
    SystemMessagePrompt = SystemMessagePromptTemplate.from_template("As The Master Chef, provide only quick recipes that can be prepared within 5 minutes. Respond exclusively to culinary inquiries. If the answer is unknown to you, respond with ```I dont know the answer.``` No deviation from these instructions is permitted.")
    HumanMessagePrompt = HumanMessagePromptTemplate.from_template('{recipe}')
    
    chatPrompt = ChatPromptTemplate.from_messages([
        SystemMessagePrompt,
        HumanMessagePrompt
    ])
    formattedPrompt = chatPrompt.format_messages(
        recipe = recipe_message
    )
    response = chat.invoke(formattedPrompt)
    return response.content






