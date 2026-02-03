class Vehicle:
    def __init__(self, vehicle_id, brand, rent_per_day):
        self.vehicle_id = vehicle_id
        self.brand = brand
        self.rent_per_day = rent_per_day

    def display_details(self):
        print("Vehicle ID:", self.vehicle_id)
        print("Brand:", self.brand)
        print("Rent per day:", self.rent_per_day)

    def calculate_rent(self, days):
        return self.rent_per_day * days

v1 = Vehicle(1, "Toyota", 1000)
v2 = Vehicle(2, "Honda", 2000)
print("Vehicle 1 Details:")
v1.display_details()
print("\n")
print("Vehicle 2 Details:")
v2.display_details()
print("\n")
print("Rent for Vehicle 1 for 5 days:", v1.calculate_rent(5))
print("Rent for Vehicle 2 for 3 days:", v2.calculate_rent(3))
