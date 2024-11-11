import streamlit as st
from qr_code import ContactInfo
import os
from PIL import Image

st.title("vCard QR Code Generator")

# Create two columns for required and optional fields
col1, col2, col3 = st.columns(3)

with col1:
    st.header("Required Fields")
    formatted_name = st.text_input("Full Name*", help="Required field")
    telephone = st.text_input("Telephone", help="Either telephone or email is required")
    email = st.text_input("Email", help="Either telephone or email is required")

with col2:
    st.header("Optional Fields")
    # Name components
    family_name = st.text_input("Family Name")
    given_name = st.text_input("Given Name")
    additional_name = st.text_input("Middle Name")
    name_prefix = st.text_input("Name Prefix (e.g., Dr.)")
    
    # Personal info
    birthday = st.date_input("Birthday", value=None)
    anniversary = st.date_input("Anniversary", value=None)
    gender = st.selectbox("Gender", ["", "M", "F", "O", "N", "U"])

with col3:
    # Professional info
    title = st.text_input("Job Title")
    role = st.text_input("Role/Occupation")
    organization = st.text_input("Organization")

    # Contact info
    url = st.text_input("Website URL")
    im_address = st.text_input("IM Address")
    
    # Address
    street = st.text_input("Street Address")
    city = st.text_input("City")
    region = st.text_input("State/Region")
    postal_code = st.text_input("Postal Code")
    country = st.text_input("Country")
    
    # Additional info
    note = st.text_area("Notes")

# File uploaders
st.header("Images")

logo_file = st.file_uploader("Upload Logo", type=['png', 'jpg', 'jpeg'])

photo_file = st.file_uploader("Upload Photo", type=['png', 'jpg', 'jpeg'])

if st.button("Generate QR Code"):
    if not formatted_name:
        st.error("Full Name is required!")
    elif not (telephone or email):
        st.error("Either telephone or email is required!")
    else:
        # Handle uploaded files
        logo_path = None
        photo_path = None
        
        if logo_file:
            logo_path = f"temp_logo.{logo_file.type.split('/')[-1]}"
            with open(logo_path, "wb") as f:
                f.write(logo_file.getbuffer())
        
        if photo_file:
            photo_path = f"temp_photo.{photo_file.type.split('/')[-1]}"
            with open(photo_path, "wb") as f:
                f.write(photo_file.getbuffer())

        # Create contact info object
        contact = ContactInfo(
            formatted_name=formatted_name,
            family_name=family_name,
            given_name=given_name,
            additional_name=additional_name,
            name_prefix=name_prefix,
            photo=photo_path,
            birthday=str(birthday) if birthday else "",
            anniversary=str(anniversary) if anniversary else "",
            gender=gender,
            street=street,
            city=city,
            region=region,
            postal_code=postal_code,
            country=country,
            telephone=telephone,
            email=email,
            im_address=im_address,
            title=title,
            role=role,
            logo=logo_path,
            organization=organization,
            note=note,
            url=url
        )
        
        try:
            # Generate QR code
            contact.generate_qr()
            
            # Display QR code
            if os.path.exists('contact_qr.png'):
                st.image('contact_qr.png', caption='Your vCard QR Code')
                
                # Download button
                with open('contact_qr.png', 'rb') as f:
                    st.download_button(
                        label="Download QR Code",
                        data=f,
                        file_name='contact_qr.png',
                        mime='image/png'
                    )
        except Exception as e:
            st.error(f"An Error has Occurred: {e}")
            
        # Cleanup temporary files
        if logo_path and os.path.exists(logo_path):
            os.remove(logo_path)
        if photo_path and os.path.exists(photo_path):
            os.remove(photo_path)
