def number_of_tickets(prompt):
    input_value = input(prompt)
    while not input_value.isdigit():
        print("please enter valid input")
        input_value = input(prompt)
    return int(input_value)


def play():
    print("please enter the number of tickets accordingly")
    child_ticket = number_of_tickets("please enter number of child tickets")
    adult_ticket = number_of_tickets("please enter number of adult tickets")
    senior_ticket = number_of_tickets("please enter number of senior tickets")
    concession_ticket = number_of_tickets("please enter number of concession tickets")
    total_bill = (child_ticket * 2) + (adult_ticket * 5) + (senior_ticket * 3) + (concession_ticket * 4)
    print(total_bill)



def checkout():
    card_no = input("please enter your credit card details")
    while len(card_no)!=16:
        card_no = input("please enter valid credit card details")
    expiry_date=input("expiry date in the form MM YY")
    while len(expiry_date)!=4:
        expiry_date=input("expiry date in the form MM YY")
    cvv_no = input("please enter cvv")
    while len(cvv_no) != 3:
        cvv_no = input("enter correct cvv")
    print("payment successfull!")

def main():
    main_menu = input("u wamt reservation  enter reservation(r) or  no(n)").lower()
    while main_menu != "n":
        play()
        end=input("checkout r quit").lower()
        if end == "c":
            checkout()
        else:
            print("thank you")
        return main()
main()
