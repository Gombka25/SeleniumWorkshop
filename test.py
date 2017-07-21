from selenium.webdriver import Ie
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import re
from selenium.webdriver.support.select import Select
from selenium.webdriver import Firefox
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

def test_selenum():
    caps = DesiredCapabilities.INTERNETEXPLORER
    caps['nativeEvents'] = False
    driver = Ie(capabilities=caps)
    driver = Ie()
    driver.get('worldshop.eu')

    search_text_box = driver.find_element_by_name('term')
    search_text_box.send_keys('t-shirt')

    loupe_button = driver.find_element_by_name('searchButton')
    loupe_button.click()
    results = driver.find_element_by_xpath('//div[@class="ProductNumber"]/span')
    match = re.search('\d+', results.text)
    print(match.group())
    assert int(match.group()) == 95

    tshirt_image = driver.find_element_by_xpath('//div[@class="ProductListItem"]/a[@class="PictureLink"]/div[@class="ProductPicture"]/img[@title="TOMMY HILFIGER, Herren T-Shirt FLAG TEE, Dunkelblau"]')
    tshirt_image.click()
    size_selectbox = Select(driver.find_element_by_name('variantChooser:variantChooserSelect'))
    size_selectbox.select_by_visible_text("L")

    WebDriverWait(driver, timeout=10).until(EC.element_to_be_clickable((By.XPATH,'//a[@class="AddToCartLink"]/span')))
    add_to_chart = driver.find_element_by_xpath('//a[@class="AddToCartLink"]/span')
    add_to_chart.click()

    WebDriverWait(driver, timeout=5).until(EC.visibility_of_element_located((By.CLASS_NAME, 'CartMessageBox')))
    add_to_cart_popup = driver.find_element_by_class_name('CartMessageBox')
    assert add_to_cart_popup.is_displayed() is True

    continue_shopping = driver.find_element_by_xpath('//img[@title="Continue Shopping"]')
    continue_shopping.click()

    cart_number = driver.find_element_by_xpath('//a/span[@class="Quantity"]')
    quantity = cart_number.text
    assert int(quantity) == 1

    your_price = driver.find_element_by_xpath('//div[@class="PriceCash"]/span[@class="PriceCashValue"]').get_attribute('data-price')
    basket_price = driver.find_element_by_xpath('//li[@class="Clearfix"][1]/span[@class="Value"]').text
    print(driver.find_element_by_xpath('//li[@class="Clearfix"][1]/span[@class="Value"]').text)
    basket_price_re = re.match('\d+', basket_price)
    print(basket_price_re.group())
    assert int(your_price) == int(basket_price_re.group())

    for i in range(4):
        WebDriverWait(driver, timeout=10).until(
            EC.element_to_be_clickable((By.XPATH, '//a[@class="AddToCartLink"]/span')))
        add_to_chart = driver.find_element_by_xpath('//a[@class="AddToCartLink"]/span')
        add_to_chart.click()

        WebDriverWait(driver, timeout=5).until(EC.visibility_of_element_located((By.CLASS_NAME, 'CartMessageBox')))
        add_to_cart_popup = driver.find_element_by_class_name('CartMessageBox')
        assert add_to_cart_popup.is_displayed() is True

        continue_shopping = driver.find_element_by_xpath('//img[@title="Continue Shopping"]')
        continue_shopping.click()

        cart_number = driver.find_element_by_xpath('//a/span[@class="Quantity"]')
        quantity = cart_number.text

        basket_price = driver.find_element_by_xpath('//li[@class="Clearfix"][1]/span[@class="Value"]').text
        print(driver.find_element_by_xpath('//li[@class="Clearfix"][1]/span[@class="Value"]').text)
        basket_price_re = re.match('\d+', basket_price)

    assert int(5 * your_price) == int(basket_price_re.group())

test_selenum()