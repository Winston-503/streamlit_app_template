import json
import os
import time
from textwrap import dedent

import openai
import streamlit as st


def generate_prompt(job_description: str) -> str:
    """
    Get the information extraction prompt for the given job description:
    - Asking for JSON output
    - Keys are: job_title, company, key_skills (as list),
        job_description_summary and job_responsibilities_summary
    - Asking to complete summarization in two steps (CoT)
    """

    # using textwrap.dedent to unindent strings, e.g. ignore tabs
    prompt = dedent("""\
                Given the job description separated by <>, extract useful information. 
                Format your response as JSON with the following structure:
                {
                    "job_title": Job title,
                    "company": Company,
                    "key_skills": ["list", "of", "key", "skills"],
                    "job_description_summary": Job description summary,
                    "job_responsibilities_summary": Job responsibilities summary
                }
                To effectively complete the summarization, follow these steps:
                - First, summarize the whole job description and write it as value for "job_description" key
                - Then, summarize the job description summary with a focus on day-to-day responsibilities
                """)

    prompt += f"<{job_description}>"

    return prompt


def ask_chatgpt(input_text: str) -> str:
    """ Call OpenAI's gpt-3.5-turbo model API with prompt by 'generate_prompt()' function """

    openai.api_key = os.getenv('OPENAI_API_KEY')

    prompt = generate_prompt(input_text)

    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )

    return response.choices[0].message["content"]


def toy_ask_chatgpt(input_text: str) -> str:
    """ Try to call 'ask_chatgpt()' function and returns the same result if OpenAI key is not valid """

    try:
        return ask_chatgpt(input_text)
    except openai.error.AuthenticationError:
        time.sleep(2)  # wait two seconds
        return "OpenAI key is not valid. Input was:\n\n" + generate_prompt(input_text)


def main():
    """ Build Streamlit app """

    st.header("LLM-based application template with Streamlit")
    st.subheader("Information extraction system from job descriptions")

    with open('sample_job_description.txt', 'r') as f:
        sample_job_description = f.read()

    input_text = st.text_area('Enter job description', height=500, value=sample_job_description)
    if st.button('Extract information', use_container_width=True):
        with st.spinner('In progress...'):
            # replace with 'ask_chatgpt' if you have configured your key
            model_output = toy_ask_chatgpt(input_text)

        with st.expander("Input prompt", expanded=False):
            st.text(generate_prompt(input_text))

        st.subheader("Full model output")
        try:
            model_output = json.loads(model_output)
            st.json(model_output)
        except json.JSONDecodeError:
            st.text(model_output)


if __name__ == "__main__":
    main()
