import HashTable


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    myHashTable = HashTable.HashTable(50)

    myHashTable.set_val('gfg@example.com', '23')
    print(myHashTable)

    myHashTable.set_val('portal@example.com', '200')
    print(myHashTable)

