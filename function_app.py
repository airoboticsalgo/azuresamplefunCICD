import azure.functions as func
import logging

app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)

@app.route(route="balafuncicd1")
def balafuncicd1(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    logging.debug("corent20......")
    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name:
        return func.HttpResponse(f"Hello12, {name}. This HTTP triggered function executed successfully.")
    else:
        logging.info("corent21.....info.")
        logging.error("corent22.....errpr.")
        return func.HttpResponse(
         
             "Good day executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )