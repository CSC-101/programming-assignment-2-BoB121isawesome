import data
from data import Point, Rectangle

# Write your functions for each part in the space below.

# Part 1
def create_rectangle(point1, point2):
    top_left= Point(min(point1.x,point2.x),max(point1.y,point2.y))
    bottom_right= Point(max(point1.x,point2.x),min(point1.y,point2.y))
    return Rectangle(top_left,bottom_right)

# Part 2
def shorter_duration_than(dur1,dur2):
    if dur1.minutes != dur2.minutes:
        return dur1.minutes < dur2.minutes
    return dur1.seconds < dur2.seconds

# Part 3
def songs_shorter_than(song_list,dur):
    short_songs=[]
    for i in range(len(song_list)):
        if shorter_duration_than(song_list[i].duration,dur) == True:
            short_songs.append(song_list[i])
    return short_songs

# Part 4
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
def largest(some_list:[[int]]):
    large=0
    for i in range(len(some_list)):
        if some_list[large][0] <some_list[i][0]:
            large=i
    return large


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
