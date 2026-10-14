#Tuples = data that should never change while the program runs (bonus marks!)
AGE_GROUPS = ("infant", "toddler", "child", "teen", "adult")


# ----------------------------------------------------------------------
# CLASS 1: Patient  (anonymous on purpose -> privacy-respecting DPG rule)
# ----------------------------------------------------------------------
class Patient:
    _counter = 0  # class attribute: shared by ALL patients, used to make IDs

    def __init__(self, patient_id, age_group):
        self.patient_id = patient_id
        self.age_group = age_group

    # Class method: builds a Patient and auto-generates the next anonymous ID
    @classmethod
    def register(cls, age_group):
        cls._counter += 1
        return cls(f"P{cls._counter:03d}", age_group)

    # Class method: reads the shared counter
    @classmethod
    def total_patients(cls):
        return cls._counter

    # Static method: doesn't need self or cls, just a helpful checker
    @staticmethod
    def is_valid_age_group(age_group):
        return age_group in AGE_GROUPS

    # Instance method
    def display_info(self):
        return f"Patient {self.patient_id} ({self.age_group})"


# ----------------------------------------------------------------------
# CLASS 2: Vaccine
# ----------------------------------------------------------------------
class Vaccine:
    def __init__(self, name, doses_required):
        self.name = name
        self.doses_required = doses_required

    def display_info(self):
        return f"{self.name} ({self.doses_required} dose(s) needed)"


# A tuple of Vaccine objects: the clinic's fixed list of vaccines
VACCINES = (
    Vaccine("Measles", 2),
    Vaccine("Polio (OPV)", 4),
    Vaccine("Hepatitis B", 3),
    Vaccine("Yellow Fever", 1),
)


# ----------------------------------------------------------------------
# CLASS 3: VaccinationRecord  (this is where the objects interact:
#          one record HAS a Patient and HAS a Vaccine)
# ----------------------------------------------------------------------
class VaccinationRecord:
    def __init__(self, record_id, patient, vaccine):
        self.record_id = record_id
        self.patient = patient      # a Patient object
        self.vaccine = vaccine      # a Vaccine object
        self.doses_taken = 0

    # Instance method: give one dose (stops when the course is complete)
    def give_dose(self):
        if self.is_complete():
            return "Already fully vaccinated, no more doses needed."
        self.doses_taken += 1
        left = self.vaccine.doses_required - self.doses_taken
        if left == 0:
            return "Dose given. Vaccination course COMPLETE!"
        return f"Dose given. {left} dose(s) remaining."

    # Instance method
    def is_complete(self):
        return self.doses_taken >= self.vaccine.doses_required

    # Instance method
    def display_info(self):
        status = "COMPLETE" if self.is_complete() else "IN PROGRESS"
        return (f"[{self.record_id}] {self.patient.display_info()} | "
                f"{self.vaccine.name}: {self.doses_taken}/"
                f"{self.vaccine.doses_required} -> {status}")


# ----------------------------------------------------------------------
# DATA STRUCTURE: one dictionary -> key = record ID, value = record object
# ----------------------------------------------------------------------
def add_record(registry, patient, vaccine):
    """Create a record and store it in the dictionary."""
    record_id = f"VR-{len(registry) + 1:03d}"
    record = VaccinationRecord(record_id, patient, vaccine)
    registry[record_id] = record
    return record


def display_records(registry):
    """Loop through the dictionary and print every record."""
    if not registry:
        print("  (no records yet)")
        return
    for record in registry.values():
        print("  " + record.display_info())


# ----------------------------------------------------------------------
# Small helpers for the menu (keeps main() clean and modular)
# ----------------------------------------------------------------------
def choose_age_group():
    print("Age groups:", ", ".join(AGE_GROUPS))
    while True:
        answer = input("Enter age group: ").strip().lower()
        if Patient.is_valid_age_group(answer):
            return answer
        print("  Oops, that's not on the list. Try again.")


def choose_vaccine():
    for number, vaccine in enumerate(VACCINES, start=1):
        print(f"  {number}. {vaccine.display_info()}")
    while True:
        answer = input("Pick a vaccine number: ").strip()
        if answer.isdigit() and 1 <= int(answer) <= len(VACCINES):
            return VACCINES[int(answer) - 1]
        print("  Please type a number from the list.")


def load_demo_data(registry):
    """Pre-loads a few anonymous examples so the program shows something."""
    first = Patient.register("infant")
    second = Patient.register("child")
    r1 = add_record(registry, first, VACCINES[0])
    add_record(registry, second, VACCINES[3]).give_dose()
    r1.give_dose()


# ----------------------------------------------------------------------
# MAIN MENU
# ----------------------------------------------------------------------
def main():
    registry = {}
    load_demo_data(registry)

    print("=" * 50)
    print("   VACCINATION TRACKER (privacy-friendly, no names)")
    print("=" * 50)

    while True:
        print("\n1. Register patient + start vaccination record")
        print("2. Give a dose")
        print("3. Show all records")
        print("4. Summary")
        print("0. Exit")
        choice = input("Choose: ").strip()

        if choice == "1":
            patient = Patient.register(choose_age_group())
            record = add_record(registry, patient, choose_vaccine())
            print(f"  Saved! Record {record.record_id} for {patient.patient_id}.")

        elif choice == "2":
            display_records(registry)
            record_id = input("Enter record ID (e.g. VR-001): ").strip().upper()
            if record_id in registry:
                print("  " + registry[record_id].give_dose())
            else:
                print("  Record not found.")

        elif choice == "3":
            display_records(registry)

        elif choice == "4":
            done = sum(1 for r in registry.values() if r.is_complete())
            print(f"  Patients registered : {Patient.total_patients()}")
            print(f"  Records in total    : {len(registry)}")
            print(f"  Fully vaccinated    : {done}")

        elif choice == "0":
            print("Stay healthy! Goodbye.")
            break
        else:
            print("  Invalid choice, try again.")


if __name__ == "__main__":
    main()
