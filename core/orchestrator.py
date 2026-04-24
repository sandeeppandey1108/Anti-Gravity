
from agents.research_agent import research
from agents.script_agent import generate_script
from core.tts import generate_voice
from core.video_pipeline import create_video
from core.thumbnail import create_thumbnail

def run():
    topic = research()
    script = generate_script(topic)
    audio = generate_voice(script)
    video = create_video(audio)
    thumb = create_thumbnail(topic)

    print("DONE")
    print("Video:", video)
    print("Thumbnail:", thumb)

if __name__ == "__main__":
    run()
