# CFA API

The CFA API (*Customer Feedback Analysis API*) is a small platform for submitting and analyzing customer feedback. This project is intended to be **a demo**; the focus is on the platform structure and code quality, while the analytic tools are simple stubs.

## Description

The CFA API allows users to submit product reviews through API requests, which are stored internally as database records. The platform also offers a selection of tools for analyzing the submitted feedback and these tools can be accessed via API requests as well.

## API Endpoints

The platform exposes a few API endpoints to allow interaction. Specifically:

 - *(post)* `/v1/feedbacks` to submit a new feedback (request body: [Feedback](cfa_api/schemas/feedback.py));
 - *(get)* `/v1/feedbacks/ratings/average/{product_id}` to get product average ratings;
 - *(get)* `/v1/feedbacks/comments/keywords/{product_id}` to extract keywords from the comments related to a specific product.

 Please refer to the FastAPI-generated documentation for a comprehensive description of these endpoints. [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

 ## Deployment

 I suggest running this platform with Docker. Usage is facilitated by a Makefile:

  - `make build` to build the Docker image;
  - `make test` to run the unit tests;
  - `make run` to spin up a Docker container.
