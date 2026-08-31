appliances = [
    {"device_name": "Refrigerator", "wattage": 150, "usage_hours": 24},
    {"device_name": "Air Conditioner", "wattage": 1500, "usage_hours": 8},
    {"device_name": "Washing Machine", "wattage": 500, "usage_hours": 2},
    {"device_name": "Television", "wattage": 120, "usage_hours": 6},
    {"device_name": "Microwave", "wattage": 1200, "usage_hours": 0.5},
    {"device_name": "Electric Water Heater", "wattage": 2000, "usage_hours": 3},
    {"device_name": "Laptop", "wattage": 65, "usage_hours": 8},
    {"device_name": "LED Lighting", "wattage": 50, "usage_hours": 10},
    {"device_name": "Ceiling Fan", "wattage": 75, "usage_hours": 12},
    {"device_name": "Electric Iron", "wattage": 1000, "usage_hours": 0.5}
]


def calculate_energy_consumption(appliances):
    total_energy_consumption = 0
    for appliance in appliances:
        energy_consumption = appliance["wattage"] * appliance["usage_hours"] / 1000  # Convert to kWh
        total_energy_consumption += energy_consumption
        print(f"{appliance['device_name']} consumes {energy_consumption} kWh per day.")
    return total_energy_consumption


def calculate_energy_consumption_weekly(appliances):
    total_energy_consumption = 0
    for appliance in appliances:
        energy_consumption = appliance["wattage"] * appliance["usage_hours"] / 1000  # Convert to kWh
        total_energy_consumption += energy_consumption
        print(f"{appliance['device_name']} consumes {energy_consumption} kWh weekly.")

    total_energy_consumption *= 7
    print(f"Total energy consumption for the week: {total_energy_consumption} kWh.")
    return total_energy_consumption



check_agreemnent = input("Do you want anything ?(yes/no): ")

try:

    while check_agreemnent.lower() == "yes":
        print("--------------------------------------")
        print("                                      ")
        task = input("What kwh do you want to calculate?(daily/weekly) ")
        print("--------------------------------------")
        print("                                      ")
        if task.lower() == "daily":
            calculate_energy_consumption(appliances)
            print("--------------------------------------")
            print("                                      ")
            check_agreemnent = input("Do you want to calculate weekly?(yes/no): ")
            print("--------------------------------------")
            print("                                      ")
            if check_agreemnent.lower() == "yes":
                print("--------------------------------------")
                print("                                      ")
                calculate_energy_consumption_weekly(appliances)
                break               
            else:
                print("Thank you for using the appliance energy calculator.")
                break
                 
                 
        elif task.lower() == "weekly":
                calculate_energy_consumption_weekly(appliances)
                check_agreemnent = input("Do you want to calculate daily?(yes/no): ")
                print("--------------------------------------")
                print("                                      ")
                if check_agreemnent.lower() == "yes":
                    print("--------------------------------------")
                    print("                                      ")
                    calculate_energy_consumption(appliances)
                    break
                    
                elif check_agreemnent.lower() == "no":
                    print("Thank you for using the appliance energy calculator.")
                    break

        elif check_agreemnent.lower() == "no":
            print("--------------------------------------")
            print("                                      ")
            print("Thank you for using the appliance energy calculator.")
                  

except TypeError:
    print("Invalid input. Please enter 'daily' or 'weekly'.")
except SyntaxError:
    print("That's a syntax error. Please check your inputs.")
#------------------------------------------




