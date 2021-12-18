
import json

# Open data/course-info.jsonline, read each line and parse into json
f = open("data/course-info.jsonlines", "r")
w = open("sql/course-info.json", "w")
for line in f:
    # Parse to json
    json_data = json.loads(line)
    
    if json_data['code'] != "CPSC":
        continue

    sql = "INSERT INTO `course` (`course_id`, `code`, `number`, `topic`, `description`, `credit`, `units`, `prerequisites`, `antirequisites`, `corequisites`, `no_gpa`, `repeat`, `notes`) VALUES ('" + str(json_data["cid"]) + "', '" + str(json_data["code"]) + "', '" + str(json_data["number"]) + "', '" + str(json_data["topic"]) + "', '" + str(json_data["description"]) + "', '" + str(json_data["credits"]) + "', '" + str(json_data["units"]) + "', '" + str(json_data["prereq"]) + "', '" + str(json_data["antireq"]) + "', '" + str(json_data["coreq"]) + "', '" + str(json_data["nogpa"]) + "', '" + str(json_data["repeat"]) + "', '" + str(json_data["notes"]) + "');"
    
    # Write to file
    w.write(sql + ";\n")
