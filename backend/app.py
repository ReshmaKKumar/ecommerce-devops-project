from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)

CORS(app)

products = [

    {
        "id": 1,
        "name": "iPhone",
        "price": "₹70,000",
        "category": "Electronics",
        "rating": 4.8,
        "image": "https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?q=80&w=1000"
    },

    {
        "id": 2,
        "name": "Headphones",
        "price": "₹3,000",
        "category": "Accessories",
        "rating": 4.3,
        "image": "https://images.unsplash.com/photo-1505740420928-5e560c06d30e?q=80&w=1000"
    },

    {
        "id": 3,
        "name": "Camera",
        "price": "₹45,000",
        "category": "Electronics",
        "rating": 4.6,
        "image": "https://images.unsplash.com/photo-1526170375885-4d8ecf77b99f?q=80&w=1000"
    },

    {
        "id": 4,
        "name": "Shoes",
        "price": "₹4,000",
        "category": "Fashion",
        "rating": 4.1,
        "image": "https://images.unsplash.com/photo-1542291026-7eec264c27ff?q=80&w=1000"
    }

]

@app.route('/')

def home():

    return "Amazon Clone Backend Running"


@app.route('/products')

def get_products():

    return jsonify(products)


if __name__ == '__main__':

    app.run(
        host='0.0.0.0',
        port=5000,
        debug=True
    )