import uvicorn
import VoiceAssistant


from fastapi import FastAPI

app = FastAPI()

@app.post("/calls")
async def welome(resp):
    response = '''<Response>
            <Play url="/KaraBankVoice/Welcome.mp3"/>
            </Response>'''

            