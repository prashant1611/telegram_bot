from datetime import  datetime

def sample_responses(input_text):
    user_message = str(input_text).lower()

    if user_message in ("hello","hi","hy"):
        return "hey! How's it going?"

    if user_message in ("who are you","who are you?"):
        return "I am Chandigrah university"

    if user_message in ("time","time?","date"):
        now = datetime.now()
        date_time = now.strftime("%d/%m/%y,  %H:%M:%S")

        return str(date_time)

    return "I don't understand you."