import mysql.connector
from mysql.connector import errorcode

config = {
    "user": "outland_adventures_user",
    "password": "cheese1",
    "host": "localhost",
    "database": "outland_adventures",
    "raise_on_warning": True
}

try:
    mydb = mysql.connector.connect(
        host = "localhost",
        database = "outland_adventures",
        user = "outland_adventures_user",
        password = "cheese1"
    )

    print(f"Database user {config['user']} connected to MySQL on host {config['host']} with database {config['database']}")

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print(" The username or password is invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print(" The database does not exist")
    
    else:
        print(err)

# enough customers buy equipment to keep equipment sales?
cursor = mydb.cursor()
cursor.execute("SELECT clients.first_name, clients.last_name, inventory.product_name, inventory.purchase_cost, inventory.rental_cost from clients JOIN equipment ON clients.client_id = equipment.client_id JOIN inventory ON inventory.inventory_id = equipment.inventory_id")


print("-- DISPLAYING Equipment Sales RECORDS --")
result = cursor.fetchall()

for first_name, last_name, product_name, purchase_cost, rental_cost in result:
  print(f"Client Name: {first_name} {last_name}\nProduct Name: {product_name}\nPurchase Cost: {purchase_cost}\nRental Cost: {rental_cost}\n".format(result))


# they have conducted treks in Africa, Asia, and Southern Europe. Is there anyone of those locations that has a downward trend in bookings?
cursor2 = mydb.cursor()
cursor2.execute("SELECT clients.first_name, clients.last_name, trips.trip_name, country.country_name from clients JOIN clients_attending_trip ON clients.client_id = clients_attending_trip.client_id JOIN trips ON clients_attending_trip.trip_id = trips.trip_id JOIN country ON trips.country_id = country.country_id")

print("-- DISPLAYING TREKS RECORDS --")
result2 = cursor2.fetchall()

for first_name, last_name, trip_name, country_name in result2:
  print(f"Client Name: {first_name} {last_name}\nTrip Name: {trip_name}\nCountry Name: {country_name}\n".format(result2))


# Are there inventory items that are over five years old?
cursor3 = mydb.cursor()
cursor3.execute("SELECT inventory.product_name, equipment.equip_expired from inventory JOIN equipment ON inventory.inventory_id = equipment.inventory_id WHERE equipment.restock_date < DATE_SUB('2023-07-15', INTERVAL 5 YEAR)")

print("-- DISPLAYING Expired Equip RECORDS --")
result3 = cursor3.fetchall()

for product_name, equip_expired in result3:
  print(f"Product Name: {product_name}\nExpired: {equip_expired}\n".format(result2))