from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

import json

with open('./orders.json') as json_file:
    data = json.load(json_file)


@app.route("/api/orders", methods=['GET'])
def get_order_by_id():
    order_id = request.args.get("id")
    if valid_order_id(order_id) is not True:
        return jsonify({"error": f"{order_id} is incorrectly formatted"})
    return jsonify(next((order for order in data if order["id"] == order_id), {}))


def valid_order_id(order_id: str) -> bool:
    try:
        int(order_id, 16)
        return True
    except ValueError:
        return False


# url example api/currency?currency=USD
@app.route("/api/currency", methods=['GET'])
def get_order_by_currency():
    currency = request.args.get("currency")

    orders = []
    for order in data:
        if order["currency"] == currency:
            orders.append(order)
    results = orders[:3]

    return render_template("currency.html", results=results)



@app.route("/api/shipping_address", methods=['GET'])
def get_order_by_shipping_address():
    shipping_address = request.args.get("shipping_address")
    orders = []
    for order in data:
        if order["shipping_address"] == shipping_address:
            orders.append(order)
    results = orders[:3]

    return render_template("shipping_address.html", results=results)


# url example api/price?price=0.33
@app.route("/api/price", methods=['GET'])
def get_order_by_price():
    price = request.args.get("price")
    
    orders = []
    for order in data:
        if order["price"] == price:
            orders.append(order)
    results = orders[:3]

    return render_template("cost.html", results=results)


if __name__ == '__main__':
    import json
    with open('./orders.json') as json_file:
        data = json.load(json_file)

    app.run(debug=True)
