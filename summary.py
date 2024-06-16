import anthropic
import json

client = anthropic.Client(
    api_key="api-key-here")
def claudeApiCall(transcript, system):
    return client.messages.create(
        model="claude-2.1",
        max_tokens=1024,
        temperature=0.3,
        # <-- system prompt
        system=system,
        messages=[
            # <-- user prompt
            {"role": "user", "content": transcript}
        ]
    )

def summaryAndKeyword(transcript):
    summary_system = "Assume you are a summariser bot who needs to summarise whatever the user gives in the same language your recieve it in. Note you should not give any heading to the response"
    keywords_system = "Assume your are a bot who needs to give 5 keywords in json format for the text provided by the user. Note: no heading is neccesary you just need to write the keywords in hindi"
    summary = claudeApiCall(transcript, summary_system)
    keywords = claudeApiCall(transcript,keywords_system)
    summary = summary.json()
    # conver this res into json
    summary = json.loads(summary)['content'][0]['text']
    keywords = keywords.json()
    # conver this res into json
    keywords = json.loads(keywords)
    keywords = json.loads(keywords['content'][0]['text'])['keywords']
    return {
        "summary": summary,
        "keywords": keywords
    }