from openai import OpenAI
import json

f = open("/content/api.txt", "r")

client = OpenAI(
    api_key = f.read()
)

example_json = {
  "resume": [
    {
      "name": "farhaana",
      "clg cpga": 8.6
    }
  ]
}

prompt = "Provide valid JSON output.Extract the data from the provided PDF file and structure it as JSON. Ensure that the JSON output accurately represents the key elements and sections of the document, including any text, headings, tables, lists, and other relevant information. Maintain the integrity and hierarchy of the content, using appropriate key-value pairs to organize the data."
chat_completion = client.chat.completions.create(
    model="gpt-3.5-turbo-1106",
    response_format={"type":"json_object"},
    messages=[
        {"role":"system","content":"Provide output in valid JSON. The data schema should be like this: "+json.dumps(example_json)},
        {"role":"user","content":prompt}
    ]
)

finish_reason = chat_completion.choices[0].finish_reason

if(finish_reason == "stop"):
    data = chat_completion.choices[0].message.content

    ski_resorts = json.loads(data)

    for ski_resort in ski_resorts['resume']:
        print(ski_resort['name']+" : "+str(ski_resort['clg cgpa']))
else :
    print("Error! provide more tokens please")