import streamlit as st
import pandas as pd
import numpy as np
import joblib

model = joblib.load('model.pkl')
image = 'Banner.jpg'

def display_sidebar():
    st.sidebar.subheader("Masukkan Data Siswa")

    marital_status = st.sidebar.selectbox("Status Pernikahan", ["Single", "Married", "Divorced"], key='marital_status')
    application_mode = st.sidebar.selectbox("Mode Pendaftaran", [
        "1st phase - general contingent",
        "2nd phase - general contingent",
        "International student (bachelor)",
        "Over 23 years old",
        "Change of course",
        "Technological specialization diploma holders",
        "Holders of other higher courses",
        "3rd phase - general contingent",
        "Transfer",
        "Change of institution/course",
        "1st phase - special contingent (Madeira Island)",
        "Short cycle diploma holders",
        "1st phase - special contingent (Azores Island)",
        "Ordinance No. 854-B/99",
        "Ordinance No. 612/93",
        "Change of institution/course (International)",
        "Ordinance No. 533-A/99, item b2 (Different Plan)",
        "Ordinance No. 533-A/99, item b3 (Other Institution)"
    ], key='application_mode')
    application_order = st.sidebar.selectbox("Pilihan Kursus", ["First Choice", "Second Choice"], key='application_order')
    course = st.sidebar.selectbox("Program Studi", [
        "Animation and Multimedia Design",
        "Tourism",
        "Communication Design",
        "Journalism and Communication",
        "Social Service (evening attendance)",
        "Management",
        "Social Service",
        "Veterinary Nursing",
        "Advertising and Marketing Management",
        "Management (evening attendance)",
        "Agronomy",
        "Basic Education",
        "Informatics Engineering",
        "Equinculture",
        "Oral Hygiene",
        "Biofuel Production Technologies"
    ], key='course')
    daytime_evening_attendance = st.sidebar.selectbox("Waktu Kuliah", ["Daytime", "Evening"], key='daytime_evening_attendance')
    previous_qualification_grade = st.sidebar.slider("Nilai Kualifikasi Sebelumnya", min_value=0, max_value=200, step=1, key='previous_qualification_grade')
    nationality = st.sidebar.selectbox("Kebangsaan", [
        "Portuguese",
        "German",
        "Spanish",
        "Italian",
        "Dutch",
        "English",
        "Lithuanian",
        "Angolan",
        "Cape Verdean",
        "Guinean",
        "Mozambican",
        "Santomean",
        "Turkish",
        "Brazilian",
        "Romanian",
        "Moldova (Republic of)",
        "Mexican",
        "Ukrainian",
        "Russian",
        "Cuban",
        "Colombian"
    ], key='nationality')
    mothers_qualification = st.sidebar.selectbox("Kualifikasi Ibu", [
        "Basic Education",
        "Secondary Education",
        "Higher Education",
        "Other"
    ], key='mothers_qualification')
    fathers_qualification = st.sidebar.selectbox("Kualifikasi Ayah", [
        "Basic Education",
        "Secondary Education",
        "Higher Education",
        "Other"
    ], key='fathers_qualification')
    mothers_occupation = st.sidebar.selectbox("Pekerjaan Ibu", [
        "Unskilled Workers",
        "Administrative Staff",
        "Service Workers",
        "Technicians",
        "Professionals",
        "Skilled Workers",
        "Student",
        "Managers",
        "Agricultural Workers",
        "Other",
        "Machine Operators"
    ], key='mothers_occupation')
    fathers_occupation = st.sidebar.selectbox("Pekerjaan Ayah", [
        "Unskilled Workers",
        "Skilled Workers",
        "Service Workers",
        "Administrative Staff",
        "Technicians",
        "Machine Operators",
        "Armed Forces",
        "Agricultural Workers",
        "Professionals",
        "Managers",
        "Student",
        "Other"
    ], key='fathers_occupation')
    admission_grade = st.sidebar.slider("Nilai Penerimaan", min_value=0, max_value=200, step=1, key='admission_grade')
    displaced = st.sidebar.selectbox("Apakah siswa tersebut adalah orang yang terlantar", ["Yes", "No"], key='displaced')
    educational_special_needs = st.sidebar.selectbox("Kebutuhan Pendidikan Khusus", ["Yes", "No"], key='educational_special_needs')
    debtor = st.sidebar.selectbox("Debitor", ["Yes", "No"], key='debtor')
    tuition_fees_up_to_date = st.sidebar.selectbox("Biaya Kuliah Terbayar", ["Yes", "No"], key='tuition_fees_up_to_date')
    gender = st.sidebar.selectbox("Jenis Kelamin", ["Male", "Female"], key='gender')
    scholarship_holder = st.sidebar.selectbox("Penerima Beasiswa", ["Yes", "No"], key='scholarship_holder')
    age_at_enrollment = st.sidebar.number_input("Usia Saat Pendaftaran", key='age_at_enrollment', format='%f')
    international = st.sidebar.selectbox("Apakah siswa tersebut adalah siswa internasional", ["Yes", "No"], key='international')
    curricular_units_1st_sem_credited = st.sidebar.number_input("Curricular units 1st sem (credited)", min_value=0, key='curricular_units_1st_sem_credited')
    curricular_units_1st_sem_enrolled = st.sidebar.number_input("Curricular units 1st sem (enrolled)", min_value=0, key='curricular_units_1st_sem_enrolled')
    curricular_units_1st_sem_evaluations = st.sidebar.number_input("Curricular units 1st sem (evaluations)", min_value=0, key='curricular_units_1st_sem_evaluations')
    curricular_units_1st_sem_grade = st.sidebar.number_input("Curricular units 1st sem (grade)", key='curricular_units_1st_sem_grade')
    curricular_units_1st_sem_approved = st.sidebar.number_input("Curricular units 1st sem (approved)", min_value=0, key='curricular_units_1st_sem_approved')
    curricular_units_1st_sem_without_evaluations = st.sidebar.number_input("Curricular units 1st sem (without evaluations)", key='curricular_units_1st_sem_without_evaluations')
    curricular_units_2nd_sem_without_evaluations = st.sidebar.number_input("Curricular units 2nd sem (without evaluations)", key='curricular_units_2nd_sem_without_evaluations')
    unemployment_rate = st.sidebar.number_input("Unemployment Rate", key='unemployment_rate', format='%f')
    inflation_rate = st.sidebar.number_input("Inflation Rate", key='inflation_rate', format='%f')
    gdp = st.sidebar.number_input("GDP", key='gdp', format='%f')
    input_data = pd.DataFrame({
        'Previous_qualification_grade': [previous_qualification_grade],
        'Admission_grade': [admission_grade],
        'Age_at_enrollment': [age_at_enrollment],
        'Curricular_units_1st_sem_credited': [curricular_units_1st_sem_credited],
        'Curricular_units_1st_sem_evaluations': [curricular_units_1st_sem_evaluations],
        'Curricular_units_1st_sem_grade': [curricular_units_1st_sem_grade],
        'Curricular_units_1st_sem_without_evaluations': [curricular_units_1st_sem_without_evaluations],
        'Curricular_units_2nd_sem_without_evaluations': [curricular_units_2nd_sem_without_evaluations],
        'Unemployment_rate': [unemployment_rate],
        'Inflation_rate': [inflation_rate],
        'GDP': [gdp],
        'Application_mode': [application_mode],
        'Application_order': [application_order],
        'Course': [course],
        'Mothers_qualification': [mothers_qualification],
        'Fathers_qualification': [fathers_qualification],
        'Mothers_occupation': [mothers_occupation],
        'Fathers_occupation': [fathers_occupation],
        'Displaced': [displaced],
        'Gender': [gender]
    })

    return input_data

def predict_status_proba(model, data):
    prediction_proba = model.predict_proba(data)
    return prediction_proba

def main():
    st.set_page_config(page_title="Aplikasi Prediksi Dropout", page_icon=":bar_chart:", layout="wide")

    st.image(image, use_column_width=True)

    input_data = display_sidebar()

    st.markdown("***")

    if st.sidebar.button("Prediksi"):
        if input_data.isnull().values.any():
            st.error("Harap isi semua data siswa terlebih dahulu.")
        else:
            prediction_proba = predict_status_proba(model, input_data)
            dropout_prob = prediction_proba[0][1]
            not_dropout_prob = prediction_proba[0][0]

            st.subheader("Prediksi Status Dropout:")
            if dropout_prob > 0.5:
                st.error(f"Probabilitas Dropout: {dropout_prob:.2%}")
                st.write("Ada kemungkinan besar siswa akan mengalami dropout.")
            else:
                st.success(f"Probabilitas Tidak Dropout: {not_dropout_prob:.2%}")
                st.write("Kemungkinan besar siswa tidak dropout.")

    st.markdown("***")
    st.markdown(
        "<div style='text-align: center; color: #666; margin-top: 30px;'>Copyright © 2024 | arifsofyan004@gmail.com</div>",
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()
