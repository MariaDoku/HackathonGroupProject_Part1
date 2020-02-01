import sys, json

def create_json(bus_route, stop_name, user_time):
    """
    Creates .json file for an bus info file, can be accessed by vanillaJS or html

    example inputs:
    bus_route: "71B"
    stop_name: "HIGHLAND AVE AT FIFTH AVE"
    user_time: "12:00:00"

    :param str bus_route: name of bus route (letters and numbers)
    :param str stop_name: bus stop (number or street names)
    :param str user_time: time in military format
    :returns: name of json file
    """
    stop_name_text = stop_name.replace(' ', "-")
    user_time_text = user_time.replace(':', '-')

    json_file = bus_route + "_" + stop_name_text + "_" + user_time_text + ".json"

    bus_route_line = ' "bus_route" : "' + bus_route + '", \n'
    bus_stop_name_line = ' "stop_name" : "' + stop_name + '", \n'
    user_time_line = ' "user_time" : "' + user_time + '" \n'


    with open(json_file, "w") as writefile:
        writefile.write("{\n")
        writefile.write(bus_route_line)
        writefile.write(bus_stop_name_line)
        writefile.write(user_time_line)
        writefile.write("}\n")

    return json_file

#sys.argv grabs the n=1 argument of the command line
create_json(sys.argv[1], sys.argv[2], sys.argv[3])
