import data
from data import Point, Rectangle

# Write your functions for each part in the space below.

# Part 1
# Creates a rectangle defined by two points and returns it.
# Parameters: point1 (Point): The first point.
#     point2 (Point): The second point.
# Returns: Rectangle: A rectangle with top_left and bottom_right corners.
def create_rectangle(point1, point2):
    top_left= Point(min(point1.x,point2.x),max(point1.y,point2.y))
    bottom_right= Point(max(point1.x,point2.x),min(point1.y,point2.y))
    return Rectangle(top_left,bottom_right)

# Part 2
# Compares two durations and checks if the first duration is shorter than the second.
#  Parameters: dur1 (data.Duration): The first duration.
#     dur2 (data.Duration): The second duration.
#  Returns: bool: True if dur1 is shorter than dur2, otherwise False.
def shorter_duration_than(dur1,dur2):
    if dur1.minutes != dur2.minutes:
        return dur1.minutes < dur2.minutes
    return dur1.seconds < dur2.seconds

# Part 3
# Filters a list of songs to include only those with a shorter duration than the specified duration.
# Parameters: song_list (list[data.Song]): A list of Song objects.
#     dur (data.Duration): The maximum duration to filter by.
# Returns: list[data.Song]: A list of songs shorter than the given duration.
def songs_shorter_than(song_list,dur):
    short_songs=[]
    for i in range(len(song_list)):
        if shorter_duration_than(song_list[i].duration,dur) == True:
            short_songs.append(song_list[i])
    return short_songs

# Part 4
# Calculates the total running time of a subset of songs specified by indices.
# Parameters: songs_list (list[data.Song]): A list of Song objects.
#    num_list (list[int]): A list of indices referencing songs in songs_list.
# Returns: data.Duration: The total duration of the specified songs.
def running_time(songs_list,num_list):
    run_time=data.Duration(0,0)
    for song in num_list:
        run_time.minutes=run_time.minutes+songs_list[song].duration.minutes
        run_time.seconds=run_time.seconds+songs_list[song].duration.seconds
    while run_time.seconds>=60:
        run_time.seconds=run_time.seconds-60
        run_time.minutes=run_time.minutes+1
    return run_time

# Part 5
# Validates if a given route follows the available routes list.
# Parameters: routes (list[list[int]]): A list of valid routes represented as pairs of cities.
#     route (list[int]): A specific route to validate as a list of cities.
# Returns: bool: True if the route is valid based on the routes list, otherwise False.
def validate_route(routes:list[list],route:list):
    valid_routes=len(route)-1
    for i in range(len(routes)-2):
        city1 = route[i]
        city2 = route[i+1]
        if ([city1,city2] not in routes) and ([city2,city1] not in routes):
            valid_routes==valid_routes
        else:
            valid_routes=valid_routes-1
    if valid_routes==0:
        return True
    else:
        return False

# Part 6
# Finds the index of the sublist with the largest first element.
# Parameters: some_list (list[list[int]]): A list of integer sublists.
# Returns: int: The index of the sublist with the largest first element.
def largest(some_list:[[int]]):
    large=0
    for i in range(len(some_list)):
        if some_list[large][0] <some_list[i][0]:
            large=i
    return large

#Finds the length of the longest consecutive repetition in a list of numbers.
# Parameters: num_list (list[int]): A list of integers.
# Returns: int or None: The length of the longest repetition or None if the list is empty.
def longest_repetition(num_list):
    if len(num_list)==0 or num_list == []:
        return None
    counter=1
    index=0
    counts_array=[]
    for i in range(len(num_list)-1):
        if num_list[i]==num_list[i+1]:
            counter=counter+1
        else:
            counts_array.append([counter,index])
            index= i + 1
            counter=1
    counts_array.append([counter, index])
    return counts_array[largest(counts_array)][1]
