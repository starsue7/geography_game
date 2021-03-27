import turtle
import pandas
import time

screen = turtle.Screen()
screen.title('GeoKids')
image = 'map.gif'
screen.addshape(image)
turtle.shape(image)

starting_time = time.time()
time_limit = 300

data = pandas.read_csv('data_districts.csv')
all_districts = data.district.to_list()

guessed_districts = []
missed_districts = []

condition = turtle.Turtle()
condition.hideturtle()
condition.penup()
condition.goto(-290, 300)
condition.write('Разполагаш с 5 минути за да въведеш всички области', font=('Ariel', 15, 'bold'))

def write_district(name, color):
    t = turtle.Turtle()
    t.hideturtle()
    t.color(color.strip())
    t.penup()
    district_data = data[data.district == name]
    t.goto(int(district_data.x), int(district_data.y))
    t.write(name, font=('Ariel', 12, 'bold'))

while (time.time() - starting_time) < time_limit:
    if len(guessed_districts) < 28:
        answer_district = screen.textinput(title=f'{len(guessed_districts)}/28 познати',
                                               prompt='Въведи област').title()
        if (time.time() - starting_time) > time_limit:
            for district in all_districts:
                if district not in guessed_districts:
                    missed_districts.append(district)
            for missed in missed_districts:
                write_district(missed, 'medium blue')
            condition.clear()
            condition.goto(-100, 300)
            condition.write("ЗАГУБА!", font=("Arial", 30, 'normal'))
            break

        if answer_district in all_districts and answer_district not in guessed_districts:
            guessed_districts.append(answer_district)
            write_district(answer_district, 'black')


    elif len(guessed_districts) == 28 and (time.time() - starting_time) < time_limit:
        condition.clear()
        condition.goto(-100, 300)
        condition.write("ПОБЕДА!", font=("Arial", 30, 'normal'))
        break

turtle.mainloop()

