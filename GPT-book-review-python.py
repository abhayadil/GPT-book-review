#You will need to install the openai module
import openai

#You will need an api key from openai to run this code
openai.api_key = "<insert your openai api key here>"
#Note: api keys are chargable and you need to get it from openai

print("\n\nStarting GPT 3.5!\n\n")

def get_completion(prompt, model = "gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model = model,
        messages = messages,
        temperature = 0.3,
    )
    return response.choices[0].message["content"]

#If you want to give a diiferent name to the file that is being read, change it here
inputer = open("inserthere.txt", encoding="utf8", mode="r")

text = inputer.read()

#This is the prompt that is being feed to the GPT model
prompt = f"""I want you to act as a book critic and expert in the subject of literature, \
You are working with one of the top book reviewing magazine. \
Criticize and review the content of the book, the content of the book is delimited by triple backticks. \
Your review should be at least 10 paragraph long explaining in vivid details your thoughts along with at least 3 good and 3 bad things about the book. \
Also mention the names of every character in the book. \
Provide your response in HTML format that displays a well structured and colorful web page \
use an appealing and creative style to make the webpage very appealing and vibrant with some elements of personality. \
Feel free to utilize any HTML and CSS elements to make the result more appealing.\
``` {text}``` """

response = get_completion(prompt)

#If you want the name of the resulting file to be different than change it here, keep it in .html format
outputer = open("response-gpt.html", "w")

outputer.write(response)

inputer.close()

outputer.close()

print("\nResult is processed and saved in an html file\n")
