from flask import Flask, render_template, request

app = Flask(__name__)


# =========================
# TRANG CHỦ
# =========================

@app.route("/")
@app.route("/coi-san-pham-o-day")
def home():
    return render_template("index.html")


# =========================
# TRANG THANH TOÁN
# =========================

@app.route("/checkout")
def checkout():

    product = request.args.get("product", "Sản phẩm")
    price = request.args.get("price", "0đ")

    return render_template(
        "checkout.html",
        product=product,
        price=price
    )


# =========================
# ĐẶT HÀNG
# =========================

@app.route("/order", methods=["POST"])
def order():

    name = request.form.get("name")
    phone = request.form.get("phone")
    address = request.form.get("address")
    payment = request.form.get("payment")

    return render_template(
        "checkout.html",
        success=True,
        name=name,
        phone=phone,
        address=address,
        payment=payment
    )


# =========================
# CHẠY WEBSITE
# =========================

if __name__ == "__main__":
    app.run(debug=True)