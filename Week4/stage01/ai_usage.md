# Microsoft Copilot Response to Part C

Copilot said:
Part C – Use AI as Tutor (AI ON)

Role: Python Tutor

You are learning introductory software technology, and this small appointment-booking program demonstrates how Python stores data in variables and displays information using output statements.

1. What the code does

The program simulates a simple appointment booking system for a community clinic called SmartCare.

It prints a welcome message to the user.
It creates variables to store details for two appointments:
Patient name
Practitioner name
Appointment time
It uses f-strings (f"...") to format and display the appointment details in a readable way.
The output shows two scheduled appointments:
Alice Smith with Dr. John Doe at 10:00 AM
Bob Johnson with Dr. Jane Roe at 11:30 AM

This introduces key programming concepts such as:

Variables
Strings
Output using print()
String formatting with f-strings

2. Three limitations

Appointment details are hard-coded

The program only displays the appointments already written into the code.
Users cannot enter their own appointment information.

Limited scalability

Each appointment requires a new set of variables.
Managing many appointments would result in repetitive code.

No validation or booking logic

The program does not check whether appointment times overlap.
It does not verify that dates or times are valid.

3. Suggested improvements

Allow user input

Use the input() function so users can enter patient names, practitioner names, and appointment times.

Use lists or dictionaries

Store appointment information in a data structure to manage multiple bookings more efficiently.

Add basic validation

Check that required fields are not empty.
Verify that appointment times are entered in the correct format.

Create functions

Separate tasks such as creating and displaying appointments into functions to improve readability and reusability.

4. Application Rewrite

As requested, I have not rewritten the whole application. The suggestions above focus on incremental improvements that build on the existing code.

5. Questions to test your understanding

What is the purpose of using an f-string in the print() statements instead of writing the appointment details directly as text?

Why might using a list or dictionary be a better approach than creating separate variables for every new appointment?