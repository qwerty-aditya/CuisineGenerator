from langchain.llms import OpenAI
import os
from langchain.prompts import PromptTemplate
from langchain.chains import SequentialChain
from langchain.chains import LLMChain

os.environ['OPENAI_API_KEY'] = [YOUR_API_KEY_HERE]
llm = OpenAI(temperature = 0.6)

def restaurant_name_and_item(cuisine):
    promt_template_name = PromptTemplate(
    input_variables=['cuisine'],
    template = "I want to open restauraunt for {cuisine} food. Suggest a fancy named food restauraunt."
    )
    name_chain = LLMChain(llm = llm, prompt = promt_template_name, output_key='restauraunt_name')
    promt_template_items = PromptTemplate(
        input_variables=['restauraunt_name'],
        template = "Suggest some fancy vegeterian menu items for {restauraunt_name}."
    )
    food_items_chain = LLMChain(llm=llm, prompt=promt_template_items, output_key='menu_items')
    chain = SequentialChain(
        chains = [name_chain, food_items_chain],
        input_variables = ['cuisine'],
        output_variables = ['restauraunt_name','menu_items']
    )
    return chain({'cuisine': cuisine})

if __name__ == '__main__':
    print(restaurant_name_and_item("Indian"))
    