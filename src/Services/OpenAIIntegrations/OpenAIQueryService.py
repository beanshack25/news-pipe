from openai import OpenAI
import os
from src.Services.OpenAIIntegrations.OpenAIAdapter import parseJson


client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY")
)


def OpenAIGetArticlePredecessors(content, depth=0):
    if depth > 5:
        print("crying rn")
        return None

    response = (client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system",
             "content": "Your goal is to respond with a list of events. You will be provided"
                        "with information in the format: "

                        "{title:'...',"
                        "content:'...',"
                        "publish_date:'...'"
                        "}. '"

                        "You must then respond with a list in the format: "

                        "event1|event2|event3|... "
                        "the events should be ordered from oldest to newest. "
                        "the events should be names of important events that preceded and in some way "
                        "caused the event on which the content sent is about. For example, 'Trump innaugurated "
                        "as 47th president of United States' may have predecessor 'Trump beats Harris in 2024 election' "
                        ". Crucially, try to keep predecessors one logical level of implication "
                        "backwards, rather than several. So for example, 'Battle of the Somme' may not have 'Assasination "
                        "of Franz Ferdinand' as a predecessor, but it may be linked maybe 5-6 levels back. "
                        "Significance should be an integer scale quantifying approximately how much sigificance "
                        "a particular predecessor had on a predecessor. Do not include any new line characters"

             },
            {"role": "user", "content": str(content)}
        ]
    ))

    try:
        ret = response.choices[0].message.content.split("|")
    except:
        return OpenAIGetArticlePredecessors(content, depth + 1)

    return ret


def OpenAIGetArticleSucessors(content, depth=0):
    if depth > 5:
        return None


    response = (client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system",
             "content": "Your goal is to respond with information in a Json format. You will be provided "
                        "with information in the format: "

                        "{title:'...',"
                        "content:'...',"
                        "publish_date:'...'"
                        "}. '"

                        "You must then respond with a Json of the format: "

                        "event1|event2|event3|..."

                        "sucessors must be a list of strings. "
                        "The strings should be names of important events that suceeded and in some way were "
                        "directly caused by the given event. If there exist no such sucessors (ie if the event "
                        "is too recent), then just return sucessors as an empty list. For example, Japan leaving "
                        "the League of Nations was a direct sucessor to the Manchurian Crisis, and so you would "
                        "return 'japan leaves the league of nations' if the input content is 'manchurian crisis'."

             },
            {"role": "user", "content": str(content)}
        ]
    ))

    try:
        ret = parseJson(response.choices[0].message.content)["sucessors"]
    except:
        return OpenAIGetArticlePredecessors(content, depth + 1)

    return ret

def OpenAIGetFuture(content):
    response = (client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system",
             "content": "Your goal is to respond with short, concise news headlines."
                        "You will be given content from a news article and you must predict, "
                        "to the best of your ability, a future news headline that could follow "
                        "as a direct response to the headline."
                        "Do your best to make the response as rooted in world events occuring at "
                        "the time of the news article as possible."

             },
            {"role": "user", "content": str(content)}
        ]
    ))

    return response.choices[0].message.content