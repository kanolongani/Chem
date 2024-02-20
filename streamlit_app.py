import requests
import json
import streamlit as st
from urllib.request import urlopen


def display_product_page(image_url, product_info):
    st.title(product_info['CAS Number'])
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
    st.markdown(page_bg_img, unsafe_allow_html=True)

    col1, col2 = st.columns([2, 3])

    with col1:
        st.image(image_url, use_column_width=True)

    with col2:
        st.markdown("**Description**")
        for key, value in product_info.items():
            st.markdown(f"<span class='json-key'>{key}:</span> {value}", unsafe_allow_html=True)



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
    st.markdown(page_bg_img, unsafe_allow_html=True)

    
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


def product(ref_id):
    url = f"https://pubchem.ncbi.nlm.nih.gov/rest/pug_view/data/compound/{ref_id}/JSON/"
    response = requests.request("GET", url)
    response = response.text
    response = json.loads(response)

    chemical_name = response["Record"]["RecordTitle"]
    cas_number = response["Record"]["Reference"][0]["SourceID"]

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
        sheet_url = "https://docs.google.com/spreadsheets/d/1mHiSsr4Mxjc8Q36C42cCUWunsMatF2YS6Flv91Grkms/edit?usp=sharing"
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
                    details = product(cid)

                    product_info = {
                        "Catalog Number": cid,
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
