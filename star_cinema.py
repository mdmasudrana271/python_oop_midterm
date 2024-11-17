class Star_cinema:
    
    hall_list = []    
    @classmethod
    def entry_hall(self,hall):
        self.hall_list.append(hall)


class Hall(Star_cinema):
    def __init__(self,rows:int,cols:int,hall_no:int) -> None:
        super().__init__()
        self.__seats = {}
        self.__show_list = []
        self.__rows = rows
        self.__cols = cols
        self.__hall_no = hall_no

        Star_cinema.entry_hall(self)


    def entry_show(self,show_id,movie_name,show_time):
        show_details = (show_id,movie_name,show_time)
        self.__show_list.append(show_details)

        seats_allocations = [["Free" for _ in range(self.__cols)] for _ in range(self.__rows)]

        self.__seats[show_id] = seats_allocations

    def book_seats(self,show_id,seat_list):
        if show_id not in self.__seats:
            print(f"Show id {show_id} does not exist")
            return
            
        for row, col in seat_list:
                if row < 0 or row > self.__rows or col<0 or col >self.__cols:
                    print(f"given seat is out of range")
                    continue
                if self.__seats[show_id][row-1][col-1]=="Booked":
                    print("This seat is already booked")

                else:
                    self.__seats[show_id][row-1][col-1]="Booked"
                    print(f"Seat ({row},{col}) booked successfully!")
            
        

    
    def view_show_list(self):
        if not self.__show_list:
            print("No shows are currently running ")
        else:
            print("\nShow list:\n")
            for show in self.__show_list:
                print(f"Show ID:{show[0]} Movie Name: {show[1]}, Show Time: {show[2]}\n")

    def view_available_seats(self,show_id):
        if show_id not in self.__seats:
            print(f"Show ID {show_id} does not exist")
        else:
            print(f"Available seats for show: {show_id}\n")
            flag = False
            for row in range(self.__rows):
                for col in range(self.__cols):
                    if self.__seats[show_id][row-1][col-1]=="Free":
                        print(f"{self.__seats[show_id][row][col]}",end=" ")
                        flag = True
                    elif self.__seats[show_id][row-1][col-1]=="Booked":
                        print(f"{self.__seats[show_id][row][col]}",end=" ")
                    
                print("")

            if not flag:
                print("No seats are available in this show")

            print("")


def cinema():
    print("Wellcome To Star Cinema!")

    while True:
        print("\nMenu")
        print("1. View all show")
        print("2. View available seats for shows")
        print("3. Book seats for a show")
        print("4. Exit")

        choice =int(input("Enter your choice: "))

        if choice == 1:
            hall_no = int(input("Enter Hall Number: "))
            hall = Star_cinema.hall_list[hall_no-1]
            hall.view_show_list()
        elif choice ==2:
            hall_no = int(input("Enter Hall Number: "))
            hall = Star_cinema.hall_list[hall_no-1]
            show_id = input("Enter Show ID: ")
            hall.view_available_seats(show_id)
        elif choice ==3:
            hall_no = int(input("Enter Hall Number: "))
            hall = Star_cinema.hall_list[hall_no-1]
            show_id = input("Enter Show ID: ")
            seat_cnt = int(input("Enter how many seat do you want to book: "))
            seat_list = []
            for _ in range(seat_cnt):
                row = int(input("Enter Row: "))
                col = int(input("Enter Column: "))
                seat_list.append((row,col))

            hall.book_seats(show_id,seat_list)
        elif choice ==4:
            print("Thank you for using Star Cinema. Goodbye!")
            break
        else:
            print("Invalid choice. please try again later.")






hall1 = Hall(10,10,1)

hall1.entry_show("S1","Jawan","05:00 PM")
hall1.entry_show("S2","Pathan","09:00 PM")

hall2 = Hall(10,10,1)
hall2.entry_show("S3","Dunky","11:00 AM")
hall2.entry_show("S4","Don","08:00 AM")


cinema()


                    