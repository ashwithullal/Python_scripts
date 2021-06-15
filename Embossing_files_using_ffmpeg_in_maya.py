import os

file_path_01 = "D:\\Sequence1\\play_blast_01.mov"
file_path_02 = "D:\\Sequence1\\play_blast_02.mov"

output = "D:\\Sequence1\\output.mov"
#output.mov will output 2 playblast in a single file  to look for any diffrences
os.system("T:/FFMpeg/bin/ffmpeg.exe -i {0} -i {1} -filter_complex \"concat = n = 2:v = 1: a = 1\" -f MOV -y {2}".format(file_path_01,file_path_02,output))