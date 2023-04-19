# Data Management Project/ Music Playlist
import os

songs = [{'title': 'Jungle', 'artist': 'Drake'},
         {'title': 'Replay', 'artist': 'Tems'}]

# User Options
loop = True
while loop == True:
    user_selection = int(input(
        "1-Display\n2-Filter Data\n3-Sort Data\n4-Add Data to Favourites\n5-Remove Data from Favourites\n6-Display Favourites\n\nInput: "))
    if user_selection == 1:
        os.system('cls')
        print("Displaying All Songs:")

        # Display all Songs
        for i in range(len(songs)):
            print('\t' + songs[i]['title'] +
                  ' (By ' + songs[i]['artist'] + ')')
        loop = False
    elif user_selection == 2:
        os.system('cls')
        print("Filter")

        # Filter songs
        filter_by = int(
            input('1-By Title\n2-By Artist\n3-By Genre\nEnter Here:'))
        if filter_by == 1:
            filter_data = input('Enter Title: ')
            for i in range(len(songs)):
                if songs[i]['title'] == filter_data:
                    print('\t' + songs[i]['title'] +
                          ' (By ' + songs[i]['artist'] + ')')
        elif filter_by == 2:
            filter_data = input('Enter Artist: ')
            for i in range(len(songs)):
                if songs[i]['artist'] == filter_data:
                    print('\t' + songs[i]['title'] +
                          ' (By ' + songs[i]['artist'] + ')')
        elif filter_by == 3:
            filter_data = input('Enter Genre: ')
            for i in range(len(songs)):
                if songs[i]['genre'] == filter_data:
                    print('\t' + songs[i]['title'] +
                          ' (By ' + songs[i]['artist'] + ')')
        loop = False
    elif user_selection == 3:
        print("Sort")
    elif user_selection == 4:
        print("Add to Favourites")
    elif user_selection == 5:
        print("Remove from Favourites")
    elif user_selection == 6:
        print("Display Favourites")
