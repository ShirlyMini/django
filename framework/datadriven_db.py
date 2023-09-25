from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
# 1. import mysql
import mysql.connector

servcie_obj = Service("E:\selenium\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=servcie_obj)

driver.get("https://cleartax.in/s/simple-compound-interest-calculator")
driver.maximize_window()
driver.implicitly_wait(10)
try:
# 2. get number of rows and column from database
    con = mysql.connector.connect(host='localhost',
                            user='root',
                            password='',
                            database="mydb")
    curs = con.cursor()
    curs.execute("SELECT * FROM sicalc")

    # skip the first row
    for r in curs:
        # 3. get data database
        principal_amt = r[0]
        interest = r[1]
        period_num = r[2]
        period_type = r[3]
        int_type = r[4]
        total_amt = r[5]

        # give input in web page
        int_type_elem = driver.find_element(By.XPATH, '//*[@id="a"]')
        int_type_drp = Select(int_type_elem)
        int_type_drp.select_by_visible_text(int_type)  # -------------> pass value from db
        driver.find_element(By.XPATH, '//*[@id="c"]').clear()
        driver.find_element(By.XPATH, '//*[@id="c"]').send_keys(principal_amt)  # -------------> pass value from db
        driver.find_element(By.XPATH, '//*[@id="d"]').clear()
        driver.find_element(By.XPATH, '//*[@id="d"]').send_keys(interest)  # -------------> pass value from db

        period_unit_elem = driver.find_element(By.XPATH, '//*[@id="f"]')
        period_unit_drp = Select(period_unit_elem)
        period_unit_drp.select_by_visible_text(period_type)

        driver.find_element(By.XPATH, '//*[@id="e"]').clear()
        driver.find_element(By.XPATH, '//*[@id="e"]').send_keys(period_num)  # -------------> pass value from db

        # validation part
        get_total_amt = driver.find_element(By.XPATH, '//*[@id="calc"]/div/div[8]/div/span').text
        print(get_total_amt[1:].replace(",", "").replace(" ", ""))
        print(total_amt.replace(",", ""))
        if float(get_total_amt[1:].replace(",", "").replace(" ", "")) == float(total_amt.replace(",", "")):
            print("test passed...")
        else:
            print("test falied...")
    con.close()
except:
    print("unsuccessful connection........")
    driver.quit()

