import schedule
import time
import subprocess


def job():
    try:
        subprocess.run(
            ["python3", "/Users/simoncrystal/Projects/Json experiment/backend/story1.py"],
            check=True
        )
    except subprocess.CalledProcessError as e:
        print(f"Job failed with error: {e}. Retrying in 60 seconds...")
        time.sleep(60)
        job()
    except Exception as e:
        print(f"Unexpected error: {e}. Retrying in 60 seconds...")
        time.sleep(60)
        job()

schedule.every().day.at('19:24').do(job)