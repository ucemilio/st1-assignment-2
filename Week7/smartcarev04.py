# SmartCare V04
# This builds on Python_Class_Skeleton_Week6.py, and upgraded per the Stage 4 requirements
# Encapsulation review, composition/inheritance decisions, and the AI Pair-Programming Record 
# (Appointment status is now protected behind an enum + cancel() instead of a raw, publicly settable string).

from enum import Enum


class AppointmentStatus(Enum):
    SCHEDULED = "scheduled"
    CANCELLED = "cancelled"


class InvalidTransitionError(Exception):
    """Raised when an appointment status change is not allowed."""
    pass


class Patient:
    def __init__(self, name: str, contact_details: str = "") -> None:
        if not name.strip():
            raise ValueError("Patient name cannot be empty.")
        self.name: str = name
        self.contact_details: str = contact_details

    def update_info(self, new_details: str) -> None:
        self.contact_details = new_details


class Practitioner:
    # Task C: now carries an identifier and specialty
    # Lab instruction ("Practitioner with identifier, name and specialty").
    def __init__(self, identifier: str, name: str, specialty: str = "") -> None:
        if not name.strip():
            raise ValueError("Practitioner name cannot be empty.")
        self.identifier: str = identifier
        self.name: str = name
        self.specialty: str = specialty
        self._appointments: list["Appointment"] = []

    def has_conflict(self, time: str) -> bool:
        # Only SCHEDULED (i.e. still-active) appointments count as a conflict
        # A cancelled appointment at the same time is not a clash (FR-05/FR-07).
        return any(
            appt.time == time and appt.status == AppointmentStatus.SCHEDULED
            for appt in self._appointments
        )

    def get_scheduled_appointments(self) -> list["Appointment"]:
        return [a for a in self._appointments if a.status == AppointmentStatus.SCHEDULED]

    def _register_appointment(self, appointment: "Appointment") -> None:
        # Internal use only, called from Appointment.__init__ and not external callers.
        # Keeps the appointment list out of public reach (encapsulation review, Activity 1).
        self._appointments.append(appointment)


class Appointment:
    # Composition/association decision (Stage 4, Activity 2)
    # Appointment holds references to Patient and Practitioner. It is not a subtype of either, so no inheritance is used here.
    def __init__(self, patient: Patient, practitioner: Practitioner, time: str) -> None:
        if practitioner.has_conflict(time):
            raise InvalidTransitionError(
                f"{practitioner.name} already has a scheduled appointment at {time}."
            )
        self.patient: Patient = patient
        self.practitioner: Practitioner = practitioner
        self.time: str = time
        self._status: AppointmentStatus = AppointmentStatus.SCHEDULED
        practitioner._register_appointment(self)

    @property
    def status(self) -> AppointmentStatus:
        return self._status

    def cancel(self) -> None:
        # Only a SCHEDULED appointment can become CANCELLED - protects the
        # domain invariant identified in the Stage 4 Workbook, Section 2.
        if self._status != AppointmentStatus.SCHEDULED:
            raise InvalidTransitionError("Only a scheduled appointment can be cancelled.")
        self._status = AppointmentStatus.CANCELLED


if __name__ == "__main__":
    # Stage 4 Lab Activities: F - Manual Behaviour Checks
    print("Welcome to SmartCare: Community Clinic Appointment Booking System!")

    p1 = Patient("Alice Smith")
    pr1 = Practitioner("PR001", "Dr. John Doe", "General Practice")

    # Valid object creation
    appt1 = Appointment(p1, pr1, "2024-07-20 10:00 AM")
    print(f"Appointment created - status: {appt1.status}")

    # Invalid input - empty patient name
    try:
        Patient("")
    except ValueError as e:
        print(f"Validation caught: {e}")

    # Conflicting appointment for the same practitioner/time
    p2 = Patient("Bob Johnson")
    try:
        Appointment(p2, pr1, "2024-07-20 10:00 AM")
    except InvalidTransitionError as e:
        print(f"Conflict caught: {e}")

    # Cancel a scheduled appointment
    appt1.cancel()
    print(f"After cancel - status: {appt1.status}")

    # Attempt an illegal repeated transition
    try:
        appt1.cancel()
    except InvalidTransitionError as e:
        print(f"Illegal transition caught: {e}")

    # Confirm the same time slot is now free again after cancellation
    appt2 = Appointment(p2, pr1, "2024-07-20 10:00 AM")
    print(f"New appointment after cancellation - status: {appt2.status}")