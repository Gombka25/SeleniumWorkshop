from page_object_example.base_page import BasePage


class MainPage(BasePage):

    @property
    def manager_id_label(self):
        return self.driver.find_element_by_xpath('.//tr[@class="heading3"]/td')
