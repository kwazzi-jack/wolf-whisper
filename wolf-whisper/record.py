import whisper
import wolframalpha
  
app_id = "3TQPXY-QVA8XE5WRR"
client = wolframalpha.Client(app_id)
# model = whisper.load_model("base")
# result = model.transcribe("output.wav")
# print(f"Detected: {result['text']}")
res = client.query(input=f'integral of x squared', params=(("format", "minput"),))
# answer = next(res.results).text
answer = res
print("Result:", answer)