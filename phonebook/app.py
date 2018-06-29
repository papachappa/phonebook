import cmd

from phonebook import Phonebook

class PhonebookShell(cmd.Cmd):
    intro = 'Welcome to the phonebook shell. Type help or ? to list commands.\n'
    prompt = '(phonebook) '

    def do_list(self, args):
        """Show records in the phonebook, usage 'list'"""
        phonebook.list_records()

    def do_add(self, args):
        """Add user to phonebook, usage 'add <username_without_spaces> <number>'"""
        try:
            name, num = args.split(" ")
            phonebook.add_record(name, num)
        except ValueError:
            print('use add <username_without_spaces> <number>')

    def do_delete(self, name):
        """Delete records from phonebook by name, usage 'delete <username>'"""
        phonebook.delete_record(name)

    def do_search(self, name):
        """Search in phonebook by name, usage 'search <username>'"""
        phonebook.search_record(name)


if __name__ == '__main__':
    phonebook = Phonebook()
    PhonebookShell().cmdloop()
