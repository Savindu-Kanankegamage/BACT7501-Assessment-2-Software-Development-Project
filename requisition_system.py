
# BACT7501 - Assessment 2
# Software Development Project
# Purchase Requisition System

from datetime import datetime
import math


class Requisition:
    requisition_counter = 0
    all_requisitions = []

    def __init__(self, date, staff_id, staff_name):
        Requisition.requisition_counter += 1

        self.requisition_id = 10000 + Requisition.requisition_counter
        self.date = date
        self.staff_id = staff_id
        self.staff_name = staff_name

        self.items = []
        self.total = 0.0
        self.status = "Pending"
        self.approval_reference = "Not available"

        Requisition.all_requisitions.append(self)

    def add_requisition(self):
        print("\nEnter purchase items:")

        while True:
            item_name = input("Item Name: ").strip()

            if item_name == "":
                print("Please enter an item name.")
                continue

            try:
                item_price = float(input("Item Price ($): "))
            except ValueError:
                print("Please enter a valid price.")
                continue

            # Step 17 - Price Validation Fix
            if not math.isfinite(item_price):
                print("Invalid price. Please enter a finite number.")
                continue

            if item_price <= 0:
                print("Item price must be greater than zero.")
                continue

            self.items.append([item_name, item_price])
            self.total = self.total + item_price

            while True:
                another_item = input(
                    "Add another item (yes/no): "
                ).strip().lower()

                if another_item == "yes" or another_item == "no":
                    break

                print("Please enter yes or no.")

            if another_item == "no":
                break

        return self.total

    def approve_requisition(self):
        self.status = "Pending"
        self.approval_reference = "Not available"

        if self.total < 500:
            self.status = "Approved"
            self.approval_reference = (
                self.staff_id + str(self.requisition_id)[-3:]
            )

        return self.status

    # Step 18 - Improved Manager Response
    def manager_response(self, decision):
        if self.status != "Pending":
            print("Only pending requisitions can be reviewed.")
            return False

        decision = decision.strip().lower()

        if decision == "approved":
            self.status = "Approved"
            self.approval_reference = (
                self.staff_id + str(self.requisition_id)[-3:]
            )

        elif decision == "not approved":
            self.status = "Not approved"
            self.approval_reference = "Not available"

        else:
            print("Invalid decision. Status remains Pending.")
            return False

        print("Manager decision updated successfully.")
        return True

    # Display Requisitions
    def display_requisitions(self):
        print("\nPrinting requisitions:")
        print("Date:", self.date)
        print("Requisition ID:", self.requisition_id)
        print("Staff ID:", self.staff_id)
        print("Staff Name:", self.staff_name)

        print("Items:")
        for item in self.items:
            print(" -", item[0], "- $" + format(item[1], ".2f"))

        print("Total: $" + format(self.total, ".2f"))
        print("Status:", self.status)
        print("Approval Reference Number:", self.approval_reference)

    # Requisition Statistics
    def requisition_statistics(self):
        total_submitted = len(Requisition.all_requisitions)
        approved = 0
        pending = 0
        not_approved = 0

        for requisition in Requisition.all_requisitions:
            if requisition.status == "Approved":
                approved += 1

            elif requisition.status == "Pending":
                pending += 1

            elif requisition.status == "Not approved":
                not_approved += 1

        print("\nRequisition Statistics:")
        print("Total Submitted:", total_submitted)
        print("Approved:", approved)
        print("Pending:", pending)
        print("Not approved:", not_approved)


# Create Multiple Requisitions
if __name__ == "__main__":
    print("Purchase Requisition System")

    while True:
        try:
            number = int(input("How many requisitions? (minimum 5): "))

            if number >= 5:
                break

            print("Please enter at least 5 requisitions.")

        except ValueError:
            print("Please enter a valid whole number.")

    requisitions = []

    for i in range(number):
        print("\nRequisition", i + 1)

        # Step 17 - Date Validation Fix
        while True:
            date = input("Date (DD/MM/YYYY): ").strip()

            try:
                valid_date = datetime.strptime(date, "%d/%m/%Y")

                if valid_date.strftime("%d/%m/%Y") != date:
                    print("Please use DD/MM/YYYY format.")
                    continue

                break

            except ValueError:
                print("Invalid date. Please enter a real date in DD/MM/YYYY format.")

        staff_id = input("Staff ID: ").strip()
        while staff_id == "":
            staff_id = input("Please enter Staff ID: ").strip()

        staff_name = input("Staff Name: ").strip()
        while staff_name == "":
            staff_name = input("Please enter Staff Name: ").strip()

        requisition = Requisition(date, staff_id, staff_name)

        print("Requisition ID:", requisition.requisition_id)

        requisition.add_requisition()
        requisition.approve_requisition()

        print("Initial Status:", requisition.status)

        if requisition.status == "Pending":
            while True:
                review = input(
                    "Manager review now (yes/no): "
                ).strip().lower()

                if review == "yes" or review == "no":
                    break

                print("Please enter yes or no.")

            if review == "yes":
                # Retry until the manager enters a valid decision.
                while True:
                    decision = input(
                        "Manager Decision (approved/not approved): "
                    )
                    if requisition.manager_response(decision):
                        break
                    

        requisitions.append(requisition)

        print("Requisition saved successfully.")

    print("\n===== ALL REQUISITIONS =====")

    for requisition in requisitions:
        requisition.display_requisitions()

    print("\n===== FINAL STATISTICS =====")
    requisitions[0].requisition_statistics()
