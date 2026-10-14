# Oop_Assignment1.py
VACINATION TRACKER

Module: PROG211 – Object-Oriented Programming 1 (Individual Assignment) Domain: Health – Vaccination Tracker Language: Python 3 (no external libraries needed)

The problem

Clinics can easily lose track of who has finished their vaccine doses. This program tracks each person's progress through a vaccine course (e.g. Measles needs 2 doses) and shows who is complete and who still needs follow-up.


HOW TO RUN:
python vaccination_tracker.py
OOP concepts used
Task	What I did
Task 1 – Classes & objects	Patient, Vaccine, VaccinationRecord.
 A record contains a Patient and a Vaccine object, so the objects interact.
Task 2 – Data structure	A dictionary (registry): record ID → VaccinationRecord. Functions add_record() and display_records() add and show records. Tuples (AGE_GROUPS, VACCINES) hold fixed data (optional bonus).
Task 3 – Methods	Instance: give_dose(), is_complete(), display_info(). Class (@classmethod): Patient.register(), Patient.total_patients(). Static (@staticmethod): Patient.is_valid_age_group().

 
 HOW IT ALIGNS WITH DIGITAL PUBLIC GOODS(DPG)STANDARDS   

OPEN SOURSCE: The code is public on GitHub and free to reuse or improve.


INCLUSIVE AND ACCESSIBLE: Simple text menu, plain-English prompts, input validation with friendly error messages, no internet or paid software needed (works on low-end computers).


PRIVACY RESPECTING: No names, phone numbers or addresses are stored. People are identified only by anonymous IDs (e.g. P001) and a broad age group.


MODULAR & REUSABLE: Each class has one job; helper functions keep the menu clean. Another developer can reuse Patient or Vaccine or add new vaccines by editing one tuple.


EXAMPLE USAGE: (sample input/output)

Choose: 1
Age groups: infant, toddler, child, teen, adult
Enter age group: toddler
  1. Measles (2 dose(s) needed)
  2. Polio (OPV) (4 dose(s) needed)
...


Pick a vaccine number: 2
  Saved! Record VR-003 for P003.

Choose: 2
Enter record ID (e.g. VR-001): VR-003
  Dose given. 3 dose(s) remaining.

Choose: 3
  [VR-001] Patient P001 (infant) | Measles: 1/2 -> IN PROGRESS
  [VR-002] Patient P002 (child) | Yellow Fever: 1/1 -> COMPLETE
  [VR-003] Patient P003 (toddler) | Polio (OPV): 1/4 -> IN PROGRESS

Choose: 4
  Patients registered : 3
  Records in total    : 3
  Fully vaccinated    : 1

AUTHOUR:
Alfreda Victoria Dumbuya – 905005462 – Limkokwing University of Creative Technology, Sierra Leone
