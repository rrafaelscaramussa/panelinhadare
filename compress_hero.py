import sys
try:
    from moviepy import VideoFileClip
except ImportError:
    print("Error: Could not import moviepy.")
    sys.exit(1)

def compress_video():
    input_file = "hero.mp4"
    output_file = "hero_light.mp4"
    
    print(f"Compressing {input_file}...")
    
    try:
        # Load video
        clip = VideoFileClip(input_file)
        
        # Strip audio (reduces size)
        clip = clip.without_audio()
        
        # Resize to 480p width to make it super light
        # Since it's behind a dark gradient overlay, blurriness won't be noticeable
        clip_resized = clip.resize(width=640)
        
        # Lower frame rate if it's very high (e.g. drop from 60 to 24)
        clip_resized = clip_resized.set_fps(24)
        
        # Write out with low bitrate
        clip_resized.write_videofile(
            output_file, 
            codec="libx264", 
            bitrate="400k", 
            preset="ultrafast",
            logger=None
        )
        print("Compression finished successfully!")
        
    except Exception as e:
        print(f"Failed to process video: {e}")

if __name__ == "__main__":
    compress_video()
