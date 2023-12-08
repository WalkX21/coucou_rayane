
import flet
from flet import Page, AppBar, TextField, Image, FilledButton, Text, colors, Column, Container


def test(page: Page):
    page.window_width = 720
    page.window_height=1280
    def btn_clicked(e):
        page.clean()
        page_2(page)

            
    page.appbar=AppBar(title=Text("Coucou Rayane "), bgcolor=colors.CYAN_700, center_title=True)
    img =Image(
        src =f"https://img.freepik.com/free-vector/assortment-confident-people-smiling_23-2148411467.jpg?w=2000",
        # src =f"C:\Users\moham\OneDrive\Bureau\Chingu B-Days\spmn.png",

        fit= "contain"
    )
    global login
    global password
    login = TextField(label="Email", hint_text="Email Adresse")
    btn = FilledButton(text="Login", width=700, height=100, on_click=btn_clicked)
    password=TextField(label="Passeword", password=True,can_reveal_password=True, hint_text="your password")

    page.add(
        Container(
            content=Column([
        img,
        login,
        password, btn
    ], spacing=20)
        )
        )
    
global page_2
def page_2(page: Page):
    page.window_width = 720
    page.window_height=1280
# ya une erreur, trouver une fonction qui ferme la page
    def quite():
        quit()

    def new_pagee(e):
        page.clean()
        new_page(page)
    
    

    


    ajouter = FilledButton(text="ajouter un contact", width=700, height=100, on_click=new_pagee)
    quiter = FilledButton(text="Quiter", width=700, height=100, on_click=quite)



    page.add(
        Container(
            content=Column([
                ajouter,
                quiter,
            ], spacing=20)
        )
    )




global new_page
global third_page
global fourth_page
def new_page(page: Page):
    page.window_width = 720
    page.window_height = 1280
    def submit_clicked(e):



        page.clean()
        third_page(page)

                
            # Crée de nouveaux champs de texte ou d'autres éléments que tu veux sur la nouvelle page
    global new_text_field
    global textField1
    new_text_field = TextField(label="Nouveau champ de texte", hint_text="Entrez quelque chose")
            
    textField1= TextField(label="Nouveau champ de texte", hint_text="Entrez quelque chose")
    submit_btn = FilledButton(text="Submit", width=700, height=100, on_click=submit_clicked)

            # Ajoute les éléments à la nouvelle page
    page.add(
        Container(
            content=Column([
                Text("Entrez les informations du contact :\n Quel est le nom de contact 1"),
                        
                new_text_field,
                Text("Quel age a contact 1"),
                textField1,
                submit_btn,
            ], spacing=20)
        )
    )

def third_page(page: Page):
    page.window_width = 720
    page.window_height = 1280
    def submit_clicked2(e):



        page.clean()
        fourth_page(page)
    global third_text
    global fourth_text
    third_text = TextField(label="Nouveau champ de texte", hint_text="Entrez quelque chose")
    fourth_text = TextField(label="Nouveau champ de texte", hint_text="Entrez quelque chose")
    submit_btn2 = FilledButton(text="Submit", width=700, height=100, on_click=submit_clicked2)
    page.add(
        Container(
            content=Column([
                # Ajoute ici les éléments pour la troisième page
                Text("quel est le numero de telephone de contact 1 ? avec indicatif regionnal !"),
                third_text,
                Text("Quel est la position de contact 1 (ami, pere, mere, soeur ...)"),
                fourth_text,
                submit_btn2,
            ], spacing=20)
        )
    )

def fourth_page(page:Page):
    page.window_width = 720
    page.window_height = 1280

    def retour_a_page_2(e):
        page.clean()
        page_2(page)
        print (ai)

    global retour
    global ai
    global stokage
    retour = FilledButton(text="Submit", width=700, height=100, on_click= retour_a_page_2)
    stokage = []
    ai = " Voila les info sur contact1 : \n {nama} \n {agex} \n {ph} \n {pos}" .format(nama = new_text_field.value, agex = textField1.value, ph = third_text.value, pos =  fourth_text.value )
    stokage.append(ai)
    
    page.add(
        Container(
            content=Column([
                Text(ai),
                retour,
            ])
                        
            )
        )

flet.app(target=test)

print(stokage)
        

