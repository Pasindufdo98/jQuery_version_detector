from bs4 import BeautifulSoup
import requests
import re

try:
    source = requests.get('https://www.seylan.lk/')
    source.raise_for_status()

    soup = BeautifulSoup(source.text, 'html.parser')
    
    jquery_detected = False

    for script in soup.find_all('script'):
        if 'jquery' in str(script).lower():
            jquery_detected = True

            if 'ver' in str(script).lower():
            
                jquery_source = str(script.get('src'))
                if jquery_source.startswith("//"):
                    jquery_source_with_ssl = "https:"+jquery_source
                    print("jQuery source:", jquery_source_with_ssl)
                    break    
                    
                else:
                    print("jQuery source:",jquery_source)
                    break
                
            elif '.js' in str(script).lower():

                jquery_source = str(script.get('src'))
                if jquery_source.startswith("//"):
                    jquery_source = "https:"+jquery_source
                    print("jQuery source:", jquery_source)
                    break
                else:
                    print("jQuery source:",jquery_source)
                    break
            
            
    # if jquery_source is None:
    #     url = jquery_source_with_ssl
    # else: url = jquery_source
        
   
       
    url = jquery_source
    # url = jquery_source
    response = requests.get(url)
    response.raise_for_status()
    jquery_content = response.text

    
    #soup1 = BeautifulSoup(jquery_content, 'html.parser')
    pattern = r'v([\d\.]+)'
    #print(jquery_content)


   
    # jquery_found = False
    match = re.search(pattern, jquery_content)

    if match:
        jquery_version = match.group(1)
        print(f"jQuery version: {jquery_version}")
    else:
        print("jQuery version not found")

    # for line in str(soup1).splitlines():
    #     if "/*! jQuery" in line:
    #         print("jQuery version:")
    #         print(line)
    #         jquery_found = True
    #         break
    #     elif " * jQuery" in line:
    #         print("jQuery version:")
    #         print(line)
    #         jquery_found = True
    #         break
    #     else:
    #         continue
    # if jquery_found == False:
    #     print("'jQuery' not found in the content.")


except Exception as e:
    print(e)

