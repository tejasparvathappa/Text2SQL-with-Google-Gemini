from dotenv import load_dotenv
load_dotenv()  # Load environment variables from a .env file

import streamlit as st
import os
import sqlite3
import google.generativeai as genai

# Configure the GenAI API key using environment variables
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to interact with the Gemini model and get an SQL query back
def get_gemini_response(question, prompt):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content([prompt[0], question])  # Basic content generation using Gemini
    return response.text  # Assume the text is good to use directly

# Function to actually run the SQL query against the SQLite database
def read_sql_query(sql, db):
    conn = sqlite3.connect(db)  # Connect to the SQLite database
    cur = conn.cursor()
    try:
        cur.execute(sql)  # Execute the query
        rows = cur.fetchall()  # Get the results
    except sqlite3.Error as e:
        rows = [(str(e),)]  # In case of error, return it as part of the result
    finally:
        conn.close()  # Always close the connection
    return rows

# Define the prompt that tells the AI how to generate SQL queries from natural language
prompt = [
    """
    You are an assistant skilled in converting natural language to SQL queries.
    The SQL database is called 'STUDENT' and has the following columns: NAME, CLASS, SECTION.

    Example queries:
    1. "How many entries are in the database?"
       SQL: SELECT COUNT(*) FROM STUDENT;
    
    2. "Show me the students in the Data Science class."
       SQL: SELECT * FROM STUDENT WHERE CLASS = 'Data Science';

    Make sure the SQL query doesn't have any backticks or the word 'sql' in it.
    """
]

# Streamlit app setup
st.set_page_config(page_title="SQL Query Generator")
st.title("SQL Query Generator with Gemini AI")
st.write("Enter a question related to the 'STUDENT' database, and this app will generate the corresponding SQL query.")

# Text input field for the user's question
question = st.text_input("Your question:")

# Button to submit the question
submit = st.button("Generate SQL Query")

# When the button is pressed and the user has entered a question
if submit and question:
    # Show a spinner while the AI is generating the SQL query
    with st.spinner("Generating SQL query..."):
        # Call the function to get the SQL query
        generated_sql = get_gemini_response(question, prompt)
        st.write(f"**Generated SQL Query:** `{generated_sql}`")

        # Execute the query against the SQLite database
        st.write("Running query against the database...")
        query_result = read_sql_query(generated_sql, "student.db")

        # Display the results of the query
        st.subheader("Results:")
        if query_result:
            for row in query_result:
                st.write(row)
        else:
            st.write("No results found, or there was an error in your query.")
else:
    st.info("Please enter a question to generate an SQL query.")

# Basic styling for the app (nothing too fancy)
st.markdown(
    """
    <style>
        .stButton>button {
            background-color: #28a745;
            color: white;
        }
        .css-1d391kg {
            background-color: #f9f9f9;
        }
    </style>
    """, unsafe_allow_html=True
)
