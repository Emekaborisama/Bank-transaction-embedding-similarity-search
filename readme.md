
# Deployment 
To deploy this application, create an instance on an cloud provider of your choice, install docker, clone or copy the repo to the instance then build and run the image.

PS: Ensure your networking configuration is suitable for e.g allow port 8080 for inbound.

## Build container 

```bash 
docker build -t my_fastapi_app .
```


## Run the Container:


```bash
docker run -p 8000:8000 -e PINECONE_INDEX_NAME=deel-demo -e EMBED_MODEL=text-embedding-3-small -e OPEN_API_KEY=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 -e PINECONE_API_KEY=14921cd0-631f-47bb-b841-7e08f158752d --rm my_fastapi_app


```


# Improvement 


- Efficient Algorithms: Optimize algorithms for vectorization and similarity calculation to handle large datasets efficiently.

- Batch Processing: Implement batch processing for handling multiple requests simultaneously to improve response time and resource utilization.

- Caching: Introduce caching mechanisms to store precomputed embeddings and similarity scores for frequently queried transactions, reducing computation overhead.

- Logging: Implement comprehensive logging across the application to track user activities, errors, and performance metrics for troubleshooting and auditing purposes.

- Monitoring: Set up monitoring tools like Prometheus and Grafana to monitor application health, performance metrics, and resource utilization in real-time, enabling proactive detection and resolution of issues.

- Unit and Integration Testing: Write unit tests to validate individual components and integration tests to verify end-to-end functionality, ensuring reliability and stability of the application.
Deployment and Continuous Integration/Continuous Deployment (CI/CD):

- CI/CD Pipeline: Set up a CI/CD pipeline using tools like Jenkins or GitLab CI/CD to automate the build, test, and deployment process, ensuring faster delivery of updates and improvements.

- Deployment Strategies: Implement deployment strategies like blue-green deployment or canary deployment to minimize downtime and risk during updates.