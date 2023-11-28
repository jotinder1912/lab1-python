
a = input("Enter patient's name: ")
print("Hi! ", a)
b = input("Has the patient been here before? (y/n): ")
print("nice to see you :- ",b)
c = int(input("What is the patient's height (in cm)?: " ))
print(c,"cm ")
w = float(input("What is the patient's weight (in kg)?: " ))
print(w,"kg")
l_date = input("When was the patient last weighed in (1/1/2000 if never weighed)?: ")
print("okk",l_date)
p_weight = float(input("What was the patient's weight (in kg, -1 if never weighed)?: "))
print(p_weight,"kg")
assessment = int(input("Practitioner's overall assessment of the patient's health (-5=very poor to +5=excellent, 0 for neutral)?: "))

w_change= w - p_weight
print("change in weight" ,w_change,"kg")

bmi=(w/(c*2))*1000 
round(bmi,1)
print("BMI: " )

if bmi>30:
    print("Obese!" ,bmi)
    intermediate_score=0

elif 29.9>bmi>18.5:
    print("Overweight!",bmi)
    intermediate_score=3
elif 24.9>bmi>18.5:
    print("health",bmi)
    intermediate_score=5
elif 18.4>bmi>17:
    print("Underweight",bmi)
    intermediate_score=3
else:
    print("Too Thin",bmi)
    intermediate_score=0

print("intermediate health score is:",intermediate_score)
if p_weight==-1:
    new_intermediate=intermediate_score+1
    print("new intermediate health score: ",new_intermediate)
else:
    if w_change==0 or   w_change==-1 or w_change== 1:
        new_intermediate =intermediate_score-1
        print("new intermediate health score: ",new_intermediate)
    else:    
        if   18.4>bmi>17:
          if w_change<0:
            new_intermediate=intermediate_score-3
            print("new intermediate health score: ",new_intermediate)
          else:
            new_intermediate=intermediate_score+2
            print("new intermediate health score: ",new_intermediate)

        elif bmi<17: 
           if w_change<0:
            new_intermediate=intermediate_score-5
            print("new intermediate health score: ",new_intermediate)
           else:
            new_intermediate=intermediate_score+5
            print("new intermediate health score: ",new_intermediate) 
        
        elif 29.9>bmi>25: 
            if w_change>0:
              new_intermediate=intermediate_score-3
              print("new intermediate health score: ",new_intermediate)
            elif w_change<-1:
               new_intermediate=intermediate_score+2
               print("new intermediate health score: ",new_intermediate)
            else:
              new_intermediate=intermediate_score+2
              print("new intermediate health score: ",new_intermediate)  
        elif bmi>30: 
            if w_change<0:
              new_intermediate=intermediate_score-5
              print("new intermediate health score: ",new_intermediate)
            elif w_change<-1:
               new_intermediate=intermediate_score+2
               print("new intermediate health score: ",new_intermediate)
            else:
              new_intermediate=intermediate_score
              print("new intermediate health score: ",new_intermediate)
        else:
            new_intermediate= intermediate_score
            print("new intermediate health score: " ,new_intermediate)  


final_score=new_intermediate+assessment
if final_score > 5:
        print("Great condition!", final_score) 
elif 3 <= final_score <= 5:
        print("Need a little work", final_score)
elif 1 <= final_score < 3:
        print("Need a lot of work",final_score) 
else:
    print("At resk!")


            


print("Melanie Dental Clinic")
print("*-----------------------*")
print("Patient Report")
print("Patient Name:", a)
print("Days since last visit : ", "First visit" )
print("*------------------------*")
print("BMI : ", bmi)
print("Health : ",assessment )
("*-------------------*")
print("Overall : ", final_score)
