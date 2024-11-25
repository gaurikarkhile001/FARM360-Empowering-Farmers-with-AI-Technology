from flask import Flask, render_template, request, jsonify
import joblib
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import os

app = Flask(__name__)

# Load models and scalers
crop_model = joblib.load('random_forest_model.pkl')
crop_scaler = joblib.load('scaler.pkl')
plant_disease_model = load_model('plant_disease_model.h5')

# Class labels for the plant disease model
plant_disease_labels = ['Healthy', 'Common Rust', 'Blight', 'Gray Leaf Spot']

# Utility functions
def preprocess_crop_data(data):
    """Preprocess crop recommendation features."""
    features = [
        data['N'],
        data['P'],
        data['K'],
        data['temperature'],
        data['ph'],
        data['rainfall']
    ]
    features_array = np.array([features])
    features_scaled = crop_scaler.transform(features_array)
    return features_scaled

def load_and_preprocess_image(img_path, target_size=(224, 224)):
    """Preprocess plant disease image."""
    img = image.load_img(img_path, target_size=target_size)
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension
    img_array /= 255.0  # Normalize to [0, 1]
    return img_array

def predict_plant_disease(img_path):
    """Predict plant disease from an image."""
    img_array = load_and_preprocess_image(img_path)
    predictions = plant_disease_model.predict(img_array)
    predicted_class_index = np.argmax(predictions, axis=1)[0]
    return plant_disease_labels[predicted_class_index]

# Routes for the combined application
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/crop_recommendation')
def crop_recommendation():
    return render_template('crop_recommendation.html')

@app.route('/market_price')
def market_price():
    return render_template('market_price.html')

@app.route('/disease_prediction')
def disease_prediction():
    return render_template('disease_prediction.html')

@app.route('/suggest_fertilizers')
def suggest_fertilizers():
    return render_template('suggest_fertilizers.html')

@app.route('/disease_info')
def disease_info():
    return render_template('disease_info.html')

@app.route('/fertilizers')
def fertilizers():
    return render_template('fertilizers.html')

@app.route('/blogs')
def blogs():
    return render_template('blogs.html')

@app.route('/contact_us')
def contact_us():
    return render_template('contact_us.html')

@app.route('/predict', methods=['POST'])
def predict_crop():
    data = request.get_json()
    features_scaled = preprocess_crop_data(data)
    prediction = crop_model.predict(features_scaled)
    return jsonify({'crop': prediction[0]})


@app.route('/predict_plant_disease', methods=['POST'])
def predict_plant_disease_route():
    if 'file' not in request.files:
        print("No file uploaded!")
        return jsonify({'error': 'No file uploaded!'}), 400

    file = request.files['file']
    
    if file.filename == '':
        print("No file selected!")
        return jsonify({'error': 'No selected file!'}), 400

    print(f"File uploaded: {file.filename}")

    # Save the file to the uploads folder
    filepath = os.path.join('uploads', file.filename)
    file.save(filepath)

    # Predict the disease
    prediction = predict_plant_disease(filepath)
    print(f"Prediction: {prediction}")

    # Clean up the uploaded file
    os.remove(filepath)

    return jsonify({'prediction': prediction})


if __name__ == '__main__':
    # Ensure the uploads directory exists
    if not os.path.exists('uploads'):
        os.makedirs('uploads')

    app.run(debug=True)
