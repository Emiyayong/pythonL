import sys,shelve
def store_person(db):
    pid=input('Enter unique Id number:')
    person={}
    person['name']=input('Enter name:')
    person['age']=input('Enger age:')
    person['phone']=input('Enter phone')
    db[pid]=person
def lookup_person(db):
    pid= input('Enter ID Number:')
    field = input('What would you like to konw?(name,age,phone)')
    field=field.strip().lower()
    print(field.capitalize()+':',db[pid][field])
def print_hlep():
    print('The available commands are:')
    print('store:Stores infomation about a person')
    print('lookup:Looks up a person form ID number')
    print('?:Prints this message')
def enter_command():
    cmd = input('Enter command(? for help):')
    cmd = cmd.strip().lower()
    return cmd

def main():
    database=shelve.open()
    try:
        while True:
            cmd=enter_command()
            if cmd=='store':
                store_person(database)
            elif cmd=='lookup':
                lookup_person(database)
            elif cmd=='?':
                print_hlep()
            elif cmd=='quit':
                return