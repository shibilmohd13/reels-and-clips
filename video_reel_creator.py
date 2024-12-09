import os
import subprocess

def merge_videos_with_frame_rate_fix(video1_path, video2_path, output_path):
    try:
        # Ensure both input videos exist
        if not os.path.exists(video1_path) or not os.path.exists(video2_path):
            raise FileNotFoundError("One or both input video files not found.")

        # Command to merge videos with fixed frame rate and re-encoding
        command = [
            "ffmpeg",
            "-i", video1_path,
            "-i", video2_path,
            "-filter_complex", "[0:v:0][0:a:0][1:v:0][1:a:0]concat=n=2:v=1:a=1[outv][outa]",
            "-map", "[outv]",
            "-map", "[outa]",
            "-vsync", "2",                  # Handle frame duplication
            "-r", "30",                     # Normalize frame rate to 30 fps
            "-profile:v", "high",           # Use High profile for H.264
            "-level:v", "4.1",              # Limit encoding level for compatibility
            "-preset", "medium",            # Optimize encoding speed vs. quality
            "-crf", "23",                   # Control output quality (lower = better)
            output_path
        ]

        # Run the command
        subprocess.run(command, check=True)
        print(f"Videos merged successfully into {output_path}")

    except subprocess.CalledProcessError as e:
        print(f"Error during merging: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
video1 = '/home/shibil/Downloads/coding1.mp4'
video2 = '/home/shibil/Downloads/coding3.mp4'
output = "output2.mp4"
merge_videos_with_frame_rate_fix(video1, video2, output)
