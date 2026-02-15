import logging
from typing import Dict
import tensorflow as tf
from flask import Flask, request, jsonify

app = Flask(__name__)
app.config.from_object('config.Config')

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

def load_model() -> tf.keras.Model:
    """Load the TensorFlow model"""
    try:
        model = tf.keras.models.load_model(app.config['MODEL_PATH'])
        return model
    except Exception as e:
        logger.error(f"Failed to load model: {e}")
        raise

@app.route('/review', methods=['POST'])
def review_code() -> Dict:
    """Review code using the AI model"""
    try:
        data = request.get_json()
        model = load_model()
        # Call the model prediction function
        prediction = model.predict(data['code'])
        return jsonify({'review': prediction})
    except Exception as e:
        logger.error(f"Error reviewing code: {e}")
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=app.config['DEBUG'])