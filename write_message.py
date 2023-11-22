import proto.addressbook_pb2 as addressbook_pb2

address_book = addressbook_pb2.AddressBook()

person = address_book.people.add()

person.id = 1
person.name = "Joe"
person.email = "Joe@email.com"
phone_number = person.phones.add()
phone_number.number = "07999999999"
phone_number.type = addressbook_pb2.Person.PhoneType.PHONE_TYPE_MOBILE

filename = "packet.bin"

with open(filename,"wb") as f:
    f.write(address_book.SerializeToString())

print("Written protobuf message to " + filename + "!")