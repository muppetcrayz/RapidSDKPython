import app

rapidSDK = app.RapidSDK()

firstname = "Tat"
lastname = "Nastold"
username = "tat@example.com"
password = "tatthecat"

registerResult = rapidSDK.register(firstname, lastname, username, password)

print "Register User: " + registerResult

username = "tat@example.com"
password = "tatthecat"

loginResult = rapidSDK.login(username, password)

print "User Log In: " + loginResult

json_data = { "Animal":"Cat", "Pet Name": "Tat"}

createResult = rapidSDK.create(json_data)

print "Create: " + createResult

string_data = "Animal,Pet Name"

readResult = rapidSDK.read(string_data)

print "Read: "
print readResult

json_data = { "Animal":"Dog", "Pet Name": "Butch"}

updateResult = rapidSDK.update(json_data)

print "Update: " + updateResult

string_data = "Animal,Pet Name"

readResult = rapidSDK.read(string_data)

print "Read Again: "
print readResult

string_data = "Animal,Pet Name"

deleteResult = rapidSDK.delete(string_data)

print "Delete: " + deleteResult
