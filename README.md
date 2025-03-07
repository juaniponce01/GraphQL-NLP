#Python Code Challenge - GraphQL & NLP

## Programming Challenge for Back End position

We require the development of an API with 2 services and 3 endpoints (optionally 4):

## Data Service

The Data service shall connect to a CSV file that can be downloaded from the following link:

[Data example - Python Coding Challenge - GraphQL.csv](https://prod-files-secure.s3.us-west-2.amazonaws.com/8bdb40ef-cc0d-4853-862c-95ff2b4790ca/b82763a3-3ac0-4c8a-99bb-d763c0b00b54/Data_example_-_Python_Coding_Challenge_-_GraphQL.csv)

### GraphQL endpoint

An endpoint shall offer access to the data in the CSV file using GraphQL. This endpoint shall have the proper schema.

This endpoint shall be fully developed and properly documented.

### NLP endpoint

An endpoint shall offer the option to query the data in the CSV file using natural language and respond in the same manner.

## Docs Service

This endpoint shall offer a swagger service documenting these 3 endpoints in Swagger 2.0 or OpenAPI 3.0.

Swagger shall include examples.

## Optional Auth Service

An optional service shall implement the oAuth 2.0 client credentials flow and return a JWT.

If the Auth service is implemented, the JWT shall be required as a bearer token in the an Authorization header for the Data Service endpoints

## General guidelines

- We require the code to be implemented in docker.
- We require the code to be hosted in a public git repository at Github, Gitlab or other similar service, with real usage of the repo, with commits as the development process takes place, not just a final commit.
- We require the repo to have a Readme file explaining how to compile and launch the service.
- We accept the use of AI tools such as ChatGPT, Gemini or Perplexity as long as the chats are provided as shared links or printed PDFs.
