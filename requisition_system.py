
# BACT7501 - Assessment 2
# Software Development Project
# Purchase Requisition System


class Requisition:
    requisition_counter = 0

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

            if item_price <= 0:
                print("Item price must be greater than zero.")
                continue

            self.items.append([item_name, item_price])
            self.total = self.total + item_price

            while True:
                another_item = input("Add another item (yes/no): ").strip().lower()

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


# Testing the requisition and approval methods
if __name__ == "__main__":
    requisition1 = Requisition("01/11/2026", "ST24", "Test Staff")

    print("Requisition ID:", requisition1.requisition_id)
    print("Staff Name:", requisition1.staff_name)

    requisition1.add_requisition()
    requisition1.approve_requisition()

    print("\nApproval Information:")
    print("Total: $" + format(requisition1.total, ".2f"))
    print("Status:", requisition1.status)
    print("Approval Reference Number:", requisition1.approval_reference)
