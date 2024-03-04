import requests
import json
import streamlit as st
from urllib.request import urlopen
import base64
import webbrowser
import streamlit.components.v1 as components

# embed streamlit docs in a streamlit app

@st.experimental_memo
def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()


img = get_img_as_base64("image.jpg")

page_bg_img__ = f"""

[data-testid="stAppViewContainer"] > .main {{
background-image: url("data:image/png;base64,{img}");
# background-repeat: no-repeat;
background-attachment: local;
}}

"""

def display_product_page(image_url, product_info):
    col1, col3 , col2 = st.columns([5,2,5])
    with col1:
        
        # st.image('logo.png', use_column_width=True)
        st.markdown(
        """<a href="http://www.aswmedchem.com/">
        <img src="data:image/png;base64,{}" width="283px">
        </a>""".format(
            base64.b64encode(open("logo.png", "rb").read()).decode()
        ),
        unsafe_allow_html=True,
)
        # st.markdown("[![Logo](logo.png)](http://www.aswmedchem.com/)", unsafe_allow_html=True)
    page_bg_img = f"""
    <style>

    {page_bg_img__}
    body {{
        font-family: Arial, sans-serif;
    }}
    .json-key {{
        font-weight: bold;
        color: #000000; 
        font-family : Calibri, sans-serif;

    }}
    .custom-div {{
        height: 300px;
        width: 350px;
        border-radius: 5%;
        background-color: #91ACE1;
        color: black;
        font-size: 20px;
    }}
    .custom-divss {{
        height: 300px;
        width: 400px;
        border-radius: 5%;
        background-color: #91ACE1;
        display: flex;
        justify-content: center;
        align-items: center;
        color: black;
        font-size: 25px;
    }}
    .description {{
        display: flex;
        flex-direction: column;
        align-items: flex-start;
        padding: 2px;
    }}
    .description-item {{
        justify-content: space-between;
        width: 100%;
        word-break: break-word; /* Adding word break to handle long values */
    }}
    .value {{
        flex: 1; /* Allow the value to grow and shrink */
        # overflow: hidden; /* Hide overflowing text */
        # text-overflow: ellipsis; /* Show ellipsis for overflowed text */
        font-family : Calibri, sans-serif;
    }}
     .footer {{
        left: 0;
        bottom: 0;
        width: 100%;
        margin-top: 50px;
        color: #ffffff;
        text-align: center;
        padding: 10px;
        font-size: 20px;
    }}

    </style>
    """
    st.markdown("""
    <style>
    @import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css');
    </style>
    """, unsafe_allow_html=True)
    
    st.markdown(page_bg_img, unsafe_allow_html=True)
    

    col1, col3 , col2 = st.columns([5,2,5])

    with col1:
        st.markdown(f"<div class='custom-div'><img src='{image_url}' style='border-radius: 5%;width:350px;height:302px;  '></div>", unsafe_allow_html=True)

    with col2:
        h = "<div class='custom-divss description'>"
        for key, value in product_info.items():
            h += f"<div class='description-item'><span class='json-key'>{key}: &nbsp</span><span class='value'>{value}</span></div>"
        h+= "</div>"
        st.markdown(h,unsafe_allow_html=True)

    st.markdown("""
    <div class='footer'>
        <span style='font-weight: bold;'>Contact us</span><br>
        <i class="fas fa-envelope" style="color: orange;"></i> <span style='font-weight: bold;'>sales@aswmedchem.com</span><br>
        <i class="fas fa-phone" style="color: orange;"></i> <span style='font-weight: bold;'>732-342-6911</span><br>
    </div>
    """, unsafe_allow_html=True)


def display_not_found(str_nm,cas_num):
    # # st.title(f"{str_nm} not found  for {cas_num}")
    # page_bg_img = f"""
    # <style>

    # {page_bg_img__}
    # body {{
    #     font-family: Arial, sans-serif;
    # }}
    # .json-key {{
    #     font-weight: bold;
    #     color: #000000; 
    #     font-family : Calibri, sans-serif;

    # }}
    # .custom-div {{
    #     height: 300px;
    #     width: 350px;
    #     border-radius: 5%;
    #     background-color: #91ACE1;
    #     color: black;
    #     font-size: 20px;
    # }}
    # .custom-divss {{
    #     height: 300px;
    #     width: 400px;
    #     border-radius: 5%;
    #     background-color: #91ACE1;
    #     display: flex;
    #     justify-content: center;
    #     align-items: center;
    #     color: black;
    #     font-size: 25px;
    # }}
    # .description {{
    #     display: flex;
    #     flex-direction: column;
    #     align-items: flex-start;
    #     padding: 2px;
    # }}
    # .description-item {{
    #     justify-content: space-between;
    #     width: 100%;
    #     word-break: break-word; /* Adding word break to handle long values */
    # }}
    # .value {{
    #     flex: 1; /* Allow the value to grow and shrink */
    #     # overflow: hidden; /* Hide overflowing text */
    #     # text-overflow: ellipsis; /* Show ellipsis for overflowed text */
    #     font-family : Calibri, sans-serif;
    # }}
    #  .footer {{
    #     left: 0;
    #     bottom: 0;
    #     width: 100%;
    #     margin-top: 50px;
    #     color: #ffffff;
    #     text-align: center;
    #     padding: 10px;
    #     font-size: 20px;
    # }}
    # </style>
    # """
    # st.markdown("""
    # <style>
    # @import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css');
    # </style>
    # """, unsafe_allow_html=True)
    
    # st.markdown(page_bg_img, unsafe_allow_html=True)
    # st.markdown("""
    # <div class='footer'>
    #     <span style='font-weight: bold;'>Contact us</span><br>
    #     <i class="fas fa-envelope" style="color: orange;"></i> <span style='font-weight: bold;'>sales@aswmedchem.com</span><br>
    #     <i class="fas fa-phone" style="color: orange;"></i> <span style='font-weight: bold;'>732-342-6911</span><br>
    # </div>
    # """, unsafe_allow_html=True)
    # # js = """
    # # <script>
    # # window.parent.parent.postMessage("notfound", '*');
    # # </script>
    # # """
    # print("sent")
    # # st.components.v1.html(js, height=0)
    # components.iframe("https://aswmedchem.com/contact/") 
    st.markdown("""
    <style>
    @import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css');
    </style>
    """, unsafe_allow_html=True)

    # st.title("Product Inquiry")
    
    page_bg_img = f"""
    <style>
    {page_bg_img__}
    body {{
        font-family: Arial, sans-serif;
        background-image: url('your_bg_image.jpg');
        background-size: cover; /* Ensure the background image covers the entire screen */
    }}
    .custom-div {{
        height: 250px; /* Increase height */
        width: 350px; /* Increase width */
        border-radius: 5%;
        background-color: #ffffff;
        display: flex;
        justify-content: center;
        align-items: center;
        color: black;
        font-size: 20px;
        flex-direction: column
    }}
    .icon-div {{
        height: 100px; /* Increase height */
        width: 350px; /* Increase width */
        border-radius: 5%;
        display: flex;
        justify-content: center;
        align-items: center;
        color: black;
        font-size: 20px;
        flex-direction: column
        
    }}
    .space {{
        width: 20px; /* Width of space between the boxes */
    }}
    
      .hexagon {{
            width: 100px;
            height: 55px;
            background-color: #f0f0f0; /* Change this to your desired color */
            position: relative;
            margin: 0 auto;
            background: linear-gradient(to right, orange, yellow, red);
    /* fallback for older browsers */
    background: -webkit-linear-gradient(to right, orange, yellow, red);
    /* Chrome 10-25, Safari 5.1-6 */
    background: -moz-linear-gradient(to right, orange, yellow, red);
    /* Firefox 3.6-15 */
    background: -o-linear-gradient(to right, orange, yellow, red);
    /* Opera 11.1-12 */
        
        }}

      
        
        .hexagon:before,
        .hexagon:after {{
            content: '';
            width: 0;
            border-left: 50px solid transparent;
            border-right: 50px solid transparent;
            position: absolute;
        }}

        .hexagon:before {{
            top: -25px;
            border-bottom: 25px solid #f0f0f0; /* Change this to your desired color */
        }}

        .hexagon:after {{
            bottom: -25px;
            border-top: 25px solid #f0f0f0; /* Change this to your desired color */
        }}

        
        .icon {{
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            color: #FFD43B; /* Change this to your desired color */
        }}
    </style>
    """

    st.markdown(page_bg_img, unsafe_allow_html=True)
    
    col1, col3, col2 = st.columns([5, 2, 5])

    with col1:
        st.markdown("""
        <div class='icon-div '>
                    <svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" id="Layer_1" x="0px" y="0px" viewBox="0 0 92 100" style="enable-background:new 0 0 92 100;" xml:space="preserve"><style type="text/css">	.st0{fill:url(#SVGID_1_);}	.st1{fill:#FFFFFF;}</style><linearGradient id="SVGID_1_" gradientUnits="userSpaceOnUse" x1="0.9" y1="740" x2="91.1" y2="740" gradientTransform="matrix(1 0 0 1 0 -690)">	<stop offset="0" style="stop-color:#E72E27"></stop>	<stop offset="1" style="stop-color:#F08519"></stop></linearGradient><path class="st0" d="M8.5,19.4L38.7,2c4.7-2.7,10.4-2.7,15,0l29.9,17.4c4.6,2.7,7.5,7.6,7.5,13v35.2c0,5.3-2.8,10.3-7.5,13L53.7,98  c-4.7,2.7-10.4,2.7-15.1,0L8.4,80.4c-4.6-2.7-7.5-7.6-7.5-13v-35C0.9,27,3.8,22.1,8.5,19.4z"></path><g transform="translate(-1 -1)">	<g>		<g>			<path class="st1" d="M70.6,64.5l-10.1-6.7c-1.3-0.8-3-0.6-3.9,0.6l-2.9,3.8c-0.4,0.5-1.1,0.6-1.6,0.3l-0.6-0.3     c-1.9-1-4.2-2.3-8.8-6.9c-4.6-4.7-5.9-7-6.9-8.8L35.4,46c-0.3-0.5-0.2-1.2,0.3-1.6l3.8-2.9c1.2-1,1.5-2.7,0.6-3.9l-6.7-10.1     c-0.9-1.3-2.6-1.7-4-0.9L25.3,29c-1.3,0.8-2.3,2-2.7,3.5c-1.5,5.5-0.4,15.1,13.7,29.2c11.2,11.2,19.5,14.2,25.3,14.2     c1.3,0,2.6-0.2,3.9-0.5c1.5-0.4,2.7-1.4,3.5-2.7l2.5-4.2C72.3,67.2,71.9,65.4,70.6,64.5z M70.1,67.6l-2.5,4.2     c-0.6,1-1.5,1.7-2.5,2c-5.1,1.4-14,0.2-27.6-13.3S22.8,38.1,24.2,33c0.3-1.1,1-2,2-2.5l4.2-2.5c0.6-0.3,1.3-0.2,1.7,0.4l3.7,5.5     l3.1,4.6c0.4,0.6,0.2,1.3-0.3,1.7L34.8,43c-1.2,0.9-1.5,2.5-0.8,3.7l0.3,0.5c1.1,1.9,2.4,4.4,7.2,9.2s7.2,6.1,9.2,7.2l0.5,0.3     c1.3,0.7,2.9,0.4,3.7-0.8l2.9-3.8c0.4-0.5,1.2-0.6,1.7-0.3l10.1,6.7C70.3,66.3,70.4,67.1,70.1,67.6z"></path>			<path class="st1" d="M50.3,34.4c7.8,0,14.1,6.3,14.1,14.1c0,0.5,0.4,0.8,0.8,0.8s0.8-0.4,0.8-0.8c0-8.7-7.1-15.8-15.8-15.8     c-0.5,0-0.8,0.4-0.8,0.8C49.5,34,49.9,34.4,50.3,34.4z"></path>			<path class="st1" d="M50.3,39.4c5,0,9.1,4.1,9.1,9.1c0,0.5,0.4,0.8,0.8,0.8c0.5,0,0.8-0.4,0.8-0.8c0-6-4.8-10.8-10.8-10.8     c-0.5,0-0.8,0.4-0.8,0.8C49.5,39,49.9,39.4,50.3,39.4z"></path>			<path class="st1" d="M50.3,44.4c2.3,0,4.1,1.9,4.2,4.2c0,0.5,0.4,0.8,0.8,0.8c0.5,0,0.8-0.4,0.8-0.8c0-3.2-2.6-5.8-5.8-5.8     c-0.5,0-0.8,0.4-0.8,0.8C49.5,44,49.9,44.4,50.3,44.4z"></path>		</g>	</g></g></svg>
</div>
        <div class='custom-div'>
            <h2 style='color: #115AA7'>&nbsp &nbsp &nbsp Phone</h2>
            <p style='padding: 10px;'>To inquire about product pricing and availability &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp please call us at</p>
            <p style='font-size: 1.2em; color: #115AA7'>732-342-6911</p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    
    
    with col2:
        st.markdown("""<div class='icon-div '>
                    <svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" id="Layer_1" x="0px" y="0px" viewBox="0 0 92 100" style="enable-background:new 0 0 92 100;" xml:space="preserve"><style type="text/css">	.st0{fill:url(#SVGID_1_);}	.st1{fill:#FFFFFF;}</style><linearGradient id="SVGID_1_" gradientUnits="userSpaceOnUse" x1="0.9412" y1="50" x2="91.0588" y2="50">	<stop offset="0" style="stop-color:#E72E27"></stop>	<stop offset="1" style="stop-color:#F08519"></stop></linearGradient><path class="st0" d="M8.5,19.4L38.7,2c4.7-2.7,10.4-2.7,15,0l29.9,17.4c4.6,2.7,7.5,7.6,7.5,13l0,35.2c0,5.3-2.8,10.3-7.5,13  L53.7,97.9c-4.7,2.7-10.4,2.7-15.1,0L8.4,80.4c-4.6-2.7-7.5-7.6-7.5-13V32.4C0.9,27,3.8,22.1,8.5,19.4z"></path><g>	<g>		<g>			<path class="st1" d="M70.9,44.2C70.9,44.2,70.9,44.1,70.9,44.2c0-0.1,0-0.2,0-0.2c0,0,0-0.1,0-0.1c0,0-0.1-0.1-0.1-0.1     c0,0-0.1-0.1-0.1-0.1c0,0,0,0,0,0l-8-6.2v-6.4c0-1.4-1.1-2.5-2.5-2.5h-9l-3.6-2.8c-0.9-0.7-2.1-0.7-3,0l-3.6,2.8h-9     c-1.4,0-2.5,1.1-2.5,2.5v6.4l-8,6.2c0,0,0,0,0,0c0,0-0.1,0.1-0.1,0.1c0,0-0.1,0.1-0.1,0.1c0,0,0,0.1,0,0.1c0,0.1,0,0.1,0,0.2     c0,0,0,0,0,0v28.3c0,0.3,0.1,0.5,0.1,0.8c-0.2,0.3-0.2,0.7,0,0.9c0.2,0.3,0.6,0.4,0.9,0.3c0.4,0.3,0.9,0.5,1.4,0.5h44.9     c0.5,0,1-0.2,1.4-0.5c0.1,0,0.1,0,0.2,0c0.3,0,0.6-0.2,0.7-0.4c0.1-0.3,0.1-0.6,0-0.8c0.1-0.3,0.1-0.5,0.1-0.8L70.9,44.2     L70.9,44.2z M45.5,26.9c0.3-0.2,0.7-0.2,1,0l1.9,1.5h-4.8L45.5,26.9z M23.7,73.3l21.8-16.9c0.3-0.2,0.7-0.2,1,0l21.8,16.9H23.7z      M69.3,72L47.5,55.1c-0.9-0.7-2.1-0.7-3,0L22.7,72V45.4L36.3,56c0.4,0.3,0.9,0.2,1.2-0.1c0.3-0.4,0.2-0.9-0.1-1.2L23.5,44     l5.9-4.5v6.4c0,0.5,0.4,0.8,0.8,0.8s0.8-0.4,0.8-0.8v-15c0-0.5,0.4-0.8,0.8-0.8h28.3c0.5,0,0.8,0.4,0.8,0.8v15     c0,0.5,0.4,0.8,0.8,0.8s0.8-0.4,0.8-0.8v-6.4l5.9,4.5L54.6,54.7c-0.4,0.3-0.4,0.8-0.1,1.2c0.3,0.4,0.8,0.4,1.2,0.1l13.7-10.6V72z     "></path>			<path class="st1" d="M37.7,35.9h16.6c0.5,0,0.8-0.4,0.8-0.8c0-0.5-0.4-0.8-0.8-0.8H37.7c-0.5,0-0.8,0.4-0.8,0.8     C36.8,35.5,37.2,35.9,37.7,35.9z"></path>			<path class="st1" d="M55.1,40c0-0.5-0.4-0.8-0.8-0.8H37.7c-0.5,0-0.8,0.4-0.8,0.8s0.4,0.8,0.8,0.8h16.6     C54.8,40.9,55.1,40.5,55.1,40z"></path>			<path class="st1" d="M55.1,45c0-0.5-0.4-0.8-0.8-0.8h-7.5c-0.5,0-0.8,0.4-0.8,0.8c0,0.5,0.4,0.8,0.8,0.8h7.5     C54.8,45.8,55.1,45.5,55.1,45z"></path>		</g>	</g></g></svg>
                    </div>  
                    <div class='custom-div'><h2 style='color: #115AA7'> &nbsp &nbsp &nbsp Email</h2><p style='padding: 10px;'>To inquire about product pricing and availability &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp please send us an email at</p><p style='font-size: 1.2em; color: #115AA7'>sales@aswmedchem.com</p></div>""", unsafe_allow_html=True)


    
def find_dictonary(list_of_dictonary,key_,value_):
    for dic in list_of_dictonary:
        value_from_dic = dic.get(key_,"")

        if value_ == value_from_dic:
            return dic
    else:
        return {}


def get_cid(cas_no):
    print(cas_no)
    url = f"https://pubchem.ncbi.nlm.nih.gov/rest/pug/concepts/name/JSON?name={cas_no}"
    
    response = requests.request("GET", url)
    response = response.text
    response = json.loads(response)
    try:
        cid_no = response["ConceptsAndCIDs"]["CID"][0]
    except:
        cid_no = None
    return cid_no


def product(ref_id,cas_number):
    url = f"https://pubchem.ncbi.nlm.nih.gov/rest/pug_view/data/compound/{ref_id}/JSON/"
    print(url)
    print("-----------------------")
    response = requests.request("GET", url)
    response = response.text
    response = json.loads(response)

    chemical_name = response["Record"]["RecordTitle"]
    # cas_number = response["Record"]["Reference"][0]["SourceID"]

    mf = response["Record"]["Section"]
    mf = find_dictonary(mf,"TOCHeading","Names and Identifiers")
    mf = find_dictonary(mf["Section"],"TOCHeading","Molecular Formula")
    mf = mf["Information"][0]
    mf = mf["Value"]["StringWithMarkup"][0]["String"]

    mw = response["Record"]["Section"]
    mw = find_dictonary(mw , "TOCHeading" , "Chemical and Physical Properties")
    mw = find_dictonary(mw["Section"] , "TOCHeading" , "Computed Properties")
    mw = find_dictonary(mw["Section"],"TOCHeading","Molecular Weight")
    mw = mw["Information"][0] 
    mw = mw["Value"]["StringWithMarkup"][0]["String"]

    return [chemical_name , cas_number , mf , mw]


def pc_to_cas(pc_num: str):
    try:
        # Open the Google Sheet by its URL (assuming it has public read access)
        sheet_url = "https://docs.google.com/spreadsheets/d/1DLmFhnKSRLlTF5Fzu2KglJBlzC7YpKC_A_ecNQJ6vrY/edit?usp=sharing"
        sheet_id = sheet_url.split('/')[-2]
        url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:json"
        response = requests.get(url)
        json_data_str = response.text.replace("google.visualization.Query.setResponse(", "").rstrip(");")
        json_data_str = json_data_str.replace('/*O_o*/','').strip()
        print(json_data_str)
        data = json.loads(json_data_str)
        
        # Extract the rows from the JSON response
        rows = data['table']['rows']

        # Find CAS number corresponding to PC number
        for row in rows[1:]:  # Skip the first row as it contains headers
            cells = row['c']
            if cells[0]['v'] == pc_num:
                return cells[1]['v']

        # Return a default value if PC number is not found
        return 404 
    except Exception as e:
        print(f"Error occurred: {e}")
        return "Error"


    


def main():
    params = st.experimental_get_query_params()
    pc_num = params.get('pc_num', [None])[0]

    # st.write("Parameter value:", pc_num)

    if pc_num:
        with st.spinner('Loading...'):
            cas_num = pc_to_cas(pc_num=pc_num)
            
            if cas_num == 404:

                display_not_found(str_nm="product catalog mapping",cas_num=pc_num)

            else: 
            # cas_num = '21871-47-6'
                cid = get_cid(cas_no=cas_num)

                if cid is None:
                    display_not_found(str_nm="product", cas_num=cas_num)

                else:
                    details = product(cid,cas_num)

                    product_info = {
                        "Catalog Number": pc_num,
                        "Chemical Name": details[0],
                        "CAS Number": details[1],
                        "Molecular Formula": details[2],
                        "Molecular Weight": details[3]
                    }

                    product_image_url = f"https://pubchem.ncbi.nlm.nih.gov/image/imgsrv.fcgi?cid={cid}&t=l"

                    display_product_page(product_image_url, product_info)

if __name__ == "__main__":
    main()
    # print(pc_to_cas())
