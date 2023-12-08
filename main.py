import pywhatkit
import openai
import datetime



contacts = []

def add_contact():
    global name
    global name_user
    global age_user
    global phone_number
    name_user = input("entrez votre nom ")
    age_user = int(input('quel age avez vous ?'))
    name = input("Entrez le nom du contact : ")
    while True:
        phone_number = input("Entrez le numéro de téléphone (AVEC INDICATIF REGIONAL EXPL + +212 123456789) : ")
        global age 
        global position 
        global other_info
        age = input("Quel est l'âge du contact ? ")
        position = input("Quelle est la position dans la famille ? (ami(e), soeur, pere ...) ")
        other_info = input("Autres informations sur le contact : ")
        
        contact = {
            "Nom": name,
            "Numéro de téléphone": phone_number,
            "Âge": age,
            "Position dans la famille": position,
            "Autres informations": other_info
        }
        contacts.append(contact)
        print("Contact ajouté avec succès !")
    

while True:
    print("1. Ajouter un contact")
    print("2. Quitter")
    
    choice = input("Choisissez une option : ")
    
    if choice == "1":
        add_contact()
    elif choice == "2":
        break
    else:
        print("Option invalide. Veuillez choisir une option valide.")


openai.api_key = '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'

# prompt = ('parle comme si tu avais {age_utilisateur} , stp ecris moi un message de joyeux anniversaire pour {nam} qui a {age_destinataire} et qui est mon/ma {position_1} et qui  {autres}' .format(nam = name, age_utilisateur = age_user, age_destinataire = age, position_1 = position, autres = other_info ))

prompt = ('BONJOUR CHAT GPT COMMENT CA VA')
completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages = [{"role": "user", "content": prompt}]

)
ai = (completion['choices'][0]['message']['content'])


pywhatkit.sendwhatmsg(+212603170206, ai, 8, 55,10, True )

# maintenant = datetime.datetime.now()

# date = (e.strftime(" %m-%d %H:%M:%S"))

# mois_actuel = maintenant.month
# jour_actuel = maintenant.day
# heure_actuelle = maintenant.hour
# minute_actuelle = maintenant.minute

# for contact in contacts:
#             anniversaire = contact.get("Âge")
#             if anniversaire:
#                 mois_anniversaire, jour_anniversaire = map(int, anniversaire.split("-"))
#                 if mois_actuel == mois_anniversaire and jour_actuel == jour_anniversaire:
#                     # C'est l'anniversaire du contact, envoie le message ici
#                     print(f"C'est l'anniversaire de {contact['Nom']} ! Envoi du message...")
#                     envoi_message_anniversaire(contact)

# def envoi_message_anniversaire(contact):
#     # Ton code pour générer et envoyer un message d'anniversaire avec OpenAI et pywhatkit ici
#     # ...
#     pass

# if mois_actuel == 12 and jour_actuel == 11 and heure_actuelle == 0 and minute_actuelle == 0:

    
