from openai import OpenAI
from src.KEYS import OPENAI_API_KEY

client = OpenAI(
    api_key=OPENAI_API_KEY
)


def OpenAIGetArticlePredecessors(content):
    response = (client.chat.completions.create(
        model="o3-mini",
        messages=[
            {"role": "system",
             "content": "Your goal is to respond with information in a Json format. You will be provided"
                        "with information in the format: "

                        "'{title:'...',"
                        "content:'...',"
                        "publish_date:'...'"
                        "}. '"

                        "You must then respond with a Json of the format: "

                        "{event_timeline: Tuple(DateTime, DateTime), "
                        "predecessors: [Tuple(String, Int)], "
                        "broad_category: String"
                        "}. "

                        "To explain each: "

                        "event_timeline must be a message of the format 15-12-2001:01-03-2002, stating the"
                        "approximate start and end times of the event (not the article!) - if the event is still ongoing, "
                        "write something like 15-12-2001:Present. "

                        "predecessors must be a list of tuples each of which contains a string and an int:"
                        "the strings should be names of important events that preceded and in some way"
                        "caused the event on which the content sent is about. For example, 'Austro'Hungary's"
                        "declaration of War in 1914' may have predecessors 'Assasination of Franz Ferdinand'"
                        "and 'The July Crisis'. Crucially, try to keep predecessors one logical level of implication"
                        "backwards, rather than several. So for example, 'Battle of the Somme' may not have 'Assasination"
                        "of Franz Ferdinand' as a predecessor, but it may be linked maybe 5-6 levels back."
                        "Significance should be an integer scale quantifying approximately how much sigificance"
                        "a particular predecessor had on a predecessor. "

                        "broad_category should be a string describing the overarching historical event which"
                        "the particular articls is about. For example, 'Assasination of Franz Ferdinand'"
                        "may be in 'World War 1', 'Plane hits twin towers' may be 'War on Terrorism',"
                        "'US lands ship on moon' could be in 'Space Race'. Note, these are just"
                        "examples - if there are more suitable titles or overarching events, use them instead."

             },
            {"role": "user", "content": content}
        ]
    ))

    return response.choices[0].message.content