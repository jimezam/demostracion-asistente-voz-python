import assistant
from assistant import text_to_number
from order import Order


menu_food = [
    {"name": "Frijoles",    "price": 100},
    {"name": "Pollo",       "price": 200},
    {"name": "Hamburguesa", "price": 300}
]

menu_drink = [
    {"name": "Gaseosa",  "price": 100},
    {"name": "Juguito",  "price": 200},
    {"name": "Limonada", "price": 300}
]


def show():
    order = Order()
    count = ask_guests_count()
    order = ask_food_drinks(count, order)
    bill = calculate_bill(order)
    assistant.speak(f"La cuenta es de {bill} pesotes")


def ask_food_drinks(count, order):
    for i in range(count):
        order_item(i, menu_food, order)
        order_item(i, menu_drink, order)
    return order


def order_item(i, menu, order):
    while True:
        assistant.speak(f"¿Qué va a pedir el invitado #{i + 1}?")
        show_menu(menu)
        item = assistant.listen()
        item_found = check_item_menu(menu, item)
        print(f"Checking for ... {item} ... {item_found}")
        if item_found is not None:
            assistant.speak(f"Recibido {item}")
            order.append(item_found)
            break
        else:
            assistant.speak(f"La opción {item} no está disponible")


def ask_guests_count():
    success = False
    count = 0

    while not success: 
        assistant.speak("¿Cuántos invitados vendrán?")
        count = assistant.listen()
        count = text_to_number(count)

        try:
            count = int(count)
            assistant.speak(f"Vendrán {count} invitados")
            success = True
        except ValueError:
            assistant.speak(f"Error: {count}")
            success = False
    return count


def calculate_bill(order):
    bill = 0
    for item in order.items:
        bill += item['price']
    return bill


def check_item_menu(menu, item_name): 
    for item in menu:
        if item['name'].lower() == item_name.lower():
            return item
    return None

                
def show_menu(menu):
    for item in menu:
        assistant.speak(f"{item['name']}")
