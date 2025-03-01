from urllib import request

from flask import Flask, jsonify, request, session
from flask_cors import CORS
from db_connector import products_col, customers_col, orders_col
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash
import logging
import re

app = Flask(__name__)
app.secret_key = "your_secret_key"
CORS(app, supports_credentials=True)
logging.basicConfig(level=logging.INFO)



@app.route("/products/<category>", methods=["GET"])
def get_products_by_category(category):
    """ מחזיר את כל המוצרים לפי קטגוריה """
    try:
        category = category.upper()
        print(f" מחפש מוצרים בקטגוריה: {category}")

        products = list(products_col.find({"category": category}, {"_id": 0}))

        if not products:
            print(" לא נמצאו מוצרים!")
            return jsonify({"error": "No products found"}), 404

        print(f" נמצא {len(products)} מוצרים.")
        return jsonify(products)

    except Exception as e:
        print(f" שגיאה בבקשת הנתונים: {e}")
        return jsonify({"error": str(e)}), 500


@app.route("/customers", methods=["GET"])
def get_all_customers():
    """ מחזיר את כל המשתמשים ללא קשר לקטגוריה """
    try:
        print("מחפש את כל המשתמשים...")

        customers = list(customers_col.find({}, {"_id": 0, "category": 0}))

        if not customers:
            print("⚠ לא נמצאו משתמשים!")
            return jsonify({"error": "No customers found"}), 404

        print(f"נמצא {len(customers)} משתמשים.")
        return jsonify(customers)

    except Exception as e:
        print(f"שגיאה בבקשת הנתונים: {e}")
        return jsonify({"error": str(e)}), 500





@app.route("/customers", methods=["POST"])
def create_customer():
    """ יוצר משתמש חדש בבסיס הנתונים """
    try:
        data = request.get_json()

        # בדיקה שכל השדות קיימים
        required_fields = ["first_name", "last_name", "email", "password"]
        if not all(field in data for field in required_fields):
            print(" חסרים נתונים!")
            return jsonify({"error": "Missing required fields"}), 400

        first_name = data["first_name"].strip()
        last_name = data["last_name"].strip()
        email = data["email"].strip().lower()
        password = data["password"].strip()

        # בדיקה אם המשתמש כבר קיים על פי האימייל
        if customers_col.find_one({"email": email}):
            print(" משתמש עם אימייל זה כבר קיים!")
            return jsonify({"error": "User already exists"}), 409

        # הצפנת סיסמה
        hashed_password = generate_password_hash(password)

        # יצירת מסמך חדש
        new_customer = {
            "first_name": first_name,
            "last_name": last_name,
            "email": email,
            "password": hashed_password
        }

        # שמירה במסד הנתונים
        customers_col.insert_one(new_customer)
        print(" משתמש נוצר בהצלחה!")

        return jsonify({"message": "User created successfully"}), 201

    except Exception as e:
        print(f" שגיאה ביצירת המשתמש: {e}")
        return jsonify({"error": str(e)}), 500




@app.route("/login", methods=["POST"])
def login():
    """מאמת משתמש על פי אימייל וסיסמה ושומר ב-Session"""
    try:
        data = request.get_json()

        if "email" not in data or "password" not in data:
            logging.warning("חסרים נתונים!")
            return jsonify({"error": "Missing email or password"}), 400

        email = data["email"].strip().lower()
        password = data["password"].strip()

        user = customers_col.find_one({"email": email})
        if not user:
            logging.warning(f"משתמש עם האימייל {email} לא נמצא!")
            return jsonify({"error": "Invalid email or password"}), 401

        if not check_password_hash(user["password"], password):
            logging.warning("סיסמה שגויה!")
            return jsonify({"error": "Invalid email or password"}), 401

        full_name = f"{user['first_name']} {user['last_name']}"

        # שמירת המשתמש ב-Session
        session["user"] = {"email": email, "full_name": full_name}
        session.modified = True

        logging.info(f"משתמש {email} התחבר בהצלחה!")
        return jsonify({"message": "Login successful", "full_name": full_name}), 200

    except Exception as e:
        logging.error(f"שגיאה בהתחברות: {e}")
        return jsonify({"error": "Internal server error"}), 500



@app.route("/logout", methods=["POST"])
def logout():
    """התנתקות מהמערכת"""
    session.clear()  # מנקה את כל הנתונים
    return jsonify({"message": "Logout successful"}), 200



@app.route("/session", methods=["GET"])
def check_session():
    """בודק אם המשתמש מחובר ומחזיר את פרטיו"""
    user = session.get("user")
    if user:
        return jsonify({"logged_in": True, "full_name": user["full_name"]}), 200
    return jsonify({"logged_in": False}), 401


@app.route("/orders", methods=["POST"])
def create_order():
    """יוצר הזמנה חדשה בבסיס הנתונים"""
    try:
        data = request.get_json()

        # בדיקה שכל השדות קיימים
        required_fields = [
            "first_name", "last_name", "email", "phone", "address",
            "postal_code", "city", "country", "card_number",
            "expiration_date", "security_code", "cardholder_name", "id_number"
        ]
        if not all(field in data for field in required_fields):
            print("חסרים נתונים בהזמנה!")
            return jsonify({"error": "Missing required fields"}), 400

        # ניקוי נתונים
        first_name = data["first_name"].strip()
        last_name = data["last_name"].strip()
        email = data["email"].strip().lower()
        phone = data["phone"].strip()
        address = data["address"].strip()
        postal_code = data["postal_code"].strip()
        city = data["city"].strip()
        country = data["country"].strip()
        card_number = data["card_number"].strip()
        expiration_date = data["expiration_date"].strip()
        security_code = data["security_code"].strip()
        cardholder_name = data["cardholder_name"].strip()
        id_number = data["id_number"].strip()

        # בדיקות תקינות
        if not re.match(r"05[0-9]{8}$", phone):
            return jsonify({"error": "Invalid phone number format"}), 400

        if not re.match(r"\d{16}$", card_number):
            return jsonify({"error": "Invalid card number format"}), 400

        if not re.match(r"(0[1-9]|1[0-2])/\d{2}$", expiration_date):
            return jsonify({"error": "Invalid expiration date format"}), 400

        if not re.match(r"\d{3}$", security_code):
            return jsonify({"error": "Invalid security code format"}), 400

        if not re.match(r"\d{9}$", id_number):
            return jsonify({"error": "Invalid ID number format"}), 400

        # הצפנת מספר כרטיס אשראי (הצפנה אמיתית דורשת ספרייה מאובטחת יותר)
        hashed_card_number = generate_password_hash(card_number)

        # יצירת מסמך חדש
        new_order = {
            "first_name": first_name,
            "last_name": last_name,
            "email": email,
            "phone": phone,
            "address": address,
            "postal_code": postal_code,
            "city": city,
            "country": country,
            "card_number": hashed_card_number,
            "expiration_date": expiration_date,
            "security_code": security_code,
            "cardholder_name": cardholder_name,
            "id_number": id_number
        }

        # שמירה במסד הנתונים
        orders_col.insert_one(new_order)
        print("הזמנה נוצרה בהצלחה!")

        return jsonify({"message": "Order created successfully"}), 201

    except Exception as e:
        print(f"שגיאה ביצירת ההזמנה: {e}")
        return jsonify({"error": str(e)}), 500

@app.route("/orders", methods=["GET"])
def get_orders():
    """ מחזיר את כל ההזמנות ממסד הנתונים """
    try:
        orders = list(orders_col.find({}, {"_id": 0}))  # מביא את כל ההזמנות ללא ה-_id
        return jsonify(orders), 200

    except Exception as e:
        print(f"שגיאה בשליפת ההזמנות: {e}")
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    print(" שרת Flask מופעל...")
    app.run(debug=True)
