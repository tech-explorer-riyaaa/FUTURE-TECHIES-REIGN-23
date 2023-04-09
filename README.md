# FUTURE-TECHIES-REIGN-23

# Introduction

The "Global Health Hospitals" is a chain of multi-speciality hospitals across India, specializing in different techniques and modern technology based procedures for the patients to have better treatments. To publicize the hospital's name an official website is created for the users, so that they can get the needed information and services from the site, saving their time from going offline to resolve their queries. Also while designing the website convenience of users have been kept in mind, hence we provided the site with an easy to use interface with multiple functionalities.

# Features
Multiple features have been provided in the site-
- **Ambulance help**-statewise availability of phone numbers incase of emergency situations. Each state is provided with one number, so as the person in need calls and inform about their location, their call is redirected to the nearest branch of hospital.
- **Book an Appointment**-form to book an appointemnt is provided at the site. Also the form can't get submitted until all entries are filled and the phone number and email id are in the correct format to maintain truthfulness of the data. These entries get stored in the excel sheet "appointment_list".
- **Request a Callback**- One can request for a callback by filling the details asked in the attached form. These entries get stored in the excel sheet "callback_requests".
- **Doctors**-List of all doctors alongwith their specialities, fees and the hospital's name is provided in this section.
- **Hospitals**-Since there is a big chain of these hospitals, statewise hospitals alongwith pincode and city name are mentioned in this section.
- **Specialities**-Since it is a multi-speciality hospital, all of its specialities alongwith their technical meanings are provided at the site.
- **Procedures**-All surgeries and other medical procedures that the hospital can provide are written in this section.
- **BMI CALCULATOR**-an easy health check that can be performed within a matter of seconds is by analysing BMI, also we have provided a few suggestions inaccordance with the BMI of the users.
- **Chatbot**-Though we have added the button for this purpose, but this lies within the future scope of the website that can make the user's experience better and more convenient.
- **Records**-We have attached the "book and appointment" form with an excel sheet so as to store the data in an organised manner.


# Technologies

- Python 3.11.2
- Python Modules:
    - tkinter
    - sqlite3
    - openpyxl
    - pillow
    - tkcalendar
- Excel Sheet

# How to Use

## Dashboard

Dashboard is the main window which opens when the code is run. It consists of various buttons which direct you to the required sub-window. The dashboard is easy to understand and easy to use, the buttons are named after exactly what their functions are, hence making it easy for the user to go through the website.

### Book an Appointment

- This sub-window get the form filled by the user for making an appointment.
- Entry Fields: These entries get stored in the excel sheet "Appointment_list".
    
    | FULL NAME |
    | MOBILE NUMBER |
    | EMAIL ADDRESS |
    
  Dropbox:
  
    | HOSPITAL NAME |
    | DEPARTMENT |
    | SELECT A DATE | 
    | TIME SLOT |
    
    - Drop Box: This helps in restricting the possible entries.
 
- Buttons:
    
    | SUBMIT |
    
    After clicking on the button, a popup will be shown confirming your appointment booking submitted in their records.

    
### Request CallBack

- This sub-window provides a form to be filled to get a callback.
- Entry Fields: These entries get stored in the excel sheet "callback_requests".
- Following entries have to be filled:
    
    
    | FIRST NAME |
    | LAST NAME |
    | MOBILE NUMBER |
    | EMAIL ADDRESS |
    | COMMENTS(optional) |
    
    Dropbox:
    | HOSPITAL |
    
    - Drop Box: This helps in restricting the possible entries. 
   
   
- Buttons:
    
    
    | SUBMIT |
    
    After clicking on the button, a popup will be shown confirming your callback request submitted in their records.


### DOCTORS

- This sub-window provides details of all the doctors across all the hospitals of this chain.

- Buttons:
    
    
    | BOOK AN APPOINTMENT |
    
    this button redirect you to the page of "Book an Appointment".
    

### HOSPITALS

- It provides the list and address of all the hospitals under this chain.
    

- Buttons:
    
   | REQUEST CALLBACK |
   
   this button redirects you to the page of "Request Callback".
   

### Ambulance Help

- It provides the list of statewise numbers to contact for an ambulance in an emergency situation.


### SPECIALITIES

- It is the list of specialities of the chain of hospitals alongwith the description of 'what they are'.

- Buttons:
 
    | Cancer Care/Oncology |
    | Cardiac Sciences |
    | Orthopaedics and Joint Replacement |
    | Gastroenterology and Heptalogy |
    | Robotic |
    | Liver Transplant and Biliary Sciences |
    | Neurosciences |
    | Thoracic Surgery |
    
    Clicking on these buttons will take you to the details ot the mentioned speciality.
    
### PROCEDURES

- This provides the user the exposure to the technologies used, procedures, operations, surgeries, ...etc that can be performed in these hospitals.

- Buttons:

     | Aortic Valve Surgery |
     | Da Vinci Robotic Surgery |
     | Lung Transplant |
     | LVAD Surgery |
     | Knee Replacement Surgery |
     | Bone Marrow Transplant |
     | Thoracic Surgery |
     | Bariatric Surgery |
     
     Clicking on these buttons will take you to the details ot the mentioned procedure.
     
### BMI Calcualtor

An easy and quick health check for the users to perform on their own within a few seconds at their homes.

- Entries:

     | Enter height (in m) |
     | Enter weight (in kg) |
     
 - Buttons:
 
     | Calculate |
     
 - By clicking on the 'calculate' button, BMI of the user will be shown on the screen, alongwith a healthy suggestion at the bottom of the window regrading their fitness.
 
# Team - FUTURE TECHIES here :)

This project was successfully developed by the contribution of the following team members:

- Anupriya Biala (CSE-AI , 2026)
- Payal (CSE-AI , 2026)
- Riya Ahlawat (CSE-AI , 2026)
- Samriddhi Tiwari (CSE-AI , 2026)
