import streamlit as st
import pandas as pd

# Sample data for demonstration
patients_data = {
    'PatientID': [1, 2, 3],
    'Name': ['John Doe', 'Jane Smith', 'Bob Johnson'],
    'Age': [30, 25, 40],
    'Admission Date': ['2024-01-01', '2024-02-15', '2024-03-10']
}

patients_df = pd.DataFrame(patients_data)

# Streamlit UI
def main():
    st.title('Hospital Management System')

    page = st.sidebar.selectbox('Select a page', ['Home', 'Patients'])

    if page == 'Home':
        display_home()
    elif page == 'Patients':
        display_patients()

def display_home():
    st.write('Welcome to the Hospital Management System!')

def display_patients():
    st.header('Patients Information')

    # Display patient data
    st.dataframe(patients_df)

    # Add new patient
    st.subheader('Add New Patient')
    name = st.text_input('Name:')
    age = st.number_input('Age:')
    admission_date = st.date_input('Admission Date:')

    if st.button('Add Patient'):
        new_patient = {
            'PatientID': len(patients_df) + 1,
            'Name': name,
            'Age': age,
            'Admission Date': admission_date
        }
        patients_df = patients_df.append(new_patient, ignore_index=True)
        st.success('Patient added successfully!')

if __name__ == '__main__':
    main()
