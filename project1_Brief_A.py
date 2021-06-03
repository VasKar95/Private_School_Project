
'''To πρόγραμμα αυτό αφορά τη δομή ενός ιδιωτικού σχολείου'''
class Private_School():
      pass

class Name_info:
      def __init__(self, first_name,last_name):
            self.first_name=first_name
            self.last_name=last_name
      def __repr__(self):
             return f"First Name: {self.first_name},Last Name: {self.last_name}"
      
class Course:
      def __init__(self, course,course_2,duration,duration2):
            self.course=course
            self.duration2=duration2
            self.course_2=course_2
            self.duration=duration
      def __repr__(self):
             return f"{self.course},{self.duration},{self.course_2},{self.duration2}"

class Trainer(Private_School,Name_info):
      def __init__(self, first_name,last_name):
            Name_info.__init__(self, first_name,last_name)
            
      def __repr__(self):
             return f"First Name:{self.first_name},Last Name:{self.last_name}"
class Date_of_Birth:
      def __init__(self,date):
            self.date=date
      def __repr__(self):
             return f"Date of Birth:{self.date}"
class Student(Private_School,Name_info,Course,Date_of_Birth):
      def __init__(self, first_name,last_name,date,course,duration,course_2,duration2):
            Name_info.__init__(self, first_name,last_name)
            Course.__init__(self,course,duration,course_2,duration2)
            Date_of_Birth.__init__(self,date)
            
      def __repr__(self):
             return f"{self.first_name},{self.last_name},{self.date},{self.course},{self.duration},{self.course_2},{self.duration2}"

class Assignment():
       def __init__(self,title,description1,date_of_sub1,title2,description2,date_of_sub2):
              self.title=title
              self.description1=description1
              self.date_of_sub1=date_of_sub1
              self.title2=title2        
              self.description2=description2
              self.date_of_sub2=date_of_sub2
              
       def __repr__(self):
             return f"Title of 1st Course:{self.title},Description of 1st Course:{self.description1},Date of Submission 1:{self.date_of_sub1},Title of 2nd Course:{self.title2},Description of 2nd Course:{self.description2},Date of Submission 2:{self.date_of_sub2},"

          
               
trainers=[]
courses=[]
python_trainers=[]
java_trainers=[]
javasc_trainers=[]
c_trainers=[]
############################################################################################################################################################################
import datetime
students=[]
student_n=[]
students_name=[]
courses_student=[]
python_students=[]
java_students=[]
javasc_students=[]
c_students=[]
birth=[]
courses_2=[]

all_courses=[]
coursesss=[]
coursesss2=[]
########################################################################

assignment_list=[]

python_assignment=[]
java_assignment=[]
javascript_assignment=[]
c_assignment=[]

  
#Ζητάμε από το χρήστη να δώσει τον αριθμό των μαθητών που θέλει να εκχωρησει

while True:#Eδώ βάζουμε τα exceptions για να μην σταματήσει το προγραμμα σε περιπτωση error
      try:
            n_of_st=int(input('Add the number of students'))
            while n_of_st>=0:
                  n_of_st=n_of_st
                  break
            else:
                  n_of_st=int(input('Add the number of Students'))
                  
            break
      except ValueError:
            print('No Valid Number')
while True:
      try:
            n_of_tr=int(input('Add the number of Trainers'))
            while n_of_tr>=0:
                  n_of_tr=n_of_tr
                  break
            else:
                  n_of_st=int(input('Add the number of Trainers'))
                  
            break
      except ValueError:
            print('No Valid Number')


if n_of_st>0:
      for i in range (n_of_st):
         #Ζητάμε από το χρήστη να δώσει πόσους μαθητές θέλει να εκχωρησει
            first_name=str(input('Insert students΄ First Name:'))
            last_name=str(input('Insert students΄Last Name:'))
         #Ζητάμε απο το χρήστη να μας δώσει την ημερομηνία γέννησής του
            while True:
                  try:
                        currentDate = datetime.date.today()
                        year=int(input('Give the year of birth'))
                        month=int(input('Give the month of birth'))
                        day=int(input('Give the date of birth'))
                        birthday=datetime.date(year,month,day)
                  
                        break
                  except ValueError:
                        print('No Valid Date')
            
            students_=Name_info(first_name,last_name)

         #Ενημερώνουμε το χρήστη αν θέλει να παρακολουθήσει 1 ή 2 μαθήματα
           
            while True:
                   try:
                          choice=input('Would you like to have one(1) or two(2 )courses? If one press 1, else, 2)')
                          while choice=='1' or choice=='one'or choice=='two' or choice=='2':
                                 choice=choice
                                 break
                          else:
                                 choice=input('Would you like to have one(1) or two(2 )courses? If one press 1,else,2)')
                          break
                   except ValueError:
                          print('No valid choice')

         #Aφορά την διαδικασία που λαμβάνει χώρα όταν ο χρήστης δηλώνει ένα μάθημα  
            if choice=='one'or choice=='1':
                  course=input('Give one of the following Courses:Pyhton,C#,Java,Javascript').lower()
                  while (course=='python') or (course=='c#')or (course=='java') or (course=='javascript'):
                      course=course
                      all_courses.append(course)
                      
         #Διάρκεια μαθήματος
                      duration=input('Give the Duration of the Course. Would you like full(12 weeks) or part time(24 weeks)?').lower()
                      while duration=='full time' or duration=='12 weeks' or duration=='full' or duration=='part time' or duration=='24 weeks' or duration=='part':
                            if duration=='full time' or duration=='12 weeks' or duration=='Full Time'or duration=='full':
                                    duration="Full time (12 weeks)"
                                    break
                            else:
                                    duration="Part time (24 weeks)"
                                    break
                        
                      else:
                           duration=input('Give the duration of the course. Would you like full or part time?')
                      
                      
                      
         #Eδώ ζητάμε απο το χρήστη το τίτλο του assignment και την περιγραφή του(στην περιγράφή έθεσα ένα όριο 100 λέξεις )
                      title=input('Give the title of the Assignment')
         #Περιγραφή Μαθήματος
                      description1=input('Give the description of this Assigniment.Max 50 characters')
                      while len(description1)<50:
                         description1=description1
                         break
                      else:
                         description1=input('Give again the description of this Assigniment and it must be under 50 characters')
                         
          #Ζητάμε απο το χρήστη να δώσει το Submission Date
                      while True:
                              try:
                                    currentDate = datetime.date.today()
                                    year=int(input('Give the year of submission'))
                                    month=int(input('Give the month of submission'))
                                    day=int(input('Give the date of submission'))
                                    date_of_sub1=datetime.date(year,month,day)
                  
                                    break
                              except ValueError:
                                    print('No Valid Date')
           #Ανάλογα το μάθημα εκχωρούμε στους αντίστοιχους φακέλους τα assignment και τους μαθητές
                      if course=="python":
                          python_students.append(students_)  
                          python_assignment.append(title)
                      elif course=="java":
                          java_students.append(students_)
                          java_assignment.append(title)
                      elif course=="javascript":
                          javasc_students.append(students_)
                          javascript_assignment.append(title)
                      else:   
                          c_students.append(students_)
                          c_assignment.append(title)
                   
                      break 
                      
                  else:
                        course=input('Give one of the following Courses:Pyhton,C#,Java,Javascript')
                       
                  title2='No second course'     
                  duration2='No second course'
                  course_2='No second course'
                  description2='No second course'
                  date_of_sub2='No second course'
                  course=Course(course,duration,course_2,duration2)
                  courses_student.append(course)
                  assignment=Assignment(title,description1,date_of_sub1,title2,description2,date_of_sub2)
                  assignment_list.append(assignment)


                  coursesss.append(course)
                  course2=''
                  coursesss.append(course2)
                  coursesss2.append(course)
                  
                  
      #Αφορά την διαδικασία όταν έχει να διαλέξει ο χρήστης πάνω απο ένα μάθημα          
            else:
                  course=input('Give one of the following Courses:Pyhton,C#,Java,Javascript').lower()
                  course_2=input('Give the second Course:Pyhton,C#,Java,Javascript').lower()
                  while course!=course_2 and((course=='python') or (course=='c#')or (course=='java') or (course=='javascript'))and((course_2=='python') or (course_2=='c#')or (course_2=='java') or (course_2=='javascript')):
                        course=course
                        course_2=course_2
                        all_courses.append(course)
                        all_courses.append(course_2)
                        
                        coursesss.append(course)
                        coursesss.append(course_2)
                        
                        #Διάρκεια μαθήματος 1 
                        duration=input('Give the duration of the 1st course. Would you like full(12 weeks) or part time(24 weeks)?').lower()
                        while duration=='full time' or duration=='12 weeks' or duration=='full' or duration=='part time' or duration=='24 weeks' or  duration=='part':
                            if duration=='full time' or duration=='12 weeks' or duration=='full':
                                    duration="Full time (12 weeks)"
                                    break
                            else:
                                    duration="Part time (24 weeks)"
                                    break
                        
                        else:
                             duration=input('Give the duration of the 1st course. Would you like full or part time?')
                         #Διάρκεια μαθήματος 2
                        duration2=input('Give the duration of the 2nd course. Would you like full(12 weeks) or part time(24 weeks)?')
                        while duration2=='full time' or duration2=='12 weeks' or duration2=='full' or duration2=='part time' or duration2=='24 weeks' or duration2=='part':
                            if duration2=='full time' or duration2=='12 weeks' or duration2=='full':
                                    duration2="Full time (12 weeks)"
                                    break
                            else:
                                    duration2="Part time (24 weeks)"
                                    break
                        
                        else:
                             duration2=input('Give the duration of the 2nd course. Would you like full or part time?')
                               
                        courses_2.append(students_)#Στη λίστα courses_2 οι μαθητές με 2 μαθήματα
       #Τίτλος Μαθήματος 1
                        title=input('Give the Title of the first Assignment')
                        
       #Περιγραφή Μαθήματος 1

                        description1=input('Give the description of 1st Assigniment.Max 50 characters.')
                        while len(description1)<50:
                            description1=description1
                            break
                        else:
                            description1=input('Give again the description of Assigniment and it must be under 50 characters')

       #Ζητάμε απο το χρήστη να δώσει το Submission Date για το μάθημα 1 
                        while True:
                              try:
                                    currentDate = datetime.date.today()
                                    year=int(input('Give the year of submission'))
                                    month=int(input('Give the month of submission'))
                                    day=int(input('Give the date of submission'))
                                    date_of_sub1=datetime.date(year,month,day)
                  
                                    break
                              except ValueError:
                                    print('No Valid Date')

      #Τίτλος Μαθήματος 1 

                        title2=input('Give the title of the 2nd Assignment')   
      #Περιγραφή Μαθήματος 2
                        description2=input('Give the description of 2nd Assigniment.Max 50 characters.')
                        while len(description2)<50:
                            description2=description2
                            break
                        else:
                            description=input('Give again the description of assigniment, with max 50 characters')
      #Ζητάμε απο το χρήστη να δώσει το Submission Date για το μάθημα 2                    
                        while True:
                              try:
                                    currentDate = datetime.date.today()
                                    year=int(input('Give the year of submission'))
                                    month=int(input('Give the month of submission'))
                                    day=int(input('Give the date of submission'))
                                    date_of_sub2=datetime.date(year,month,day)
                  
                                    break
                              except ValueError:
                                    print('No Valid Date')
       #Ανάλογα το μάθημα εκχωρούμε στους αντίστοιχους φακέλους τα assignment και τους μαθητές
                        
                        if   course=="python":
                              python_students.append(students_)
                              python_assignment.append(title)
                        elif course=="java":
                              java_students.append(students_)
                              java_assignment.append(title)
                        elif course=="javascript":
                              javasc_students.append(students_)
                              javascript_assignment(title)
                        else:
                              c_students.append(students_)
                              c_assignment.append(title)
                        
                        if course_2=="python":
                              python_students.append(students_)
                              python_assignment.append(title2)
                        elif course_2=="java":
                              java_students.append(students_)
                              java_assignment.append(title2)
                        elif course_2=="javascript":
                              javasc_students.append(students_)
                              javascript_assignment.append(title2)
                        else:
                              c_students.append(students_)
                              c_assignment.append(title2)

                        course=Course(course,duration,course_2,duration2)
                        courses_student.append(course)

                        
                        break
                  else:
                        course=input('Give one of the following Courses:Pyhton,C#,Java,Javascript')
                        course_2=input('Give the second Course:Pyhton,C#,Java,Javascript')
                        
                  course=Course(course,duration,course_2,duration2)
                  courses_student.append(course)
                  assignment=Assignment(title,description1,date_of_sub1,title2,description2,date_of_sub2)
                  assignment_list.append(assignment)

                  coursesss.append(course)
                  coursesss2.append(course_2)
           
            students_=Name_info(first_name,last_name)
            student=Student( first_name,last_name,birthday,course,duration,course_2,duration2)
            students.append(student)
            students_name.append(students_)
            
            
      


#Ζηταμε απο το χρηστη να δωσει ποσους εκπαιδευτες θελει να εκχωρησει
if n_of_tr>0:
      for i in range (n_of_tr):
      #Ζηταμε απο το χρηστη να δωσει first,last name και το course που κανει καθε εκπαιδευτής
             first_name=str(input('Insert Traines΄ First Name'))
             last_name=str(input('Insert Trainers΄ Last Name'))
             course=input('Give one of the following Courses:Pyhton,C#,Java,Javascript')
             while (course=='Python') or (course=='C#')or (course=='Java') or (course=='Javascript')or(course=='python') or (course=='c#')or (course=='java') or (course=='javascript'):
                      course=course
                      break
             else:
                        course=input('Give one of the following subjects:Pyhton,C#,Java,Javascript')

             trainer=Trainer(first_name,last_name)
             trainers.append(trainer)
             
             if course=="Python" or course=="python":
                   python_trainers.append(trainer)
             elif course=="Java" or course=="java":
                   java_trainers.append(trainer)
             elif course=="Javascript" or course=="javascript":
                   javasc_trainers.append(trainer)
             else:
                   c_trainers.append(trainer)
             course_2=''
             duration=''
             duration2=''
             course=Course(course,duration,course_2,duration2)
             courses.append(course)


#Εδώ ρωτάμε το χρήστη αν θέλει να δει όλους τους μαθητές ανά μάθημα
answer1=input('Would you like to see all the students per course?  Yes or No')
while answer1=="Yes" or answer1=='yes'or answer1=='no'or answer1=='No':
      if answer1=="Yes" or answer1=='yes':
            if len(python_students)==0:
                  print('No Python students')
            else:
                  print('The Python students are:',python_students)
            if len(java_students)==0:
                  print('No Java students')
            else:
                  print('The Java students are:',java_students)
            if len(javasc_students)==0:
                  print('No Javascript students')
            else:
                  print('The Javascript students are:',javasc_students)
            if len(c_students)==0:
                  print('No C# students')
            else:
                  print('The C# students are:',c_students)
            break
      else:
            break
else:
     answer1=input('Would you like to see all the students per course? Yes or No')
     

#Eδώ ρωτάμε το χρήστη αν θέλει να δεί όλους τους καθηγητές
answer2=input('Would you like to see all traines? Yes or No')
while answer2=="Yes" or answer2=='yes'or answer2=='no'or answer2=='No':
      if answer2=="Yes" or answer2=='yes':
             if len(trainers)==0:
                    print('No Trainers')
             else:
                   print(trainers)
             break
      else:
            break
else:
      answer2=input('Would you like to see all traines? Yes or No')

#Zητάμε απο το χρήστη αν θέλει να δει τι λίστα με όλα τα assignments(Title,Description,Date of Submition)
answer3=input('Would you like to see all assignments(Title,Description,Date of Submition)? Yes or No?')
while answer3=="Yes" or answer3=='yes'or answer3=='no'or answer3=='No':
      if answer3=="Yes" or answer3=='yes':
             if len(assignment_list)==0:
                    print('No assignments')
                    break
             else:
                    print(assignment_list)
                    break
else:
      answer3=input('Would you like to see all assignments(Title,Description,Date of Submition)?, Yes or No?')


  
#Εδώ ρωτάμε το χρήστη αν θέλει να δει όλους τους μαθητές ανά μάθημα
answer4=input('Would you like to see all students per course? Yes or No')
while answer4=="Yes" or answer4=='yes'or answer4=='no'or answer4=='No':
      if answer4=="Yes" or answer4=='yes':
            if len(python_students)==0:
                  print('No Python students')
            else:
                  print('The Python students are:',python_students)
            if len(java_students)==0:
                  print('No Java students')
            else:
                  print('The Java students are:',java_students)
            if len(javasc_students)==0:
                  print('No Javascript students')
            else:
                  print('The Javascript students are:',javasc_students)
            if len(c_students)==0:
                  print('No C# students')
            else:
                  print('The C# students are:',c_students)
            break
      else:
            break
else:
     answer4=input('Would you like to see all the students per course? Yes or No')




#Εδώ ρωτάμε το χρήστη αν θέλει να δει όλους τους καθηγητές ανα μαθημα
answer5=input('Would you like to see all trainers per course? Yes or No')
while answer5=="Yes" or answer5=='yes'or answer5=='no'or answer5=='No':
      if answer5=="Yes" or answer5=='yes':
            if len(python_trainers)==0:
               print('No Python trainers')
            else:
               print('The Python trainers are:',python_trainers)
            if len(java_trainers)==0:
               print('No Java trainers')
            else:
               print('The Java trainers are:',java_trainers)
            if len(javasc_trainers)==0:
               print('No Javascript trainers')
            else:
               print('The Javascript trainers are:',javasc_trainers)
            if len(c_trainers)==0:
               print('No C# trainers')
            else:
               print('The C# trainers are:',c_trainers)
            break
      else:
            break
else:
      answer5=input('Would you like to see all the trainers per course? Yes or No')
      


#Εδώ ρωτάμε το χρήστη αν θέλει να δει όλα τα assignment ανά μάθημα
answer6=input('Would you like to see all the assignments per course? Yes or No')
while answer6=="Yes" or answer6=='yes'or answer6=='no'or answer6=='No':
      if answer6=="Yes" or answer6=='yes':
         if len(python_assignment)==0:
            print('No Python assignment')
         else:
                  print('The Python assignment are:',python_assignment)
         if len(java_assignment)==0:
                  print('No Java assignment')
         else:
                  print('The Java assignment are:',java_assignment)
         if len(javascript_assignment)==0:
                  print('No Javascript assignment')
         else:
                  print('The Javascript assignment are:',javascript_assignment)
         if len(c_assignment)==0:
                  print('No C# assignment')
         else:
                  print('The C# assignment are:',c_assignment)
         break
      else:
            break
else:
     answer2=input('Would you like to see all the assignments per course? Yes or No')



#Εδώ ρωτάμε το χρήστη αν θέλει να δει τα assignments ανά μαθητή ανά μάθημα.
answer7=input('Would you like to see all assignments per students per course? Yes or No')
while answer7=="Yes" or answer7=='yes' or answer7=='no'or answer7=='No':
      if answer7=="Yes" or answer7=='yes':
             if (n_of_st)==0:
                    print('No Students')
                    break
             else:
                   for i in range (n_of_st):
                         i= "\n".join("{} {} {} {}".format(x, y, z ,d) for x, y, z ,d in zip(students_name,assignment_list,coursesss,coursesss2))
                   print('All assignments per student per course:',i)
                   break
             

else:
       answer7=input('Would you like to see all assignments per student per course? Yes or No')

#Eδώ ρωτάμε το χρήστη αν θέλει να δεί ποιοί μαθητές έχουν πάνω απο ένα μάθημα(δηλαδή 2)       
answer8=input('Would you like to see the students with over one lesson? Yes or No?')
while answer8=="Yes" or answer8=='yes'or answer8=='no'or answer8=='No':
      if answer8=="Yes" or answer8=='yes':
            if len(courses_2)==0:
                  print('There are no students with more than 1 student')
                  break
            else:
                  print(courses_2)
                  break

      else:
            break
else:
      answer8=input('Would you like to see the students with over one student? Yes or No?')

#Εδώ ρωτάμε το χρήστη αν θέλει να δει όλα τα μαθήματα .
answer9=input('Would you like to see all courses? Yes or No')
while answer9=="Yes" or answer9=='yes' or answer9=='no'or answer9=='No':
      if answer9=="Yes" or answer9=='yes':
             if (len(all_courses))!=0:
                  offerd_courses=list(set(all_courses))
                  print(offerd_courses)
                  break
      else:
            break
             

else:
       answer9=input('Would you like to see all courses? Yes or No')
