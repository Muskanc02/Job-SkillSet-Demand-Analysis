import time
import pickle
from selenium.webdriver.common.by import By
import re
# LinkedIn credentials (for the first-time login only)
#fetch using envt variables
username = "***"
password = "***"

def main():
    print("Hello from final-project!")


if __name__ == "__main__":
    main()



# Function to save cookies to a file
def save_cookies(driver, cookie_file):
    with open(cookie_file, "wb") as file:
        pickle.dump(driver.get_cookies(), file)

# Function to load cookies from a file
def load_cookies(driver, cookie_file):
    with open(cookie_file, "rb") as file:
        cookies = pickle.load(file)
        for cookie in cookies:
            driver.add_cookie(cookie)

#function to save login creds as cookies 
def login_and_save_cookies(cookie_file,driver):
# Check if the cookies file exists (used for skipping login)
    cookies_exist = False
    try:
        with open(cookie_file, "rb") as file:
            cookies_exist = True
    except FileNotFoundError:
            cookies_exist = False

    if cookies_exist:
        driver.get("https://www.linkedin.com")
        time.sleep(2)  # Wait for LinkedIn page to load
        load_cookies(driver, cookie_file)
        driver.refresh()  # Refresh the page to apply the cookies
        print("Cookies loaded and session restored.")
    else:
        # If cookies don't exist, log in manually
        driver.get("https://www.linkedin.com/login")
        time.sleep(2)  # Wait for the login page to load
         # Enter credentials
        email_field = driver.find_element(By.ID, "username")
        password_field = driver.find_element(By.ID, "password")
        email_field.send_keys(username)
        password_field.send_keys(password)
        password_field.send_keys(Keys.RETURN)

        time.sleep(5)  # Wait for login to complete
         # Save cookies after successful login
        save_cookies(driver, cookie_file)
        print("Login successful and cookies saved.")

#fetch all job listings details using all tags and store in dictionary
def fetch_and_store_job_listings(driver,job_links_list,job_dict):
    job_listings = driver.find_elements(By.XPATH, '//a[contains(@class, "job-card-list__title--link")]')
    for link in job_listings:
             job_links_list.append(link)
             job_url = link.get_attribute("href")
             #job_title=link.text.strip()
             match = re.search(r"/jobs/view/(\d+)/", job_url)
             if match:
                 job_id = match.group(1)  # Extract Job ID
                 #print(f" URL :{job_url}\nJob ID: {job_id}")
             link.click()
             time.sleep(3)
             try:
                #use div tag with job title class to fetch job title 
                job_title = driver.find_element(By.XPATH, '//div[contains(@class, "job-title")]').text
             except:
                job_title= "Not Found" 
             try:
                #use class name to fetch the company name from right pane
                company_div = driver.find_element(By.CLASS_NAME, 'job-details-jobs-unified-top-card__company-name')
                company_name = company_div.find_element(By.TAG_NAME, 'a').text.strip()
             except:
                company_name = "Not Found"
             try:
                 #use div class to fetch the location bar as whole on right pane
                location_stats = driver.find_element(By.XPATH, '//div[contains(@class, "primary-description-container")]').text
                # Extract location using first span
                location = driver.find_element(By.XPATH,'(//div[contains(@class, "primary-description-container")]//span[1])')    
             except:
                location = "Not Found"
             try:    
                 #use div class and all list elements with span label to fetch job mode and type
                span_elements = driver.find_elements(By.XPATH, '//div[contains(@class, "mt2 mb2")]//ul//li//span[@aria-hidden="true"]')
             except:
                span_elements="Not Found"

             try:
                 #use div class and all span , header and paras with job descriptions
                job_description_elements = driver.find_elements(By.XPATH, '//div[contains(@class, "jobs-description-content__text--stretch")]//*[self::span or self::h1 or self::h2 or self::h3 or self::p or self::strong]')
                seen = set()
                all_text = []
                for element in job_description_elements:
                        text = element.text.strip()
                        if text and text not in seen:
                                seen.add(text)
                                all_text.append(text)


             except:
                job_description_elements="Not found"

           
             print(f"Job id: {job_id}")
             print(f"Job title: {job_title}")
             print(f"Company_name: {company_name} ") 
             print(f"Job location: {location.text}")
             print(f"Job location stats: {location_stats} ")
             list_span=[]
             
             for span in span_elements:
                 list_span.append(span.text.strip())
             if len(list_span)== 2:
                  print(f"Work Mode: {list_span[0]}")
                  work_mode=list_span[0]
                  print(f"Type: {list_span[1]} ")
                  job_type=list_span[1]
             else:
                  print("Mode and Type both are null")
                  list_span.append("NULL")
                  work_mode="NULL"
                  job_type="NULL"
             print(f"Job description:")
             
             # Replace the raw '\n' with actual line breaks
             cleaned_text = [re.sub(r'\\n', '\n', text) for text in all_text]
             all_description="\n".join(cleaned_text)
             
             #print below at each job listing
             print(f"******\n")

             #Store results in dictionary
             # Store the job data in the dictionary using job_id as the key
             job_dict[job_id] = {
                                "title": job_title,
                                "company": company_name,
                                "location": location.text,
                                "work_mode": work_mode,
                                "job_type": job_type,
                                "description": all_description
                                }