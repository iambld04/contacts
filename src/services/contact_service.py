from src.models.db_models import Contact,db

def create_new_contact(data,username):
    new_contact = Contact(
            FirstName=data.get('FirstName'),
            LastName=data.get('LastName'),
            PhoneNo=data.get('PhoneNo'),
            Email=data.get('Email'),
            Area=data.get('Area'),
            City=data.get('City'),
            State=data.get('State'),
            Pincode=data.get('Pincode'),
            username=username
        )
    db.session.add(new_contact)
    db.session.commit()
    return

def get_a_contact(contact):
    contact_data = {
            'id': contact.id,
            'FirstName': contact.FirstName,
            'LastName': contact.LastName,
            'PhoneNo': contact.PhoneNo,
            'Email': contact.Email,
            'Area': contact.Area,
            'City': contact.City,
            'State': contact.State,
            'Pincode': contact.Pincode,
        }
    return contact_data

def get_all_contacts(contacts):
    output = []
    for contact in contacts:
        contact_data = {
                'id': contact.id,
                'FirstName': contact.FirstName,
                'LastName': contact.LastName,
                'PhoneNo': contact.PhoneNo,
                'Email': contact.Email,
                'Area': contact.Area,
                'City': contact.City,
                'State': contact.State,
                'Pincode': contact.Pincode,
            }
        output.append(contact_data)
    return output

def update_a_contact(data,contact):
    contact.FirstName = data.get('FirstName', contact.FirstName)
    contact.LastName = data.get('LastName', contact.LastName)
    contact.PhoneNo = data.get('PhoneNo', contact.PhoneNo)
    contact.Email = data.get('Email', contact.Email)
    contact.Area = data.get('Area', contact.Area)
    contact.City = data.get('City', contact.City)
    contact.State = data.get('State', contact.State)
    contact.Pincode = data.get('Pincode', contact.Pincode)
    db.session.commit()
    return

def delete_a_contact(contact):
    db.session.delete(contact)
    db.session.commit()
    return
