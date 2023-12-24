#Imports
import os
import matplotlib.pyplot as plt
from pyAudioAnalysis import audioBasicIO
from pyAudioAnalysis import ShortTermFeatures, MidTermFeatures
from pyAudioAnalysis import audioAnalysis

#Functions
def short_term_feature_extraction(audio_path, output_dir):
    #Read audio file
    [Fs, x] = audioBasicIO.read_audio_file(audio_path)
    #Extract short-term features
    F, f_names = ShortTermFeatures.feature_extraction(x, Fs, 0.050*Fs, 0.025*Fs)
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
    MidTermFeatures.mid_feature_extraction_to_file(audio_path, 1.0, 1.0, 0.050, 0.050, os.path.join(output_dir, 'mid_term_features', os.path.basename(audio_path)), True, True)

def spectrogram_extraction(audio_path, output_dir):
    audioAnalysis.fileSpectrogramWrapper(input_file=audio_path, output_file=os.path.join(output_dir, 'spectrograms', os.path.basename(audio_path) + '_spectrogram.png'))

def chromagram_extraction(audio_path, output_dir):
    audioAnalysis.fileChromagramWrapper(input_file=audio_path, output_file=os.path.join(output_dir, 'chromagrams', os.path.basename(audio_path) + '_chromagram.png'))

def beat_extraction(audio_path, output_dir):
    [Fs, x] = audioBasicIO.read_audio_file(audio_path)
    F, _ = ShortTermFeatures.feature_extraction(x, Fs, 0.050*Fs, 0.025*Fs)
    beat, _ = MidTermFeatures.beat_extraction(F, 0.050)
    with open(os.path.join(output_dir, 'beats', os.path.basename(audio_path) + '_beat.txt'), 'w') as f:
        f.write(f'Beat: {beat}\n')

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
            beat_extraction(file_path, output_dir)
            print(f'Completed analysis for {file}')

#----------Calling process----------
data_directory = "data/processed"  #Directory containing audio files
output_directory = "results/analysis"  #Directory for storing results
process_all_files(data_directory, output_directory)
