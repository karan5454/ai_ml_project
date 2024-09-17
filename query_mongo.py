
from pymongo import MongoClient
from langchain.prompts import PromptTemplate
import pandas as pd

# Connect to MongoDB
try:
    client = MongoClient('mongodb://localhost:27017/')
    db = client['product_db']
    collection = db['products']
except Exception as e:
    print(f"Error connecting to MongoDB: {e}")
    exit(1)

# Define LLM prompt template for generating MongoDB queries
prompt_template = """You are an expert in MongoDB query generation.
Based on the following user input, generate the appropriate MongoDB query.

User Input: {input}

MongoDB Query:"""

def generate_mongodb_query(user_input):
    try:
        # Simulating an LLM prompt to generate MongoDB query
        prompt = PromptTemplate(input_variables=["input"], template=prompt_template)
        prompt_text = prompt.format(input=user_input)
        
        # Example placeholder for a generated query (you should replace this with actual LLM output)
        generated_query = "{'Price': {'$gt': 50}}"  # Example of a valid query
        print(f"Generated Query: {generated_query}")
        
        # Save the generated query to queries_generated.txt
        with open('queries_generated.txt', 'a') as file:
            file.write(f"User Input: {user_input}\n")
            file.write(f"Generated Query: {generated_query}\n\n")
        
        return generated_query
    
    except Exception as e:
        return f"Error generating MongoDB query: {str(e)}"

def execute_query(query):
    try:
        # Validate if the query is a valid MongoDB query
        if not isinstance(query, dict):
            raise ValueError("The generated query is not a valid MongoDB query.")
        
        # Execute the query in MongoDB
        result = collection.find(query)
        data = list(result)
        
        if not data:
            return "No results found."
        
        return data
    
    except Exception as e:
        return f"Error executing query: {str(e)}"

def save_or_display_data(data, save=False, filename="output.csv"):
    try:
        if isinstance(data, str):
            # If data is a string (error or no result message), print it
            print(data)
        else:
            df = pd.DataFrame(data)
            if save:
                df.to_csv(filename, index=False)
                print(f"Data saved to {filename}")
            else:
                print(df)
    except Exception as e:
        print(f"Error saving or displaying data: {str(e)}")

if __name__ == "__main__":
    try:
        # Test Case 1: Find all products with a rating below 4.5, reviews > 200, and brand 'Nike' or 'Sony'
        user_input = input("Enter query condition : ")
        generated_query = generate_mongodb_query(user_input)

        # Check if the generated query is a valid dictionary
        query_dict = eval(generated_query)
        if not isinstance(query_dict, dict):
            raise ValueError("Generated query is not in a valid format.")

        # Execute the query
        result = execute_query(query_dict)

        # Save result of Test Case 1 to test_case1.csv
        save_or_display_data(result, save=True, filename="test_case3.csv")
    
    except Exception as e:
        print(f"Error: {str(e)}")
