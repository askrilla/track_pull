import subprocess
import os
import yt_dlp

os.chdir(r'C:\Users\askri\Documents\Soulseek Downloads\complete\Converted')
def download_soundcloud_mp3(url, output_file=None):
    if output_file is None:
        output_file = ''
    try:
        # Call yt-dlp as a shell command
        subprocess.run([
            'yt-dlp',
            '--extract-audio',
            '--audio-format', 'best',
            '-o', '%(title)s.%(ext)s' if output_file == '' else output_file+'.%(ext)s' ,
            url
        ], check=True)
        print(f"Download complete. The MP3 file is saved")
    except subprocess.CalledProcessError as e:
        print(f"Error downloading the file: {e}")

#url = 'https://soundcloud.com/streetcornermusic/k-le-maestro-dem-boyz-lab-sounds-8219-on-scm'

#download_soundcloud_mp3(url)

if __name__ == "__main__":
    print('Enter soundcloud URL:')
    soundcloud_url = input()
    download_soundcloud_mp3(soundcloud_url, output_file=None)
