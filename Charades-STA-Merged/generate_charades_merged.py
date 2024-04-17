import pandas as pd
import numpy as np
import os
import math
from tqdm import tqdm
import argparse
import ffmpeg
import shutil

# Create the parser
parser = argparse.ArgumentParser()
# Add an argument
parser.add_argument('--input_video_dir', type=str, required=True, help="Dir with Charades Dataset Videos")
parser.add_argument('--output_dir', type=str, required=True, help="Dir where you want to save ")
parser.add_argument('--train_csv_path', type=str, required=True)
parser.add_argument('--test_csv_path', type=str, required=True)
# Parse the argument
args = parser.parse_args()
# Print "Hello" + the user input argument
print("-------------------------------------------------------------")
print("Creating Charades-STA-Merged Dataset Videos")
print("input_dir:", args.input_video_dir)
print("output_dir:", args.output_dir)
print("train_csv_path:", args.train_csv_path)
print("test_csv_path:", args.test_csv_path)

CHARADES_DATASET_DIR = args.input_video_dir
OUTPUT_DIR = args.output_dir
TEMP_FILE_PATH = "temp_file_list_storage.txt"  # A temp txt file to store the names of videos to be merged
# Read the dataset and make a video merge list
df_test = pd.read_csv(args.test_csv_path)
df_train = pd.read_csv(args.train_csv_path)
video_merge_list = list({tuple(id_list.split("_")) for id_list in df_test['id']}) + list({tuple(id_list.split("_")) for id_list in df_train['id']})

# 1) Make sure OUTPUT_DIR is empty (otherwise ffmeg-python will hang on the replace question)
if len(os.listdir(OUTPUT_DIR)) >= 1:
    raise Exception("Output directory must be empty !!!!")

print("Merging Videos")
copy_list_ids = []  # To store all the unmerged videos that will be copied later
joining_error_list = []  # To store all the videos that couldn't be merged due to errors
for id_list in tqdm(video_merge_list):
    # 2) Filter out unmerged videos
    if len(id_list) < 2:
        copy_list_ids.append(id_list[0])
        continue
    # 3) Create file path list
    file_path_list = [os.path.join(CHARADES_DATASET_DIR, f"{el}.mp4") for el in id_list]
    # 4) Create temp txt file to store file_path_list
    with open(TEMP_FILE_PATH, 'w') as f:
        for el in file_path_list:
            print(f"file {el}", file=f)
    # 5) Generate output_path
    output_path = os.path.join(OUTPUT_DIR, f"{'_'.join(id_list)}.mp4")
    # 6) Ask ffmpeg to merge the videos
    try:
        ffmpeg.input("temp_file_list_storage.txt",
             format='concat', safe=0).output(output_path, c='copy', loglevel="quiet").run()
    except:
        joining_error_list.append(id_list)
        continue

# 7) Copy Unmerged videos to new dir
print("Copying unmerged videos to output_dir")
for vid_id in tqdm(copy_list_ids):
    src = os.path.join(CHARADES_DATASET_DIR, f"{vid_id}.mp4")
    shutil.copy(src=src, dst=OUTPUT_DIR)  
    
print("Done!\n-------------------------------------------------------------")# '''