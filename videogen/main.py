import os
import re
import requests
import shutil
from gtts import gTTS
from moviepy import (
    VideoFileClip, AudioFileClip, concatenate_videoclips, ImageClip, vfx
)
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk import pos_tag
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Clear NLTK data cache (Windows-compatible path)
nltk_data_path = os.path.expanduser('~/nltk_data')
shutil.rmtree(nltk_data_path, ignore_errors=True)

# Download required NLTK resources
nltk.download('punkt_tab', quiet=True)
nltk.download('averaged_perceptron_tagger', quiet=True)
nltk.download('averaged_perceptron_tagger_eng', quiet=True)
nltk.download('stopwords', quiet=True)

API_KEY = "REDACTED"
DOWNLOAD_FOLDER = os.path.join(os.getcwd(), "pixabay_downloads")
os.makedirs(DOWNLOAD_FOLDER, exist_ok=True)

TARGET_RESOLUTION = (1920, 1080)
TARGET_FPS = 24
CLIP_DURATION = 6  # seconds for image-based clips

def simple_phrase_tokenize(text):
    phrases = re.split(r'(?<=[.!?,;])\s+', text.strip())
    return [p.strip() for p in phrases if p.strip() and len(p.strip()) >= 3]

stop_words = set(stopwords.words('english'))

def extract_keywords_per_phrase_nouns(phrases):
    keywords = []
    for phrase in phrases:
        words = word_tokenize(phrase)
        pos_tags = pos_tag(words)
        nouns = [word for word, pos in pos_tags if pos.startswith('NN') and word.lower() not in stop_words and word.isalpha()]
        if nouns:
            keyword = max(nouns, key=len).lower()
        else:
            filtered_words = [w.lower() for w in words if w.lower() not in stop_words and w.isalpha()]
            if filtered_words:
                keyword = max(filtered_words, key=len)
            else:
                keyword = "nature"
        keywords.append(keyword)
    return keywords

def download_pixabay_video(keyword, quality='medium'):
    url = f"https://pixabay.com/api/videos/?key={API_KEY}&q={keyword}&per_page=3"
    try:
        resp = requests.get(url)
        resp.raise_for_status()
        data = resp.json()
    except Exception as e:
        logging.error(f"Failed to decode JSON response for keyword '{keyword}': {e}")
        return None
    
    if 'hits' not in data or not data['hits']:
        logging.warning(f"No video found for keyword: {keyword}")
        return None
    
    video_info = data['hits'][0]['videos']
    if quality not in video_info:
        logging.warning(f"Requested quality '{quality}' not found. Using 'medium'.")
        quality = 'medium'
    
    video_url = video_info[quality]['url']
    video_id = data['hits'][0]['id']
    file_path = os.path.join(DOWNLOAD_FOLDER, f"{keyword}_{video_id}_{quality}.mp4")

    if not os.path.exists(file_path):
        logging.info(f"Downloading {quality} quality video for keyword: {keyword}")
        try:
            vid_data = requests.get(video_url).content
            with open(file_path, 'wb') as f:
                f.write(vid_data)
            # Verify file integrity
            temp_clip = VideoFileClip(file_path)
            logging.info(f"Verified video file: {file_path}, duration={temp_clip.duration:.2f}s")
            temp_clip.close()
        except Exception as e:
            logging.error(f"Invalid video file {file_path}: {e}. Deleting.")
            if os.path.exists(file_path):
                os.remove(file_path)
            return None
    else:
        logging.info(f"Video already downloaded for keyword: {keyword} ({quality})")
    return file_path

def download_pixabay_image(keyword):
    url = f"https://pixabay.com/api/?key={API_KEY}&q={keyword}&image_type=photo&per_page=3"
    try:
        resp = requests.get(url)
        resp.raise_for_status()
        data = resp.json()
    except Exception as e:
        logging.error(f"Failed to decode JSON response for image keyword '{keyword}': {e}")
        return None
    
    if 'hits' not in data or not data['hits']:
        logging.warning(f"No image found for keyword: {keyword}")
        return None
    
    img_url = data['hits'][0]['largeImageURL']
    img_id = data['hits'][0]['id']
    file_path = os.path.join(DOWNLOAD_FOLDER, f"{keyword}_{img_id}.jpg")

    if not os.path.exists(file_path):
        logging.info(f"Downloading image for keyword: {keyword}")
        try:
            img_data = requests.get(img_url).content
            with open(file_path, 'wb') as f:
                f.write(img_data)
        except Exception as e:
            logging.error(f"Error downloading image for '{keyword}': {e}")
            return None
    else:
        logging.info(f"Image already downloaded for keyword: {keyword}")
    return file_path

def text_to_audio(text, filename):
    try:
        tts = gTTS(text=text, lang='en', slow=False)
        tts.save(filename)
        logging.info(f"Generated audio: {filename}")
        return filename
    except Exception as e:
        logging.error(f"Error generating audio for text '{text}': {e}")
        return None

def create_image_clip_with_zoom(image_path, duration=CLIP_DURATION):
    try:
        clip = ImageClip(image_path).resize(TARGET_RESOLUTION)
        zoomed = clip.fx(vfx.zoom_in, final_scale=1.1, duration=duration)
        zoomed = zoomed.set_duration(duration).set_fps(TARGET_FPS)
        return zoomed
    except Exception as e:
        logging.error(f"Error creating image clip from {image_path}: {e}")
        return None

def process_clip(video_path, audio_path, output_path):
    try:
        video = VideoFileClip(video_path)
        audio = AudioFileClip(audio_path)
        video_duration = video.duration
        audio_duration = audio.duration
        logging.info(f"Processing clip: video_duration={video_duration:.2f}s, audio_duration={audio_duration:.2f}s")

        if video_duration <= 0 or audio_duration <= 0:
            logging.error(f"Invalid duration: video={video_duration}, audio={audio_duration}. Skipping.")
            video.close()
            audio.close()
            return None

        MIN_SPEED_FACTOR = 0.5
        if video_duration < audio_duration:
            speed_factor = max(video_duration / audio_duration, MIN_SPEED_FACTOR)
            logging.info(f"Slowing video by factor {speed_factor:.2f} to match audio.")
            video = video.fx(vfx.speedx, factor=speed_factor)
            video_duration = video.duration

        duration = min(video_duration, audio_duration) - 0.1
        if duration <= 0:
            duration = min(video_duration, audio_duration)

        # Use set_duration instead of subclip
        trimmed_video = video.set_duration(duration)
        trimmed_audio = audio.set_duration(duration)
        trimmed_video = trimmed_video.resize(newsize=TARGET_RESOLUTION)
        final_clip = trimmed_video.set_audio(trimmed_audio).set_fps(TARGET_FPS)

        final_clip.write_videofile(
            output_path,
            codec='libx264',
            audio_codec='aac',
            temp_audiofile='temp-audio.m4a',
            remove_temp=True,
            fps=TARGET_FPS,
            preset='medium',
            threads=4,
            verbose=False,
            logger=None
        )

        video.close()
        audio.close()
        trimmed_video.close()
        trimmed_audio.close()
        final_clip.close()
        logging.info(f"Generated clip: {output_path}")
        return output_path
    except Exception as e:
        logging.error(f"Error processing clip {video_path}: {e}")
        for clip in [locals().get('video'), locals().get('audio'), locals().get('trimmed_video'), locals().get('trimmed_audio'), locals().get('final_clip')]:
            if clip:
                clip.close()
        return None

def create_video_from_script(script_text):
    phrases = simple_phrase_tokenize(script_text)
    logging.info(f"Detected {len(phrases)} phrases.")
    keywords = extract_keywords_per_phrase_nouns(phrases)
    logging.info(f"Extracted keywords: {keywords}")

    processed_clips = []

    for i, (phrase, keyword) in enumerate(zip(phrases, keywords)):
        logging.info(f"Processing phrase {i+1}/{len(phrases)}: '{phrase}' (keyword: {keyword})")

        video_path = download_pixabay_video(keyword)
        audio_path = os.path.join(DOWNLOAD_FOLDER, f"audio_{i}.mp3")
        if not text_to_audio(phrase, audio_path):
            logging.error(f"Failed to generate audio for phrase {i+1}, skipping.")
            continue

        output_path = os.path.join(DOWNLOAD_FOLDER, f"final_clip_{i}.mp4")

        if video_path is None:
            logging.warning(f"No video found for keyword '{keyword}', trying image.")
            image_path = download_pixabay_image(keyword)
            if image_path is None:
                logging.error(f"No image found for keyword '{keyword}', skipping phrase.")
                continue
            
            image_clip = create_image_clip_with_zoom(image_path)
            if image_clip is None:
                logging.error(f"Failed to create image clip for keyword '{keyword}', skipping.")
                continue
            audio_clip = AudioFileClip(audio_path)
            audio_duration = min(image_clip.duration, audio_clip.duration)
            audio_clip = audio_clip.set_duration(audio_duration)

            final_clip = image_clip.set_audio(audio_clip).set_fps(TARGET_FPS)
            try:
                final_clip.write_videofile(
                    output_path,
                    codec='libx264',
                    audio_codec='aac',
                    temp_audiofile='temp-audio.m4a',
                    remove_temp=True,
                    fps=TARGET_FPS,
                    preset='medium',
                    threads=4,
                    verbose=False,
                    logger=None
                )
            except Exception as e:
                logging.error(f"Error writing image-based clip {output_path}: {e}")
                image_clip.close()
                audio_clip.close()
                final_clip.close()
                continue
            image_clip.close()
            audio_clip.close()
            final_clip.close()
        else:
            if not process_clip(video_path, audio_path, output_path):
                logging.error(f"Failed to process clip for keyword '{keyword}', skipping.")
                continue

        try:
            clip = VideoFileClip(output_path).resize(TARGET_RESOLUTION)
            logging.info(f"Verified clip: {output_path}, duration={clip.duration:.2f}s")
            processed_clips.append(clip)
        except Exception as e:
            logging.error(f"Invalid clip {output_path}: {e}. Skipping.")
            continue

    if not processed_clips:
        logging.error("No clips processed. Exiting.")
        return None

    try:
        final_video = concatenate_videoclips(processed_clips, method="compose")
        final_video = final_video.resize(TARGET_RESOLUTION).set_fps(TARGET_FPS)

        final_output_path = os.path.join(os.getcwd(), "final_stitched_video.mp4")
        final_video.write_videofile(
            final_output_path,
            codec='libx264',
            audio_codec='aac',
            temp_audiofile='temp-audio.m4a',
            remove_temp=True,
            fps=TARGET_FPS,
            preset='medium',
            threads=4,
            verbose=False,
            logger=None
        )
    except Exception as e:
        logging.error(f"Error writing final video {final_output_path}: {e}")
        for clip in processed_clips:
            clip.close()
        if 'final_video' in locals():
            final_video.close()
        return None

    for clip in processed_clips:
        clip.close()
    final_video.close()

    logging.info(f"Final video saved at: {final_output_path}")
    return final_output_path

# Example YouTube script input
yt_script = """
Imagine earning money while you’re hiking through a lush forest, sipping coffee at a cozy café, or even binge-watching your favorite series, all thanks to passive income streams that AI can help you build."""

if __name__ == "__main__":
    final_video_path = create_video_from_script(yt_script)
    if final_video_path:
        logging.info(f"Video generation complete. You can find the video at: {final_video_path}")
        # Optionally open the file explorer to the video location
        import subprocess
        subprocess.run(['explorer', os.path.dirname(final_video_path)], shell=True)
    else:
        logging.error("Video generation failed.")