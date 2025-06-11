from openai import OpenAI
import pyttsx3
engine = pyttsx3.init()
voices = engine.getProperty('voices')
female_voice = next((v for v in voices if "female" in v.name.lower() or "zira" in v.name.lower() or "victoria" in v.name.lower() or "samantha" in v.name.lower()), voices[0])
engine.setProperty('voice', female_voice.id)
client = OpenAI(
    api_key="AIzaSyAn-M7t_iBTHjpQjKMmfpAttpA-SuUV9V0",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/")
try:
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            break
        response = client.chat.completions.create(
            model="gemini-2.5-flash-preview-04-17",
            reasoning_effort="high",
            messages=[{"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_input}])
        result = response.choices[0].message.content
        print("AI:", result)
        engine.say(result)
        engine.runAndWait()
except Exception as a:
    print(a)