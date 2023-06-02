from terminaltables import AsciiTable

class Patient:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

class Doctor:
    def __init__(self, name, specialization):
        self.name = name
        self.specialization = specialization


class Appointment:
    def __init__(self, patient, doctor, date, time):
        self.patient = patient
        self.doctor = doctor
        self.date = date
        self.time = time

    def calculate_cost(self):
        # Define your billing logic here
        # Example: Calculate cost based on doctor's specialization and appointment duration
        if self.doctor.specialization == "Anesthesiologists":
            base_cost = 200  # Base cost for Anesthesiologists appointments
        elif self.doctor.specialization == "Neurologists":
            base_cost = 150  # Base cost for Neurologists appointments
        else:
            base_cost = 100  # Base cost for other specializations

        # Calculate additional charges based on appointment duration
        appointment_duration = 1  # Assuming each appointment lasts for 1 hour
        additional_charges = appointment_duration * 20  # Additional charges of Ghc 20 per hour

        # Calculation of Cost
        total_cost = base_cost + additional_charges

        return total_cost


class HospitalManagementSystem:
    def __init__(self):
        self.patients = []
        self.doctors = []  # List to store doctor objects
        self.appointments = []  # List to store appointment objects

    def add_patient(self):
        name = input("Enter patient name: ")
        age = int(input("Enter patient age: "))
        gender = input("Enter patient gender: ")
        patient = Patient(name, age, gender)
        self.patients.append(patient)
        print("Patient added successfully.")

    def add_doctor(self):
        name = input("Enter the doctor name: ")
        specialization = input("Enter the doctor specialization: ")
        doctor = Doctor(name, specialization)
        self.doctors.append(doctor)
        print("Doctor added successfully.")

    def schedule_appointment(self):
        patient_name = input("Enter the patient name: ")
        doctor_name = input("Enter the doctor name: ")
        date = input("Enter the appointment date (DD-MM-YYYY): ")
        time = input("Enter the appointment time: ")

        # Find patient and doctor objects
        patient = next((p for p in self.patients if p.name.lower() == patient_name.lower()), None)
        doctor = next((d for d in self.doctors if d.name.lower() == doctor_name.lower()), None)

        if patient and doctor:
            appointment = Appointment(patient, doctor, date, time)
            self.appointments.append(appointment)
            print("Appointment scheduled successfully.")
        else:
            print("Patient or doctor not found. Please check the names.")

    def search_patient(self, name):
        found_patients = [patient for patient in self.patients if patient.name.lower() == name.lower()]

        if found_patients:
            table_data = [["Name", "Age", "Gender"]]
            for patient in found_patients:
                table_data.append([patient.name, str(patient.age), patient.gender])

            table = AsciiTable(table_data)
            print(table.table)
        else:
            print("No patient found with the given name.")

    def generate_bill(self):
        patient_name = input("Enter the patient name: ")
        appointment_date = input("Enter the appointment date (DD-MM-YYYY): ")

        # Find the patient's appointments
        patient_appointments = [appointment for appointment in self.appointments
                                if appointment.patient.name.lower() == patient_name.lower()
                                and appointment.date == appointment_date]

        if patient_appointments:
            table_data = [["Doctor", "Date", "Time", "Cost"]]
            total_cost = 0
            for appointment in patient_appointments:
                # Calculate the cost for each appointment based on some criteria
                appointment_cost = appointment.calculate_cost()
                total_cost += appointment_cost
                table_data.append([appointment.doctor.name, appointment.date, appointment.time, str(appointment_cost)])

            table = AsciiTable(table_data)
            print(table.table)
            print("Total bill for", patient_name, "on", appointment_date, "is:", total_cost)
        else:
            print("No appointments found for the patient on the given date.")


hospital = HospitalManagementSystem()

while True:
    option = input("Enter '1' to add a patient, '2' to add a doctor, '3' to schedule an appointment, "
                   "'4' to search for a patient, '5' to generate a bill, or '6' to exit: ")

    if option == '1':
        hospital.add_patient()
    elif option == '2':
        hospital.add_doctor()
    elif option == '3':
        hospital.schedule_appointment()
    elif option == '4':
        name = input("Enter the patient name to search: ")
        hospital.search_patient(name)
    elif option == '5':
        hospital.generate_bill()
    elif option == '6':
        break
    else:
        print("Invalid option. Please try again.")
