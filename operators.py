'''
1)Assume Dhoni's current age is 6. After 3 years, Dhoni's mother Devki Devi would be 4 times Dhoni's age. What is Devki Devi's current age? Write a program to determine the same.
Input Format:
First line of input consists of one integer value as age of Dhoni.
Output Format:
Output should display an integer that specifies Devki Devi's current age.
Sample Input and Output1:
6
33
Sample Input and Output2:
3
21
Note: Bold highlighted is the output value.
'''
#code for the first question
#code:-
cAge=int(input())
deviAge =((cAge+3)*4)-3
print(deviAge)

'''
2) Dhoni once wished to join a a reputed Cricket Coaching Camp to be held at a place "X" kms away from his house. He told about this to his father and got his consent to use his friend's bike for the Camp. The Camp was to be held on all days of the month. His friend's bike provides a mileage of Y km/litre and the cost of petrol was Rs. Z. Dhoni's father now wanted to know the total amount that was needed by Dhoni to spend on his travel to the Camp. Help him find the same and assume number of days in a month as 30 days.
Input Format:
First line of the input is an integer "X" in kms that specifies the distance of the Camp from Dhoni's house.
Second line is an integer "Y" in km/litre that specifies the mileage of his friend's bike.
Third line is a float "Z" that specifies the cost of petrol in rupees.
Output Format:
Output should display a float that gives the total amount that is needed by Dhoni to spend on his travel in rupees. The float value is displayed correct to 2 decimal places.
Sample Input and Output 1:
75
55
63
2577.27
Sample Input and Output 2:
35
78
65.0
875.00
'''
#code for second question

x=float(input())
y=float(input())
z=float(input())
a=(x*z*30)/y
print(round(a,2))

'''
3)MS Dhoni is a grade A player according to BCCI Central Contracts in 2016. MSD's net worth in 2016 is around 31 million and is said to be the richest Indian cricketer.
Apart from his salary as an Indian cricketer, Dhoni endorses various popular brands and earns a large amount from endorsements. Besides that individual and team bonuses are also given on the basis of individual and team performances. So precisely the sources of income for Dhoni are from - Salary, Bonuses and Awards through Winning and Endorsements.
Write a program that finds Dhoni's percentage of income earned from each of the 3 individual sources.
Input Format:
First line of the input is an integer that specifies Dhoni's income in rupees from Salary.
Second line is an integer that specifies Dhoni's income in rupees from Bonuses and Awards.
Third line is an integer that specifies Dhoni's income in rupees from endorsements.
Output Format:
Output should display 3 floats in a line, separated by a space. The first float corresponds to the percentage of income from Salary, the second float corresponds to the percentage of income from Bonuses and Awards and the third float corresponds to the percentage of income from endorsements.
All float values should be displayed correct to 2 decimal places.
Sample Input and Output 1:
100
20
80
50.00 10.00 40.00
Sample Input and Output2:
50000
10000
35000
52.63 10.53 36.84
Note: Bold highlighted is the output
'''
#code for third question
s=int(input ())
b=int(input ())
e=int(input ())
ti=s+b+e
ps=(s/ti)*100
pb=(b/ti)*100
pe=(e/ti)*100
print("%.2f"%ps,"%.2f"%pb,"%.2f"%pe)

'''
4)
Extras
Extras are runs scored by a means other than a batsman hitting the ball. A batsman is not given credit for extras other than runs scored off the bat from a no ball, and the extras are tallied separately on the scorecard and count only towards the team’s score. the types of extras are No ball, Wide, Bye, Leg-bye and Penalty. 1 Penalty corresponds to 5 runs.
Find the total runs that the Extras contribute to the team’s score, given the number of No-balls, wides, byes, leg-byes and penalty given off by the bowlers in innings.
Input format:
First line of the input contains an integer that corresponds to the number of No-balls.
Second line of the input contain an integer that corresponds to the numbers of wides.
Third line of the input contains an integer that corresponds to the number of byes.
Fourth line of the input contain an integer that corresponds to the numbers of led-byes.
Fifth line of the input contains an integer that corresponds to the numbers of penalty runs.
Output format:
Output should display an integer that returns the total runs that the extras together contribute to team’s total.
Sample input and output 1:
4
7
3
10
3
39
Sample input and output 2:
2
3
7
1
17
'''

#code for fourth question
a=int(input("number of no balls"))
b=int(input("number of wides"))
c=int(input("number of no byes"))
d=int(input("number of no led-byes"))
e=int(input("number of penalty runs"))
total=a+b+c+d+e*5
print(total)

'''
5)
Tamilnadu was battling one if it’s worst floods in a century last December, as several part of the state have been submerged and cut off from essential supplies. It was heartening that the Cricketers came forward to contribute for the cause of floods and it was decided amongst the team that the senior players donate 50% of their salary and junior players to donate 40% against the flood relief measures
Assume there are 6 senior players and 5 junior players. The salary of senior players Rs.X and that of junior players is Rs.Y. Find the total contribution from the cricket team towards the floods.
Input format:
First line of the input is an integer “X” that specifies the salary of the senior players in rupees.
Second line is an integer “Y” that specifies the salary of the junior players in rupees.
Output format:
Output should display a flood that gives the total contribution of money in rupees from the cricket team. The float value should be displayed correct to 2 decimal places.
Sample input and output 1:
45000
40000
215000.00
Sample input and output 2:
78000
60000
354000.00
'''
#code for fifth problem
X = int(input("the salary of senior players : "))
Y = int(input("the salary of junior players : "))
senior_players = 6
junior_players = 5
senior_contribution = senior_players * (0.50 * X)
junior_contribution = junior_players * (0.40 * Y)
total_contribution = senior_contribution + junior_contribution
print(f"Total contribution towards flood relief: Rs {total_contribution:.2f}")






'''6)
It were the days of domination from the traditional metros in the team selections and everytime the team is announced for the Indian Squad, mere disappointment was left with this small town player. Dhoni’ill fate continued even during the team selections for the India A squad to tour to Zimbabwe.3 new players from Mumbai were on the list for the Indian team and it was claimed by the selectors that Dhoni was a bit younger than the 3 selected players.
  Assume the 3 players are Named X,Y and Z. The ages of the players X and Y are the same and the age of the Z is 10 more than other 2 players. Given the total age of the 3 players, find the age of the 3 players.
Input format:
First line of the input is an integer that corresponds to the total age of the 3 players.
Output format:
Output should display the ages of the three players in 3 lines. The age of the eldest player should be displayed in the last line.
Sample input and output 1:
70
20
20
30
Sample input and output 2:
100
30
30
40
'''
#code:
a=int(input("give the total age of those three players  "))
x=(a-10)/3
y=x
z=x+10
print(x)
print(y)
print(z)




'''
7)
You are given principal amount, rate of interest per annum, and time in years. You need to calculate the simple interest.
Input and Output Format
Input Format:
The first line contains the principal amount (principal).
The second line contains the rate of interest (rate) per annum.
The third line contains the time (time) in years.
Output Format:
A single line containing the simple interest calculated.
'''

#code:
principal_amt=int(input("enter the principal amount "))
interest_amt=int(input("enter the rate of interest "))
time=int(input("time "))
simple_interest=(principal_amt*interest_amt*time)/100
print(simple_interest)


'''
8)
You are given a temperature in Celsius. You need to convert it to Fahrenheit.
Input and Output Format
Input Format:
A single integer celsius.
Output Format:
A single line containing the temperature in Fahrenheit.
To convert a temperature from Celsius to Fahrenheit, you use the following formula:
Multiply the temperature in Celsius by 9/5.
Add 32 to the result of step 1.
'''

#code:
a=int(input("enter the degree celsius "))
x=a*(9/5)
y=x+32
print({},"the fahrenheit of cenlsius degrees",{},"is:",y,a )



'''
9)
Ajay, Binoy and Chandru were very close friends at school. They were very good in Mathematics 
and they were the pet students of Emily Mam. Their gang was known as 3-idiots. Ajay, Binoy and Chandru live in the same locality.
A new student Dinesh joins their class and he wanted to be friends with them. 
He asked Binoy about his house address. Binoy wanted to test Dinesh's mathematical skills. 
Binoy told Dinesh that his house is at the midpoint of the line joining Ajay's house and Chandru's house. 
Dinesh was puzzled. Can you help Dinesh out? Given the coordinates of the 2 end points of a line (x1,y1) and (x2,y2), 
write a python program to find the midpoint of the line. 
Input Format: Input consists of 4 integers. 
The first integer corresponds to x1 .
The second integer corresponds to y1. 
The third and fouth integers correspond to x2 and y2 respectively. 
Output Format: Refer Sample Input and Output for exact formatting specifications. 
[All floating point values are displayed correct to 1 decimal place]


#code:
a = int(input())
b = int(input())
c = int(input())
d = int(input())
x=(a+c)/2
y=(b+d)/2
print("the midpoints are: ")
print(x)
print(y)



