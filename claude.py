import anthropic
import json

def translateText(text):

    client = anthropic.Client(api_key="api-key-here")

    response = client.messages.create(
        model="claude-2.1",
        max_tokens=1024,
        temperature=0.7,
        system="Assume that your are a translator and you have to translate the following text from English to Hindi. Just give me the traslated text nothing other than that in the response. I don't need this \"Here is the Hindi translation:\"", # <-- system prompt
        messages=[
            {"role": "user", "content": text} # <-- user prompt
        ]
    )
    res = response.json()
    res = json.loads(res)
    print("Doneeee: ")
    return str(res['content'][0]['text'])
        