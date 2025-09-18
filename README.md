# -Tugas SisTer 2025 Genap-
- Youtube: 
- Github: https://github.com/agkristiawan/-Sister-2-2025-Genap

How to do API Testing:
1. Run ```docker build -t html-api .``` to build Docker image
2. Run ```docker run -p 5000:5000 html-api``` to start the API
3. Access the API at:
- http://localhost:5000/html/10kb
- http://localhost:5000/html/100kb
- http://localhost:5000/html/1mb
- http://localhost:5000/html/5mb
- http://localhost:5000/html/10mb

How to do Locust Testing:
1. Follow previous instructions for API access
2. Set directory to ```locust-test```
3. Create a Python virtual environment and install Locust:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements-locust.txt
   ```
4. Run ```locust``` and then open http://localhost:8089

Configure the test:
   - Number of users: Start with 10–50 users to simulate concurrent requests.
   -  Spawn rate: Set to 1–5 users per second.
   -  Host: Enter http://localhost:5000

Click ```Start swarming``` to begin the test.

5. Analyze Results:
- The Locust web interface will display real-time metrics, including:
```
Requests per second (RPS)
Response times (average, median, min, max)
Failure rates (if any)
```
- Test each endpoint (/html/10kb, /html/100kb, etc.) to evaluate performance under load.
- You can adjust the number of users or test duration to simulate different scenarios.

6. Expected Deliverables:
- The Locust script tests all five endpoints with equal weight (each @task(1)).
- Metrics collected include response times and error rates for each endpoint.
- You can observe how the API handles different payload sizes under load.

## Check back for update on links and instructions
