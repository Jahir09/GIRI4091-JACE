from flask import Flask, jsonify, request
app = Flask(__name__)
@app.route('/', methods=['GET'])
def home(): return jsonify({"Description":"Producto de JACE",
                                    "id":"1","image":"Nueva imagen", "price":"4815", "Title":"Nuevo producto de JACE"})



import requests
URL = "https://fakestoreapi.com/products"
products = requests.get(URL).json()

@app.route('/products', methods=['GET'])
def get_products():
    return jsonify(products)

def get_element(product_id):
    for product in products:
        if product["id"] == product_id:
            return product
    return None


@app.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    product = get_element(product_id)
    print(product)
    if product is None:
        return jsonify({"error": "Producto No encontrado"}), 404
    return jsonify(product)

@app.route('/products', methods=['POST'])
def create_product():
    data = request.get_json()
    product_id = max_id() + 1  
    data['id'] = product_id
    products.append(data)
    return jsonify(data), 201


def max_id():
    if not products:  
        return 0
    maximo = products[0]['id']
    for product in products:
        if product['id'] > maximo:
            maximo = product['id']
    return maximo

@app.route('/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    global products
    product_to_delete = next((product for product in products if product['id'] == product_id), None)
    if product_to_delete is None:
        return jsonify({"error": "Producto no encontrado"}), 404
    products = [product for product in products if product['id'] != product_id]
    return jsonify({"message": "Producto eliminado exitosamente"}), 200

@app.route('/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    product = get_element(product_id)
    if product is None:
        return jsonify({"error": "Producto no encontrado"}), 404
    data = request.get_json()
    for id in data:
        product[id] = data[id]
    return jsonify(product)


if __name__ == '__main__':
    app.run(port=5001, debug=True)
