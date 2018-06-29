class Phonebook():
    phonebook = {}
    
    def add_record(self, name, number):
        try:
            Phonebook.phonebook[name] = number
        except Exception as err:
            print("Error occurred: {}".format(err))

    def delete_record(self, name):
        if name in Phonebook.phonebook.keys():
            del Phonebook.phonebook[name]
            print("Record with name '{}' was deleted".format(name))
        else:
            print("No such name in the phonebook")

    def list_records(self):
        print("\nPhonebook has following entries:")
        for k,v in Phonebook.phonebook.items():
            print("'{key}' => {value}".format(key=k,value=v))

    def search_record(self, name):
        if name in Phonebook.phonebook.keys():
            print("Record with name '{}' has number '{}'"
                  .format(name, Phonebook.phonebook.get(name))
                 )
        else:
            print("No such name in the phonebook")
