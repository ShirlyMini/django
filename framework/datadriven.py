from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
# 1. open excel
from framework import xlutils

servcie_obj = Service("E:\selenium\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=servcie_obj)

driver.get("https://cleartax.in/s/simple-compound-interest-calculator")
driver.maximize_window()
driver.implicitly_wait(10)

# 2. get number of rows and column
file = r"C:\Users\user\Desktop\simple_interest.xlsx"
n_row = xlutils.getRowCount(file, "Sheet1")
n_col = xlutils.getColoumnCount(file, "Sheet1")

# skip the first row
for r in range(2, n_row + 1):
    # 3. get data from excel sheet
    principal_amt = xlutils.readData(file, "Sheet1", r, 1)
    interest = xlutils.readData(file, "Sheet1", r, 2)
    period_num = xlutils.readData(file, "Sheet1", r, 3)
    period_type = xlutils.readData(file, "Sheet1", r, 4)
    int_type = xlutils.readData(file, "Sheet1", r, 5)
    total_amt = xlutils.readData(file, "Sheet1", r, 6)

    # give input in web page
    int_type_elem = driver.find_element(By.XPATH, '//*[@id="a"]')
    int_type_drp = Select(int_type_elem)
    int_type_drp.select_by_visible_text(int_type)  # -------------> pass value from xl
    driver.find_element(By.XPATH, '//*[@id="c"]').clear()
    driver.find_element(By.XPATH, '//*[@id="c"]').send_keys(principal_amt)  # -------------> pass value from xl
    driver.find_element(By.XPATH, '//*[@id="d"]').clear()
    driver.find_element(By.XPATH, '//*[@id="d"]').send_keys(interest)  # -------------> pass value from xl

    period_unit_elem = driver.find_element(By.XPATH, '//*[@id="f"]')
    period_unit_drp = Select(period_unit_elem)
    period_unit_drp.select_by_visible_text(period_type)

    driver.find_element(By.XPATH, '//*[@id="e"]').clear()
    driver.find_element(By.XPATH, '//*[@id="e"]').send_keys(period_num)  # -------------> pass value from xl

    # validation part
    get_total_amt = driver.find_element(By.XPATH, '//*[@id="calc"]/div/div[8]/div/span').text
    xlutils.writeData(file, "Sheet1", r, 8, get_total_amt)
    print(get_total_amt[1:].replace(",", "").replace(" ", ""))
    print(total_amt)
    if float(get_total_amt[1:].replace(",", "").replace(" ", "")) == float(total_amt):
        print("test passed...")
        xlutils.writeData(file, "Sheet1", r, 9, "Passed")
        xlutils.fillGreenColour(file, "Sheet1", r, 9)
    else:
        print("test falied...")
        xlutils.writeData(file, "Sheet1", r, 9, "Failed")
        xlutils.fillRedColour(file, "Sheet1", r, 9)
