# -*- coding: utf-8 -*-
{
    'name': "hospital_system",

    'summary': "Comprehensive hospital management system for managing patients, doctors, appointments, and medical records.",

    'description': """
        The Hospital Management System is designed to streamline the day-to-day operations of hospitals and clinics. 
        It provides a robust solution for managing patient data, doctor schedules, appointments, medical records, billing, 
        and hospital departments. This module aims to improve the efficiency of hospital administration and enhance 
        the quality of patient care. Key features include:
        - Patient registration and management
        - Doctor information and schedules
        - Appointment booking and management
        - Electronic medical records
        - Hospital billing and invoicing
        - Department management
    """,

    'author': "Amul Babariya",
    'category': 'Healthcare',
    'version': '17.0.0.1',

    'depends': ['base','mail'],

    'data': [
        'security/ir.model.access.csv',
        'views/hms_patient_views.xml',
        'views/hms_appointmnet_views.xml',
        'views/hms_appointmnet_views.xml',
        'views/hms_prescription_line_views.xml',
        'views/hms_gender_patient_view.xml',
        'views/hms_doctor_views.xml',
    ],

    'demo': [
        'demo/demo.xml',
    ],
    'images': ['static/description/icon.png'],
    'license': 'LGPL-3',
}
