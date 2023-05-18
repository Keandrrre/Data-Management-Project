# Data Management Project/ Music Playlist
# Imports
import os
import json

# Functions


def displayAll(list):
    for i in range(len(list)):
        print('[' + str(i + 1) + '] ' + list[i]['title'] +
              ' (By ' + list[i]['artist'] + ')')


def filterData(filterBy):
    filterIn = input('Search by ' + str(filterBy) + ': ')
    for i in range(len(songs)):
        if filterIn.lower() in songs[i][str(filterBy)].lower():
            print(songs[i]['title'] + ' (By ' + songs[i]['artist'] + ')')


def loadFavourites():
    if os.path.getsize('favourite_songs.json') > 0:
        with open('favourite_songs.json', 'r') as file_ref:
            return json.load(file_ref)
    else:
        return []


def saveFavourites():
    with open('favourite_songs.json', 'w') as file_ref:
        json.dump(fav_songs, file_ref)


def addToFavourites(song):
    if song > 0 and song - 1 in range(len(songs)) and songs[song - 1] not in fav_songs:
        fav_songs.append(songs[song - 1])
        print('\nSONG ADDED')


def removeFromFavourites(song):
    if song > 0 and len(fav_songs) > song - 1:
        fav_songs.pop(song - 1)
        print('\nSONG REMOVED')


def confirmUser(username):
    ind = -1
    for i in range(len(users)):
        if users[i]['user'] == username:
            ind = i
    return ind


# Lists
users = []
songs = [{'title': 'Jungle', 'artist': 'Drake', "genre": 'Hip-Hop/Rap'}, {'title': 'Replay', 'artist': 'Tems', 'genre': 'Nigerian R&B, Afropop'}, {'title': 'Search & Rescue', 'artist': 'Drake', 'genre': 'Hip-Hop/Rap'}, {'title': 'Kill Bill', 'artist': 'SZA', 'genre': 'Pop music, R&B/Soul, Doo-wop, psychedelic pop, pop soul'},
         {'title': "Creepin'", 'artist': 'Metro Boomin, The Weekend & 21 Savage', 'genre': 'Hip-Hop/Rap'}, {'title': 'drive Me crazy!', 'artist': 'Lil Yachty', 'genre': 'Alternate/Indie'}, {'title': 'Impossible', 'artist': 'Travis Scott', 'genre': 'Hip-Hop/Rap'}]
fav_songs = loadFavourites()

# Sign in/Sign up
sign_in = str(input('[LOGIN]\n\nType "login" or "register": '))
if sign_in.lower() == 'register':
    username = str(input('Username: '))
    password = str(input('Password: '))
    confirm_password = str(input('Confirm Password: '))
    if len(username) == 0 or len(password) == 0 or len(confirm_password) == 0:
        print("\nMissing Inputs")
    elif password == confirm_password and confirmUser(username) == -1:
        users.append({'user': username, 'password': password})
elif sign_in.lower() == 'login':
    username = str(input('Username: '))
    password = str(input('Password: '))


# User Options
user_selection = int(input(
    "[SONG LIBRARY]\n1-Display All\n2-Filter Songs\n3-Sort Songs\n4-Add Songs to Favourites\n5-Remove Songs from Favourites\n6-Display Favourites\n\nInput: "))
if user_selection == 1:
    # Display All Songs
    os.system('cls')
    print('[ALL SONGS]')
    displayAll(songs)
elif user_selection == 2:
    # Filter songs
    filterBy = input('Options: "title" "artist" "genre": ')
    filterData(filterBy)
elif user_selection == 3:
    os.system('cls')
    # Sort List
    sort_by = input(
        '[SORT]\n\n1-By Title\n2-By Artist\n3-By Genre\n\nEnter Here:')
    if sort_by == 1:
        songs.sort()
    loop = False
elif user_selection == 4:
    # Add To Favourites
    os.system('cls')
    print('[ADD TO FAVOURITES]')
    displayAll(songs)
    choose_song = int(input('Enter the # of the song you want to add: '))
    addToFavourites(choose_song)
    saveFavourites()
elif user_selection == 5:
    os.system("cls")
    print("[Remove from Favourites]")
    displayAll(fav_songs)
    choose_song = int(input('\nEnter # of song you want to remove: '))
    removeFromFavourites(choose_song)
    saveFavourites()
elif user_selection == 6:
    os.system('cls')
    print("[FAVOURITE SONGS]")
    displayAll(fav_songs)
