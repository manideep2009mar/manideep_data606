import streamlit as st
import os
import librosa
import numpy as np
import tensorflow as tf  # Or any other ML library for your model
import pickle


def process_audio(uploaded_file):
    # Load audio data using librosa
    audio_data, sr = librosa.load(uploaded_file)

    # Perform any necessary preprocessing (e.g., feature extraction, scaling, etc.)
    try:
        S = librosa.feature.melspectrogram(y=audio_data, sr=sr)
        print(S.shape)
        fill = 305 - S.shape[1]
        if fill > 0:
            S = np.concatenate((S, np.zeros((128, fill))), axis=1)
        if S.shape[0] != 32:
            upsampled_rows = 128 - S.shape[0]
            upsampled_array = np.vstack((S, np.zeros((upsampled_rows, 305))))
            S = upsampled_array
    except Exception as e:
        return f"Error processing {uploaded_file} : {e} "

    # return S.shape
    current_directory = os.getcwd()

    # Get the parent directory by using os.path.dirname()
    parent_directory = os.path.dirname(current_directory)

    folder_name = "data"

    # Construct the path to the desired folder using os.path.join()
    desired_folder_path = os.path.join(parent_directory, folder_name)

    print("Current directory (parent directory):", desired_folder_path)

    os.chdir(desired_folder_path)

    # Load your pre-trained machine learning model (e.g., using TensorFlow)
    model = tf.keras.models.load_model(os.path.join("models", "model3.h5"))

    # Perform inference on the audio data
    test = np.stack(np.array([S])).astype(np.float32)

    # return test.shape
    prediction = model.predict(test)

    with open("label_encoder_mapping.pkl", "rb") as file:
        mapping = pickle.load(file)

    prediction_label = mapping[np.argmax(prediction[0])]

    if prediction_label == "hu":
        return "Hungry"
    elif prediction_label == "bu":
        return "needs burping"
    elif prediction_label == "bp":
        return "Belly pain"
    elif prediction_label == "dc":
        return "Discomfort"
    elif prediction_label == "ti":
        return "Tired"
    elif prediction_label == "ch":
        return "Cold/Hot"

    return prediction_label


def main():
    st.title("Why my kid is crying")
    uploaded_file = st.file_uploader("Upload an audio file", type=["wav", "mp3"])
    if uploaded_file is not None:
        st.audio(uploaded_file, format="audio/mp3")
        result = process_audio(uploaded_file)
        st.write("Reason:", result)


if __name__ == "__main__":
    main()
