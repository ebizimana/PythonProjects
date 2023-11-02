import pandas
# data = pandas.read_csv("weather_data.csv")
# temp_list = data["temp"].to_list()
# # average = sum(temp_list) / len(temp_list)
# # print(round(average, 2))
# # mean
# max_temp = data["temp"].max()
# max_raw = data[data.temp == max_temp]
# print(max_raw)
#
# # Write using panda
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

# The long Method:
# colors = data["Primary Fur Color"].to_list()
# grey = 0
# red = 0
# black = 0
# for color in colors:
#     if color == "Gray":
#         grey += 1
#     elif color == "Cinnamon":
#         red += 1
#     elif color == "Black":
#         black += 1

# The shorter Method:
grey = len(data[data["Primary Fur Color"] == "Gray"])
red = len(data[data["Primary Fur Color"] == "Cinnamon"])
black = len(data[data["Primary Fur Color"] == "Black"])

fur_colors = {
    "fur Color": ["grey", "red", "black"],
    "Count": [grey, red, black]
}
print(fur_colors)
fur_colors_files = pandas.DataFrame(fur_colors)
fur_colors_files.to_csv("squirrel_count.csv")
