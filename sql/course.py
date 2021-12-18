
import json

# Open data/course-info.jsonline, read each line and parse into json
f = open("data/course-info.jsonlines", "r")
w = open("sql/course-info.sql", "w")
for line in f:
    # Parse to json
    json_data = json.loads(line)

    if json_data["code"] != "CPSC":
        continue

    # For every key in json_data
    for key in json_data:
        if json_data[key] == None:
            json_data[key] = "null"
        elif json_data[key] == True:
            json_data[key] = "true"
        elif json_data[key] == False:
            json_data[key] = "false"
        elif type(json_data[key]) == int or type(json_data[key]) == float:
            json_data[key] = str(json_data[key])
        else:
            json_data[key] = "'" + str(json_data[key]) + "'"

    # sql = "INSERT INTO `course` (`course_id`, `code`, `number`, `topic`, `description`, `credits`, `units`, `prerequisites`, `antirequisites`, `corequisites`, `no_gpa`, `repeat`, `notes`) "
    sql = "INSERT INTO `course` "
    sql += "VALUES (" + str(json_data["cid"]) + ", " + str(json_data["code"]) + ", " + str(json_data["number"]) + ", " + str(json_data["topic"]) + ", " + str(json_data["description"]) + ", " + str(json_data["credits"]) + ", " + str(json_data["units"]) + ", " + str(json_data["prereq"]) + ", " + str(json_data["antireq"]) + ", " + str(json_data["coreq"]) + ", " + str(json_data["nogpa"]) + ", " + str(json_data["repeat"]) + ", " + str(json_data["notes"]) + ");"
    
    # Write to file
    w.write(sql + "\n")
