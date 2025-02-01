from OpenAIQueryService import OpenAIGetArticlePredecessors
from OpenAIAdapter import parseJson

def query(event_json):
    jsonData = OpenAIGetArticlePredecessors(event_json)
    queryResults = parseJson(jsonData)
    return queryResults


def main():
    event_json = {"title": 'Putin declares war on Ukraine',
                  "content": 'Since the invasion began on 24 February 2022, the Russian government and media outlets have consistently used the term “special military operation” to refer to the attacks on its neighbour’s territory. Russia made extensive efforts to refrain from labelling the military conflict in Ukraine a war.',
                  "publish_date":'03-04-2024'}

    print(query(str(event_json)))

if __name__ == '__main__':
    main()
