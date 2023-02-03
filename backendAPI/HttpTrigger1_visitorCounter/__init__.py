import logging
import json
import azure.functions as func


def main(req: func.HttpRequest, inputDocument: func.DocumentList, outputDocument: func.Out[func.Document]) -> func.HttpResponse:

    logging.info('Python HTTP trigger function processed a request.')

    # Create/Initalize counter document object
    counter = func.Document

    # Point counter document object to the incoming DB object
    counter = inputDocument[0]

    # Increment the DB object count field by 1
    counter['count'] += 1

    # Parse the counter data to JSON
    jsonReturn = json.dumps(counter.data)

    # Logging the return data
    logging.info("UPDATE DATA JSON: %s", jsonReturn)

    # Write to DB. We use the outputDocument db object and set it to the incremented inputDocument object
    outputDocument.set(counter)

    # Return visitorCount
    return func.HttpResponse(body=jsonReturn, status_code=200, headers={'content-type': 'application/json', 'charset': 'utf-8'})
