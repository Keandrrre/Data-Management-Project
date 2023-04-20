# Data Management Project/ Music Playlist
import os
import json

songs = [{'title': 'Jungle', 'artist': 'Drake'},
         {'title': 'Replay', 'artist': 'Tems'}, {'title': 'Search & Rescue', 'artist': 'Drake'}, {'title': 'Kill Bill', 'artist': 'SZA'}, {'title': "Creepin'", 'artist': 'Metro Boomin, The Weekend & 21 Savage'}, {'title': 'Rich Flex', 'artist': 'Drake & 21 Savage'}]

# User Options
loop = True
while loop == True:
    user_selection = int(input(
        "1-Display\n2-Filter Data\n3-Sort Data\n4-Add Data to Favourites\n5-Remove Data from Favourites\n6-Display Favourites\n\nInput: "))
    if user_selection == 1:
        os.system('cls')
        print("DISPLAY ALL")
        # Display all Songs
        for i in range(len(songs)):
            print(songs[i]['title'] +
                  ' (By ' + songs[i]['artist'] + ')')
        loop = False
    elif user_selection == 2:
        os.system('cls')
        print("FILTER")
        # Filter songs
        filter_by = int(
            input('1-By Title\n2-By Artist\n3-By Genre\n\nEnter Here:'))
        os.system('cls')
        if filter_by == 1:
            filter_data = input('Enter Title: ')
            os.system('cls')
            print('DISPLAYING SONGS TITLED "' + str(filter_data) + '"')
            for i in range(len(songs)):
                if filter_data.lower() in songs[i]['title'].lower():
                    print(songs[i]['title'] +
                          ' (By ' + songs[i]['artist'] + ')')
        elif filter_by == 2:
            filter_data = input('Enter Artist: ')
            os.system('cls')
            print('DISPLAYING SONGS BY "' + str(filter_data) + '"')
            for i in range(len(songs)):
                if filter_data.lower() in songs[i]['artist'].lower():
                    print(songs[i]['title'] +
                          ' (By ' + songs[i]['artist'] + ')')
        elif filter_by == 3:
            filter_data = input('Enter Genre: ')
            os.system('cls')
            print('DISPLAYING SONGS UNDER "' + str(filter_data) + '"')
            for i in range(len(songs)):
                if filter_data.lower() in songs[i]['genre'].lower():
                    print(songs[i]['title'] +
                          ' (By ' + songs[i]['artist'] + ')')
        loop = False
    elif user_selection == 3:
        os.system('cls')
        print("SORT")
        # Sort Songs
        sort_by = int(input('1-Title\n2-Artist\n3-Genre\n\nEnter Here: '))
        os.system('cls')
        if sort_by == 1:
            songs.sort(key=songs['title'])
            for i in range(len(songs)):
                print(songs[i]['title'] +
                      ' (By ' + songs[i]['artist'] + ')')
        loop = False
    elif user_selection == 4:
        print("Add to Favourites")
    elif user_selection == 5:
        print("Remove from Favourites")
    elif user_selection == 6:
        print("Display Favourites")
