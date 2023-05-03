# Data Management Project/ Music Playlist
import os
import json
import time


songs = [{'title': 'Jungle', 'artist': 'Drake', "genres": 'Hip-Hop/Rap'}, {'title': 'Replay', 'artist': 'Tems', 'genres': 'Nigerian R&B, Afropop'}, {'title': 'Search & Rescue', 'artist': 'Drake', 'genres': 'Hip-Hop/Rap'}, {'title': 'Kill Bill', 'artist': 'SZA',
                                                                                                                                                                                                                               'genres': 'Pop music, R&B/Soul, Doo-wop, psychedelic pop, pop soul'}, {'title': "Creepin'", 'artist': 'Metro Boomin, The Weekend & 21 Savage', 'genres': 'Hip-Hop/Rap'}, {'title': 'drive Me crazy!', 'artist': 'Lil Yachty', 'genres': 'Alternate/Indie'}, {'title': 'Impossible', 'artist': 'Travis Scott', 'genres': 'Hip-Hop/Rap'}]


def displayAll(array):
    for i in range(len(array)):
        print('[' + str(i + 1) + '] ' + array[i]['title'] +
              ' (By ' + array[i]['artist'] + ')')


# User Options
loop = True
while loop == True:
    os.system('cls')
    user_selection = int(input(
        "SONG LIBRARY\n0-Exit Library\n1-Display All\n2-Filter Songs\n3-Sort Songs\n4-Add Songs to Favourites\n5-Remove Songs from Favourites\n6-Display Favourites\n\nInput: "))
    if user_selection == 1:
        os.system('cls')
        print("DISPLAY ALL")
        # Display all Songs
        displayAll(songs)
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
        if os.path.getsize('favourite_songs.json') > 0:
            with open('favourite_songs.json', 'r') as file_ref:
                fav_songs = json.load(file_ref)
        else:
            fav_songs = []
        add_song = True
        while add_song == True:
            os.system('cls')
            print('ADD TO FAVOURITES')
            displayAll(songs)
            choose_song = int(
                input('\nEnter Song "#" to Add or "0" to Exit & Save: '))
            if choose_song > 0 and choose_song - 1 in range(len(songs)) and songs[choose_song - 1] not in fav_songs:
                fav_songs.append(songs[choose_song - 1])
                print('\nSONG ADDED...')
                time.sleep(3)
            elif songs[choose_song - 1] in fav_songs:
                add_anyway = str(input(
                    '\nWARNING: This song has already been added to your Favourites, would you still like to add it? (type "yes" or "no"): '))
                if add_anyway == 'yes':
                    fav_songs.append(songs[choose_song - 1])
                    print('\nSONG ADDED...')
                    time.sleep(3)
                elif add_anyway == 'no':
                    print('\nSONG NOT ADDED...')
                    time.sleep(3)
            elif choose_song == 0:
                add_song = False
                print('\nEXITING...')
                time.sleep(3)
                os.system('cls')
            else:
                print('\nERROR: Input Not Available')
                time.sleep(3)
        with open('favourite_songs.json', 'w') as file_ref:
            json.dump(fav_songs, file_ref)
    elif user_selection == 5:
        print("Remove from Favourites")
        choose_song = input()
    elif user_selection == 6:
        os.system('cls')
        print("DISPLAY FAVOURITES")
        if os.path.getsize('favourite_songs.json') > 0:
            with open('favourite_songs.json', 'r') as file_ref:
                fav_songs = json.load(file_ref)
                displayAll(fav_songs)
        else:
            print('\nNo Songs in Favourites')
            time.sleep(3)
        loop = False
    elif user_selection == 0:
        loop = False
        print('\nExiting Library...')
        time.sleep(3)
        os.system('cls')
