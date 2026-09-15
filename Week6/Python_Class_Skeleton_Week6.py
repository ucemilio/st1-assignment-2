# Python Class Skeleton for Week 6

class Patient:
    def __init__(self, name, contact_details=""):
        self.name = name
        self.contact_details = contact_details

    def update_info(self, new_details):
        self.contact_details = new_details


class Practitioner:
    def __init__(self, name):
        self.name = name
        self.appointments = []

    def has_conflict(self, time):
        return any(appt.time == time and appt.status == "active" for appt in self.appointments)

    def get_scheduled_appointments(self):
        return [appt for appt in self.appointments if appt.status == "active"]


class Appointment:
    def __init__(self, patient, practitioner, time):
        self.patient = patient
        self.practitioner = practitioner
        self.time = time
        self.status = "active"

    def cancel(self):
        self.status = "cancelled"