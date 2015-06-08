__author__ = 'Shtav'

# This file takes json, processes the information (in this case, just the
# Youtube URL). Use with caution; it does not check if movie already exists,
# meaning you can end up with duplicates.
import json
import re
import sys
import ast


def manually_add_movie(processed_data_file):  # Dialog input: user adds movie
    new_movie = {
        'title': take_user_input("title", []),
        'poster_image_url': take_user_input("poster_image", []),
        'trailer_youtube_url': take_user_input("trailer_youtube_url", []),
        'imdb': take_user_input("imdb", []),
        'itunes': take_user_input("itunes", []),
        'amazon': take_user_input("amazon", []),
        'additional': {
            "release":take_user_input("release", []),
            "director":take_user_input("director", []),
            "actors":take_user_input("actors", []),
            "story_line": take_user_input("story_line", [])
        }
    }
    save_to_json(processed_data_file, process_movie_data(new_movie))
    print('Movie added :)')


def process_movie_file(processed_data_file):  # Returns processed data from file data
    movie_file = open(take_user_input("What is the name/location of the file (relative to this file)?", []), 'r')
    movies = json.load(movie_file)
    for movie in movies:
        movie = process_movie_data(movie)
    save_to_json(processed_data_file, movies)
    print('Movie file added :)')


def process_movie_data(movie_data):  # Returns processed data from file data
    # this function only retrieves Youtube vid IDs from URL
    youtube_id_match = re.search(r'(?<=v=)[^&#]+', movie_data['trailer_youtube_url'])
    youtube_id_match = youtube_id_match or re.search(r'(?<=be/)[^&#]+', movie_data['trailer_youtube_url'])
    trailer_youtube_id = youtube_id_match.group(0) if youtube_id_match else None
    movie_data['trailer_youtube_id'] = trailer_youtube_id
    return movie_data


def save_to_json(file_directory, new_data):  # Save new data to Json file
    try:
        data_read_file = open(file_directory)
        data_read = data_read_file.read()
        data_read_file.close()  # Close data_read after json_data assignment
    except IOError:
        data_read = ""
    if data_read == "":  # Check if any data exists in file
        if type(new_data) == list:
            json_data = new_data
        else:
            json_data = list(new_data)
    else:  # Data does exist, load existing data
        json_data = ast.literal_eval(data_read)  # Str to list
        if type(new_data) == list:
            json_data.extend(new_data)  # If new_data is list, extend existing
        else:
            json_data.append(new_data)  # Add non-list item to list
    data_dump_file = open(file_directory, 'w')  # Overwrite file w/combined data
    json.dump(json_data, data_dump_file, ensure_ascii=False)
    data_dump_file.close()  # Close data_dump after data is stored


def remove_movie(file_directory):
    title = take_user_input('What movie would you like to remove?', [])
    try:
        data_read_file = open(file_directory)
        data_read = data_read_file.read()
        data_read_file.close()  # Close data_read after json_data assignment
    except IOError:
        print('Unable to remove a movie because no such file exists.')
        print('Please try again with a new input')
        sys.exit()
    json_data = ast.literal_eval(data_read)  # Str to list
    for movie in json_data:
        if movie['title'] == title:
            json_data.remove(movie)
            data_dump_file = open(file_directory, 'w')  # Overwrite file w/ new data
            json.dump(json_data, data_dump_file)
            data_dump_file.close()  # Close data_dump after data is stored
            print(title + " deleted :)")

    #print(title + ' was not in the list of movies.')
    print(json_data)


def take_user_input(prompt, responses):
    user_input = raw_input(prompt)
    while user_input not in responses and responses != []:
        print("Please try again. You can respond with " + str(responses) + " or type 'q' to quit.")
        user_input = raw_input(prompt)
    if user_input == 'q' or user_input == 'Q':
        sys.exit()
    elif user_input in responses or responses == []:
        return user_input


def main(processed_data_file):
    a = take_user_input("Manually add (m), add from file (f), or remove a movie (r)", ['m', 'M', 'f', 'F', 'r', 'R'])
    if a == 'm' or a == 'M':  # Manual input
        manually_add_movie(processed_data_file)
    elif a == 'f' or a == 'F':  # Retrieve from file
        process_movie_file(processed_data_file)  # Process data from file
    elif a == 'r' or a == 'R':
        remove_movie(processed_data_file)

    sys.exit()  # prevent recursion by explicitly exiting



# Give the name and location of file you want to mod; if there is none, state
# where you would like the new file to be placed
main('development/data/movies.json')
