# Data Management Project/ Music Playlist
import os
import json
import time


songs = [{'title': 'Jungle', 'artist': 'Drake', "genres": 'Hip-Hop/Rap'}, {'title': 'Replay', 'artist': 'Tems', 'genres': 'Nigerian R&B, Afropop'}, {'title': 'Search & Rescue', 'artist': 'Drake', 'genres': 'Hip-Hop/Rap'}, {'title': 'Kill Bill', 'artist': 'SZA',
                                                                                                                                                                                                                               'genres': 'Pop music, R&B/Soul, Doo-wop, psychedelic pop, pop soul'}, {'title': "Creepin'", 'artist': 'Metro Boomin, The Weekend & 21 Savage', 'genres': 'Hip-Hop/Rap'}, {'title': 'Rich Flex', 'artist': 'Drake & 21 Savage', 'genres': 'Hip-Hop/Rap'}, {'title': 'Impossible', 'artist': 'Travis Scott', 'genres': 'Hip-Hop/Rap'}]


def displayAll():
    for i in range(len(songs)):
        print('[' + str(i + 1) + '] ' + songs[i]['title'] +
              ' (By ' + songs[i]['artist'] + ')')


# User Options
loop = True
while loop == True:
    user_selection = int(input(
        "1-Display\n2-Filter Data\n3-Sort Data\n4-Add Data to Favourites\n5-Remove Data from Favourites\n6-Display Favourites\n\nInput: "))
    if user_selection == 1:
        os.system('cls')
        print("DISPLAY ALL")
        # Display all Songs
        displayAll()
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
                if filter_data.lower() in songs[i]['genres'].lower():
                    print(songs[i]['title'] +
                          ' (By ' + songs[i]['artist'] + ')')
        loop = False
    elif user_selection == 3:
        os.system('cls')
        print("SORT")
        # Sort List
        sort_by = input('1-By Title\n2-By Artist\n3-By Genre\n\nEnter Here:')
        if sort_by == 1:
            songs.sort()
        loop = False
    elif user_selection == 4:
        # Add To Favourites
        if os.path.getsize('favourtie_songs.json') == 0:
            fav_songs = []
        else:
            with open('favourite_songs.json', 'r') as file_ref:
                fav_songs = json.load
        add_song = True
        while add_song == True:
            os.system('cls')
            print('ADD TO FAVOURITES')
            displayAll()
            choose_song = int(
                input('\nEnter Song "#" to Add or "0" to Exit: '))
            if choose_song > 0:
                fav_songs.append(songs[choose_song - 1])
                print('\nSONG ADDED...')
                time.sleep(3)
            else:
                add_song = False
        with open('favourite_songs.json', 'w') as file_ref:
            json.dump(fav_songs, file_ref)
    elif user_selection == 5:
        print("Remove from Favourites")
    elif user_selection == 6:
        print("Display Favourites")
