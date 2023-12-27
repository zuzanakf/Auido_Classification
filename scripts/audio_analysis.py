#Imports
import os
import matplotlib.pyplot as plt
from pyAudioAnalysis import audioBasicIO
from pyAudioAnalysis import ShortTermFeatures, MidTermFeatures

#Functions
def short_term_feature_extraction(audio_path, output_dir):
    #Read audio file
    [Fs, x] = audioBasicIO.read_audio_file(audio_path)
    print("Sample rate (Fs):", Fs)
    print("Audio length:", len(x))
    #Extract short-term features
    F, f_names = ShortTermFeatures.feature_extraction(x, Fs, 1024, 512)
    #Plot and save the first two features
    plt.figure(figsize=(10, 6))
    plt.subplot(2, 1, 1)
    plt.plot(F[0, :])
    plt.xlabel('Frame no')
    plt.ylabel(f_names[0])

    plt.subplot(2, 1, 2)
    plt.plot(F[1, :])
    plt.xlabel('Frame no')
    plt.ylabel(f_names[1])

    plt.savefig(os.path.join(output_dir, 'short_term_features', os.path.basename(audio_path) + '_features.png'))
    plt.close()

def mid_term_feature_extraction(audio_path, output_dir):
    MidTermFeatures.mid_feature_extraction(audio_path, 1.0, 1.0, 0.050, 0.050, os.path.join(output_dir, 'mid_term_features', os.path.basename(audio_path)), True, True)

def spectrogram_extraction(audio_path, output_dir):
    ShortTermFeatures.Spectrogram(input_file=audio_path, output_file=os.path.join(output_dir, 'spectrograms', os.path.basename(audio_path) + '_spectrogram.png'))

def chromagram_extraction(audio_path, output_dir):
    ShortTermFeatures.Chromagram(input_file=audio_path, output_file=os.path.join(output_dir, 'chromagrams', os.path.basename(audio_path) + '_chromagram.png'))

#-----Looping through files-----
def process_all_files(data_dir, output_dir):
    # Create directories for storing results
    for folder in ['short_term_features', 'mid_term_features', 'spectrograms', 'chromagrams', 'beats']:
        os.makedirs(os.path.join(output_dir, folder), exist_ok=True)
    
    #Process each file
    for file in os.listdir(data_dir):
        if file.lower().endswith('.wav'):
            file_path = os.path.join(data_dir, file)
            short_term_feature_extraction(file_path, output_dir)
            mid_term_feature_extraction(file_path, output_dir)
            spectrogram_extraction(file_path, output_dir)
            chromagram_extraction(file_path, output_dir)
            print(f'Completed analysis for {file}')

#----------Calling process----------
data_directory = "data/processed"  #Directory containing audio files
output_directory = "results/analysis"  #Directory for storing results
process_all_files(data_directory, output_directory)
