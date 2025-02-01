from openai import OpenAI
import os
from src.Services.OpenAIIntegrations.OpenAIAdapter import parseJson


client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY")
)


def OpenAIGetArticlePredecessors(content, depth=0):
    if depth > 5:
        return None

    response = (client.chat.completions.create(
        model="o3-mini",
        messages=[
            {"role": "system",
             "content": "Your goal is to respond with information in a Json format. You will be provided"
                        "with information in the format: "

                        "{title:'...',"
                        "content:'...',"
                        "publish_date:'...'"
                        "}. '"

                        "You must then respond with a Json of the format: "

                        "{"
                        "predecessors: [Tuple(String, Int)] "
                        "}. "
                        "predecessors must be a list of tuples each of which contains a string and an int: "
                        "the strings should be names of important events that preceded and in some way "
                        "caused the event on which the content sent is about. For example, 'Austro'Hungary's "
                        "declaration of War in 1914' may have predecessors 'Assasination of Franz Ferdinand' "
                        "and 'The July Crisis'. Crucially, try to keep predecessors one logical level of implication "
                        "backwards, rather than several. So for example, 'Battle of the Somme' may not have 'Assasination "
                        "of Franz Ferdinand' as a predecessor, but it may be linked maybe 5-6 levels back. "
                        "Significance should be an integer scale quantifying approximately how much sigificance "
                        "a particular predecessor had on a predecessor. "

             },
            {"role": "user", "content": str(content)}
        ]
    ))

    try:
        ret = parseJson(response.choices[0].message.content)["predecessors"]
    except:
        return OpenAIGetArticlePredecessors(content, depth + 1)

    return ret


def OpenAIGetArticleSucessors(content, depth=0):
    if depth > 5:
        return None


    response = (client.chat.completions.create(
        model="o3-mini",
        messages=[
            {"role": "system",
             "content": "Your goal is to respond with information in a Json format. You will be provided "
                        "with information in the format: "

                        "{title:'...',"
                        "content:'...',"
                        "publish_date:'...'"
                        "}. '"

                        "You must then respond with a Json of the format: "

                        "{"
                        "sucessors: [Tuple(String, Int)] "
                        "}. "
                        "sucessors must be a list of tuples each of which contains a string and an int:"
                        "The strings should be names of important events that suceeded and in some way were "
                        "directly caused by the given event. If there exist no such sucessors (ie if the event "
                        "is too recent), then just return sucessors as an empty list. For example, Japan leaving "
                        "the League of Nations was a direct sucessor to the Manchurian Crisis."

             },
            {"role": "user", "content": str(content)}
        ]
    ))

    try:
        ret = parseJson(response.choices[0].message.content)["sucessors"]
    except:
        return OpenAIGetArticlePredecessors(content, depth + 1)

    return ret