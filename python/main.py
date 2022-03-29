from flask import Flask, jsonify, request

app = Flask(__name__)

import json

with open('./orders.json') as json_file:
    data = json.load(json_file)


@app.route("/api/orders", methods=['GET'])
def get_order_by_id():
    # query parameters
    order_id = request.args.get("id")
    currency = request.args.get("currency")
    shipped_to = request.args.get("shipped_to")
    cost = request.args.get("price")
    query = "{},{},{},{}".format(order_id, currency, shipped_to, cost)

    result = []
    if order_id != None:
        filterData = list(filter(lambda d: d['id'] == order_id, data))
        result.append(filterData)

    if currency != None:
        if result:
            result = list(filter(lambda d: d['currency'] == currency, result))
        else:
            result = list(filter(lambda d: d['currency'] == currency, data))

    '''
    I was unable to access the values of the nested 'shipping_address' 
    dictionary to impliment this filter correctly
    I have left where I got to in place to show my working.
    '''
    # if shipped_to != None:
    #     if result:
    #         result = list(filter(lambda d: shipped_to in d['customer']['shipping_address'], result))
    #     else:
    #         result = list(filter(lambda d: shipped_to in d['customer']['shipping_address'], data))

    if cost != None:
        if result:
            result = list(filter(lambda d: d['price'] == cost, result))
        else:
            result = list(filter(lambda d: d['price'] == cost, data))

    resultDict = {
        "results": len(result),
        "filters": query,
        "orders": result,
    }

    return jsonify(resultDict)


def valid_order_id(order_id: str) -> bool:
    try:
        int(order_id, 16)
        return True
    except ValueError:
        return False


if __name__ == '__main__':
    import json
    with open('./orders.json') as json_file:
        data = json.load(json_file)

    app.run(debug=True)
