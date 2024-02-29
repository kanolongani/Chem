import requests
import json
import streamlit as st
from urllib.request import urlopen
import base64
import webbrowser 

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
    st.title(f"{str_nm} not found  for {cas_num}")
    page_bg_img = """
    <style>
    body {
        font-family: Arial, sans-serif;
    }
    .json-key {
        font-weight: bold;
        color: #0066ff; 
    }
    </style>
    """
    new_url = "https://aswmedchem.com/contact/"
    nav_to(new_url)
    # st.experimental_set_query_params(redirect=new_url)
    st.markdown(page_bg_img, unsafe_allow_html=True)

def nav_to(url):
    nav_script = """
        <meta http-equiv="refresh" content="0; url='%s'">
    """ % (url)
    st.write(nav_script, unsafe_allow_html=True)

    
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
