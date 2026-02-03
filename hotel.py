guests = {}
rooms = {}




def add_guest():
    guest_id = input("Enter guest ID: ")
    name = input("Enter guest name: ")
    age = int(input("Enter guest age: "))
    room_number = input("Enter room number: ")
    check_in_date = input("Enter check-in date (YYYY-MM-DD): ")
    check_out_date = input("Enter check-out date (YYYY-MM-DD): ")



    guest = {
        'id': guest_id,
        'name': name,
        'age': age,
        'room_number': room_number,
        'check_in_date': check_in_date,
        'check_out_date': check_out_date
    }

    guests[guest_id] = guest
    print("Guest added successfully.")





def view_guests():
    if not guests:
        print("No guests found.")
    else:
        print("List of guests:")
        for guest_id, guest_info in guests.items():
            print(f"ID: {guest_id}, Name: {guest_info['name']}, Age: {guest_info['age']}, Room: {guest_info['room_number']}, Check-in: {guest_info['check_in_date']}, Check-out: {guest_info['check_out_date']}")





def search_guest():
    guest_id = input("Enter guest ID to search: ")
    if guest_id in guests:
        guest_info = guests[guest_id]
        print(f"Guest found - ID: {guest_info['id']}, Name: {guest_info['name']}, Age: {guest_info['age']}, Room: {guest_info['room_number']}, Check-in: {guest_info['check_in_date']}, Check-out: {guest_info['check_out_date']}")
    else:
        print("Guest not found.")





def update_guest():
    guest_id = input("Enter guest ID to update: ")
    if guest_id in guests:
        name = input("Enter updated name: ")
        age = int(input("Enter updated age: "))
        room_number = input("Enter updated room number: ")
        check_in_date = input("Enter updated check-in date (YYYY-MM-DD): ")
        check_out_date = input("Enter updated check-out date (YYYY-MM-DD): ")

        guests[guest_id]['name'] = name
        guests[guest_id]['age'] = age
        guests[guest_id]['room_number'] = room_number
        guests[guest_id]['check_in_date'] = check_in_date
        guests[guest_id]['check_out_date'] = check_out_date

        print("Guest updated successfully.")
    else:
        print("Guest not found.")







def delete_guest():
    guest_id = input("Enter guest ID to delete: ")
    if guest_id in guests:
        del guests[guest_id]
        print("Guest deleted successfully.")
    else:
        print("Guest not found.")






def add_room():
    room_number = input("Enter room number: ")
    room_type = input("Enter room type: ")
    capacity = int(input("Enter room capacity: "))
    price_per_night = float(input("Enter price per night: "))

    room = {
        'room_number': room_number,
        'type': room_type,
        'capacity': capacity,
        'price_per_night': price_per_night
    }

    rooms[room_number] = room
    print("Room added successfully.")





def view_rooms():
    if not rooms:
        print("No rooms found.")
    else:
        print("List of rooms:")
        for room_number, room_info in rooms.items():
            print(f"Room Number: {room_number}, Type: {room_info['type']}, Capacity: {room_info['capacity']}, Price per Night: ${room_info['price_per_night']}")




def main_menu():
    while True:
        print("1. Add Guest")
        print("2. View Guests")
        print("3. Search Guest")
        print("4. Update Guest")
        print("5. Delete Guest")
        print("6. Add Room")
        print("7. View Rooms")
        print("8. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 8:
            break
        else:
            handle_choice(choice)




def handle_choice(choice):
    if choice == 1:
        add_guest()
    elif choice == 2:
        view_guests()
    elif choice == 3:
        search_guest()
    elif choice == 4:
        update_guest()
    elif choice == 5:
        delete_guest()
    elif choice == 6:
        add_room()
    elif choice == 7:
        view_rooms()




main_menu()
