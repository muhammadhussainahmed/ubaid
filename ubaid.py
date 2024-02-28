import streamlit as st
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

# Database setup
Base = declarative_base()
engine = create_engine('sqlite:///:memory:', echo=True)  # Use a real database URL in a production environment

class Patient(Base):
    __tablename__ = 'patients'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    records = relationship('MedicalRecord', back_populates='patient')

class MedicalRecord(Base):
    __tablename__ = 'medical_records'
    id = Column(Integer, primary_key=True)
    diagnosis = Column(String)
    patient_id = Column(Integer, ForeignKey('patients.id'))
    patient = relationship('Patient', back_populates='records')

Base.metadata.create_all(engine)

# Streamlit app
def main():
    st.title("Hospital Management System")

    # Sidebar for adding patients
    st.sidebar.header("Add Patient")
    patient_name = st.sidebar.text_input("Patient Name")
    if st.sidebar.button("Add Patient"):
        add_patient(patient_name)

    # Display patient data
    display_patients()

def add_patient(name):
    Session = sessionmaker(bind=engine)
    session = Session()

    new_patient = Patient(name=name)
    session.add(new_patient)
    session.commit()

def display_patients():
    Session = sessionmaker(bind=engine)
    session = Session()

    patients = session.query(Patient).all()

    st.header("Patient List")
    for patient in patients:
        st.write(f"Patient ID: {patient.id}, Name: {patient.name}")
        for record in patient.records:
            st.write(f"  Record ID: {record.id}, Diagnosis: {record.diagnosis}")
        st.write("\n")

if __name__ == "__main__":
    main()
