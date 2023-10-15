from connect import connect_db
from create_db_load_date import create_db_load_date


def menu():

    commands = [" 1  - Create DB and load date",
                " 2  - Check DB connection",
                " 3  - Load to DB ",
                " 4  - Output from DB ",
                " 5  - Create ",
                " 6  - Find ",
                " 7  - Update ",
                " 8  - Delete ",
                " 0  - Exit"
                ]

    while True:

        print("_"*31)
        print("| {:<1} {:^27}|".format("☰", "Welcome to main menu"))
        print('|'+'_'*30 + '|')
        for el in commands:
            print('|{:<30}|'.format(el))
        print('|'+'_'*30 + '|')
        print('|{:<30}|'.format('Type number to start:  '))
        user_input = input("|>>> ")
        print('|'+'_'*30 + '|')

        if user_input == '1':
            print("_"*31)
            print("|{:^28}|".format("✨ Create DB! ✨"))
            print("|"+"_"*30 + "|")
            name_db = input(("|>>> Input name DB "))
            print(create_db_load_date(name_db))

        elif user_input == '2':
            print("_"*30)
            print("|{:^28}|".format("✨ Connect DB! ✨"))
            print("|"+"_"*29 + "|")
            name_db = input(("|>>> Input name DB "))
            print(connect_db(name_db))
        elif user_input == '3':
            print("_"*30)
            print("|{:^30}|".format("✨ Load date to DB! ✨"))
            print("|"+"_"*28 + "|")
            print('В розробці')
            # result = load_to_db()
            # print(result)
        elif user_input == '4':
            print("_"*30)
            print("|{:^30}|".format("✨ Output date from DB! ✨"))
            print("|"+"_"*28 + "|")
            print('В розробці')
            # output_from_db()
        elif user_input == '5':
            print("_"*30)
            print("|{:^30}|".format("✨ Create document! ✨"))
            print("|"+"_"*30 + "|")
            print('В розробці')
            # create_doc()
        elif user_input == '6':
            print("_"*30)
            print("|{:^30}|".format("✨ Find date! ✨"))
            print("|"+"_"*30 + "|")
            print('В розробці')
            # find_date()
        elif user_input == '7':
            print("_"*30)
            print("|{:^30}|".format("✨ Update date! ✨"))
            print("|"+"_"*30 + "|")
            print('В розробці')
            # update_doc()
        elif user_input == '8':
            print("_"*30)
            print("|{:^30}|".format("✨ Delete date! ✨"))
            print("|"+"_"*30 + "|")
            print('В розробці')
            # delete_doc()
        elif user_input == '0' or user_input.lower() == "exit":

            print('\nGoodbye!\n')
            break
        else:
            print("_"*30)
            print("|{:^30}|".format("Wrong number... Try again..."))
            print("|"+"_"*30 + "|")


if __name__ == '__main__':
    menu()
