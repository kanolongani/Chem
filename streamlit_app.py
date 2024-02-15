import requests
import json
import streamlit as st
import base64

def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

# Define a function to display the product page
def display_product_page(image_url, product_info):
    # Set title and page layout
    st.title("1000340-35-1")
    bin_str = get_base64("bg.jpg")
    
    st.markdown(
        """
        <style>
        /* Add a background with a chemistry-themed image */
        body {
            background-image: url("data:image/png;base64,%s");
            background-size: cover;
            background-repeat: no-repeat;
            font-family: Arial, sans-serif;
        }
        /* Style for bold key in JSON */
        .json-key {
            font-weight: bold;
            color: #0066ff; /* Blue color for keys */
        }
        </style>
        """% bin_str,
        unsafe_allow_html=True,
    )

    # Use Streamlit columns for layout
    col1, col2 = st.columns([2, 3])

    # Display image on the left side
    with col1:
        st.image(image_url, use_column_width=True)

    # Display product information on the right side
    with col2:
        st.markdown("**Description**")
        # Iterate over product info and display key-value pairs
        for key, value in product_info.items():
            st.markdown(f"<span class='json-key'>{key}:</span> {value}", unsafe_allow_html=True)

# Sample product information
product_info = {
    "Catalog Number": "24729564",
    "Chemical Name": "4-Bromo-1H-pyrrolo[2,3-B]pyridine-3-carbaldehyde",
    "CAS Number": "1000340-35-1",
    "Molecular Formula": "C8H5BrN2O",
    "Molecular Weight": "225.0421"
}

# URL of the product image
product_image_url = "https://pubchem.ncbi.nlm.nih.gov/image/imgsrv.fcgi?sid=391946015&t=s&deposited=t&version=1"

# Display the product page
display_product_page(product_image_url, product_info)

# response = requests.request("GET", url)

# response = response.text
# response = json.loads(response)

# chemical_name = response["Record"]["RecordTitle"]
# print(chemical_name)
# cas_number = response["Record"]["Reference"][0]["SourceID"]




# print(cas_number)

# st.json(response)




