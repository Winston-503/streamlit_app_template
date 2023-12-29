# LLM-based App Template

Template for LLM-based application built with Streamlit and OpenAI API (`gpt-3.5-turbo` model).

## Article

This template was created for the [Summarising Best Practices for Prompt Engineering](https://towardsdatascience.com/summarising-best-practices-for-prompt-engineering-c5e86c483af4) article. Check it out for more details about prompt engineering techniques used to design prompts for LLMs.

## Getting started

Install `streamlit` and `openai` libraries by running `pip install -r requirements.txt`.

Configure your OpenAI key by following instructions on the [introduction to the OpenAI API page](https://platform.openai.com/docs/api-reference/introduction). See [Generating OpenAI Key article section](https://towardsdatascience.com/summarising-best-practices-for-prompt-engineering-c5e86c483af4#:~:text=Generating%20OpenAI%20Key) for more details.

## Usage

With configured OpenAI key, the app extracts job title, company name, key skills, job summary and responsibilities from the provided job description. Prompt v5 is used - zero-shot with CoT for two-step summarization, output in JSON.

Note that **without OpenAI key specified the app just waits two seconds and copies the input prompt to the output**, appending "OpenAI key is not valid" note at the start.

![](assets/app.gif)
