from flask import Flask, render_template, request, redirect, url_for, session
import stripe

app = Flask(__name__)
app.secret_key = "your_secret_key"


stripe.api_key = "sk_test_your_secret_key"
PUBLIC_KEY = "pk_test_your_public_key"


test_items = {
    1: {"name": "T-Shirt", "price": 2000},
    2: {"name": "Mug", "price": 1500},
    3: {"name": "Sticker", "price": 500},
}


@app.route("/")
def index():
    return render_template("index.html", items=test_items)


@app.route("/add_to_cart/<int:item_id>")
def add_to_cart(item_id):
    cart = session.get("cart", {})
    cart[item_id] = cart.get(item_id, 0) + 1
    session["cart"] = cart
    return redirect(url_for("index"))


@app.route("/cart")
def cart():
    cart = session.get("cart", {})
    cart_items = []
    total = 0
    for item_id, qty in cart.items():
        item = test_items[item_id]
        subtotal = item["price"] * qty
        total += subtotal
        cart_items.append(
            {"id": item_id, "name": item["name"], "qty": qty, "subtotal": subtotal})
    return render_template("cart.html", cart_items=cart_items, total=total, public_key=PUBLIC_KEY)


@app.route("/checkout", methods=["POST"])
def checkout():
    cart = session.get("cart", {})
    line_items = []
    for item_id, qty in cart.items():
        item = test_items[item_id]
        line_items.append({
            'price_data': {
                'currency': 'usd',
                'product_data': {'name': item['name']},
                'unit_amount': item['price'],
            },
            'quantity': qty,
        })

    session_stripe = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=line_items,
        mode='payment',
        success_url=url_for('success', _external=True),
        cancel_url=url_for('cart', _external=True)
    )
    return redirect(session_stripe.url, code=303)


@app.route("/success")
def success():
    session.pop("cart", None)
    return "<h1>Payment successful! Thank you for your order.</h1>"


if __name__ == "__main__":
    app.run(debug=True)
