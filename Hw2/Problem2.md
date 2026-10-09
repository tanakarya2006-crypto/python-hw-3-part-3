# HW 2: Homework Problem

## Problem Description
Homework Question:
A spacecraft from Earth is getting ready to journey on a mission in space. Before
the ship launches, one of the astronauts needs to run a program to figure out
whether or not their ship will have enough fuel for their planned destination. What
is given is that the spacecraft will use 2.5 kilograms of fuel per kilometer traveled.

## Instructions 
The program you write should do the following:
1. Write a function titled “fuel
_
needed(distance)” such that it:
a. Uses the trip distance in kilometers as an input function
b. Calculates how many kilometers of fuel are necessary
c. And returns the amount of fuel required
2. Next, write a function titled “valid
_
input(distance, available
_
fuel) such that:
a. It returns False if the distance is <= 0
b. It returns False if the available fuel is <= 0
c. Otherwise, it will return True
3. Then, Write a function calling it “mission
_
status(required
fuel,
_
available
_
fuel)” that will return:
a.
“Mission is possible” if there is enough fuel needed
b.
“Mission is not possible” if there isn’t enough fuel
4. Under this code:
a. Create an “if
name
== ‘
main
’:” function
__
__
__
__
b. Under that write a driver code so it does the following
i. Will ask the user for the trip distance with kilometers as the unit
ii. Asks how many kilograms of fuel is available
iii. Validates those inputs
iv. Then, calculates the fuel required
v. Determines if the mission can proceed
vi. Prints amount of fuel required and the missions status
vii. If either of those inputs are invalid, the program should print
out “Invalid input.
”
5. Finally, test the program by using three different cases
a. A mission with more than the necessary amount of fuel
b. A case with invalid inputs
c. A mission without enough fuel
Explanation of this homework problem
