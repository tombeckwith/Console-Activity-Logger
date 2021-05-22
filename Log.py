from datetime import datetime
import os
import csv

class Log():
    def __init__(self):
        self.date = datetime.now()
        self.detail = []

    def add_detail(self, *detail):
        self.detail.append([self.date.__str__(), *detail])
    
    def read_detail(self):
        for detail in self.detail:
            print(detail)

    def time_spent(self):
        t = 0
        for _, _, _, m in self.detail:
            t += m
        return t
    
    def save(self):
        if not os.path.isfile(os.path.join(os.path.dirname(__file__), 'log.csv')):
            try:
                with open(os.path.join(os.path.dirname(__file__), 'log.csv'), "w") as file:
                    csv_writer = csv.writer(file)
                    csv_writer.writerow([
                        "Logged", 
                        "Category",
                        "Name",
                        "Minutes",
                    ])
            except:
                print("Unable to create file")
                exit()
        try:
            with open(os.path.join(os.path.dirname(__file__), 'log.csv'), "a") as file:
                csv_writer = csv.writer(file)
                csv_writer.writerows(self.detail)
            
            print(f"\nSAVED ({len(self.detail)} lines written to log.csv)\n")
            self.detail = []
        except:
            print("Fail. Something went wrong. Unable to write to log.csv\n")


if __name__ == "__main__":
    logger = Log()

    categories = [
        "Computers",
        "Phones",
        "Network",
        "CMS",
        "Invoicing"
    ]

    print("\nIT AND SYSTEMS SUPPORT LOGGER")
    log = input("\nActivity to be logged? (y/n): ")
    if log.lower() != "y":
        exit()

    print('\nCATEGORIES')
    for i, category in enumerate(categories):
        print(f"{i+1}: {category}")
    selected = []
    category = input("\nPlease choose categories separated by a comma:\n")
    if category == "":
        exit()
    [selected.append([int(x)-1, categories[int(x)-1]]) for x in category.split(",")]

    print("\nTIME SPENT (minutes)\n")
    for i, cat in enumerate(selected):
        mins = input(f"{cat[0]}: {categories[cat[0]]:<15}: ")
        selected[i].append(int(mins))
        logger.add_detail(*selected[i])

    if logger.time_spent() > 60:
        time_check = input(f"\nTotal logged time exceeds 60 minutes ({logger.time_spent()}).\nConfirm save? (y/n): ")
        if time_check.lower() == "y":
            logger.save()
    else:
        logger.save()
