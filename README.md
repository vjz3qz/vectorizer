# Vectorizer
## Objective:
Convert natural language queries and documents to numerical vectors.

## Functional Requirements:
### Input:

- Accept natural language text as input, which can be either a user query or raw text from documents.
- Should handle varying lengths of text.
### Processing:

- Tokenize the input text to break it down into words or smaller units.
- Vectorize the tokenized text using a suitable method (like TF-IDF, Word2Vec, etc.).
- Handle errors and exceptions gracefully, such as invalid input formats or empty strings.
### Output:

- Return the generated vector representation of the input text.
- Should return errors and statuses properly, indicating whether the operation was - successful or not and why.
Security:

Should only accept inputs and interactions from authorized services or users.
Should sanitize inputs to prevent injection attacks.

### Development Plan
- [x] Setup the project repository and development environment.
- [x] Develop the initial structure of the microservice, defining main components and interactions.
- [x] Implement the tokenization logic.
- [x] Implement the vectorization logic using a suitable method (like TF-IDF, Word2Vec).
- [ ] Develop error handling and input sanitization logic.
- [ ] Unit test the tokenization and vectorization logic.
- [ ] Optimize the microservice for performance and throughput.
- [ ] Develop integration tests and perform extensive testing.
- [ ] Implement logging and monitoring features.
- [ ] Finalize the documentation and comments in the codebase.
- [ ] Deploy the microservice to a suitable environment.
- [ ] Perform sanity checks and final testing on the deployed instance.





