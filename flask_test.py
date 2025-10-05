from flask import Flask, render_template, request
import json
from encryption import encryption
from decrypt import decryption

app = Flask(__name__) 


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/sign-up")
def sign_up():
    return render_template("sign-up.html")


@app.route("/sign-up", methods=["POST"])
def make_new_account():
    global master_username

    master_username = request.form.get("master_username")
    password = request.form.get("password")
    confirm_password = request.form.get("confirm_password")

    if password == confirm_password:
        encrypted_website = encryption("website")
        enc_website_name = encryption("SecureLocal")
        
        encrypted_username = encryption("username") 
        enc_master_username = encryption(master_username)

        encrypted_password = encryption("password")
        enc_master_password = encryption(password)

        account_creation = {
        "passwords": [
            {
                f"{encrypted_website}": f"{enc_website_name}",
                f"{encrypted_username}": f"{enc_master_username}",
                f"{encrypted_password}": f"{enc_master_password}"
            },
        ]
        }


        
        file = open(f"{master_username}_passwords.txt", "w") 
        json.dump(account_creation, file)
        file.close()
        return render_template("account.html")    
    else:
        return render_template("sign-up.html", msg="Passwords do not match. Please try again.")


@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/login", methods=["POST"])
def login_account():
    global master_username

    master_username = request.form.get("master_username")
    password = request.form.get("password")

    try:
        with open(f"{master_username}_passwords.txt", "r") as file:
            file_contents = json.load(file)

        supposed_master_password = file_contents["passwords"][0][encryption("password")]

        if supposed_master_password == encryption(password):

            all_passwords_list = []
            account_username_password = []
            passwords_list = []

            for information in file_contents["passwords"]:
                for key, value in information.items():
                    key = decryption(key)
                    value = decryption(value)
                    account_username_password.append(value)
                    if len(account_username_password) == 3:
                        passwords_list.append({
                            "website": account_username_password[0],
                            "username": account_username_password[1],
                            "password": account_username_password[2]
                        })
                        passwords_list[0]

                        all_passwords_list.append(passwords_list[0])

                        account_username_password = []
                        passwords_list = []
            return render_template("account.html", passwords=passwords_list, msg="Access Granted")
        
        else:
            return render_template("login.html", msg="Wrong Username or Password. Please try again.")
        
    except FileNotFoundError:
        return render_template("sign-up.html", msg="Account does not exist. Please sign up first.")        


@app.route("/account-page", methods=["POST"])
def show_account_page():
    return render_template("account.html")

#This allows for passwords to be displayed to the user
@app.route("/account-page", methods=["GET"])
def display_passwords():
    with open(f"{master_username}_passwords.txt", "r") as file:
        file_contents = json.load(file)

    encrypted_list = file_contents["passwords"]

    passwords_list = [] 
    for entry in encrypted_list:
        website = entry[0][encryption("website")]
        username = entry[0][encryption("username")]
        password = entry[0][encryption("password")]

        passwords_list.append({
            "website": website,
            "username": username,
            "password": password
        })

    # Pass the list to the template
    return render_template("account.html", passwords=passwords_list)



@app.route("/add-password-page")
def add_password_page():
    return render_template("add-password.html")


@app.route("/add-password", methods=["POST"])
def add_password():
    website = request.form.get("website")
    username = request.form.get("username")
    account_password = request.form.get("account_password")

    enc_website = encryption(website)
    enc_username = encryption(username)
    enc_account_password = encryption(account_password)

    with open(f"{master_username}_passwords.txt", "r") as file:
        file_contents = json.load(file)


    #this adds a new password to the json file
    new_entry = {
        encryption("website"): enc_website,
        encryption("username"): enc_username,
        encryption("password"): enc_account_password
    }

#File "c:\Users\razir\OneDrive\Desktop\vscoding\projects\PASSWORD_MANAGER_APP\flask_test.py", line 152, in add_password
#file_contents = file_contents["passwords"][0].append(new_entry)
#                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#AttributeError: 'dict' object has no attribute 'append'

    file_contents["passwords"].append(new_entry)

    with open(f"{master_username}_passwords.txt", "w") as file:
        json.dump(file_contents, file)

    #add a list of passwords to the account page

    with open(f"{master_username}_passwords.txt", "r") as file:
        file_contents = json.load(file)
    
    account_username_password = []
    all_passwords_list = []
    passwords_list = []

    for information in file_contents["passwords"]:
        for key, value in information.items():
            key = decryption(key)
            value = decryption(value)
            account_username_password.append(value)
            if len(account_username_password) == 3:
                passwords_list.append({
                    "website": account_username_password[0],
                    "username": account_username_password[1],
                    "password": account_username_password[2]
                })
                passwords_list[0]

                all_passwords_list.append(passwords_list[0])

                account_username_password = []
                passwords_list = []

    return render_template("account.html", msg="Password added successfully!", passwords=all_passwords_list)

            
if __name__ == "__main__":
    app.run(debug=True)