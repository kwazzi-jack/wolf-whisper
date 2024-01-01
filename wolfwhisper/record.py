import whisper
import wolframalpha

app_id = "3TQPXY-QVA8XE5WRR"
client = wolframalpha.Client(app_id)


def speech_to_text(audio_file):
    # Load the Whisper model and transcribe the audio
    model = whisper.load_model("base")
    result = model.transcribe(audio_file)
    return result["text"]


def text_to_math_code(text):
    # Send a query to Wolfram Alpha to get the Mathematica code
    res = client.query(text, format="moutput")
    # Extract the Mathematica code from the response
    # Assume the Mathematica code is available in the first pod's subpod
    # math_code = next(res.results).subpod["minput"]
    return res


def math_code_to_latex(math_code):
    # Placeholder for sending a request to your custom API to get the LaTeX
    # latex_response = ...  # Your logic here
    # latex = latex_response.json()['latex']
    # return latex
    pass  # Placeholder


# Example usage:
audio_file = "output.wav"

# text = speech_to_text(audio_file)
# print("WHISPER TEXT:", text)

math_code = text_to_math_code("Alpha times integral of x squared plus 2 dx.")
print(math_code)

# latex = math_code_to_latex(math_code)
# print(latex)
