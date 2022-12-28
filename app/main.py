class Car:
    def __init__(
            self, comfort_class: int, clean_mark: int, brand: str
    ) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(
            self, distance_from_city_center: float,
            clean_power: int, average_rating: float,
            count_of_ratings: int,
    ) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: list) -> float:
        cws = CarWashStation
        income = 0
        for car in cars:
            if car.clean_mark < self.clean_power:
                income += cws.calculate_washing_price(self, car)
                car.clean_mark = cws.wash_single_car(self, car)
        return round(income, 1)

    def calculate_washing_price(self, car: Car) -> float:
        short = (self.clean_power - car.clean_mark) * self.average_rating
        wash_cost = car.comfort_class * short / self.distance_from_city_center
        return round(wash_cost, 1)

    def wash_single_car(self, car: Car) -> int:
        if self.clean_power >= car.clean_mark:
            car.clean_mark = self.clean_power
            return car.clean_mark

    def rate_service(self, new_mark: int) -> float:
        rate_sum = self.average_rating * self.count_of_ratings + new_mark
        self.count_of_ratings += 1
        new_rating = rate_sum / self.count_of_ratings
        self.average_rating = round(new_rating, 1)
        return self.average_rating
