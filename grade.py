name=input("enter the student name:")
subject1=int(input("enter the marks:"))
subject2=int(input("enter the marks:"))
subject3=int(input("enter the marks:"))
subject4=int(input("enter the marks:"))
subject5=int(input("enter the marks:"))
total=subject1+subject2+subject3+subject4+subject5
avg=total/5
if avg>=90:
	print("Grade A+")
elif avg>=85:
	 print("Grade A")
elif avg>=60:
	  print("Grade C")
elif avg>=40:
	 print( "Grade D")
else:
	print("fail")
print("name:",name)
print("total marks",total)
print("avg",avg)	
