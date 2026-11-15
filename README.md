
# Purchase Requisition System

## BACT7501 - Assessment 2

Software Development Project

## Project Description

This project is a Purchase Requisition System developed using Python and Object-Oriented Programming (OOP). It builds on the programming logic from Assessment 1 and allows users to create purchase requisitions, process approvals and view requisition statistics.

## System Features

- Enter staff details and purchase items.
- Calculate the total cost of each requisition.
- Generate unique requisition IDs.
- Automatically approve requisitions with a total below $500.
- Keep requisitions of $500 or more Pending until a manager reviews them.
- Allow managers to approve or not approve Pending requisitions.
- Generate approval reference numbers for approved requisitions.
- Display requisition details and statistics.
- Validate dates, item prices and manager decisions.
- Process at least five requisitions in one execution.

## Development Approach

The system was developed in Python using a `Requisition` class, objects, a constructor and separate methods for different functions. Each requisition object stores its own information, while the methods handle purchase items, approvals, displays and statistics. Visual Studio Code was used for development, and GitHub was used to track changes through commits.

## Testing

I tested the system using different purchase amounts, approval decisions and invalid inputs. This included checking the $500 approval boundary, date and price validation, and manager decision handling.

In the final five-requisition test, the system correctly displayed 2 Approved, 2 Pending and 1 Not approved requisition.

## How to Run

1. Download the project files.
2. Open the project folder in Visual Studio Code.
3. Make sure Python 3 is installed.
4. Open the VS Code terminal and run:

   `python requisition_system.py`

5. Follow the instructions in the terminal to enter and process requisitions.
