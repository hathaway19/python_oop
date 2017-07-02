class Patient(object):
    # Initialize information about patient (id, name, allergies)
    def __init__(self, patient_id, patient_name, allergies):
        self.patient_id = patient_id
        self.patient_name = patient_name
        self.allergies = allergies
        self.bed_number = None # no bed number assigned at start

class Hospital(object):
    # Initialize hospital name, and number of spots avaiable for patients
    def __init__(self, hospital_name, capacity):
        self.patients = [] # 0 patients at start
        self.hospital_name = hospital_name
        self.capacity = capacity
    #Method to add a patient to the hospital
    def admit(self, patient_id, patient_name, allergies, bed_number):
        # If hospital is full, can't admit patient
        if len(self.patients) >= self.capacity:
            print "The hospital is full. Can't admit patient"
            return self
        else:
            # If bed number assigned is already full, can't admit patient
            for patient in self.patients:
                if patient.bed_number == bed_number:
                    print "A different patient is already in bed", bed_number, ". Can't add patient"
                    return self
            # Set patient info
            new_patient = Patient(patient_id, patient_name, allergies)
            new_patient.bed_number = bed_number # Assign bed number for patient
            self.patients.append(new_patient) # Add patient to list
            print "The patient has successfully been admitted to the hospital!"
            return self
    def discharge(self, patient_id, patient_name):
        # Check patients for match
        for patient in self.patients:
            if patient.patient_id == patient_id and patient.patient_name == patient_name:
                print "Found the correct patient to discharge. Removing patient id:", patient.patient_id
                self.patients.remove(patient) # Remove patient from list
                return self
        print "Found no patinet with matching name and id to discharge..."
        return self

# Test case
hospital_1 = Hospital("Bellevue Hospital", 2)
hospital_1.admit(1, "Jim", ["veggies", "dairies"], 1).admit(2, "Tim", ["penuts"], 2).discharge(2,"Tim")