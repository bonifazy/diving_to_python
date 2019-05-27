import os.path
import csv


class CarBase:
    def __init__(self, brand, photo_file_name, carrying):
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = float(carrying)

    def get_photo_file_ext(self):
        return os.path.splitext(self.photo_file_name)[1]  # split filename to name, ext


class Car(CarBase):
    def __init__(self, brand, passenger_seats_count, photo_file_name, carrying):
        super().__init__(brand, photo_file_name, carrying)  # inheritance
        self.passenger_seats_count = int(passenger_seats_count)
        self.car_type = 'car'


class Truck(CarBase):
    def __init__(self, brand, photo_file_name, body_whl, carrying):
        super().__init__(brand, photo_file_name, carrying)  # inheritance
        self.body_whl = [float(i) for i in body_whl.split('x')] if body_whl else [0.0, 0.0, 0.0]
        self.body_length = self.body_whl[0]
        self.body_width = self.body_whl[1]
        self.body_height = self.body_whl[2]
        self.car_type = 'truck'

    def get_body_volume(self):
        return self.body_length * self.body_width * self.body_height


class SpecMachine(CarBase):
    def __init__(self, brand, photo_file_name, carrying, extra):
        super().__init__(brand, photo_file_name, carrying)  # inheritance
        self.extra = extra
        self.car_type = 'spec_machine'


def get_car_list(csv_file):
    try:
        cars = []
        with open(csv_file) as csv_fd:
            reader = csv.reader(csv_fd, delimiter=';')  # transform
            next(reader)  # skip header
            for row in reader:
                if len(row) > 6:
                    if row[0] == 'car':
                        obj = Car(row[1], row[2], row[3], row[5])
                    elif row[0] == 'truck':
                        obj = Truck(row[1], row[3], row[4], row[5])
                    elif row[0] == 'spec_machine':
                        obj = SpecMachine(row[1], row[3], row[5], row[6])
                    else:
                        continue
                    cars.append(obj)
                else:
                    pass
        return cars
    except OSError:
        print('Error')


if __name__ == "__main__":
    car_list = get_car_list('week3_class_inheritance_csv.csv')
    for car in car_list:
        print(car.__dict__)

"""
{'brand': 'Nissan xTtrail', 'photo_file_name': 'f1.jpeg', 'carrying': 2.5, 'passenger_seats_count': 4, 'car_type': 'car'}
{'brand': 'Man', 'photo_file_name': 'f2.png', 'carrying': 20.0, 'body_whl': [8.0, 3.0, 2.5], 'body_length': 8.0, 'body_width': 3.0, 'body_height': 2.5, 'car_type': 'truck'}
{'brand': 'Man', 'photo_file_name': 'f2.png', 'carrying': 20.0, 'body_whl': [0.0, 0.0, 0.0], 'body_length': 0.0, 'body_width': 0.0, 'body_height': 0.0, 'car_type': 'truck'}
{'brand': 'Mazda 6', 'photo_file_name': 'f3.jpeg', 'carrying': 2.5, 'passenger_seats_count': 4, 'car_type': 'car'}
{'brand': 'Hitachi', 'photo_file_name': 'f4', 'carrying': 1.2, 'extra': 'Легкая техника для уборки снега', 'car_type': 'spec_machine'}
"""
