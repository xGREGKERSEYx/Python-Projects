from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

def generate_pet_name(animal_type):
    #Initialize the OpenAI LLM
    llm =OpenAI(temperature=0.4)

    #Create a prompt template
    prompt_template_langchain = PromptTemplate(
        input_variables=['animal_type'],
        template="I have a pet {animal_type} and would like some cool names suggested. Please suggest five names!"
    )

    prompt = prompt_template_langchain.format(animal_type=animal_type)

    name=llm.invoke(prompt)

    return name

if __name__ == "__main__":
    animal_type = "horse"
    print(generate_pet_name(animal_type))