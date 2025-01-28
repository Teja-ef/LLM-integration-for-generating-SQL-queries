from langchain.prompts import PromptTemplate
from langchain_ollama import OllamaLLM

def generate_sql(natural_query : str):
    llm = OllamaLLM(model="gemma:2b")

    # Define the prompt template for SQL generation
    prompt_template = """
    You are an expert SQL generator. Use the following database schema to create SQL queries:

    ### TABLE 1: users ###
    - user_id: Integer (Primary Key, Auto Increment) - id of user
    - username: String (255, Not Null) - username of user
    - email: String (255, Unique, Not Null) - email of the user
    - password: String (255, Not Null) - password of user

    ### TABLE 2: Task ###
    - id: Integer (Primary Key, Auto Increment)
    - ToDo: String (255, Not Null)
    - CreatedAt: DateTime (Default: Current Timestamp)
    - Status: String (255, Not Null)
    - isExist: Boolean (Default: True, Not Null)
    - user_id: Integer (Foreign Key -> users.id, Cascade on Delete, Not Null)

    Using the above table schemas, **generate an optimized SQL query** for the following natural language request:

    ###DON'T GIVE THE EXPLANATION. GIVE ONLY SQL STATEMENT. GIVE STATEMENT IN ONE LINE###
    Query: {query}

    **SQL Output:**
    """
    
    prompt = PromptTemplate(input_variables=["query"], template=prompt_template)
    llm_chain = prompt | llm
    sql_query = llm_chain.invoke({"query": natural_query})
    return sql_query[6:-3]
