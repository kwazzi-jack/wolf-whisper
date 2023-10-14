import wolframalpha

app_id = "3TQPXY-QVA8XE5WRR"
client = wolframalpha.Client(app_id)

try:
    # Forming the query
    res = client.query('integral of x squared', format='minput')
    
    # Extracting the result
    answer = next(res.results).text
    print("Result:", answer)

except wolframalpha.WolframAlphaException as e:
    print(f"Wolfram Alpha Exception: {e}")

except StopIteration:
    print("No results found")

except Exception as e:
    print(f"An unexpected error occurred: {e}")

