IT5016 Assessment 3 - Programming Principles and Concepts Research Repository

Student: Oscar Ipac

Course: IT5016

Introduction

This repository contains my programming practice and research for IT5016 Assessment 3. I am using my Python Requisition System to explore programming principles and software design concepts. The purpose of this repository is to understand how different programming principles can be applied to my own code. I will look at how these principles can make software easier to understand, maintain and extend. I will also identify areas where my code could be improved and explain how the improvements could make the program more reliable and easier to develop in the future.

Code I Used

For this assessment, I used my Python Requisition System from my previous programming work. The program is stored in the Code folder as requisitionsystem.py. The program uses a RequisitionSystem class to create and manage requisitions. It contains methods for entering staff information, entering requisition items, calculating the total cost, checking the approval status, responding to requisitions and displaying requisition information. The program also uses a global counter to generate unique requisition IDs and a list to store the requisition objects. I will use this code to research and analyse programming principles and design concepts and how they are applied in my own programming.

Programming Principles and Design Concepts

Modularity:
Modularity means breaking a program into smaller parts with different jobs. In my Requisition System, I used methods such as staff_info(), requisitions_details() and display_requisitions(). This makes my code easier to understand and maintain because each method has a specific purpose. One improvement would be using a loop instead of repeating requisition1 to requisition5. This would make the program easier to extend.

Reusability:
Reusability means creating code that can be used again instead of writing the same code multiple times. In my Requisition System, I used methods such as display_requisitions() and requisition_statistic(). These methods can be called when needed, so I do not have to write the same instructions again. One improvement would be creating a separate method for repeated requisition creation. This would reduce repeated code and make the program easier to maintain.

Readability:
Readability means making code easy for other programmers to understand. In my Requisition System, I used clear method names, headings and comments to explain what different parts of the code do. For example, comments are used before methods such as staff_info() and requisition_approval(). One improvement would be reducing some of the repeated comments because this could make the code shorter and easier to read.

Maintainability:
Maintainability means making code easy to update, fix and improve in the future. In my Requisition System, I separated the program into methods, which makes it easier to change one part without changing the whole program. For example, the approval rules are handled in requisition_approval(). One improvement would be reducing the use of global variables such as requisition_counter and requisitions. This could make the program easier to manage as it becomes larger.

DRY (Don't Repeat Yourself):
The DRY principle means avoiding unnecessary repetition in code. In my Requisition System, I repeated similar code when creating requisition1 to requisition5. The repeated code works, but it makes the program longer and harder to change. I could improve this by using a loop to create the requisitions. This would reduce repetition and make the program easier to maintain if more requisitions were needed.

Object-Oriented Programming (OOP):
Object-Oriented Programming means organising code using classes and objects. In my Requisition System, I created a RequisitionSystem class and used objects such as requisition1, requisition2 and requisition3. The class contains the data and methods needed to manage each requisition. Using a class makes the program easier to organise and allows me to create multiple requisition objects using the same structure. One improvement would be keeping more of the requisition data inside the class instead of using global variables.

Input Validation:
Input validation means checking user input before the program uses it. In my Requisition System, the item price is converted directly to a float. If the user enters something that is not a number, the program can stop with an error. I could improve this by using a validation loop that asks the user to enter the price again until a valid number is entered. This would make the program more reliable and user-friendly.

Research Findings

Modularity:
From my research, modularity means dividing a program into smaller and more manageable parts. This can make software easier to understand, test, maintain and improve. In my Requisition System, I used separate methods such as staff_info(), requisitions_details() and display_requisitions() to divide the program into different tasks. This shows how modularity can be applied to my own code. However, I also noticed that I repeated similar code when creating five requisitions. Using a loop or another method could make this part more modular and reduce repetition.

Reusability:
From my research, reusability means designing code so that it can be used again in different parts of a program instead of writing the same code again. Reusable code can save development time and make a program easier to maintain. In my Requisition System, methods such as display_requisitions() and requisition_statistic() can be called when they are needed. This shows reusability in my own code. However, I could improve the repeated code used to create requisition1 to requisition5 by creating a reusable method or using a loop. This would reduce the amount of repeated code.

Readability:
From my research, readability means writing code in a way that is easy for programmers to understand. Clear names, simple structure and useful comments can make code easier to read and maintain. In my Requisition System, I used method names such as staff_info(), requisitions_details() and display_requisitions(), which help explain what each method does. I also added comments throughout the code to explain different sections. However, I noticed that some comments are repeated too often. I could improve the readability by keeping the most useful comments and removing comments that explain simple lines of code.

Maintainability:
From my research, maintainability means making software easy to update, fix and improve when changes are needed. Good code organisation and simple structure can make maintenance easier. In my Requisition System, I separated different tasks into methods, such as requisition_approval() and display_requisitions(). This means changes to one part of the program can be made without changing every part of the code. I also noticed that my program uses global variables such as requisition_counter and requisitions. I could improve the maintainability by keeping this data inside the class instead of using global variables. This could make the program easier to manage if the system becomes larger.

DRY (Don't Repeat Yourself):
From my research, the DRY principle means avoiding unnecessary repetition in a program. Repeating the same code can make a program longer and harder to maintain when changes are needed. In my Requisition System, I repeated similar code when creating requisition1 to requisition5. Although the code works, changing the process would mean making changes in several places. I could improve this by using a loop or a reusable method to create the requisitions. This would reduce repeated code and make the program easier to maintain and extend.

Object-Oriented Programming (OOP):
From my research, Object-Oriented Programming means organising a program using classes and objects. A class can contain data and methods that work together to perform related tasks. In my Requisition System, I created a RequisitionSystem class and used objects such as requisition1, requisition2 and requisition3. The class stores information such as the staff name, staff ID, total cost and requisition status, and the methods are used to manage the requisition. This makes the program more organised and allows multiple requisition objects to use the same structure. One improvement would be moving the global variables into the class so that more of the requisition data is managed by the objects.

Input Validation:
From my research, input validation means checking information entered by a user before the program uses it. This can help prevent incorrect data from causing errors in a program. In my Requisition System, I ask the user to enter information such as the staff ID, staff name, item name and item price. The item price is converted to a float, but if the user enters text instead of a number, the program can stop with an error. I could improve this by using a validation loop that checks the price before continuing. This would make my program more reliable and easier for the user to operate.

Overall Analysis and What I Learned
After researching these programming principles, I understand that making code work is not the only goal. Code should also be easy to read, maintain and improve. My Requisition System already uses a class and separate methods, which shows OOP and modularity. However, I noticed that I repeated code when creating five requisitions. Using a loop would make the code shorter and easier to extend. I also learned that input validation is important because incorrect input, such as entering text for a price, can cause an error. Overall, this research helped me understand how programming principles can be applied to improve my own code.

References

Harvard Kempner Institute. (2026). Software design principles. https://handbook.eng.kempnerinstitute.harvard.edu/s2_swe_for_research/software_design_principles.html

UK Home Office. (2025). Keep it simple. https://engineering.homeoffice.gov.uk/principles/keep-it-simple/

UK Home Office. (n.d.). Write maintainable, reusable and evolutionary code. https://engineering.homeoffice.gov.uk/principles/write-maintainable-reusable-and-evolutionary-code/

Microsoft. (2024). Maintainability. https://microsoft.github.io/code-with-engineering-playbook/non-functional-requirements/maintainability/
