# TODO
# The distance Calculation should be looked again!


def gas_stations(distance, tank_size, stations):
    stop_stations = []
    dist_taken = tank_size
    last_station = 0
    for cur_station in stations:
        # print(str(dist_taken) + " " + str(cur_station))
        if dist_taken < cur_station and distance > cur_station:
            # print("here!")
            stop_stations.append(last_station)
            if last_station < tank_size:
                dist_taken = dist_taken + last_station
            else:
                dist_taken += tank_size
        last_station = cur_station
    if dist_taken < distance:
        stop_stations.append[stations[len(stations) - 1]]
    if not stop_stations[0]:
        del stop_stations[0]
    return stop_stations

print(gas_stations(320, 90, [50, 80, 140, 180, 220, 290]))
print()
print(gas_stations(390, 80, [70, 90, 140, 210, 240, 280, 350]))
