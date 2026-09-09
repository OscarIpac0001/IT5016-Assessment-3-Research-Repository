# requisitionsystem.py
# Author: Oscar Ipac
# Part B - Requisition System Prototype

# Global counter for generating unique Requisition IDs
requisition_counter = 10000

# Store all requisition objects
requisitions = []

# Maintainability improvement:
# Using global variables works for this small program, but
# keeping this data inside the class would make the program
# easier to manage as it becomes larger.


# Object-Oriented Programming:
# The class groups the requisition data and related methods together.
# This allows multiple requisition objects to use the same structure.
class RequisitionSystem:

    # Initialise the information for a requisition
    def __init__(self):

        # Store the date of the requisition
        self.date = ""

        # Store the staff ID
        self.staff_id = ""

        # Store the staff name
        self.staff_name = ""

        # Store unique requisition ID
        self.requisition_id = 0

        # Store the total cost
        self.total = 0

        # Store the current status
        self.status = "Pending"

        # Store the approval reference number
        self.approval_reference = "Not available"
    # Modularity:
    # This method has one main responsibility: collecting staff information.
    # Separating this task into a method makes the program easier to understand
    # and allows the method to be reused when creating requisitions.
    def staff_info(self):

        # Use the global requisition counter to generate a unique ID
        global requisition_counter

        # Increase the counter by 1 to create a new requisition ID
        requisition_counter += 1

        # Store the new requisition ID in the requisition object
        self.requisition_id = requisition_counter

        # Ask the staff member to enter the date
        date = input("Enter the date (dd/mm/yyyy): ")

        # Format the date as dd/mm/yyyy
        if len(date) == 8:
            date = date[:2] + "/" + date[2:4] + "/" + date[4:]

        # Store the entered date in the requisition object
        self.date = date

        # Ask the staff member to enter their staff ID
        staff_id = input("Enter Staff ID: ").upper()

        # Store the entered staff ID in the requisition object
        self.staff_id = staff_id

        # Ask the staff member to enter their name
        staff_name = input("Enter Staff Name: ").title()

        # Store the entered staff name in the requisition object
        self.staff_name = staff_name

        # Add this requisition object to the list
        requisitions.append(self)

        # Return the staff information for the requisition
        return date, staff_id, staff_name, self.requisition_id

    # Method to enter requisition items and calculate the total cost
    def requisitions_details(self):

        # Create an empty list to store requisition items and their cost
        items = []

        # Keep asking for requisition items until the member chooses to stop
        while True:

            # Ask the staff member to enter the item name
            item = input("Enter item name:")

            # Input validation improvement:
            # The price is converted directly to a float.
            # If the user enters text instead of a number, the program will produce an error.
            # A validation loop could be added to make the program more reliable.
            price = float(input("Enter item price: $"))

            # Add the item and its price to the requisition list
            items.append((item, price))

            # Ask if the staff member wants to add another item
            another = input("Add another item? (yes/no): ").strip().lower()

            # Stop entering items if the staff member does not enter yes
            if another != "yes":
                break   

        # Add a blank line before the next requisition
        print()

        # Calculate the total cost of all requisition items
        self.total = sum(price for item, price in items)

        # Return the total cost of the requisition
        return self.total

    # Method to check the requisition total and determine its approval status
    def requisition_approval(self):

        # Get total cost of the requisition
        self.requisitions_details()

        # Check if the total cost is less than $500
        if self.total < 500:

            # Set the requisition status to approved
            self.status = "Approved"

            # Create the approval reference number
            self.approval_reference = str(self.staff_id) + str(self.requisition_id)[-3:]

        else:

            # Keep the requisition status as pending
            self.status = "Pending"

        # Return all requisition information
        return self.total, self.date, self.staff_id, self.staff_name, self.requisition_id, self.status, self.approval_reference

    # Method for manager to respond to a pending requisition
    def respond_requisition(self):

        # Check if the requisition is still pending
        if self.status == "Pending":

            # Ask the manager for their response
            response = input(f"Manager response for Requisition {self.requisition_id} - {self.staff_name} (Approve/Not approve/Pending): ").strip().lower()

            # If the manager approves the requisition
            if response == "approve":

                # Change the requisition status to approved
                self.status = "Approved"

                # Create the approval reference number using the staff ID and requisition ID
                self.approval_reference = str(self.staff_id) + str(self.requisition_id)[-3:]

            # Check if the manager does not approve the requisition
            elif response == "not approve":

                # Change the requisition status to not approved
                self.status = "Not approved"

            # Check if the manager keeps the requisition pending
            elif response == "pending":

                # Keep requisition pending
                self.status = "Pending"

    # Readability:
    # Clear method names and comments make it easier to understand
    # what each part of the program is responsible for.
    def display_requisitions(self):

        # Display the date of the requisition
        print("Date:", self.date)
            
        # Display the unique requisition ID
        print("Requisition ID:", self.requisition_id)

        # Display staff ID
        print("Staff ID:", self.staff_id)
            
        # Display staff name
        print("Staff Name:", self.staff_name)
            
        # Display total with a dollar sign and no decimal places
        print("Total: $" + f"{self.total:.0f}")
            
        # Display the current status
        print("Status:", self.status)
            
        # Display approval reference number
        print("Approval Reference Number:", self.approval_reference) 

        # Add a blank line between requisitions
        print()         

    # Method to calculate requisition statistics
    def requisition_statistic(self):

        # Start the submitted requisition count at zero
        total_submitted = 0

        # Start the approved requisition count at zero
        total_approved = 0

        # Start the pending requisition count at zero
        total_pending = 0

        # Start not approved requisition count at zero
        total_not_approved = 0

        # Go through each requisition stored in the requisitions list
        for requisition in requisitions:

            # Increase the submitted requisition count by 1
            total_submitted += 1

            # Check if the requisition has been approved
            if requisition.status == "Approved":

                # Increase the approved requisition count by 1
                total_approved += 1

            # Check if the requisition is pending
            elif requisition.status == "Pending":

                # Increase the pending requisition count by 1
                total_pending += 1

            # Check if the requisition was not approved
            elif requisition.status == "Not approved":

                # Increase the not approved requisition count by 1
                total_not_approved += 1

        # Return all requisition statistic
        return total_submitted, total_approved, total_pending, total_not_approved

# Display heading for all requisitions
print("Printing Requisitions:")

# Add a blank line to separate each requisition
print()

# DRY (Don't Repeat Yourself) improvement:
# The code below is repeated for requisition1 to requisition5.
# A loop could be used instead to reduce repetition and make the
# program easier to extend if more requisitions are required.

# Create new requisition object
requisition1 = RequisitionSystem()

# Enter staff information for the first requisition
requisition1.staff_info()

# Calculate the total and approval status for the first requisition
requisition1.requisition_approval()

# Display the first requisition information
requisition1.display_requisitions()

# Add a blank line to separate each requisition
print()

# Create new requisition object
requisition2 = RequisitionSystem()

# Enter staff information for the second requisition
requisition2.staff_info()

# Calculate the total and approval status for the second requisition
requisition2.requisition_approval()

# Manager responds to the second requisition 
# requisition2.respond_requisition()

# Display the second requisition information
requisition2.display_requisitions()

# Add a blank line to separate each requisition
print()

# Create new requisition object
requisition3 = RequisitionSystem()

# Enter staff information for the third requisition
requisition3.staff_info()

# Calculate the total and approval status for the third requisition
requisition3.requisition_approval()

# Manager responds to the third requisition 
# requisition3.respond_requisition()

# Display the third requisition information
requisition3.display_requisitions()

# Add a blank line to separate each requisition
print()

# Create new requisition object
requisition4 = RequisitionSystem()

# Enter staff information for the fourth requisition
requisition4.staff_info()

# Calculate the total and approval status for the fourth requisition
requisition4.requisition_approval()

# Display the fourth requisition information
requisition4.display_requisitions()

# Add a blank line before the statistics section 
print()

# Create new requisition object
requisition5 = RequisitionSystem()

# Enter staff information for the fifth requisition
requisition5.staff_info()

# Calculate the total and approval status for the fifth requisition
requisition5.requisition_approval()

# Manager responds to the fifth requisition
# requisition5.respond_requisition()

# Display the statistics before manager responses
print()
print("Statistics Before Manager Responses:")

# Calculate the current requisition statistics
total_submitted, total_approved, total_pending, total_not_approved = requisition1.requisition_statistic()

# Display the number of requisitions submitted
print("The total number of requisitions submitted:", total_submitted)

# Display the number of approved requisitions
print("The total number of approved requisitions:", total_approved)

# Display the number of pending requisitions
print("The total number of pending requisitions:", total_pending)

# Display the number of not approved requisitions
print("The total number of not approved requisitions:", total_not_approved)

# Manager responds to the second requisition
requisition2.respond_requisition()

# Manager responds to the third requisition
requisition3.respond_requisition()

# Manager responds to the fifth requisition
requisition5.respond_requisition()

# Display the fifth requisition information
# requisition5.display_requisitions()

# Add a blank line before the statistics section
print()

# Display the statistics heading
print("Statistics:")

# Display all requisitions after manager responses
print("Requisitions After Manager Responses:")

# Display all requisition information
for requisition in requisitions:
    requisition.display_requisitions()

# Add a blank line 
print()

# Display the heading for the requisition statistics
print("Displaying the Requisition Statistics")

# Calculate total requisition statistics
total_submitted, total_approved, total_pending, total_not_approved = requisition1.requisition_statistic()

# Display the total number of submitted requisitions
print("The total number of requisitions submitted:", total_submitted)

# Display the total number of approved requisitions
print("The total number of approved requisitions:", total_approved)

# Display the total number of pending requisitions
print("The total number of pending requisitions:", total_pending)

# Display the total number of not approved requisitions
print("The total number of not approved requisitions:", total_not_approved)
