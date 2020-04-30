import keras
import os
import numpy as np
from keras.models import Model, load_model
import tensorflow as tf
import librosa
from sklearn.preprocessing import PowerTransformer

global emotion
emotion = {1: 'neutral', 2: 'calm', 3: 'happy', 4: 'angry', 5: 'angry', 6: 'fearful', 7: 'disgust',8: 'surprised'}

#global power transformer
global pt
pt = PowerTransformer()

# creates graph for streamining all loaded models
global graph

#import model to be used for dog detection
global voice_to_emotion_model
voice_to_emotion_model = load_model(os.path.dirname(__file__)+'/data/voice_to_speech_82%.h5')
graph = tf.get_default_graph()

def wav_to_mfcc(wav_filename, num_cepstrum):
    """ extract MFCC features from a wav file
    
    :param wav_filename: filename with .wav format
    :param num_cepstrum: number of cepstrum to return
    :return: MFCC features for wav file
    """
    sig, rate = librosa.load(wav_filename)
    
    mfcc = librosa.feature.mfcc(sig, rate, n_mfcc=num_cepstrum)
    
    append = 300-mfcc.shape[1]
    mfcc = np.pad(mfcc, [(0,0), (0,append)]).transpose()
    mfcc = pt.fit_transform(mfcc)

    return mfcc

def predict_emotion(voice_path):

    ''' Takes input as image path and return the string suitable, examples given below
    Human -  "This is image of a human. Resembling breed is - Mastiff"
    Dog - "This image is of dog breed - Mastiff"
    Neither dog nor human - "Image does not belong to dog or human"
    '''

    mfcc_features = wav_to_mfcc(voice_path, num_cepstrum=40)

    with graph.as_default():
        emotion_class = np.argmax(voice_to_emotion_model.predict(np.expand_dims(mfcc_features, axis=0)))
    
    emotion_text = 'This sound file contained ' + emotion[emotion_class] + ' voice'

    return emotion_text