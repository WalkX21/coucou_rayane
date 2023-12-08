import flet
from flet import Page, AppBar, TextField, Image, FilledButton, Text, colors, Column, Container
from flask import Flask, request, jsonify

app = Flask(__name__)

# Liste de contacts (utilisée pour stocker temporairement les contacts)
contacts = []

def add_contact():
    data = {
        "name": name_input.text,
        "phone_number": phone_input.text,
        "age": age_input.text,
        "position": position_input.text,
        "other_info": other_info_input.text
    }
    contacts.append(data)
    print("Contact ajouté avec succès !")

@app.route('/get_contacts', methods=['GET'])
def get_contacts():
    return jsonify(contacts)

@app.route('/add_contact', methods=['POST'])
def api_add_contact():
    data = request.json
    contacts.append(data)
    return jsonify({"message": "Contact ajouté avec succès !"}), 200

def test(page: Page):
    page.window_width = 720
    page.window_height = 1280

    page.appbar = AppBar(title=Text("Coucou Rayane "), bgcolor=colors.CYAN_700, center_title=True)
    img = Image(
        src="https://img.freepik.com/free-vector/assortment-confident-people-smiling_23-2148411467.jpg?w=2000",
        fit="contain"
    )

    global name_input
    name_input = TextField(label="Nom", hint_text="Nom du contact")
    phone_input = TextField(label="Numéro de téléphone", hint_text="Numéro de téléphone")
    age_input = TextField(label="Âge", hint_text="Âge du contact")
    position_input = TextField(label="Position dans la famille", hint_text="Position")
    other_info_input = TextField(label="Autres informations", hint_text="Autres informations")

    btn = FilledButton(text="Ajouter un contact", width=700, height=100, on_click=add_contact)

    page.add(
        Container(
            content=Column([
                img,
                name_input,
                phone_input,
                age_input,
                position_input,
                other_info_input,
                btn
            ], spacing=20)
        )
    )

if __name__ == '__main__':
    app.run(debug=True)
    flet.app(target=test)
