# Generalization Capacity of Natural Language Video Localisation (NLVL) Models
This is the repository containing the datasets I created during my Final Year Project at Nanyang Technological University. Please cite this work if you find it useful. It can be accessed at: [Coming Soon](https://dr.ntu.edu.sg/)

## Charades-STA-Ego Dataset
This dataset contains 302 query-video pairs labelled with start and end timestamps of the video segment that best fits the given query. All the videos in this dataset are first person videos i.e, the video is taken from the perspective of the person performing the action.   

The labeled video-query can be accessed in the `Charades-STA-Ego` directory of this repo. The csv and txt file both have the same content but the txt file is formatted to be consistant with the format of the [Charades-STA dataset](https://arxiv.org/abs/1705.02101). You can download the videos of the Charades-Ego dataset from [Ai2: Charades-Ego](https://prior.allenai.org/projects/charades-ego).  

Please note that the Charades-Ego dataset is subject to its own license whoose terms may differ from that of this repo.

## Charades-STA-Merged Dataset
This dataset is built upon the [Charades-STA dataset](https://arxiv.org/abs/1705.02101) by merging various videos together in order to reduce the distributional bias in the timestamps.  

The labeled video-query can be accessed in the `Charades-STA-Merged` directory of this repo. The csv and txt file both have the same content but the txt file is formatted to be consistant with the format of the [Charades-STA dataset](https://arxiv.org/abs/1705.02101). You can generate the merged videos by following these steps:

1) Download the the videos of the Charades Dataset from: [Ai2: Charades](https://prior.allenai.org/projects/charades)
2) Download the `charades_sta_merged_train.csv` and `charades_sta_merged_test.csv` files from the `Charades-STA-Merged` directory of this repo.
3) Install FFMPEG from https://ffmpeg.org/download.html
4) Download `requirements.txt` from this repo and run:
```
pip install -r requirements.txt
```
5) Download `generate_charades_merged.py` and then run after replacing the text in the <> with the relevant paths:
```
python generate_charades_merged.py --input_video_dir "<path-to-charades-videos>" --output_dir "<path-to-dir-to-store-merged-videos>" --train_csv_path "<path-to-charades_sta_merged_train.csv>" --test_csv_path "<path-to-charades_sta_merged_test.csv>"
```

You will need atleast 12 GB of available disk space for the Charades-STA-Merged Dataset. You may also require additional space to store the Charades Dataset.
