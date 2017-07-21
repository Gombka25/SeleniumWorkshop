from selenium.webdriver import Ie
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import re
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By


def test_selenium():
    caps = DesiredCapabilities.INTERNETEXPLORER
    caps['nativeEvents'] = False
    driver = Ie(capabilities=caps)
    driver.get('https://www.worldshop.eu/')
    search_text_box = driver.find_element_by_name('term')
    search_text_box.send_keys('t-shirt')
    loupe_button = driver.find_element_by_name('searchButton')
    loupe_button.click()
    results = driver.find_element_by_xpath('.//div[@class="ProductNumber"]/span')
    match = re.search('\d+', results.text)
    assert int(match.group()) == 95

    searched_item = driver.find_element_by_xpath('.//img[@title="HUGO BOSS T-Shirt, Herren, kurzarm, TEE 5, Dunkelrot"]')
    searched_item.click()

    size_selectbox = Select(driver.find_element_by_name('variantChooser:variantChooserSelect'))
    size_selectbox.select_by_visible_text('M')

    WebDriverWait(driver, timeout=5).until(EC.element_to_be_clickable((By.CLASS_NAME, 'AddToCartLink')))

    max_iterations = 5
    for i in range(1, max_iterations + 1):
        add_to_cart_button = driver.find_element_by_class_name('AddToCartLink')
        add_to_cart_button.click()

        WebDriverWait(driver, timeout=5).until(EC.visibility_of_element_located((By.CLASS_NAME, 'CartMessageBox')))
        add_to_cart_popup = driver.find_element_by_class_name('CartMessageBox')
        assert add_to_cart_popup.is_displayed() is True

        continue_shopping_button = driver.find_element_by_xpath('.//img[@title="Continue Shopping"]')
        continue_shopping_button.click()

    items_in_basket = driver.find_element_by_xpath('.//span[@class="Quantity"]')
    assert int(items_in_basket.text) == max_iterations

    unit_price = driver.find_element_by_xpath('.//span[@class="PriceCashValue"]')
    match_price = re.search('\d+', unit_price.text)
    unit_price_int = int(match_price.group())

    all_price = driver.find_element_by_xpath('.//div[@class="Total"]//li[1]/span[@class="Value"]')
    match_all_price = re.search('\d+', all_price.text)
    all_price_int = int(match_all_price.group())
    assert all_price_int == unit_price_int * max_iterations

    to_basket_button = driver.find_element_by_class_name('ToCartButton')
    to_basket_button.click()

    remove_link = driver.find_element_by_xpath('.//div[contains(@class, "Actions EntryCell")]/a[1]')
    remove_link.click()

    WebDriverWait(driver, timeout=5).until(
        EC.invisibility_of_element_located((By.XPATH, './/div[contains(@class, "Actions EntryCell")]/a[1]')))
    WebDriverWait(driver, timeout=5).until\
        (EC.visibility_of_element_located((By.XPATH, './/div[@class="Entries"]//strong[2]')))
    number_of_items = driver.find_element_by_xpath('.//div[@class="Entries"]//strong[2]')

    assert int(number_of_items.text) == 0




