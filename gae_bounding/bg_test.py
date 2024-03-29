from google.cloud import bigquery

#client = bigquery.Client()
client = bigquery.Client.from_service_account_json('keys/w241-bounding-8972281b6e70.json')

query_job = client.query("""
    SELECT
      CONCAT(
        'https://stackoverflow.com/questions/',
        CAST(id as STRING)) as url,
      view_count
    FROM `bigquery-public-data.stackoverflow.posts_questions`
    WHERE tags like '%google-bigquery%'
    ORDER BY view_count DESC
    LIMIT 10""")

results = query_job.result()  # Waits for job to complete.

for row in results:
    print("{} : {} views".format(row.url, row.view_count))