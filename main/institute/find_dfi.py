from flask import request, render_template, url_for, session, redirect
from .models import Institute
from .. import db
from .views import *
from . import institute_bp
from .okay import *

import time




@institute_bp.route('/Indentify', methods=['GET', 'POST'])

def find_insd():
    
    try:
    
        from selenium import webdriver
        import time
        start_time = time.time()

        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        options.add_argument('--ignore-certificate-errors')
        options.add_argument("--enable-popup-blocking")
        options.add_argument("--disable-default-apps")

        driver = webdriver.Chrome(options=options, executable_path="PATH OF CHROME DRIVER")
        ins_name = session['institute_name']
        ins_address = session['institute_address']
        query = ins_name + "," + ins_address
        quote_page = 'https://www.google.com/search?q='+ query.title()

        driver.get(quote_page)
        
        try:
            rcnt_f = driver.find_element_by_id("rcnt")
            rhs_f = rcnt_f.find_element_by_id("rhs")



            SPZz6b_f = rhs_f.find_element_by_class_name("SPZz6b")
            span_tag = SPZz6b_f.find_element_by_tag_name("span")

            institute_title = span_tag.text



            IzNS7c_duf_h_f= rhs_f.find_element_by_class_name("IzNS7c.duf-h")
            QqG1Sd_f= IzNS7c_duf_h_f.find_elements_by_class_name("QqG1Sd")
        
            for el in QqG1Sd_f:
                a_f = el.find_element_by_tag_name("a")  
    
                institute_website = a_f.get_attribute('href')

                ins_lctn = a_f.get_attribute('data-url')


    
    
                if institute_website is not None:
                    if not institute_website.endswith("#"):
                        ins_ws = institute_website
                    else:
                        institute_website = "when_endswith#_url"
                        if institute_website == "when_endswith#_url":
                            rc_c = driver.find_element_by_class_name("rc")  
                            r_c = rc_c.find_element_by_class_name("r")
                            a_tag = r_c.find_element_by_tag_name("a")
                            link = a_tag.get_attribute('href')

                            if link.endswith("#"):
                                import requests
                                from bs4 import BeautifulSoup
                                quote_pagee = 'https://www.google.com/search?q=' + query.title() + ' wiki'

                                driver.execute_script("window.open('');")
                                driver.switch_to.window(driver.window_handles[1])


                                driver.get(quote_pagee)
                                rc_c = driver.find_element_by_class_name("rc")  
                                r_c = rc_c.find_element_by_class_name("r")
                                a_tag = r_c.find_element_by_tag_name("a")
                                link = a_tag.get_attribute('href')
                                a_tag.click()
                                url_bbb =  driver.current_url
                                
                                USER_AGENT = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}
                                try:
                                    page = requests.get(url_bbb, headers=USER_AGENT)
                                    soup = BeautifulSoup(page.content, 'html.parser')
                                    table = soup.find('table', class_ ='infobox vcard')   #print table , use prettify() to see in well structured way
                                    text_website = table.find(text='Website')             #print(table.prettify())
                                    bbb  = text_website.find_next('td')
                                    span_url = bbb.find('span', class_ = 'url')

                                    if span_url is not None:
                                        if True:
                                            whole_a_attrib = span_url.find('a', attrs={'class': 'external free'})
                                            if whole_a_attrib is None:
                                                whole_a_attrib = span_url.find('a', attrs={'class': 'external text'})

                                    if span_url is None:
                                        if True:
                                            whole_a_attrib = bbb.find('a', attrs={'class': 'external free'})
                                            if whole_a_attrib is None:
                                                whole_a_attrib = bbb.find('a', attrs={'class': 'external text'})

                                    ins_ws = whole_a_attrib.get('href')
                                    ins_ws1 = whole_a_attrib.get_text()
                                    
                                    driver.switch_to.window(driver.window_handles[0])

                                except Exception as e:
                                    print("AAAAAA\t" +str(e))
                                    print("Website Not Found! Try again.")

                     

                            else:
                                ins_ws = link
                                print("Found in First Line Result:\t"+ins_ws)


                elif institute_website is None:
                    rc_c = driver.find_element_by_class_name("rc")  
                    r_c = rc_c.find_element_by_class_name("r")
                    a_tag = r_c.find_element_by_tag_name("a")
                    link = a_tag.get_attribute('href')
                    
                    if link.endswith("#"):
                        import requests
                        from bs4 import BeautifulSoup
                        quote_pagee = 'https://www.google.com/search?q=' + query.title() + ' wiki'

                        driver.execute_script("window.open('');")
                        driver.switch_to.window(driver.window_handles[1])


                        driver.get(quote_pagee)
                        rc_c = driver.find_element_by_class_name("rc")  
                        r_c = rc_c.find_element_by_class_name("r")
                        a_tag = r_c.find_element_by_tag_name("a")
                        link = a_tag.get_attribute('href')
                        a_tag.click()
                        url_bbb =  driver.current_url
                        print("Brwoser Current Url:" + driver.current_url)

                        USER_AGENT = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}
                        try:
                            page = requests.get(url_bbb, headers=USER_AGENT)
                            soup = BeautifulSoup(page.content, 'html.parser')
                            table = soup.find('table', class_ ='infobox vcard')   #print table , use prettify() to see in well structured way
                            text_website = table.find(text='Website')             #print(table.prettify())
                            bbb  = text_website.find_next('td')
                            span_url = bbb.find('span', class_ = 'url')

                            if span_url is not None:
                                if True:
                                    whole_a_attrib = span_url.find('a', attrs={'class': 'external free'})
                                    if whole_a_attrib is None:
                                        whole_a_attrib = span_url.find('a', attrs={'class': 'external text'})

                            if span_url is None:
                                if True:
                                    whole_a_attrib = bbb.find('a', attrs={'class': 'external free'})
                                    if whole_a_attrib is None:
                                        whole_a_attrib = bbb.find('a', attrs={'class': 'external text'})

                            ins_ws = whole_a_attrib.get('href')
                            ins_ws1 = whole_a_attrib.get_text()
                            print("Institution Website Name is: %s and \nLink is: %s" % (ins_ws1, ins_ws))

                            driver.close()
                            driver.switch_to.window(driver.window_handles[0])

                        except Exception as e:
                            print("VVVVV\t"+ str(e))
                            print("Website Not Found! Try again.")



                    else:
                        ins_ws = link
                        print("Found in First Line Result:\t"+ins_ws)


                else:
                    print("Not Found Website!")


                

                if not ins_lctn:
                    institute_location = "Not Found!"
                    print(institute_location)

                if ins_lctn:
                    institute_location = "https://www.google.com" + ins_lctn
                    print("Direction :" + institute_location)
 
                if ins_ws and ins_lctn:
                    break
    


            print(institute_title)

            print("Final Website: "+ins_ws)


            Z1hOCe_f = rhs_f.find_elements_by_class_name("Z1hOCe")

            for el in Z1hOCe_f:
                a__f = el.find_elements_by_tag_name("a")

                for aff in a__f:

                    if aff.text != "Address":
                        print("ANF!!!")
                        ins_addr_n = "Not Found!"

                    if aff.text == "Address":
                        LrzXr_f = el.find_element_by_class_name("LrzXr")
                        LrzXr_text = LrzXr_f.text
                        ins_addr = LrzXr_text
                        print(ins_addr)

                        if not LrzXr_text:
                            span_f = LrzXr_f.find_element_by_tag_name("span")
                            ins_addr = span_f.text
                            print(ins_addr)

                            if not ins_addr:
                                print("Not Found Address!")
                                ins_addr_n = "Not Found!"

                        if not ins_addr:
                            print("Not Found Address!")
                            ins_addr_n = "Not Found!"

                if aff.text == "Address" and ins_addr:
                    break

                
  

            for ell in Z1hOCe_f:
                a__f = ell.find_elements_by_tag_name("a")
           
                for af in a__f:

                    if af.text != "Founded":
                        print("FYNF!!!")
                        ins_founded_in = "Not Found!" 

                
                    if af.text == "Founded":
                        LrzXr_kno_fv_f = ell.find_element_by_class_name("LrzXr.kno-fv")
                        LrzXr_kno_fv_text = LrzXr_kno_fv_f.text
                        ins_founded_in = LrzXr_kno_fv_text
                        print(ins_founded_in)

                        if not LrzXr_kno_fv_text:
                            span_f = LrzXr_kno_fv_f.find_element_by_tag_name("span")
                            ins_founded_in = span_f.text

                            if not ins_founded_in:
                                print("Not Found Founded Year!")
                                ins_founded_in = "Not Found!"

                    

                    
                if af.text == "Founded" and ins_founded_in:   
                    break
            
            






            try:

                cl = driver.find_element_by_class_name("PZPZlf.hb8SAc")
                sp = cl.find_element_by_tag_name('span')
                institute_summery = sp.text
                print("From DESC:   "+ institute_summery)

            except Exception as e:
                print(str(e))
                try:
                    import wikipedia
 
                    institute_summery = wikipedia.summary(institute_title)
                    length = len(institute_summery)
                    if length > 1500:
                        institute_summery = wikipedia.summary(institute_title, sentences=3)
                        print("FROM WIKI:  " + institute_summery)
                    else:
                        print("FROM WIKI:  " + institute_summery)
                except:

                    institute_summery = "Not Available"
                    print("Institute Summery:  " + institute_summery)



           
        

            

            try:
                     
                quote_pageee = 'https://www.google.com/search?q=' + query.title() + " logo"
                driver.execute_script("window.open('');")
                driver.switch_to.window(driver.window_handles[1])
                driver.get(quote_pageee)

                logo_id = driver.find_element_by_class_name("YDJP6c")

                logo_img_a = logo_id.find_element_by_tag_name("a")

                logo_href = logo_img_a.get_attribute("href")

                logo_img = logo_id.find_element_by_tag_name("img")
                logo_srca = logo_img.get_attribute("src")

                
                l_s_o = logo_srca
                
            
                driver.switch_to.window(driver.window_handles[0])   

              
            except Exception as e:
                print(str(e))
                try:
                    quote_pageee = 'https://www.google.com/search?q=' + query.title() + " Logo"
                    driver.execute_script("window.open('');")
                    driver.switch_to.window(driver.window_handles[2])
                    driver.get(quote_pageee)

                    logo_id = driver.find_element_by_class_name("vsqVBf.tapJqb.ivg-i.rg_el")

                    logo_img_a = logo_id.find_element_by_tag_name("a")
                    logo_href = logo_img_a.get_attribute("href")

                    logo_img = logo_id.find_element_by_tag_name("img")
                    logo_srcb = logo_img.get_attribute("src")
                     
                    
                    l_s_o = logo_srcb
                    
            
                    driver.switch_to.window(driver.window_handles[0])
                  
                
                except Exception as e:
                    print(str(e))
                    l_s_o = "Not Found!"
                    driver.switch_to.window(driver.window_handles[0])

        




            
            session['BBB_institute_titlee'] = institute_title
            session['BBB_ins_addrr'] = ins_addr
            session['BBB_ins_wss'] = ins_ws
            session['BBB_ins_founded_inn'] = ins_founded_in
            session['BBB_institute_locationn'] = institute_location
            session['BBB_institute_summeryy'] = institute_summery
            session['BBB_l_s_oo'] = l_s_o
            
            print(session['BBB_l_s_oo'])
            st = time.time()
            for t in range(0,6):
                print(t)
                time.sleep(t)    
            et = time.time()
            print("Time taken for Sleep Function:  %s Seconds"  %(et-st)) 

                   



            

            end_time = time.time()
            print("Took %s Seconds to complete this Task." %(end_time - start_time))        
           

            
            print("MISSION 1 SUCCESS!")
            return render_template('MBFC.html', founded_in = ins_founded_in, linkk = ins_ws, title = institute_title, loctn =institute_location, address = ins_addr, srcc = l_s_o) 
  

        except Exception as e:
            print (str(e))    
            print("Refreshing This Page...")
            driver.refresh()
            print("Page Refreshed!")

            try:
                rcnt_f = driver.find_element_by_id("rcnt")
                rhs_f = rcnt_f.find_element_by_id("rhs")

                SPZz6b_f = rhs_f.find_element_by_class_name("SPZz6b")
                span_tag = SPZz6b_f.find_element_by_tag_name("span")

                institute_title = span_tag.text

                IzNS7c_duf_h_f= rhs_f.find_element_by_class_name("IzNS7c.duf-h")
                QqG1Sd_f= IzNS7c_duf_h_f.find_elements_by_class_name("QqG1Sd")
                
                for el in QqG1Sd_f:
                    a_f = el.find_element_by_tag_name("a")  
    
                    institute_website = a_f.get_attribute('href')

                    ins_lctn = a_f.get_attribute('data-url')

                    if institute_website is not None:
                        if not institute_website.endswith("#"):
                            ins_ws = institute_website
                            print("Found in Box:\t"+ins_ws)
                        else:
                            print("Institute_Website is not Null But ends with # : " + institute_website)
                            institute_website = "when_endswith#_url"
                            if institute_website == "when_endswith#_url":
                                rc_c = driver.find_element_by_class_name("rc")  
                                r_c = rc_c.find_element_by_class_name("r")
                                a_tag = r_c.find_element_by_tag_name("a")
                                link = a_tag.get_attribute('href')

                                if link.endswith("#"):
                                    import requests
                                    from bs4 import BeautifulSoup
                                    quote_pagee = 'https://www.google.com/search?q=' + query.title() + ' wiki'

                                    driver.execute_script("window.open('');")
                                    driver.switch_to.window(driver.window_handles[1])


                                    driver.get(quote_pagee)
                                    rc_c = driver.find_element_by_class_name("rc")  
                                    r_c = rc_c.find_element_by_class_name("r")
                                    a_tag = r_c.find_element_by_tag_name("a")
                                    link = a_tag.get_attribute('href')
                                    a_tag.click()
                                    url_bbb =  driver.current_url
                                    print("Brwoser Current Url:" + driver.current_url)

                                    USER_AGENT = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}
                                    try:
                                        page = requests.get(url_bbb, headers=USER_AGENT)
                                        soup = BeautifulSoup(page.content, 'html.parser')
                                        table = soup.find('table', class_ ='infobox vcard')   
                                        text_website = table.find(text='Website')             
                                        bbb  = text_website.find_next('td')
                                        span_url = bbb.find('span', class_ = 'url')

                                        if span_url is not None:
                                            if True:
                                                whole_a_attrib = span_url.find('a', attrs={'class': 'external free'})
                                                if whole_a_attrib is None:
                                                    whole_a_attrib = span_url.find('a', attrs={'class': 'external text'})

                                        if span_url is None:
                                            if True:
                                                whole_a_attrib = bbb.find('a', attrs={'class': 'external free'})
                                                if whole_a_attrib is None:
                                                    whole_a_attrib = bbb.find('a', attrs={'class': 'external text'})

                                        ins_ws = whole_a_attrib.get('href')
                                        ins_ws1 = whole_a_attrib.get_text()
                                        print("Institution Website Name is: %s and \nLink is: %s" % (ins_ws1, ins_ws))
                                        
                                        #driver.close()
                                        driver.switch_to.window(driver.window_handles[0])

                                    except Exception as e:
                                        print("AAAAAA\t" +str(e))
                                        print("Website Not Found! Try again.")

                     

                                else:
                                    ins_ws = link
                                    print("Found in First Line Result:\t"+ins_ws)


                    elif institute_website is None:
                        print("Institute_Website is Null")
                        rc_c = driver.find_element_by_class_name("rc")  
                        r_c = rc_c.find_element_by_class_name("r")
                        a_tag = r_c.find_element_by_tag_name("a")
                        link = a_tag.get_attribute('href')
                    
                        if link.endswith("#"):
                            import requests
                            from bs4 import BeautifulSoup
                            quote_pagee = 'https://www.google.com/search?q=' + query.title() + ' wiki'

                            driver.execute_script("window.open('');")
                            driver.switch_to.window(driver.window_handles[1])


                            driver.get(quote_pagee)
                            rc_c = driver.find_element_by_class_name("rc")  
                            r_c = rc_c.find_element_by_class_name("r")
                            a_tag = r_c.find_element_by_tag_name("a")
                            link = a_tag.get_attribute('href')
                            a_tag.click()
                            url_bbb =  driver.current_url
                            print("Brwoser Current Url:" + driver.current_url)

                            USER_AGENT = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}
                            try:
                                page = requests.get(url_bbb, headers=USER_AGENT)
                                soup = BeautifulSoup(page.content, 'html.parser')
                                table = soup.find('table', class_ ='infobox vcard')   
                                text_website = table.find(text='Website')             
                                bbb  = text_website.find_next('td')
                                span_url = bbb.find('span', class_ = 'url')

                                if span_url is not None:
                                    if True:
                                        whole_a_attrib = span_url.find('a', attrs={'class': 'external free'})
                                        if whole_a_attrib is None:
                                            whole_a_attrib = span_url.find('a', attrs={'class': 'external text'})

                                if span_url is None:
                                    if True:
                                        whole_a_attrib = bbb.find('a', attrs={'class': 'external free'})
                                        if whole_a_attrib is None:
                                            whole_a_attrib = bbb.find('a', attrs={'class': 'external text'})

                                ins_ws = whole_a_attrib.get('href')
                                ins_ws1 = whole_a_attrib.get_text()
                                print("Institution Website Name is: %s and \nLink is: %s" % (ins_ws1, ins_ws))
                               
                                driver.close()
                                driver.switch_to.window(driver.window_handles[0])

                            except Exception as e:
                                print("VVVVV\t"+ str(e))
                                print("Website Not Found! Try again.")



                        else:
                            ins_ws = link
                            print("Found in First Line Result:\t"+ins_ws)


                    else:
                        print("Not Found Website!")

                    if not ins_lctn:
                        institute_location = "Not Found!"
                        print(institute_location)
                    if ins_lctn:
                        institute_location = "https://www.google.com" + ins_lctn
                        print("Direction :" + institute_location)

    
                    if ins_ws and ins_lctn:
                        break
    

                print(institute_title)

                print("Final Website: "+ins_ws)


                Z1hOCe_f = rhs_f.find_elements_by_class_name("Z1hOCe")

                for el in Z1hOCe_f:
                    a__f = el.find_elements_by_tag_name("a")

                    for aff in a__f:

                        if aff.text != "Address":
                            print("ANF!!!")
                            ins_addr_n = "Not Found!"

                        if aff.text == "Address":
                            LrzXr_f = el.find_element_by_class_name("LrzXr")
                            LrzXr_text = LrzXr_f.text
                            ins_addr = LrzXr_text
                            print(ins_addr)

                            if not LrzXr_text:
                                span_f = LrzXr_f.find_element_by_tag_name("span")
                                ins_addr = span_f.text
                                print(ins_addr)

                                if not ins_addr:
                                    print("Not Found Address!")
                                    ins_addr_n = "Not Found!"

                            if not ins_addr:
                                print("Not Found Address!")
                                ins_addr_n = "Not Found!"

                    if aff.text == "Address" and ins_addr:
                        break

                
  

                for ell in Z1hOCe_f:
                    a__f = ell.find_elements_by_tag_name("a")
           
                    for af in a__f:

                        if af.text != "Founded":
                            print("FYNF!!!")
                            ins_founded_in = "Not Found!" 

                
                        if af.text == "Founded":
                            LrzXr_kno_fv_f = ell.find_element_by_class_name("LrzXr.kno-fv")
                            LrzXr_kno_fv_text = LrzXr_kno_fv_f.text
                            ins_founded_in = LrzXr_kno_fv_text
                            print(ins_founded_in)

                            if not LrzXr_kno_fv_text:
                                span_f = LrzXr_kno_fv_f.find_element_by_tag_name("span")
                                ins_founded_in = span_f.text

                                if not ins_founded_in:
                                    print("Not Found Founded Year!")
                                    ins_founded_in = "Not Found!"


                    
                    if af.text == "Founded" and ins_founded_in:   
                        break

                try:

                    cl = driver.find_element_by_class_name("PZPZlf.hb8SAc")
                    sp = cl.find_element_by_tag_name('span')
                    institute_summery = sp.text
                    print("From DESC:   "+ institute_summery)

                except Exception as e:
                    print(str(e))
                    try:
                        import wikipedia
 
                        institute_summery = wikipedia.summary(institute_title)
                        length = len(institute_summery)
                        if length > 1500:
                            institute_summery = wikipedia.summary(institute_title, sentences=3)
                            print("FROM WIKI:  " + institute_summery)
                        else:
                            print("FROM WIKI:  " + institute_summery)
                    except:

                        institute_summery = "Not Available"
                        print("Institute Summery:  " + institute_summery)

                try:
                     
                    quote_pageee = 'https://www.google.com/search?q=' + query.title() + " logo"
                    driver.execute_script("window.open('');")
                    driver.switch_to.window(driver.window_handles[1])
                    driver.get(quote_pageee)

                    logo_id = driver.find_element_by_class_name("YDJP6c")
    
                    logo_img_a = logo_id.find_element_by_tag_name("a")

                    logo_href = logo_img_a.get_attribute("href")

                    logo_img = logo_id.find_element_by_tag_name("img")
                    logo_srca = logo_img.get_attribute("src")
                    l_s_o = logo_srca
            
                    driver.switch_to.window(driver.window_handles[0])
              
                except Exception as e:
                    print(str(e))
                    try:
                        quote_pageee = 'https://www.google.com/search?q=' + query.title() + " Logo"
                        driver.execute_script("window.open('');")
                        driver.switch_to.window(driver.window_handles[2])
                        driver.get(quote_pageee)

                        logo_id = driver.find_element_by_class_name("vsqVBf.tapJqb.ivg-i.rg_el")

                        logo_img_a = logo_id.find_element_by_tag_name("a")
                        logo_href = logo_img_a.get_attribute("href")

                        logo_img = logo_id.find_element_by_tag_name("img")
                        logo_srcb = logo_img.get_attribute("src")
                        l_s_o = logo_srcb

                        driver.switch_to.window(driver.window_handles[0])
                  
                
                    except Exception as e:
                        print(str(e))
                        l_s_o = "Not Found!"
                        driver.switch_to.window(driver.window_handles[0])

                session['BBB_institute_titlee'] = institute_title
                session['BBB_ins_addrr'] = ins_addr
                session['BBB_ins_wss'] = ins_ws
                session['BBB_ins_founded_inn'] = ins_founded_in
                session['BBB_institute_locationn'] = institute_location
                session['BBB_institute_summeryy'] = institute_summery
                session['BBB_l_s_oo'] = l_s_o
       



 
                print(session['BBB_l_s_oo'])
                st = time.time()
                for t in range(0,6):
                    print(t)
                    time.sleep(t)    
                et = time.time()
                print("Time taken for Sleep Function: %s Seconds" %(et-st)) 

               
            

           

                end_time = time.time()
                print("Took %s Seconds to complete this Task." %(end_time - start_time))        

                print("MISSION 2 SUCCESS!")
                return render_template('MBFC.html', founded_in = ins_founded_in, linkk = ins_ws, title = institute_title, loctn =institute_location, address = ins_addr, srcc = l_s_o)
            
            except Exception as e:
                print(str(e))
                print("MISSION FAILED!")
                return redirect(url_for('institute.U_D_C_0'))
  
    except Exception as e:
        print("DDDDDD\t"+str(e))
        return redirect(url_for('institute.U_D_C_0'))
