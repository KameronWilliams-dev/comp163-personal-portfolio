Full_name="Jordan Smith"
Student_email="jsmith@ncat.edu"
hometown="Charlotte, NC"
grad_year=" Spring 2028"
major="Computer Science"
current_course=["COMP 163", "MATH 150", "ENG 101", "HIS 105"]
completed_course=["Biology", "Chemistry", "Calculus", "Spanish II", "World History"]
credit_hrs=[3, 3, 3, 3]
GPA_history=[3.2, 3.6, 3.4, 3.7]
emergency_contact=("(Mom)", "Hannah Smith", "704-555-0199")
home_address=("456 Oak Street","Charlotte" ,"NC","28202")
twitter_info=("Twitter","@jordandev",127)
instagram_info=("Instagram","@jordan_codes",312)
birthday=("Birthday", 5, 22, 2006)
credit_dict={"COMP 163": 3,"MATH 150": 3, "ENG 101": 3,"HIS 105": 3 }
proffesors_dict={"COMP 163":"Prof. Rhodes", "MATH 150": "Dr. Lee", "ENG 101": "Dr. Martinez", "HIS 105": "Dr. Brown"}
room_dict={"COMP 163": "M-Eric 300", "MATH 150": "Marteena 201", "ENG 101": "Crosby 121", "HIS 105": "Crosby 210"}
budget_dict={"Food": 450, "Entertainment": 200, "Books": 125, "Transportation": 100}
study_dict={"Programming": 10, "Math": 8, "English": 4, "History":3}
contact_dict={"Mom": "704-555-0199", "Roommate": '336-55-7821', "Academic Advisor":"336-334-5000"}
skills_set={"Time management", "Photography", "Problem solving", "HTML", "Python basics"}
learing_set={"Data structures", "Web design", "JavaScript", "Git", "Public speaking"}
career_set={"Software development", "Game development", "Web development", "Data science"}
hobbies_set={"Gaming", "Photography", "Reading", "Soccer", "Memento"}
entertainment_backlog={"One Piece", "Barry", "Life", "Incantation", "Memento"}
monthly_budget=sum(budget_dict.values())
social_media_followers=instagram_info[2]+twitter_info[2]
study_hrs=sum(study_dict.values())
total_credits=sum(credit_dict.values())
academic_load=study_hrs+total_credits
study_hrs_cost=budget_dict["Books"]/study_hrs
print("="*64)
print("PERSONAL ACADEMIC & LIFE PORTFOLIO".center(64))
print("="*64)
print(f"Student: {Full_name} | Email: {Student_email}\nFrom: {hometown} | Graduating:{grad_year}\nMajor: {major}\n")
print("=== ACADEMIC PROFILE ===")
print(f"Current Semester: {sum(credit_hrs)} credits across {len(current_course)} courses")
print(f"Cumulative GPA: {sum(GPA_history) / len(GPA_history):.2f}")
print(f"Weekly Study Time: {study_hrs} hours")
print(f"Academic Investment: ${study_hrs_cost:.1f} per study hour\n")
print("Current Courses:")
print(current_course[0],"-",(credit_hrs[0]),"credits -",(proffesors_dict["COMP 163"]),"-",(room_dict["COMP 163"]))
print(current_course[1],"-",(credit_hrs[1]),"credits -",(proffesors_dict["MATH 150"]),"-",(room_dict["MATH 150"]))
print(current_course[2],"-",(credit_hrs[2]),"credits -",(proffesors_dict["ENG 101"]),"-",(room_dict["ENG 101"]))
print(current_course[3],"-",(credit_hrs[3]),"credits -",(proffesors_dict["HIS 105"]),"-",(room_dict["HIS 105"]))
print("\n=== PERSONAL DEVELOPMENT ===")
print("Current Skills:",(skills_set))
print("Learning Goals:",(learing_set))
print("Career Interests:",(career_set))
print("Skills Currently Have:",len(skills_set))
print("Skills Want to Learn:",len(learing_set))
print("\n=== FINANCIAL OVERVIEW ===")
print(f"Monthly Budget: ${monthly_budget}")
print(f"Food: ${budget_dict['Food']} (${budget_dict["Food"]/30}/day)")
print(f"Entertainment: ${budget_dict["Entertainment"]}")
print(f"Books: ${budget_dict["Books"]}")
print(f"Transportation: ${budget_dict["Transportation"]}")
print(f"Annual Projection: ${monthly_budget*12}")
print("\n=== CONNECTIONS & CONTACTS ===")
print(f"Emergency Contact: {emergency_contact[1]} {emergency_contact[0]} - {emergency_contact[2]}")
print(f"Home Address: {home_address[0]}, {home_address[1]}, {home_address[2]} {home_address[3]}")
print(f"Social Media Presence: {social_media_followers} followers across 2 platforms")
print(f"Key Contacts: {len(contact_dict)} people in directory")
print("\n=== LIFE STATISTICS ===")
print(f"Total Courses Completed: {len(completed_course)}")
print(f"Current Academic Load: {academic_load} weekly commitments")
print(f"Entertainment Backlog: {len(entertainment_backlog)} items")
print(f"Current Hobbies: {len(hobbies_set)} activities")
print("="*64)